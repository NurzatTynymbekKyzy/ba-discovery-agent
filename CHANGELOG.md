# Changelog

All notable changes to the `ba-discovery` plugin. Versions follow `version` in `plugins/ba-discovery/.claude-plugin/plugin.json`.

## Unreleased (0.9.0)

- `discovery-setup` copies master template files from a shared Drive folder (`references/master-templates.yaml`) instead of reading `templates.json` and rebuilding every Doc and Sheet; `templates.json` is now only the fallback. Live run: 26 Drive calls instead of 37, no Google Sheets writes (was 10), no template text through the model (was about 9.5k tokens read and re-written)
- README template lists `07 Prototype`
- `doc-analysis` and `discovery-docs-update` make Google Sheets calls one at a time and write each tab in as few calls as possible; on `Quota exceeded` they report what is saved and ask the BA to type "continue", instead of retrying into the limit. Live re-test: 0 quota errors (was 5)
- `discovery-docs-update` processes one meeting per run by default (up to 3 when the BA names them) and ends its review with a per-document summary, so the BA can approve document by document
- Master Sheets show dates as YYYY-MM-DD in date columns
- Removed `discovery-review`: its status and checks are mechanical counting, which belongs in code rather than a skill (independent reviews by Claude and Gemini, 2026-10-28)

## Unreleased (0.8.0)

- New skill `discovery-review`, read-only, answers in the chat: "Where are we?" (stage, meetings not yet in the docs, counts, prototype freshness, one next step) and "Is it complete?" (a five-check list: context canvas, Business and User requirements, prototype exists and is current, open P1/P2 questions and High risks without owner)

## Unreleased (0.7.0)

- New skill `prototype`: a clickable wireframe from the Requirements Register (all but Rejected), every element traced to its REQ ID, a coverage screen, and a screen spec Doc for designers; screen map approved before building; update mode after feedback; versions kept in a new `07 Prototype` folder

## Unreleased (0.5.0)

- New skill `discovery-docs-update`: after a meeting, one review updates all five documents: requirements (new, changed with History, confirmed, rejected, conflicts), Decision Log, RAID log, Open Questions Log (answers and new questions) and canvas. Built first as `requirements-register` (requirements only), then widened
- Roadmap: `session-prep` dropped (questions come from doc-analysis and docs updates); `prototype` (with an update mode) and `discovery-review` (final completeness check) added
- Requirements Register template gains History and Updates tabs

## 0.4.0

- New skill `doc-analysis`: new documents in Client Inputs become an analysis Doc, prioritized client questions (P1–P4), draft requirements and first canvas entries; one gate with partial approval; adds only, never overwrites
- Open Questions Log priority is now P1 Goals & scope / P2 Users & processes / P3 Functional / P4 Non-functional
- Roadmap: doc-analysis before requirements-register; no scheduled processing; story-map and process-diagram removed

## 0.3.0

- New skill `workshop-summary`: summary Doc per meeting in `03 Meetings`, a linked line in the Meeting Summaries log, a follow-up email as a Gmail draft; one approval; every decision and action item carries its timestamp or quote
- Meeting Summaries template is now a one-line-per-meeting log, newest first
- Install steps for the Claude app and Claude Code in the README
- Token budgets for every skill, checked in CI

## 0.2.0 — 2026-10-24

- New skill `discovery-setup`: creates the standard Discovery workspace on Google Drive (numbered folders, Docs and Sheets built from templates) after one approval, and writes `_agent/discovery.yaml` with the id of every item for the other skills
- Checks the Google Drive connector, the named location and an existing workspace before asking for approval; completes an existing workspace instead of duplicating it
- Every Doc and Sheet is built from an editable Excel or Word template in `templates-source/`; `tools/templates/build_templates.py` converts them, and CI regenerates them on main
- Eval suite: 5 cases, all passing; mean Δ vs Claude without the plugin +0.60
- `tools/check_structure.py` validates the structure file in CI
- Eval case template uses `files/` + `place-files.sh` for input files

## 0.1.0 — 2026-10-24

- Repository skeleton: marketplace, plugin manifest, skills and evals folders
- Skill contract and Definition of Done
- Eval approach with `claude plugin eval`, templates for positive and negative cases
- Data policy for client material
- CI: plugin validation on every PR; evals on demand
