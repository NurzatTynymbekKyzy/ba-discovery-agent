# Register formats

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

One row per transcript processed, with the counts actually applied:

```json
["2026-10-29", "2026-10-29 Refunds session.vtt", "https://drive.google.com/open?id=<file id>", 2, 1, 3, 0, 1]
```

## Chat preview

Group the items under **New**, **Changed**, **Confirmed**, **Rejected**, **Conflicts**. Each item: the REQ ID, the text (for changes, old → new), and the quote with speaker and timestamp. End with the totals.
