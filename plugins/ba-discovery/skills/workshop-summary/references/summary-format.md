# Summary, email and log line formats

Write every label in the language of the meeting; the English below is the default. In the chat, show the summary as Markdown with the same sections; build the HTML only when saving.

Links to Drive files: `https://drive.google.com/open?id=<file id>`.

## Summary Doc (HTML for `create_file`)

```html
<h1>{meeting title}</h1>
<p><b>Date:</b> {YYYY-MM-DD} · <b>Participants:</b> {names, as in the calendar event or the transcript} · <b>Transcript:</b> <a href="{transcript link}">{transcript file name}</a></p>
<p><b>Goal:</b> {only if the meeting's goal was stated; otherwise leave this paragraph out}</p>

<h2>Summary</h2>
<ul>
  <li><b>{Topic}:</b> {one or two sentences: what was discussed and where it landed}</li>
  <!-- 3 to 7 topics, in the order they came up -->
</ul>

<h2>Decisions</h2>
<ul>
  <li>{decision}, agreed by {who} <i>[{timestamp or "short quote"}]</i></li>
</ul>
<!-- none: <p>No decisions were made.</p> -->

<h2>Action items</h2>
<table border="1">
  <tr><td><b>Action</b></td><td><b>Owner</b></td><td><b>Due</b></td><td><b>Source</b></td></tr>
  <tr><td>{action}</td><td>{owner or "not agreed"}</td><td>{YYYY-MM-DD as said, or "not agreed"}</td><td>{timestamp or "short quote"}</td></tr>
</table>
<!-- none: <p>No action items.</p> -->

<h2>Open questions</h2>
<ul>
  <li>{question} ({who should answer, if known})</li>
  <!-- include a question for every action item without an owner or due date -->
</ul>

<h2>Changed during the meeting</h2>
<!-- only if a decision was reversed or changed; otherwise leave the section out -->
<ul>
  <li>{first position} [{timestamp}] → {final decision} [{timestamp}]</li>
</ul>

<p><i>Drafted from the transcript by workshop-summary and reviewed by the BA before saving.</i></p>
```

Relative dates ("next Friday") become a date only if the meeting date makes them certain; write the date and keep the original words in brackets: `2026-10-30 ("next Friday")`. Vague periods ("next week", "soon", "after the release") stay exactly as said, with no date or date range added.

## Email (Gmail draft)

- **To:** attendees' emails from the calendar event, without the BA's own address; for participants the event doesn't cover, the `Email` from the Stakeholder Matrix. Anyone left: list their names at the gate.
- **Subject:** `{meeting title}: summary and next steps ({YYYY-MM-DD})`
- **Body** (`htmlBody`), short, no sources or timestamps:

```html
<p>Hi all,</p>
<p>Thank you for today's session on {topic}. Here is what we agreed.</p>
<p><b>Decisions</b></p><ul><li>{decision}</li></ul>
<p><b>Action items</b></p><ul><li>{action}: {owner}, {due}</li></ul>
<p><b>Questions we need your input on</b></p><ul><li>{question}</li></ul>
<p>The full summary: <a href="{summary Doc link}">{meeting title}: summary</a></p>
<p>If anything is missing or wrong, just reply to this email.</p>
```

Leave out a section that would be empty. Don't add a name or sign-off; `includeSignature: true` adds the BA's own.

## Log line (`update_doc` on Meeting Summaries)

The line:

```
Summary · Transcript · {YYYY-MM-DD} · {meeting title}
```

The words `Summary` and `Transcript` stay in English in every language: their positions are fixed, so the links need no counting.

**Find `E`, the end of the intro paragraph.** In the log text from `read_file_content` (step 2 of the procedure), check that it starts with the title `Meeting Summaries` followed by the intro `Newest first. One line per meeting, added by the workshop-summary skill: Summary opens the meeting's summary Doc, Transcript opens its transcript.` If it does, `E = 166`. If it doesn't (an older template, or the BA edited the top), call `read_doc` once and take the `endIndex` of the first paragraph whose text starts with `Newest first`, or else of the first paragraph (the title).

**Send one `update_doc`.** The new line goes directly under the intro, so the newest meeting is always on top. Write the numbers out (for `E = 166`: 165, 166, 167, 173, 176, 186):

```json
[
  {"insertText": {"location": {"index": E - 1}, "text": "\nSummary · Transcript · 2026-10-22 · Northwind returns workshop"}},
  {"updateParagraphStyle": {"range": {"startIndex": E, "endIndex": E + 1}, "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}},
  {"updateTextStyle": {"range": {"startIndex": E, "endIndex": E + 7}, "textStyle": {"link": {"url": "{summary Doc link}"}}, "fields": "link"}},
  {"updateTextStyle": {"range": {"startIndex": E + 10, "endIndex": E + 20}, "textStyle": {"link": {"url": "{transcript link}"}}, "fields": "link"}}
]
```

The text starts with a line break and has none at the end: it is inserted just before the intro's own line break, so it inherits the intro's plain style instead of the formatting or link of the line below it.
