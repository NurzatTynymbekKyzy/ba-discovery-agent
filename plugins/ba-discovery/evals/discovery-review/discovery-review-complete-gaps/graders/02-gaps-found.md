---
type: llm
focus: last_message
weight: 3
---

The correct result: 1 of 5 checks OK.
1. Context: Gap, Success metrics and Scope: out are empty.
2. Requirements: Gap, no User requirement that isn't Rejected (REQ-003 is Rejected). Business is fine.
3. Prototype exists: OK (Screen spec v1).
4. Prototype current: Gap, REQ-011 is missing from the spec and REQ-009 changed (2026-10-15) after the spec (2026-10-12).
5. Open items: Gap, Q-001 (P1) and Q-003 (P2) are open; R-002 is High with no owner. R-003 is closed, so it is not a gap; Q-004 is P3, not a gap.

PASS if all four gaps are reported with these specifics (sections, REQ IDs, Q IDs, R-002) and check 3 is OK.
FAIL if a gap is missed, if R-003 or Q-004 is reported as a gap, if the Rejected REQ-003 is counted as a User requirement, or if checks beyond the five are added as gaps (for example stakeholders, glossary or Draft status as its own check).
FAIL if the response claims to have changed or saved any document.
Formatting and language do not affect the verdict.
