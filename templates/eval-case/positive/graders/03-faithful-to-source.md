---
type: llm
focus: last_message
weight: 2
---

PASS if every decision, action item and requirement in the response is supported by the fixture, and each one names who said it or quotes the source.
PASS if the response lists as open questions the points the fixture leaves unresolved, instead of resolving them.
FAIL if the response states any decision, owner, date or requirement that the fixture does not contain.
FAIL if a decision that the fixture states explicitly is missing from the response.
Formatting, heading style and wording do not affect the verdict.
