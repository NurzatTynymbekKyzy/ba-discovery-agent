# BA Discovery Agent (plugin)

An assistant for business analysts who join a greenfield project and run Discovery. You run the client conversations and decide what is true. The agent does the documentation: it sets up the Discovery workspace, turns client documents and workshop transcripts into structured artifacts, and proposes every change for your approval.

## What you need

- Claude with this plugin installed
- Your own Google connectors enabled in Claude: Google Drive, Google Docs, Google Sheets, Gmail

## Install

In Claude Code 2.1.275 or later:

```
/plugin install ba-discovery --marketplace NurzatTynymbekKyzy/ba-discovery-agent
```

Install steps for the Claude app are added at the first release, once the distribution path is verified (see `docs/ROADMAP.md`).

## Skills

| Skill | What it does | Status |
|---|---|---|
| `discovery-setup` | Creates the Discovery folder structure, templates and README on your Drive | Planned |
| `workshop-summary` | Turns a transcript into a summary log entry and a follow-up email draft | Planned |
| `requirements-register` | Extracts, deduplicates and versions requirements; flags conflicts | Planned |
| `doc-analysis` | Analyzes primary client documents; drafts prioritized client questions | Planned |
| `canvas-update` | Updates the Context Canvas, RAID log, Decision Log and Open Questions | Planned |

A skill moves to **Ready** only when it meets the Definition of Done in `docs/SKILL-CONTRACT.md` at the repo root.

## How you stay in control

The agent never writes to your register, canvas or logs, and never emails anyone, without showing you the change first. Every proposed change comes with its source: the transcript or document quote it is based on.
