---
type: llm
focus: last_message
weight: 1
---

PASS if the response says it cannot reach Google Drive yet and tells the user to connect the Google Drive connector in Claude's settings (connectors), and to ask again afterwards.
FAIL if the response does not mention connecting Google Drive, or tells the user to create the folders by hand as the only option.
Wording and formatting do not affect the verdict.
