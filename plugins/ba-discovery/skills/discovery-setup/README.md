# Discovery setup

**Status:** In progress
**Maintainer:** @NurzatTynymbekKyzy

## What it does for you

Creates the standard workspace for a new Discovery on your Google Drive in one step: numbered folders and Google Docs and Sheets for the plan, RAID log, decisions, stakeholders, context and requirements, each built from a shared template: column headers, dropdowns and frozen headers in Sheets, headings and guidance in Docs. Every Discovery gets the same layout, so you, the client team and the other skills always know where things live.

## How to use it

Example requests:

- "Set up a new Discovery for project Atlas"
- "Create the Discovery folders for Atlas inside my Clients folder"
- "Check the Atlas Discovery folder and add whatever is missing"

The skill shows you the full structure first and creates nothing until you say yes.

## What you get

```
Atlas — Discovery/
├── 00 README                      (Doc)
├── 01 Discovery Management/
│   ├── Discovery Plan             (Sheet)
│   ├── Communication Plan         (Sheet)
│   ├── Access Checklist           (Sheet)
│   ├── RAID Log                   (Sheet)
│   └── Decision Log               (Sheet)
├── 02 Client Inputs/
├── 03 Meetings/
│   ├── Transcripts/
│   └── Meeting Summaries          (Doc)
├── 04 Stakeholders/
│   └── Stakeholder Matrix         (Sheet)
├── 05 Context/
│   ├── Project Context Canvas     (Sheet)
│   ├── AS-IS Context              (Doc)
│   └── Glossary                   (Sheet)
├── 06 Requirements/
│   ├── Requirements Register      (Sheet)
│   ├── Open Questions Log         (Sheet)
│   └── Constraints                (Doc)
└── _agent/
    └── discovery.yaml             record of the workspace for the other skills
```

The exact list lives in `references/structure.yaml`.

## Templates

Every Doc and Sheet is built from a template in `templates-source/discovery-setup/` at the repo root: ordinary `.xlsx` and `.docx` files you can open in Excel, Word or Google. To change a template, or suggest a new one, follow [How to change a template](../../../../docs/CHANGE-A-TEMPLATE.md). No git or code needed.

If Google Sheets isn't connected in Claude, Sheets are still created, with their column headers only, and the skill tells you which ones.

## What it won't do

- Fill the documents with project content: they start from the template, with no client information.
- Change the structure per project. Add your own folders afterwards; to change the standard for everyone, propose it in the repo.
- Share, move, rename or delete anything you already have.

## What you need

The Google Drive connector enabled in Claude. Google Sheets as well, for dropdowns and formatting in Sheets.

## Smoke test

| Date | Version | Who | Result | Notes |
|---|---|---|---|---|
| 2026-10-24 | 0.2.0 | @NurzatTynymbekKyzy | Pass | "Test Project" in the root of My Drive: plan shown, created after "да", 22 items + `discovery.yaml`, verified on Drive with no missing, extra or duplicate items. Re-run found the existing workspace and created nothing. |
| 2026-10-24 | 0.2.0 | @NurzatTynymbekKyzy | Pass after fix | Named location "Clients" did not exist: the check ran only after approval, so lookups moved before the gate. BA answered "нет": nothing created, confirmed on Drive. Not yet tried by hand: several folders with the same name, a failing create call. |

## Changelog

| Version | Change |
|---|---|
| 0.2.0 | First version |
