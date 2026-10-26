---
type: llm
focus: last_message
weight: 3
---

The register has functional requirements REQ-005 (book and cancel up to 1 hour before), REQ-006 (waitlist, moved in automatically), REQ-007 (reminder 24 hours before), REQ-008 (trainer sees booked members), REQ-009 (late cancellation counts as no-show), REQ-011 (accept a freed waitlist place within 30 minutes). REQ-004 is Rejected. REQ-001, REQ-002, REQ-003, REQ-012 are business requirements; REQ-013 is non-functional.

PASS if the response shows a screen map (screens and flows) in which every functional requirement above appears with its REQ ID on at least one screen.
PASS if business and non-functional requirements that have no screen are listed as such rather than silently dropped.
FAIL if REQ-004 or a mobile-app-first screen is used.
FAIL if a screen or feature appears that no requirement asks for (for example payments, ratings, a loyalty programme) without being marked as an assumption.
The response may be in any language. Formatting does not affect the verdict.
