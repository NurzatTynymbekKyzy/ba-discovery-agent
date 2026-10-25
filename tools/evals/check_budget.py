#!/usr/bin/env python3
"""Check every skill against its token and cost budget.

Each skill keeps its budget in plugins/ba-discovery/evals/<skill>/budget.yaml.
Two checks read it:

  static   Free, runs on every pull request. Estimates the tokens of what the
           skill puts into context: its description (in every chat), its
           SKILL.md (when it runs) and the reference files it reads during a
           run. Fails if any of them grows past its budget.

  results  Runs after `claude plugin eval`. Reads aggregate-result.json and
           checks each case's mean number of turns and, when the run used the
           budget's model, its mean cost per run (judge calls excluded), with
           the plugin loaded. Cost depends on the model and the result file
           doesn't record it, so pass the model you ran with.

A budget is a ceiling, not a target. Raise it in the same pull request that
needs more, and say why in the description: a reviewer then decides whether
the extra tokens buy enough quality.

Usage:
  check_budget.py static
  check_budget.py results path/to/aggregate-result.json [--model MODEL]
"""
from __future__ import annotations

import json
import re
import statistics
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
PLUGIN = REPO / "plugins" / "ba-discovery"
CHARS_PER_TOKEN = 3.6  # rough average for English prose and compact JSON


def tokens(text: str) -> int:
    return round(len(text) / CHARS_PER_TOKEN)


def budgets() -> dict[str, dict]:
    out = {}
    for path in sorted((PLUGIN / "evals").glob("*/budget.yaml")):
        out[path.parent.name] = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return out


def skills() -> list[str]:
    return sorted(p.parent.name for p in (PLUGIN / "skills").glob("*/SKILL.md"))


def check_static() -> int:
    failed = False
    all_budgets = budgets()
    rows = []
    for skill in skills():
        budget = all_budgets.get(skill)
        if budget is None or "static" not in budget:
            print(f"✗ {skill}: no static budget in plugins/ba-discovery/evals/{skill}/budget.yaml")
            failed = True
            continue
        static = budget["static"]
        skill_dir = PLUGIN / "skills" / skill
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        match = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
        measured = {
            "description": tokens(match.group(1)) if match else 0,
            "SKILL.md": tokens(text),
        }
        limits = {"description": static.get("description"), "SKILL.md": static.get("skill_md")}
        for ref, limit in (static.get("references") or {}).items():
            path = skill_dir / ref
            measured[ref] = tokens(path.read_text(encoding="utf-8")) if path.exists() else None
            limits[ref] = limit
        for part, value in measured.items():
            limit = limits.get(part)
            if value is None:
                status = "missing file"
                failed = True
            elif limit is None:
                status = "no budget"
                failed = True
            elif value > limit:
                status = f"OVER by {value - limit}"
                failed = True
            else:
                status = "ok"
            rows.append((skill, part, value, limit, status))
        # Every file in references/ should be budgeted, or the skill could read
        # a large new file without anyone noticing.
        for path in sorted((skill_dir / "references").rglob("*")):
            ref = path.relative_to(skill_dir).as_posix()
            if path.is_file() and ref not in measured:
                rows.append((skill, ref, tokens(path.read_text(encoding="utf-8")), None, "not in budget"))
                failed = True

    print(f"{'SKILL':<20} {'PART':<34} {'TOKENS':>7} {'BUDGET':>7}  STATUS")
    for skill, part, value, limit, status in rows:
        print(f"{skill:<20} {part:<34} {value if value is not None else '-':>7} {limit if limit is not None else '-':>7}  {status}")
    return 1 if failed else 0


def check_results(path: Path, model: str | None) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("partial"):
        print(f"✗ results are partial ({data.get('partialReason')}); budget not checked")
        return 1
    all_budgets = budgets()
    failed = False
    notes = set()
    print(f"{'CASE':<44} {'COST $':>8} {'MAX $':>7} {'TURNS':>6} {'MAX':>4}  STATUS")
    for case in data.get("cases", []):
        name = case["name"]
        runs = [r for r in case.get("arms", {}).get("with", []) if not r.get("error")]
        skill = next((s for s in all_budgets if name.startswith(s + "-")), None)
        skill_budget = all_budgets.get(skill) or {}
        case_budget = (skill_budget.get("eval") or {}).get(name) if skill else None
        budget_model = skill_budget.get("eval_model")
        if not runs:
            print(f"{name:<44} {'-':>8} {'-':>7} {'-':>6} {'-':>4}  no successful runs")
            failed = True
            continue
        cost = statistics.mean(r["costUsd"] - r.get("judgeCostUsd", 0) for r in runs)
        turns = statistics.mean(r["turns"] for r in runs)
        if case_budget is None:
            print(f"{name:<44} {cost:>8.3f} {'-':>7} {turns:>6.1f} {'-':>4}  no budget")
            failed = True
            continue
        problems = []
        max_cost = case_budget.get("max_cost_usd")
        if max_cost is None:
            notes.add(f"{skill}: no cost budget yet; run with --model {budget_model} and set it")
        elif model != budget_model:
            notes.add(f"{skill}: cost not checked; budget is for {budget_model}, run used {model or 'unknown model'}")
            max_cost = None
        elif cost > max_cost:
            problems.append(f"cost +{cost - max_cost:.3f}")
        if turns > case_budget["max_turns"]:
            problems.append(f"turns +{turns - case_budget['max_turns']:.1f}")
        status = "OVER: " + ", ".join(problems) if problems else "ok"
        failed = failed or bool(problems)
        shown_max = f"{max_cost:>7.3f}" if max_cost is not None else f"{'-':>7}"
        print(f"{name:<44} {cost:>8.3f} {shown_max} {turns:>6.1f} {case_budget['max_turns']:>4}  {status}")
    for note in sorted(notes):
        print(f"note: {note}")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in ("static", "results"):
        print(__doc__)
        return 2
    if argv[0] == "static":
        return check_static()
    if len(argv) < 2:
        print("give the path to aggregate-result.json")
        return 2
    model = argv[argv.index("--model") + 1] if "--model" in argv else None
    return check_results(Path(argv[1]), model)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
