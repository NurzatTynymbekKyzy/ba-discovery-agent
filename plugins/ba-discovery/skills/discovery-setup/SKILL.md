---
name: discovery-setup
description: Sets up a new Discovery workspace on the BA's Google Drive - the standard numbered folder structure with empty Google Docs and Sheets (Discovery Plan, RAID Log, Decision Log, Stakeholder Matrix, Context Canvas, Requirements Register, Open Questions Log and more) plus a record the other skills use. Use this whenever a BA kicks off a new project, client engagement or Discovery and wants the Drive folders or workspace prepared, even if they only say "start a new discovery for X" or "prepare the drive for the new client". Also use it to check an existing Discovery folder and add whatever is missing.
---

# Discovery setup

## Purpose

Give a BA who starts a new Discovery a ready workspace on Google Drive in one step. Every Discovery gets the same structure, so the BA, the client team and the other skills of this plugin always know where things live.

## When to use

- "Set up a new Discovery for project Atlas"
- "Create the Drive folders for our new client project"
- "Some folders are missing in the Atlas Discovery, can you fix the structure?"

## When not to use

- Summarizing a workshop or transcript: `workshop-summary`
- Filling in or analyzing documents: other skills of this plugin
- Questions about how to organize a Discovery in general: answer directly, create nothing

## Inputs

| Input | Required | Source | If missing |
|---|---|---|---|
| Project name | Yes | The BA's request | Ask for it. Do not invent one |
| Location | No | A Drive folder the BA names | Use the root of My Drive and say so in the plan |
| Google Drive connector | Yes | The BA's Claude connectors | Explain how to enable it; stop |

## Output

On the BA's Google Drive, inside the chosen location:

- the folder `{project} — Discovery` with exactly the folders, empty Docs and empty Sheets listed in `references/structure.yaml`;
- `_agent/discovery.yaml`, a record of every created item and its Drive id, in the format in `references/discovery-record.md`.

## Procedure

1. **Read the structure.** Read `references/structure.yaml`. It is the only source of what to create. Do not add, drop or rename anything.

2. **Get the inputs.** Take the project name from the request. If there is none, ask for it and stop until the BA answers. Use the name exactly as the BA wrote it. If the BA named a location, keep it for step 4; otherwise the location is the root of My Drive.

Steps 3 to 5 only read. Do all of them before asking for approval, so the BA approves one plan that is known to be possible, and approves only once.

3. **Check that Google Drive is reachable.** Look for the Google Drive tools (`create_file`, `search_files`). Some environments load tools on demand: if you have a tool search, search for "Google Drive" before deciding they are missing.

   If the Drive tools are not available, reply with:
   - the plan (location as the BA named it, or the root of My Drive, and the full tree as in step 6), so the BA sees what they will get;
   - how to fix it: "I can't reach your Google Drive yet. In Claude, open Settings → Connectors and connect Google Drive. If it is already connected, turn it on for this chat in the chat's connector menu. Then ask me again and I'll create the workspace.";
   - no question "Shall I create it?": there is nothing to approve yet.

   Then stop. Do not describe anything as created.

4. **Find the location.** If the BA named a location, find it with `search_files` (`title = '<name>' and mimeType = 'application/vnd.google-apps.folder'`). One match: use it. Several: list them with their parent folder or owner and ask which one; stop until the BA answers. None: say the folder wasn't found, ask for another folder or offer the root of My Drive; stop until the BA answers. Use `'root'` for My Drive.

5. **Check for an existing workspace.** Search the location for a folder named exactly `{project} — Discovery`.
   - Not found: everything will be created.
   - Found: list what is inside it, level by level, and compare with the structure by name and type. Only the missing items will be created. Never rename, move, change or delete anything the BA already has.
   - Found and nothing is missing: tell the BA the workspace is already complete, give the link, and stop. There is nothing to approve.

6. **Show the plan and ask for approval (gate).** Show:
   - the location (the folder found in step 4, or "the root of your My Drive");
   - for a new workspace: the full tree, as a code block, with `{project}` replaced and each file marked `(Doc)` or `(Sheet)`;
   - for an existing workspace: what already exists and the list of missing items that will be added; if `_agent/discovery.yaml` exists, that the old record will be moved to Drive trash and replaced by an updated one;
   - one line: "All files are created empty. Nothing is shared, moved or deleted."

   Then ask: "Shall I create it?" Stop and wait. Continue only on a clear yes. If the BA asks for a different structure, explain that this skill creates the standard structure so that every Discovery and every skill finds things in the same place, and that they can add their own folders afterwards.

7. **Create the items.** Create the root folder first (if needed), then the items in the order they appear in the structure, each folder before its contents. Use `create_file` with:
   - `title`: the item's name;
   - `parentId`: the id of the folder it belongs to;
   - `contentMimeType`: `application/vnd.google-apps.folder`, `application/vnd.google-apps.document` or `application/vnd.google-apps.spreadsheet`;
   - no content.

   Keep the id Drive returns for every item. If a call fails, retry it once. If it fails again, stop creating and go to step 9.

8. **Write the record.** Create `_agent/discovery.yaml` as described in `references/discovery-record.md`, using only ids returned by Drive or found in step 5.

9. **Verify and report.** List the contents of the root folder and each subfolder and compare them with the structure. Then report in a few lines:
   - the link to the root folder;
   - how many items were created (and, on a re-run, how many already existed);
   - anything missing, with the reason, and that running the setup again will complete it;
   - the next step: "Put the client's materials into `02 Client Inputs` and meeting transcripts into `03 Meetings/Transcripts`."

## Gate

- The BA sees the location and the full tree (or, on a re-run, the list of missing items) before anything is created.
- Approval is a clear yes ("yes", "go", "create it", "да"). Anything else, including a question, is not approval: answer it and ask again.
- Approval covers this one run only.

## Rules, and why they matter

- **Create exactly what `references/structure.yaml` lists, with those names and types.** Other skills find files by these names and by the keys in `_agent/discovery.yaml`; a renamed or extra file breaks them, and BAs moving between Discoveries rely on the same layout.
- **Create only inside the approved location, and create the files empty.** The BA approved a specific plan; anything beyond it is a surprise in their Drive, often a shared client Drive.
- **Don't share, move, rename or delete anything.** The BA's Drive may hold client material and permissions set by others; a wrong change there is hard to notice and hard to undo. The one exception is moving the old `_agent/discovery.yaml` to trash on a re-run, and only when the BA approved it in step 6.
- **Report only what Drive confirmed.** Say an item was created only when Drive returned its id. A BA who trusts a wrong "done" will look for files that aren't there in front of a client.
- **Complete an existing workspace instead of creating a second one.** Two folders with the same name split the team's work between them without anyone noticing.

## Failure modes

| Situation | What the skill does |
|---|---|
| No project name | Asks for it; creates nothing |
| Google Drive connector not connected, or off in this chat | Shows the plan, explains how to connect or turn it on, asks no approval question; creates nothing |
| Named location not found, or several matches | Asks the BA to choose; creates nothing until then |
| Workspace already exists | Shows what exists and what is missing; creates only the missing items after approval. If nothing is missing, says so with the link and asks nothing |
| A create call fails twice | Stops; reports what was created and what is missing; says that running setup again completes it |
| BA asks for a custom structure | Explains the standard structure is fixed; offers to create it, after which the BA can add folders |
| BA does not approve | Creates nothing; offers to adjust the location or name |

## Quality criteria

- The plan shown at the gate lists every folder and file from the structure, with the project name filled in.
- Nothing is created before a clear approval.
- After a run, the Drive contents match the structure exactly: no missing, extra or duplicate items.
- A re-run on a complete workspace creates nothing.
- The final report contains a working link to the root folder and states plainly what, if anything, is missing.
