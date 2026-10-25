---
type: llm
focus: last_message
weight: 1
---

PASS if the response includes a follow-up email for the participants with a subject line and a short body that recaps the decisions and action items.
FAIL if the email lists any email address, because the transcript contains none (leaving recipients empty, or naming the participants without addresses, is correct).
FAIL if the email body is longer than about 250 words, not counting lists.
The response may be in any language. Formatting does not affect the verdict.
