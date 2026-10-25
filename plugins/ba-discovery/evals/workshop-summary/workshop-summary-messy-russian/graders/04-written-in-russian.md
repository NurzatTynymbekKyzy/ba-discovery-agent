---
type: llm
focus: last_message
weight: 1
---

PASS if both the summary and the follow-up email are written in Russian, the language of the meeting.
FAIL if the summary or the email is in English or another language. Russian with a few English labels (for example "Action items") still passes.
