# Basic UX rules for the low-fi wireframe

Apply these to the screen map and to every screen. They decide layout, flow and states; never features. Anything a rule needs that no requirement asks for (a confirmation, a filter) is an assumption, marked as such.

## Each screen

1. **One job, one primary action.** One `btn primary` per screen, for the main step forward; everything else is `btn` (secondary). A destructive action (cancel, delete) is `btn danger`, never primary.
2. **Clear title and way back.** An `h1` that names the screen in the user's words; a `crumbs` line or a back link on every screen below the first level.
3. **Most important first.** What the user came for at the top; details and secondary actions below. On a phone it reads top to bottom in the same order.
4. **Words from the requirements.** Labels, buttons and messages use the client's terms (as in the register), as verbs on buttons ("Book class", not "Submit"). The same thing has the same name on every screen.
5. **Low-fi, not designed.** Greyscale kit classes only. Text that isn't decided yet is a `ph-line`; pictures, maps and charts are a `ph-img` or a `placeholder` with a one-line label. Realistic sample data where the requirement needs it (dates, names, amounts), 3 to 6 rows per list.

## Flows

6. **Every step can be finished or left.** Each flow ends on a confirmation (`notice`) that says what happened and what comes next; every screen has a way back.
7. **Confirm what can't be undone.** A destructive or costly action shows a confirmation first (a `card` with the consequence and two buttons), unless a requirement says otherwise.
8. **Fewest steps.** Don't add a screen a requirement doesn't need; a short form goes on the screen where it's used.

## States: show the ones the requirements imply

9. For every list and every form, decide which states matter and show them on the same screen as `state` blocks with a `state-label`: **Empty** (no items yet, with the action that fills it), **Error** (what went wrong and how to fix it), **Not allowed** (a rule in the requirements blocks the action, for example a deadline passed), **Success**. Show only states that a requirement or a flow makes possible.

## Forms

10. Label above each field (`field` with a `span`), required fields marked `<span class="req-mark">*</span>`, help text under the field (`help`) when the format isn't obvious, sensible defaults. One error example per form: the field with `invalid` and an `error-text` under it.
11. Touch-friendly: the kit's buttons and inputs are at least 44 px tall; don't make them smaller.

## UX notes

12. Where a design choice isn't obvious, add one short `<div class="ux-note">` under the element: why it is there or what a designer must decide (for example "Countdown must stay visible on small screens"). At most 2–3 per screen. The toolbar's "Show UX notes" reveals them; they go into the screen spec too.
