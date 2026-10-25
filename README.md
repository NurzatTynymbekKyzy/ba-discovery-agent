# BA Discovery Agent

An open, community-maintained AI agent for business analysts who join a greenfield project and run Discovery.

**The BA owns the client conversation and the judgment. The agent owns the documentation.** It sets up the Discovery workspace on Google Drive, turns client documents and workshop transcripts into summaries, a requirements register and a context canvas, and proposes every change for the BA to approve.

## Status

Early. The repository skeleton, quality standards and eval setup are in place; skills are added one at a time, and each ships only when it passes its evals and a real-Discovery test. See [docs/ROADMAP.md](docs/ROADMAP.md).

## For business analysts

What the plugin does, skill by skill: [plugins/ba-discovery/README.md](plugins/ba-discovery/README.md).

### Install the plugin

**In the Claude app** (web or desktop):

1. Open **Customize** in the sidebar, then **Plugins**.
2. Select **Add marketplace** and enter `NurzatTynymbekKyzy/ba-discovery-agent`.
3. Find **ba-discovery** in the list and click **Install**.

The plugin is saved to your account, so it also works in Claude Code. To get new versions, select **Check for updates** on the marketplace, or turn on **Sync automatically**.

On a Team or Enterprise plan, your organization may manage plugins centrally. If you can't add a marketplace yourself, ask an Owner to add this repository for the organization.

**In Claude Code** (2.1.275 or later):

```
/plugin install ba-discovery --marketplace NurzatTynymbekKyzy/ba-discovery-agent
```

In older versions, add the marketplace first, then install:

```
/plugin marketplace add NurzatTynymbekKyzy/ba-discovery-agent
/plugin install ba-discovery@ba-discovery-agent
```

Update later with `/plugin marketplace update ba-discovery-agent`.

### Connect Google Workspace

The plugin works on your own Google account; it holds no access of its own. In Claude, connect **Google Drive**, **Google Docs**, **Google Sheets** and **Gmail**, all with the **same Google account**: files created through one connector are not visible to another on a different account.

### Check that it works

Start a new chat and type, for example:

> Set up a new Discovery workspace for project Acme on my Google Drive.

Claude shows the folder and file plan and asks before creating anything. If it doesn't, check that the plugin is enabled under **Customize → Plugins**.

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
