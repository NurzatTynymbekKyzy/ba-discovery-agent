# Data policy

This repository is public and shared. Client material must never enter it.

## The rule

**No real client transcript, document, email, screenshot or export is ever committed.** Not in fixtures, not in examples, not in issue threads, not in PR descriptions.

## Where real material can live

- Your own Google Drive, under your engagement's normal confidentiality rules.
- A local `private-fixtures/` folder for running evals on your machine. It is in `.gitignore`. Before using client material even locally with a model, check that your engagement allows it.

## Turning real material into a public fixture

A public fixture is either **synthetic** (written from scratch to look realistic) or **anonymized**. To anonymize, change all of the following, then have a second person read it:

- [ ] Company, brand, product and project names
- [ ] People's names, roles that identify a single person, emails, phone numbers
- [ ] Internal system names, URLs, domains, IP addresses, file paths
- [ ] Amounts, volumes and KPIs (scale them, keep the proportions)
- [ ] Dates (shift consistently), locations
- [ ] Any detail that would let someone from the client recognize their own project

Keep what makes the case valuable: the structure of the conversation, the contradictions, the vague answers, the crosstalk.

When in doubt, write a synthetic fixture instead. A realistic synthetic transcript is almost always good enough.

## If something slips through

Tell the maintainer immediately. We remove the file and rewrite the git history; a normal revert is not enough because the history stays public.
