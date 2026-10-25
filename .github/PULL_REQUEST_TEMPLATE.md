## What changes

<!-- One or two sentences. Which skill, what behavior. -->

## Why

<!-- The problem a BA hit, or the gap this closes. Link the issue if there is one. -->

## Checklist

- [ ] No real client material anywhere in this PR (docs/DATA-POLICY.md)
- [ ] `claude plugin validate ./plugins/ba-discovery --strict` passes
- [ ] Eval cases added or updated for the changed behavior
- [ ] Suite for the touched skill run locally: no case below 0.8, mean not lower than before
- [ ] Token budget holds (`python3 tools/evals/check_budget.py static`, and `results` after the eval run); any raised limit is explained below
- [ ] Skill README updated (usage, limits, changelog)

## Eval results

<!-- Paste the summary table from `claude plugin eval`, before and after. -->
