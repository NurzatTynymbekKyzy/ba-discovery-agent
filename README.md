# BA Discovery Agent

An open, community-maintained AI agent for business analysts who join a greenfield project and run Discovery.

**The BA owns the client conversation and the judgment. The agent owns the documentation.** It sets up the Discovery workspace on Google Drive, turns client documents and workshop transcripts into summaries, a requirements register and a context canvas, and proposes every change for the BA to approve.

## Status

Early. The repository skeleton, quality standards and eval setup are in place; skills are added one at a time, and each ships only when it passes its evals and a real-Discovery test. See [docs/ROADMAP.md](docs/ROADMAP.md).

## For business analysts

- What the plugin does and how to install it: [plugins/ba-discovery/README.md](plugins/ba-discovery/README.md)
- You need Claude with your own Google Drive, Docs, Sheets and Gmail connectors enabled.

## For contributors

| Read | To learn |
|---|---|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | How the human, harness, loops and state fit together |
| [docs/SKILL-CONTRACT.md](docs/SKILL-CONTRACT.md) | What a skill must contain and the Definition of Done |
| [docs/EVALS.md](docs/EVALS.md) | How we prove a skill works |
| [docs/DATA-POLICY.md](docs/DATA-POLICY.md) | Why no client material ever enters this repo |
| [docs/CHANGE-A-TEMPLATE.md](docs/CHANGE-A-TEMPLATE.md) | How to improve a Doc or Sheet template with only a browser |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose and land a change |

## Repository layout

```
.claude-plugin/marketplace.json   # makes this repo installable as a plugin marketplace
plugins/ba-discovery/             # the plugin BAs install
├── .claude-plugin/plugin.json
├── skills/<skill-name>/          # one capability each
└── evals/<skill-name>/           # eval cases for `claude plugin eval`
templates-source/                 # Excel and Word templates for the files skills create (edit these)
templates/                        # starting points for a new skill and its eval cases
tools/                            # template converter and structure check
docs/                             # architecture, standards, roadmap
```

## License

MIT. See [LICENSE](LICENSE).
