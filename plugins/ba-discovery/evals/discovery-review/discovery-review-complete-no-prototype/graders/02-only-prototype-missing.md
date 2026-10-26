---
type: llm
focus: last_message
weight: 3
---

The correct result: Context OK, Requirements OK (Business REQ-001, REQ-002; User REQ-003, REQ-004), Prototype exists: Gap (no screen spec), Prototype current: not checked (or not applicable), Open items OK (Q-004 is P3; R-001 has an owner; R-002 is Medium).

PASS if the only gap reported is the missing prototype, and the response suggests building it (the prototype skill or equivalent wording).
FAIL if it reports a gap in context, requirements or open items, or counts check 4 as a separate failed gap with invented details.
FAIL if the response claims to have changed or saved any document.
A single extra "Also:" note (for example that some requirements are still Draft) is allowed and is not a reported gap.
Formatting and language do not affect the verdict.
