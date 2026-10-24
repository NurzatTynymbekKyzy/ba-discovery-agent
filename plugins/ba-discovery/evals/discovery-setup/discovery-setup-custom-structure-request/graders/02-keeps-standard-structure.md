---
type: llm
focus: last_message
weight: 1
---

Judge only what the skill itself will create.
PASS if the response explains that the skill creates a standard structure, the plan it shows keeps 04 Stakeholders and has no Budget folder, and it tells the user they can add their own folders (such as Budget) afterwards.
Saying that the user may later add, remove or rename folders in Drive themselves is fine and does not affect the verdict.
FAIL if the plan the skill will create drops the Stakeholders folder or includes a Budget folder.
FAIL if the response states or implies that any folder or file was already created.
