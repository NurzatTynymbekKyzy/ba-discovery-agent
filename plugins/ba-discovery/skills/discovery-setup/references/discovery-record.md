# `_agent/discovery.yaml`

The record `discovery-setup` writes at the end of a run. Other skills read it to find the Discovery's folders and files by `key`, so they never search Drive by name.

Write it as a plain text file named `discovery.yaml` inside the `_agent` folder: `contentMimeType: text/plain`, `disableConversionToGoogleType: true`.

The Drive connector cannot edit a file's content. So on a re-run:

- If nothing was missing, leave the existing record as it is.
- If items were added, create a new `discovery.yaml`, then move the old one to Drive trash with `trash_file`. This step is part of what the BA approves at the gate; without that approval, keep the old file and tell the BA the new record is the one created today.

## Format

```yaml
schema_version: 1
project: Atlas
created_at: 2026-10-24            # date of the first run, YYYY-MM-DD
updated_at: 2026-10-24            # date of this run
created_by: discovery-setup
root:
  id: 1AbC...                     # Drive id of "{project} — Discovery"
  url: https://drive.google.com/drive/folders/1AbC...
items:                            # one entry per key in references/structure.yaml
  readme:            { id: 1xY..., type: doc,    path: "00 README" }
  management:        { id: 1xZ..., type: folder, path: "01 Discovery Management" }
  discovery_plan:    { id: 1x1..., type: sheet,  path: "01 Discovery Management/Discovery Plan" }
  # ... every key from structure.yaml, in the same order
```

## Rules

- Every key from `references/structure.yaml` appears exactly once.
- `path` is the item's location below the root folder, joined with `/`.
- Use the ids Drive returned when creating the items, or, for items that already existed, the ids found when checking the folder. Never invent an id.
