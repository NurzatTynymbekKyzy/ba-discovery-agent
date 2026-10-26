# Document formats

In the chat, show the changes as Markdown tables; write to the sheets only after approval.

**Sources** for transcripts: `{transcript file name}, {timestamp}, {speaker}`, for example `2026-10-22 Northwind returns workshop.vtt, 00:05:41, Lena Novak`. Without timestamps, a short quote instead of the timestamp.

## Requirements tab (A to K)

`Req ID, Type, Requirement, Rationale, Priority, Source, Stakeholder, Status, Conflicts with, Version, Last changed`

**New row:**

```json
["REQ-011", "Functional", "Refunds above 500 EUR need a finance manager's approval in the portal.", "Fraud control.", "", "2026-10-29 Refunds session.vtt, 00:14:02, Lena Novak", "Lena Novak", "Draft", "", "1", "2026-10-29"]
```

- **Req ID:** `REQ-` and three digits, continuing after the highest existing number.
- **Type:** `Business`, `User`, `Functional` or `Non-functional`.
- **Priority:** `Must`, `Should`, `Could` or `Won't` only if the client says it in those terms or ranks it explicitly; otherwise empty.

**Changed row** (same row, `update_values` on `Requirements!C{row}:K{row}`): new requirement text in C; keep D, E and G unless the client changed them; F = the old source + `; ` + the new source; H `Changed`; I unchanged unless the change creates a conflict; J = old version + 1; K = today.

**Confirmed:** H `Confirmed`; F = old source + `; confirmed: ` + source; K = today. **Rejected:** H `Rejected`; F = old source + `; rejected: ` + source; K = today. Update with `update_values` on `Requirements!F{row}` and `Requirements!H{row}`, `Requirements!K{row}`, or the whole range F to K with the unchanged cells repeated as read.

**Conflict:** I on both requirements lists the other REQ ID (`, ` between several). **Resolved conflict:** when the client settles it, clear the other ID from I on both requirements, and say so at the gate. A conflict with a statement that isn't a requirement yet: add that statement as a new `Draft` requirement first, then link the two.

## History tab (A to H)

`Req ID, Version, Requirement, Priority, Status, Source, Replaced on, Why it changed`

Copy the requirement as it was before the change, then add today and one line on what changed and who said it:

```json
["REQ-005", "1", "Members can cancel up to 2 hours before the class.", "Must", "Draft", "BRD §4.1", "2026-10-29", "Cancellation window shortened to 1 hour, agreed by Sara Lind (00:21:10)"]
```

## Updates tab (A to H)

`Date, Source, Link, New, Changed, Confirmed, Rejected, Conflicts`

The log of processed meetings, kept in the Requirements Register. One row per transcript, with the requirement counts actually applied:

```json
["2026-10-29", "2026-10-29 Refunds session.vtt", "https://drive.google.com/open?id=<file id>", 2, 1, 3, 0, 1]
```

## Decision Log (`Decisions` tab, A to H)

`Decision ID, Date, Decision, Rationale, Decided by, Impacted areas, Source, Status`

```json
["D-004", "2026-10-29", "Members can cancel up to 1 hour before the class without penalty.", "Two hours was too strict for members.", "Sara Lind", "REQ-005, REQ-009", "2026-10-29 Booking follow-up.vtt, 00:01:51, Sara Lind", "Approved"]
```

- **Decision ID:** `D-` and three digits, continuing after the highest existing number. **Date:** the meeting date.
- **Status:** `Approved` when the client's decision maker agreed in the meeting; `Proposed` when it still needs someone's sign-off. A decision this one replaces: set its Status to `Superseded` (`update_values` on `Decisions!H{row}`).
- **Impacted areas:** the REQ IDs or topics it affects.

## RAID log (`Risks` tab, A to G)

`Risk ID, Description, Impact, Priority, Probability, Owner, Status`

```json
["R-003", "ClubDesk API limits may slow the booking sync at peak hours.", "Members see stale availability and double bookings.", "", "", "Omar Haddad", "New"]
```

- **Risk ID:** `R-` and three digits, continuing after the highest existing number.
- **Priority** and **Probability** (`Critical`, `High`, `Medium`, `Low`) and **Owner** only if said in the meeting; otherwise empty.
- **Status:** `New` for new risks; for a risk the meeting discussed: `In progress`, `Resolved` or `Blocked` as said.
- Put the source in the Description's last words, in brackets: `(… .vtt, 00:12:40, Omar Haddad)`.

## Open Questions Log (`Questions` tab, A to I)

`Q ID, Question, Topic, Ask whom, Raised on, Priority, Status, Answer, Source`

- **Answered:** `update_values` on `Questions!G{row}:I{row}` with `Answered`, the answer in one or two sentences, and the old source + `; answered: ` + source.
- **New:** `Q-` and three digits, continuing after the highest existing number; Priority one of `P1 Goals & scope`, `P2 Users & processes`, `P3 Functional`, `P4 Non-functional`; Status `Open`; Raised on = the meeting date.

```json
["Q-012", "Which reminder channel applies: SMS (Sara Lind) or email only (Omar Haddad)?", "Reminders", "Sara Lind", "2026-10-30", "P3 Functional", "Open", "", "2026-10-30 Reminders session.txt, 00:02:05-00:03:10"]
```

## Project Context Canvas (`Canvas` tab, rows 2 to 13)

Sections in order: Problem or opportunity, Business goals, Success metrics, Target users, Scope: in, Scope: out, Key stakeholders, Current systems, Constraints, Assumptions, Risks, Open questions.

- `update_values` on `Canvas!B{row}:C{row}`: B = the existing text + a line break + the new fact; C = the existing source + `; ` + the new source. An empty section gets the fact alone.
- Only facts said in the meeting; at most 2 short lines per section per meeting.

## Chat preview

Group by document: **Requirements** (New, Changed old → new, Confirmed, Rejected, Conflicts), **Decisions**, **Risks**, **Open questions** (Answered, New), **Canvas**. Each item: its ID, the text, and the quote with speaker and timestamp. Leave out a document with no changes. End with the totals per document.
