# Roadmap

We build one skill at a time. The next step starts only when the current skill meets the Definition of Done in `SKILL-CONTRACT.md`.

## Steps

| Step | Deliverable | Why this order | Status |
|---|---|---|---|
| 0 | Repo skeleton, skill contract, eval approach, data policy, CI | Everything else plugs into it | Done |
| 1 | `discovery-setup`: Drive folder structure with empty Docs and Sheets, `_agent/discovery.yaml` | Mostly deterministic; every other skill depends on the folder layout | In review |
| 2 | `workshop-summary`: transcript → summary Doc, log line, email draft | Highest daily value; quality is easy to judge | In progress |
| 3 | `doc-analysis`: primary documents → analysis Doc, prioritized questions, draft requirements, first canvas entries | The client's documents arrive first; the first session needs the questions | In progress |
| 4 | `requirements-register`: extract, dedupe, version, flag conflicts | Merges, versions and checks the draft requirements from steps 2–3 against later meetings | In progress |
| 5 | `canvas-update`: canvas, RAID, decisions, open questions, next-session questions | Builds on steps 2–4 | Planned |
| 6 | Orchestrator (optional): chains skills in one request, with a gate before each step | Only if calling the skills one by one proves inconvenient; the BA always starts it by hand | Planned |
| 7 | `prototype` | Most effort; needs a stable register first | Planned |

## Open questions

| # | Question | Needed by |
|---|---|---|
| Q1 | How do BAs install the plugin in the Claude app? Verify the distribution path for individual users and for an organization before v0.2 | First release |
| Q2 | Where do conventions shared by all skills live (ID format, folder names, gate wording) without duplicating them in every SKILL.md? | Step 2 |
| Q3 | ~~Scheduled processing of new transcripts~~ Dropped: the BA starts every skill by hand | Done |
| Q4 | ~~How are input files given to an eval case?~~ Resolved: `files/` + `place-files.sh` (see EVALS.md) | Done |
| Q5 | Plugin icon (512–2048 px square PNG) for the plugin directory listing | First release |
