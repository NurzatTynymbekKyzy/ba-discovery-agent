# Working on this repo with Claude Code

This file guides Claude Code sessions that develop the plugin. It is not loaded for BAs using the plugin; agent behavior lives in the skills.

## Map

- `plugins/ba-discovery/skills/` — one folder per skill; the agent's instructions
- `plugins/ba-discovery/evals/` — eval cases, one folder per skill
- `templates/` — copy these to start a skill or an eval case
- `docs/` — architecture, skill contract, evals, data policy, roadmap

## Rules

1. Read `docs/SKILL-CONTRACT.md` before creating or editing a skill. Follow its section structure.
2. Never write real client material into the repo. Fixtures are synthetic or anonymized (`docs/DATA-POLICY.md`).
3. Change a skill and its eval cases in the same change.
4. Mechanical steps go into `skills/<name>/scripts/`, not into prose instructions.
5. Keep each SKILL.md under 500 lines; move formats and long examples into `references/`.
6. Do not add a `bin/` folder to the plugin: the Claude app won't install it.
7. Work on one skill at a time, in the order in `docs/ROADMAP.md`.

## Checks before finishing

```bash
claude plugin validate . && claude plugin validate ./plugins/ba-discovery --strict
cd plugins/ba-discovery && claude plugin eval . --tag <skill-name> --runs 1 --ablation none
```

Confirm any result that matters with the default 3 runs before reporting it.
