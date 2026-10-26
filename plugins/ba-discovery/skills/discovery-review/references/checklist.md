# "Is it complete?" checklist

Five checks. Each is **OK**, **Gap** or **Not checked** (a document couldn't be read). Run them all; add nothing else.

| # | Area | Check | Gap when | Suggested fix |
|---|---|---|---|---|
| 1 | Context | Canvas sections filled: Problem or opportunity, Business goals, Success metrics, Target users, Scope: in, Scope: out | A section's "What we know" is empty | Ask the client in the next meeting; then `discovery-docs-update` |
| 2 | Requirements | At least one `Business` and one `User` requirement that isn't `Rejected` | Either type has none | Ask the sponsor (Business) or users (User) |
| 3 | Prototype | A `Screen spec` exists in `07 Prototype` | No spec | `prototype` |
| 4 | Prototype | The newest spec covers every `User` and `Functional` requirement that isn't `Rejected`, and none changed after it | A REQ ID is missing from the spec, or its `Last changed` is after the spec's "Register read on" date | `prototype` (update mode) |
| 5 | Open items | No open question with priority P1 or P2; every open risk with priority High has an owner | A P1/P2 question isn't answered or closed; a High risk has no `Owner` | Ask the question or close it with a reason; agree a risk owner |

With no spec, check 4 is "Not checked".

## Answer format

```
{project}: Discovery check, {YYYY-MM-DD}: {n} of 5 OK

1 Context: OK | Gap: {sections}: empty
2 Requirements: OK ({n} Business, {n} User) | Gap: no {type} requirement
3 Prototype exists: OK (Screen spec v{N}, {date}) | Gap: no screen spec
4 Prototype current: OK | Gap: {REQ IDs} not in the spec; {REQ IDs} changed after it
5 Open items: OK | Gap: {Q IDs} ({priority}) open; {Risk IDs} High without owner

Fix first: {the gap that blocks handover most, with its fix}
```

Write the five lines first, then the header: `{n}` is the number of lines that say OK. Each gap names the document and the rows or sections, so the BA can find it. Write in the language of the documents.
