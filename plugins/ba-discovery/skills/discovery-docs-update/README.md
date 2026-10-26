# Discovery docs update

**Status:** In progress
**Maintainer:** @NurzatTynymbekKyzy

## What it does for you

After a client session, it reads the meeting transcript once and proposes the updates to all five Discovery documents:

| Document | What it proposes |
|---|---|
| Requirements Register | New requirements; changed ones (same ID, version +1, old text kept in `History`); requirements the client confirmed or rejected; conflicts between stakeholders, flagged on both, or cleared when the client settles them |
| Decision Log | Decisions taken in the meeting, with who decided; an earlier decision it replaces marked Superseded |
| RAID log | Risks a participant named; status changes of risks discussed |
| Open Questions Log | Questions answered in the meeting, with the answer; new open questions, prioritized P1 to P4 |
| Project Context Canvas | New facts, added after the text already there |

Every item carries the speaker, the timestamp and the transcript. If you made a summary with `workshop-summary`, it is used as a cross-check. Each processed transcript is logged in the register's `Updates` tab, so the next run knows where to continue.

## How to use it

1. Make sure the transcript is in `03 Meetings/Transcripts` (where `workshop-summary` takes it from).
2. Ask, for example:
   - "Update the docs after yesterday's workshop"
   - "Update the requirements and decisions from the last session"
3. Review the changes, grouped by document. Approve all ("yes"), some ("yes, but skip the risks"), or correct them in plain words.

Without a named transcript, it takes the transcripts not done yet, oldest first, up to 3 per run.

## What it won't do

- Reword, reprioritize or tidy entries nobody discussed.
- Count an idea or a vague "sounds good" as a requirement, a confirmation or a decision.
- Invent risks from its own judgment: only risks someone named.
- Decide conflicts between stakeholders. An unresolved conflict also becomes an open question.
- Replace anything: canvas text is added to, old requirement versions go to History.

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
| 2026-10-26 | 0.5.0 (as `requirements-register`) | @NurzatTynymbekKyzy | Pass after fixes | Requirements only. Test Project 3, register filled by `doc-analysis`; synthetic follow-up transcript: 2 changed (versions 2, old text in History), 2 confirmed, 1 new, 1 conflict resolved and cleared; approved with "yes"; rows re-checked before updating; everything read back. Fixes found: Drive listings return only the first file by default (now up to 100); a just-uploaded file reads empty for about a minute; resolved conflicts need clearing. |

## Changelog

| Version | Change |
|---|---|
| 0.6.0 | Renamed from `requirements-register`; also updates the Decision Log, RAID log, Open Questions Log and canvas from the same meeting, in one review |
| 0.5.0 | First version, as `requirements-register` |
