# Contributing

Thank you for helping. This project values working skills over many skills, so every change is judged by one question: **does it make a skill measurably better for a BA?**

## Ways to help

- **Improve a template.** The Docs and Sheets the agent creates come from Excel and Word files anyone can edit. See [docs/CHANGE-A-TEMPLATE.md](docs/CHANGE-A-TEMPLATE.md): a browser is enough.
- **Report a problem.** Open an issue: what you asked, what you expected, what you got. Describe the input; never attach client material.
- **Add an eval case.** A new realistic case that the current skill fails is one of the most valuable contributions.
- **Improve a skill.** Change the skill and its evals together.
- **Propose a new skill.** Open an issue first with the BA problem it solves and why an existing skill can't do it.

## Before you start

You need Claude Code 2.1.269 or later to validate the plugin and run evals. Read [docs/SKILL-CONTRACT.md](docs/SKILL-CONTRACT.md) and [docs/DATA-POLICY.md](docs/DATA-POLICY.md).

## Making a change

1. Fork, create a branch named after the skill and the change, e.g. `workshop-summary/owners-from-crosstalk`.
2. Change the skill. Add or update eval cases that cover the new behavior.
3. Validate: `claude plugin validate ./plugins/ba-discovery --strict`
4. Run the touched skill's suite from `plugins/ba-discovery/`: `claude plugin eval . --tag <skill-name>`
5. Open a PR using the template. Paste the eval summary before and after.

## How a PR gets merged

- Validation passes in CI.
- The maintainer runs the eval workflow (label `run-evals`). No case below 0.8, suite mean not lower than before.
- The skill README reflects the change.
- A maintainer of that skill approves (see `.github/CODEOWNERS`).

## Style

- Write SKILL.md instructions as direct, numbered steps. Explain the reason behind a rule when it isn't obvious; Claude follows reasons better than bare commands.
- Prefer a script over a paragraph for anything mechanical.
- Plain English in docs. Short sentences.
