# Analysis Doc, question, requirement and canvas formats

Write labels in the language of the documents; the English below is the default. In the chat, show everything as Markdown; build the HTML only when saving.

**Sources** are short and findable: `{document name}, {location}`, for example `BRD v2, §3.1`, `Current process.xlsx, sheet Returns, rows 4–9`, `Kickoff deck, slide 7`. In the Doc, link the document name: `https://drive.google.com/open?id=<file id>`.

## Analysis Doc (HTML for `create_file`)

```html
<h1>Document analysis: {YYYY-MM-DD}</h1>

<h2>Documents analyzed</h2>
<ul><li><a href="{link}">{document name}</a>: {what it is, in one line}</li></ul>
<p><b>Could not read:</b> {name and why; omit if none}</p>

<h2>Overall picture</h2>
<ul>
  <li><b>Problem:</b> {...} <i>({source})</i></li>
  <li><b>Goals:</b> {...} <i>({source})</i></li>
  <li><b>Users:</b> {...} <i>({source})</i></li>
  <li><b>Scope signals:</b> {in / out, as stated} <i>({source})</i></li>
  <li><b>Systems:</b> {...} <i>({source})</i></li>
  <!-- leave out a line the documents don't cover; it belongs under Gaps -->
</ul>

<h2>Contradictions</h2>
<ul><li>{topic}: {statement A} <i>({source A})</i> vs {statement B} <i>({source B})</i>. Question {Q-ID}.</li></ul>
<!-- none: <p>No contradictions found.</p> -->

<h2>Gaps</h2>
<ul><li>{what is missing}. Question {Q-ID}.</li></ul>

<h2>Notes per document</h2>
<h3>{document name}</h3>
<ul><li>{key point} <i>({location})</i></li></ul>
<!-- 3 to 8 points per document -->

<h2>Proposed additions to the canvas</h2>
<!-- only for canvas sections that were already filled; omit otherwise -->
<ul><li><b>{section}:</b> {addition} <i>({source})</i></li></ul>

<p><i>Drafted by doc-analysis from the documents above and reviewed by the BA before saving.</i></p>
```

## Open Questions Log rows

Columns: `Q ID, Question, Topic, Ask whom, Raised on, Priority, Status, Answer, Source`

```json
["Q-007", "Which customer groups are in scope for the first release?", "Scope", "Product owner", "2026-10-26", "P1 Goals & scope", "Open", "", "BRD v2, §2 (no scope section)"]
```

- **Q ID:** always `Q-` and three digits (`Q-001`), in the chat preview too. Sort the questions P1 to P4 first, then number them in that order, continuing after the highest existing `Q-` number; start at `Q-001`.
- **Priority:** exactly one of `P1 Goals & scope`, `P2 Users & processes`, `P3 Functional`, `P4 Non-functional`.
- **Question:** one question per row, open, neutral, answerable by one person; name the document when it helps ("The deck says mobile first, the BRD web first: which comes first?").
- **Ask whom:** a role or name from the documents; empty if unknown.

## Requirements Register rows

Columns: `Req ID, Type, Requirement, Rationale, Priority, Source, Stakeholder, Status, Conflicts with, Version, Last changed`

```json
["REQ-012", "Functional", "Customers can start a return online without contacting support.", "Returns today arrive by phone and email.", "", "BRD v2, §4.2", "Head of Operations", "Draft", "", "1", "2026-10-26"]
```

- **Req ID:** always `REQ-` and three digits (`REQ-001`), in the chat preview too; continue after the highest existing `REQ-` number; start at `REQ-001`.
- **Type:** exactly one of `Business`, `User`, `Functional`, `Non-functional`.
- **Requirement:** one testable statement, in the document's words where possible; no solution the document doesn't name.
- **Priority:** `Must`, `Should`, `Could` or `Won't` only if the document states it; otherwise empty.
- **Source:** every document and location that states it, separated by `; `.
- **Conflicts with:** the Req IDs it contradicts, separated by `, `; empty if none.
- **Status** `Draft`, **Version** `1`, **Last changed** today.

## Canvas cells

Rows 2–13 of `Canvas`, in this order: Problem or opportunity, Business goals, Success metrics, Target users, Scope: in, Scope: out, Key stakeholders, Current systems, Constraints, Assumptions, Risks, Open questions.

- Fill column B ("What we know") and C ("Source") only where B is empty; send `null` for both cells of every other row.
- Each entry: at most 3 short lines, facts only, as the documents state them.
- Open questions: `See Open Questions Log: Q-001 to Q-{last}` with the IDs of this run.
- An assumption is only something a document calls an assumption; risks only risks a document names.
