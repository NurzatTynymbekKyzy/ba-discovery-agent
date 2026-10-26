# Requirements register

**Status:** In progress
**Maintainer:** @NurzatTynymbekKyzy

## What it does for you

After client sessions, it reads the transcripts the register hasn't seen yet and proposes the changes to your Requirements Register:

- **new** requirements the client stated;
- **changed** requirements: same ID, new text, version +1; the old text is kept in the `History` tab;
- requirements the client explicitly **confirmed** or **rejected**;
- **conflicts** between stakeholders, flagged on both requirements, never resolved for you.

Every item carries the speaker, the timestamp and the transcript. Each processed transcript is logged in the `Updates` tab, so the next run knows where to continue.

## How to use it

1. Make sure the transcript is in `03 Meetings/Transcripts` (the same place `workshop-summary` uses).
2. Ask, for example:
   - "Update the requirements from yesterday's workshop"
   - "What changed in the requirements after the last sessions?"
3. Review the proposed changes. Approve all ("yes"), some ("yes, but skip the conflict on REQ-007"), or correct them in plain words.

Without a named transcript, it takes the transcripts not yet in `Updates`, oldest first, up to 3 per run.

## What it won't do

- Reword, retype or reprioritize requirements nobody discussed.
- Count an idea or a vague "sounds good" as a requirement or a confirmation.
- Decide conflicts between stakeholders.
- Touch the canvas, RAID, Decision Log or question log: `canvas-update` does that.

## Workspaces created before version 0.5

Their Requirements Register has no `History` or `Updates` tab. Add two tabs with these headers in row 1:

- `History`: Req ID, Version, Requirement, Priority, Status, Source, Replaced on, Why it changed
- `Updates`: Date, Source, Link, New, Changed, Confirmed, Rejected, Conflicts

## What you need

- A Discovery workspace created by `discovery-setup`
- Google Drive and Google Sheets connected in Claude, on the same Google account

## Smoke test

| Date | Version | Who | Result | Notes |
|---|---|---|---|---|
| 2026-10-26 | 0.5.0 | @NurzatTynymbekKyzy | Pass after fixes | Test Project 3, register filled by `doc-analysis` (10 requirements, older template: History and Updates tabs added as this README describes); synthetic follow-up transcript named by the BA: 2 changed (versions 2, old text in History), 2 confirmed, 1 new, 1 conflict resolved and cleared on all three requirements, the postponed idea and a restatement not added; approved with "yes"; rows re-checked before updating, everything read back. Fixes found: Drive listings return only the first file by default (now up to 100); a just-uploaded file reads empty for about a minute (now reported as "ask again in a minute"); resolved conflicts need clearing (now in the format). |

## Changelog

| Version | Change |
|---|---|
| 0.5.0 | First version |
