# Discovery review

**Status:** In progress
**Maintainer:** @NurzatTynymbekKyzy

## What it does for you

Reads your Discovery's documents and answers in the chat. It changes nothing.

- **"Where are we?"**, any time: which stage the Discovery is at, meetings not yet processed into the docs, requirements by status and type, open P1/P2 questions, High risks, whether the prototype is up to date, and one next step.
- **"Is it complete?"**, at the end: five checks, each OK or Gap:
  1. Context canvas: problem, goals, success metrics, target users, scope in and out filled
  2. At least one Business and one User requirement
  3. A prototype screen spec exists
  4. The prototype covers every User and Functional requirement and is newer than every change
  5. No open P1/P2 questions; every High risk has an owner

  Every gap says where it is and how to fix it.

## How to use it

Ask, for example:

- "Where are we on Meridian?" or "What should I do next?"
- "Is the Discovery complete?" or "Are we ready for handover?"

Then fix the gaps yourself or with the skill it suggests.

## What it won't do

- Change any document, or save the review anywhere.
- Judge whether a requirement is well written.

## What you need

- A Discovery workspace created by `discovery-setup`, or exports of its documents attached to the chat
- Google Drive and Google Sheets connected in Claude

## Smoke test

| Date | Version | Who | Result | Notes |
|---|---|---|---|---|

## Changelog

| Version | Change |
|---|---|
| 0.8.0 | First version |
