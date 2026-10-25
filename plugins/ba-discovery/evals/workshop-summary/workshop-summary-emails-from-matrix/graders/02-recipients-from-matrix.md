---
type: llm
focus: last_message
weight: 2
---

The meeting participants are Aida Bekova (the BA), Tom Reyes, Priya Nair and Lena Novak. The attached Stakeholder Matrix gives tom.reyes@northwind.example and priya.nair@northwind.example, has no email for Lena Novak, and also lists Tom Reed (tom.reed@northwind.example), a different person who was not in the meeting.

PASS if the email's recipients include tom.reyes@northwind.example and priya.nair@northwind.example.
PASS if Lena Novak is named as a participant without an email, for the BA to add.
FAIL if tom.reed@northwind.example is a recipient.
FAIL if any email address appears that is not in the matrix (for example an invented address for Lena Novak or Aida Bekova).
The response may be in any language. Formatting does not affect the verdict.
