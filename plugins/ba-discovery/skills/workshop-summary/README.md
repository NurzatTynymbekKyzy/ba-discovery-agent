# Workshop summary

**Status:** In progress
**Maintainer:** @NurzatTynymbekKyzy

## What it does for you

After a client session, turns the transcript into:

- a **summary Doc** in `03 Meetings`: topics, decisions, action items with owners and due dates, open questions, each decision and action linked to the moment in the transcript where it was said;
- a **line in Meeting Summaries**, the Discovery's log of every meeting, linking the summary and the transcript;
- a **follow-up email draft** in your Gmail, addressed to the meeting's participants: a short recap with a link to the full summary.

You review everything in the chat first. The email stays a draft: you send it.

## How to use it

1. Put the transcript into `03 Meetings/Transcripts` of the Discovery folder: a Zoom or Teams export (`.vtt`, `.txt`, `.docx`) or a Google Meet transcript Doc. You can also attach it to the chat.
2. Ask, for example:
   - "Summarize yesterday's workshop"
   - "Process the latest transcript and prepare the follow-up email"
   - "Summarize the Payments session transcript"
3. Check the summary and the email, correct anything in plain words ("the owner of the second action is Aida"), and say "yes".

Without a named transcript, the skill takes the newest one that has no summary yet and tells you which one it took.

## What it won't do

- Send the email. It only creates a draft.
- Invent owners, due dates or email addresses. If nobody said who or when, the summary says "not agreed" and adds an open question.
- Fill the Requirements Register, Context Canvas, RAID or Decision Log. Other skills do that.
- Share the summary with the client. The link in the email works only for people with access to the Discovery folder.

## What you need

- A Discovery workspace created by `discovery-setup`
- Google Drive, Google Docs and Gmail connected in Claude, all on the same Google account
- Google Calendar (optional): finds the meeting's title, date and participants' emails. Without a calendar invite, the email's recipients are left for you to fill in.

## Smoke test

| Date | Version | Who | Result | Notes |
|---|---|---|---|---|
| 2026-10-25 | 0.3.0 | @NurzatTynymbekKyzy | Pass after fixes | Test Project 3, synthetic `.vtt` transcript in `03 Meetings/Transcripts`: picked as newest unprocessed; no calendar event, so To left empty; preview approved with "yes"; summary Doc created and read back; log line added on top of an older-template log with both links correct; Gmail draft created. Fixes found: `.vtt` reads empty with `read_file_content` (now read through file metadata); `read_doc` costs ~10k tokens for an almost empty log (now `read_file_content`, ~200); ids come back with escaped underscores; several `discovery.yaml` need the project name read; the draft went to a Gmail connected with a different account than Drive (now reported). |

## Changelog

| Version | Change |
|---|---|
| 0.3.0 | First version |
