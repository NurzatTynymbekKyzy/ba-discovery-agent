---
type: llm
focus: last_message
weight: 1
---

PASS if the response ends with a per-document summary of the proposed changes (each document with its count) and asks the BA which to apply: all, or named documents.
FAIL if it asks only a single yes/no question for everything, or if it says changes were already applied.
Formatting and language do not affect the verdict.
