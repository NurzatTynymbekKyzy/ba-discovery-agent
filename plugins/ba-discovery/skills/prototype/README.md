# Prototype

**Status:** In progress
**Maintainer:** @NurzatTynymbekKyzy

## What it does for you

Turns your Requirements Register into:

- a **clickable wireframe** to walk the client through the product: screens, flows and realistic sample data, neutral on purpose so the client talks about flows and content, not colours. A "Show requirements" toggle puts the REQ ID next to every element, and a coverage screen shows which requirement is on which screen, which have no screen, and which elements are assumptions;
- a **screen spec** Google Doc for the designers: flows, screens, elements and their behaviour, states, REQ IDs, assumptions, and what changed since the last version.

After the client's feedback it updates both and saves a new version; earlier versions stay.

## How to use it

1. Make sure the Requirements Register is current (`discovery-docs-update` after each meeting).
2. Ask, for example:
   - "Build a prototype from the requirements"
   - "Update the prototype after the feedback session" (name the transcript to include the client's comments on the screens)
3. Approve the screen map first (cheap to change), then the built wireframe.
4. Share the wireframe with the client from the chat (the app's share or publish option). Drive keeps the file and the spec in `07 Prototype`, but Drive doesn't open HTML files as pages.

## What it won't do

- Use requirements with status Rejected.
- Add features nobody asked for. Anything the flow needs that isn't in the register is marked as an assumption, on the wireframe and in the spec.
- Do the visual design. Designers do that in Figma, from the screen spec; they can import the shared wireframe page with an HTML-to-Figma plugin as a starting frame.

## What you need

- A Discovery workspace created by `discovery-setup` (older workspaces get a `07 Prototype` folder on the first save)
- Google Drive and Google Sheets connected in Claude, on the same Google account

## Credits

The screen manifest, the link map between screens, design tokens shared by every screen and the build order follow the prototype guide in [aws-samples/sample-kiro-cli-prompts-for-product-teams](https://github.com/aws-samples/sample-kiro-cli-prompts-for-product-teams) (MIT-0). The kit, procedure, traceability and update mode are this project's own.

## Smoke test

| Date | Version | Who | Result | Notes |
|---|---|---|---|---|

## Changelog

| Version | Change |
|---|---|
| 0.7.0 | First version |
