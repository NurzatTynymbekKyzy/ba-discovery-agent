# Roadmap

We build one skill at a time. The next step starts only when the current skill meets the Definition of Done in `SKILL-CONTRACT.md`.

## Steps

| Step | Deliverable | Why this order | Status |
|---|---|---|---|
| 0 | Repo skeleton, skill contract, eval approach, data policy, CI | Everything else plugs into it | Done |
| 1 | `discovery-setup`: Drive folder structure with empty Docs and Sheets, `_agent/discovery.yaml` | Mostly deterministic; every other skill depends on the folder layout | In review |
| 2 | `workshop-summary`: transcript → summary Doc, log line, email draft | Highest daily value; quality is easy to judge | In progress |
| 3 | `doc-analysis`: primary documents → analysis Doc, prioritized questions, draft requirements, first canvas entries | The client's documents arrive first; the first session needs the questions | In progress |
| 4 | `discovery-docs-update`: after a meeting, updates requirements (with history), decisions, risks, open questions and the canvas | One meeting, one review: the BA's "update docs" step; reads the transcript once for all five documents | In progress |
| 5 | `prototype`: a clickable prototype from the register and canvas; updated after the client's feedback | Needs enough context: confirmed requirements and a clear scope | Planned |
| 6 | `discovery-review`: final completeness check of every document, with a gap list | Closes the Discovery: the BA fixes the gaps by hand or in a last session | Planned |
| 7 | Orchestrator (optional): chains skills in one request, with a gate before each step | Only if calling the skills one by one proves inconvenient; the BA always starts it by hand | Planned |

## Open questions

| # | Question | Needed by |
|---|---|---|
| Q1 | How do BAs install the plugin in the Claude app? Verify the distribution path for individual users and for an organization before v0.2 | First release |
| Q2 | Where do conventions shared by all skills live (ID format, folder names, gate wording) without duplicating them in every SKILL.md? | Step 2 |
| Q3 | ~~Scheduled processing of new transcripts~~ Dropped: the BA starts every skill by hand | Done |
| Q4 | ~~How are input files given to an eval case?~~ Resolved: `files/` + `place-files.sh` (see EVALS.md) | Done |
| Q5 | Plugin icon (512–2048 px square PNG) for the plugin directory listing | First release |
