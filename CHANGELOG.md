# Changelog

All notable changes to the `ba-discovery` plugin. Versions follow `version` in `plugins/ba-discovery/.claude-plugin/plugin.json`.

## 0.2.0 — 2026-10-24

- New skill `discovery-setup`: creates the standard Discovery workspace on Google Drive (numbered folders, empty Docs and Sheets) after one approval, and writes `_agent/discovery.yaml` with the id of every item for the other skills
- Checks the Google Drive connector, the named location and an existing workspace before asking for approval; completes an existing workspace instead of duplicating it
- Eval suite: 5 cases, all passing; mean Δ vs Claude without the plugin +0.53
- `tools/check_structure.py` validates the structure file in CI
- Eval case template uses `files/` + `place-files.sh` for input files

## 0.1.0 — 2026-10-24

- Repository skeleton: marketplace, plugin manifest, skills and evals folders
- Skill contract and Definition of Done
- Eval approach with `claude plugin eval`, templates for positive and negative cases
- Data policy for client material
- CI: plugin validation on every PR; evals on demand
