# Evals: how we prove a skill works

We measure skills with `claude plugin eval`, the eval runner built into Claude Code. We don't build our own harness.

## Why evals are required

The agent is shared. Anyone can change a skill, and a model update can change behavior without anyone touching the code. Evals are the only way to know that a change made a skill better rather than different.

## How a run works (short version)

- Each case is a realistic BA request plus graders that check the result.
- Each case runs 3 times **with** the plugin and 3 times **without** it. The difference (Δ) shows what the plugin actually adds.
- A case's score is the share of graders that passed, averaged over runs.
- Runs are isolated: empty workspace, only this plugin loaded, no personal settings or connectors.

Full reference: [Test plugins with evals](https://code.claude.com/docs/en/plugin-evals).

## How we test skills that use Google Drive and Gmail

In the Claude app, the Google connectors belong to the BA's account, not to this plugin, so an eval run does not have them. That is why every skill follows the "content in, content out" rule from `SKILL-CONTRACT.md`:

- **Evals** test the skill's judgment on fixture files: the transcript or document goes in the case's `files/` folder, and graders check what the skill produced.
- **The real run** (Definition of Done, point 4) tests the connector steps end to end in the Claude app.

## Layout

```
plugins/ba-discovery/evals/
└── <skill-name>/
    ├── <skill-name>-clean/               # a well-formed input
    ├── <skill-name>-messy/               # a realistic input: crosstalk, typos, half-finished thoughts
    ├── <skill-name>-edge/                # the hardest legitimate input (conflicts, missing parts)
    └── <skill-name>-should-not-trigger/  # a nearby request that belongs to another skill
```

Case names must be unique across the whole suite, so each case folder starts with its skill name. Every case is also tagged with its skill name. Each case folder holds `prompt.md`, `graders/`, and, when needed, `case.yaml`, `files/` and `place-files.sh`. Copy them from `templates/eval-case/`.

## Writing good graders

Give each case at least one grader on the **result** and one on the **process**:

| Grader | Use it for | Cost |
|---|---|---|
| `tool_used` with `tool: Skill` | Did our skill fire (or, in negative cases, not fire)? | Free |
| `regex` | Required sections, ID formats, forbidden phrases, anything checkable exactly | Free |
| `llm` | Faithfulness to the source, completeness, quality of questions | Judge call |

For `llm` graders, write concrete PASS and FAIL lines, and state that formatting does not affect the verdict. A vague rubric gives noisy scores.

## Quality bar

- Each positive case: score ≥ 0.8 over 3 runs.
- Each suite: mean Δ above zero. If the plugin doesn't beat plain Claude, the skill isn't earning its place.
- A change to a ready skill must not lower any case below 0.8 or the suite mean.

## Token budget

Quality comes first, but every run of a skill costs tokens for every BA, every time. So each skill has a budget in `evals/<skill-name>/budget.yaml` (copy `templates/eval-case/budget.yaml`), checked three ways:

| Check | What it measures | When | Cost |
|---|---|---|---|
| `tools/evals/check_budget.py static` | Estimated tokens of the description (in every chat), SKILL.md and every file in `references/` | Every pull request, in CI | Free |
| Efficiency graders in eval cases | Behavior that wastes tokens: a large file read before it is needed, a file read twice (`tool_used` with `max`) | Every eval run | Free (no judge) |
| `tools/evals/check_budget.py results` | Mean turns and mean cost per run of each case, with the plugin loaded | After an eval run | Part of the run |

Cost depends on the model, and the eval result file does not record which one ran, so cost is checked only when you pass the budget's `eval_model` (the model CI pins). Turns are checked on every run.

A budget is a ceiling, not a target. If a change needs more, raise the number in the same pull request and say what the extra tokens buy; the reviewer decides whether that is worth it.

What we learned on `discovery-setup`: the biggest cost was not the instructions but data the model reads and then copies into tool calls. Putting all templates in one compact file, read once and only after approval, cut the template tokens per run by 41%.

## Commands

From `plugins/ba-discovery/`:

```bash
# Whole suite, both arms (slow, the real measurement)
claude plugin eval .

# One skill's cases while iterating (cheap, noisy: confirm with 3 runs)
claude plugin eval . --tag workshop-summary --runs 1 --ablation none

# What CI runs
claude plugin eval . --trust-plugin --json results.json --threshold 0.8 \
  --model claude-sonnet-5-5 --judge-model claude-haiku-5-5 --no-publish --max-cost-usd 10

# Token budget, from the repo root
python3 tools/evals/check_budget.py static
python3 tools/evals/check_budget.py results plugins/ba-discovery/results.json --model claude-sonnet-5-5
```

Requires Claude Code 2.1.269 or later. Every run is a real model call billed to your account, so use `--max-cost-usd` and run single cases while iterating.

## Turning real work into cases

When a BA corrects an agent output in a real Discovery, that correction is the best eval case we can get. Anonymize the input (see `DATA-POLICY.md`), write the corrected output into the `llm` grader's PASS conditions, and add the case in the same PR as the fix.

## Lessons from the first suite (`discovery-setup`)

- **Input files.** Put them in the case's `files/` folder, add `place-files.sh` (copies `files/` into the run's workspace), name it in `case.yaml` under `context.scaffold_script`, and end the prompt with `Input files: <names>`. Run with `--scaffold`. The case template follows this pattern.
- **Name graders `01-…`, `02-…`** so they keep their order in reports.
- **Judges misread non-English answers and future tense.** A small judge marked "Что будет создано" (what will be created) as a claim that files were created. Say in the rubric that the answer may be in any language, and spell out what does *not* count as a failure. Re-check a surprising FAIL in the report before changing the skill.
- **Baseline matters.** On the first suite, plain Claude scored 0.00–0.50 on the positive cases and the skill 1.00, a mean Δ of +0.60. A case where both arms score the same tells you nothing about the skill.
