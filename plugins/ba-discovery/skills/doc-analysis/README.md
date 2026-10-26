# Document analysis

**Status:** In progress
**Maintainer:** @NurzatTynymbekKyzy

## What it does for you

Reads the client's documents in `02 Client Inputs` (BRD, specs, spreadsheets, decks, screenshots) and gives you, after your approval:

- a **Document Analysis** Doc in `05 Context`: what each document is, the overall picture, contradictions between documents, gaps, and what couldn't be read;
- **client questions** in the Open Questions Log, prioritized from general to specific: P1 goals and scope, P2 users and processes, P3 functional details, P4 non-functional and constraints;
- **draft requirements** in the Requirements Register, each with the document and page or section it comes from;
- **first entries in the Project Context Canvas**, only in sections that are still empty.

Every fact carries its source, so you can defend it in front of the client.

## How to use it

1. Put the client's materials into `02 Client Inputs` (subfolders are fine).
2. Ask, for example:
   - "Analyze the client documents"
   - "Go through what the client sent and prepare questions for the first session"
   - "Review the new BRD in Client Inputs"
3. Check the result in the chat. Approve everything ("yes"), or only some parts ("yes, but skip the requirements"), or correct things in plain words first.

The skill takes every document it hasn't analyzed before. Run it again when new material arrives: only the new documents are read, and questions or requirements already in your logs are not added twice.

## What it won't do

- Overwrite anything. It adds rows and fills only empty canvas sections; additions for filled sections are proposed in the analysis Doc.
- Decide between contradicting documents. It shows both and asks the client.
- Read links, dashboards (Power BI) or videos. They are listed as "could not read" and turned into a question or access request.
- Set requirement priorities the documents don't state.

## What you need

- A Discovery workspace created by `discovery-setup`
- Google Drive and Google Sheets connected in Claude, on the same Google account

## Smoke test

| Date | Version | Who | Result | Notes |
|---|---|---|---|---|

## Changelog

| Version | Change |
|---|---|
| 0.4.0 | First version |
