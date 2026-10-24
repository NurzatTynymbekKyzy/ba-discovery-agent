# Architecture

## The one-sentence version

The BA decides at gates, the harness runs the loops, and the BA's Google Drive holds the state.

## Design principles

1. **The human owns judgment, the agent owns documentation.** The BA runs client conversations and decides what is true. The agent turns raw input into structured artifacts and proposes changes. It never silently changes the source of truth.
2. **LLM for judgment, code for mechanics.** Anything deterministic is a script or a template, not a prompt.
3. **Every skill is a product.** Contract, quality rubric, eval cases, docs. A skill without evals is not shipped.
4. **State lives in the BA's Google Workspace, not in the agent.** Any BA, or any Claude session, can pick up a Discovery from its Drive folder alone.
5. **Community-ready from day one.** One public repo, installable as a plugin, configured per Discovery, improved through evals.

## Layers

```
HUMAN (BA)          runs client sessions · asks the questions · approves at gates
      ▲ review / approve / correct          │ requests, files
      │                                     ▼
HARNESS             Claude (app for BAs, Claude Code for contributors) + this plugin
                    ├─ orchestrator: workflow loop per event, gates, run log
                    ├─ skills: one capability each; the agent loop runs inside each
                    └─ tools: the BA's Google connectors + scripts bundled in skills
      │ read / write
      ▼
STATE               BA's Google Drive, one folder per Discovery
                    docs · transcripts · summaries · Requirements Register (Sheet)
                    Context Canvas · RAID · Decisions · Open Questions · _agent/
      ▲
COMMUNITY           this GitHub repo: skills, templates, eval suites, CI, releases
```

## Where each part lives

### Harness

We don't build the harness. Claude is the harness; we ship a **plugin** into it.

- **Skills hold all agent instructions.** A plugin's root `CLAUDE.md` is not loaded as context, so every rule the agent must follow lives in a skill. The repo's own `CLAUDE.md` is only for contributors working on the code.
- **Connectors are the BA's own.** Google Drive, Docs, Sheets and Gmail are connected in each BA's Claude account. The plugin doesn't bundle or proxy them, so the BA's data never passes through anything we host.
- **Scripts live inside skills** (`skills/<name>/scripts/`). We don't use the plugin `bin/` folder, because the Claude app does not install plugins that have one.

### Loops

| Loop | Scope | Who runs it |
|---|---|---|
| Agent loop | Inside one skill: think → call a tool → observe → repeat until the output contract is met | Claude |
| Workflow loop | One Discovery event, e.g. a new transcript: summary → register → canvas, each behind its gate | The orchestrator skill |
| Quality loop | One skill version: change → run evals → merge only if quality holds | Contributors and CI |

### Human gates

| Gate | When | What the BA sees |
|---|---|---|
| Approve-before-send | Any email to the client or participants | A Gmail draft; sent only after approval |
| Approve-before-write | Changes to the register, canvas or logs | A diff: added, changed, removed, each with its source quote |
| Resolve-conflict | New information contradicts an existing requirement | Both statements, their sources, and a proposed question for the client |
| Correct-and-learn | The BA edits an agent output | The correction is logged and becomes a future eval case |

Autonomy is set per Discovery in `_agent/config`. Defaults are always the safest option, for example `email: draft_only`.

### State

The Discovery folder on Drive is the system of record. Its structure is created by the `discovery-setup` skill. The agent's own bookkeeping sits in `_agent/`: the config, a manifest of processed files and their versions, and a run log of what the agent did, when, and with which plugin version.

Every requirement has an ID that links back to its source quote and forward to stories, screens and diagram steps.

## Decisions

| # | Decision | Status |
|---|---|---|
| D1 | BAs use the agent in the Claude app; contributors develop and run evals in Claude Code | Accepted |
| D2 | Google Workspace is the only workspace: Drive, Docs, Sheets, Gmail | Accepted |
| D3 | One public repo, laid out as a plugin marketplace with one plugin, `ba-discovery` | Accepted |
| D4 | Evals run with `claude plugin eval`; no custom harness | Accepted |
| D5 | No real client material in the repo; fixtures are synthetic or anonymized | Accepted |
| D6 | MIT license | Proposed |

Open questions are tracked in `ROADMAP.md`.
