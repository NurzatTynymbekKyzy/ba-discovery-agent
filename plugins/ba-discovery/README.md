# BA Discovery Agent (plugin)

An assistant for business analysts who join a greenfield project and run Discovery. You run the client conversations and decide what is true. The agent does the documentation: it sets up the Discovery workspace, turns client documents and workshop transcripts into structured artifacts, and proposes every change for your approval.

## What you need

- Claude with this plugin installed
- Your own Google connectors enabled in Claude: Google Drive, Google Docs, Google Sheets, Gmail

## Install

- **Claude app:** Customize → Plugins → Add marketplace → `NurzatTynymbekKyzy/ba-discovery-agent` → install **ba-discovery**
- **Claude Code 2.1.275 or later:** `/plugin install ba-discovery --marketplace NurzatTynymbekKyzy/ba-discovery-agent`

Full steps, Google connectors and a first check: [Install the plugin](../../README.md#install-the-plugin) in the repository README.

## Skills

| Skill | What it does | Status |
|---|---|---|
| `discovery-setup` | Creates the Discovery folder structure on your Drive, with Docs and Sheets built from shared templates | In progress: tested, 2 rare cases left to try by hand |
| `workshop-summary` | Turns a transcript into a summary Doc, a line in the Meeting Summaries log and a follow-up email draft | In progress: evals passing, tested on Drive |
| `doc-analysis` | Analyzes the client's documents: analysis Doc, prioritized questions, draft requirements, first canvas entries | In progress |
| `discovery-docs-update` | After a meeting, updates requirements (with history), decisions, risks, open questions and the canvas, in one review | In progress |
| `prototype` | Clickable wireframe traced to the requirements, plus a screen spec Doc for designers; updated after client feedback | In progress |
| `discovery-review` | "Where are we?" during the Discovery (status and the next step) and "Is it complete?" at the end (five checks with gaps), in the chat; changes nothing | In progress |

A skill moves to **Ready** only when it meets the Definition of Done in `docs/SKILL-CONTRACT.md` at the repo root.

## How you stay in control

The agent never writes to your register, canvas or logs, and never emails anyone, without showing you the change first. Every proposed change comes with its source: the transcript or document quote it is based on.
