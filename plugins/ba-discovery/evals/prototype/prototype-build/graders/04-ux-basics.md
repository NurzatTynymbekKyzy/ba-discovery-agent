---
type: llm
focus: last_message
weight: 2
---

Judge the wireframe HTML in the response against basic UX rules for a low-fi wireframe.

PASS if all of these hold:
- every screen section has an h1 title and exactly one primary action (`btn primary`), except the coverage screen, which needs none;
- screens below the first level have a way back (a crumbs line, a back link or a back button);
- the states the requirements imply are shown as `state` blocks: at least an empty state on a list, and on My bookings that cancelling is not allowed within 1 hour of the class (REQ-009);
- any form field has a visible label;
- it stays low-fi: no colours, images or styles beyond the kit's classes.
FAIL if a screen other than coverage has no primary action or several, or if none of the implied states is shown.
Formatting of the chat text around the HTML does not affect the verdict.
