# Screen map, wireframe and screen spec formats

Write screen names, labels and sample data in the language of the register.

## Screen map (chat, at the first gate)

```
Wireframe v1 — {project}
Users: {roles from the register}

Flow: {name}  ({role})
  1. {Screen}  →  2. {Screen}  →  3. {Screen}

Screens
| # | Screen (id) | For | What's on it | Requirements |
| 1 | Class list (class-list) | Member | List of classes with free places, filter by club, "Book" | REQ-002, REQ-005 |

Assumptions (not in the register; marked on the wireframe)
- {screen}: {element}, because {why the flow needs it}

Not shown as a screen
- REQ-001 (Business): a goal, no screen of its own
- REQ-0xx (Non-functional): availability, not visible
```

- One row per screen, including states that matter (empty list, confirmation, error).
- Every functional and user requirement that can be shown appears in at least one row. Business and non-functional requirements go under "Not shown as a screen" unless one clearly has a screen.
- An element no requirement asks for is an assumption, listed and marked, never silently added.

## Wireframe (one HTML file)

Copy `wireframe-kit.html` unchanged and fill its three markers:

- **title:** `{project} — Wireframe v{N}`.
- **sidebar:** `<aside class="sidebar">` with `<div class="sidebar-logo">{project}</div>`, one `<a class="nav-item" data-go="{id}">{name}</a>` per main screen (not per state), and `<div class="sidebar-footer">Wireframe v{N} · {YYYY-MM-DD}</div>`.
- **screens:** one `<section class="screen" id="{id}">` per row of the screen map, ids exactly as in the map, then the coverage screen.

Inside screens use only the kit's classes: `page-header`, `card`, `grid`, `stat`, `label`, `table`, `btn`, `btn secondary`, `field`, `badge ok|warn|bad`, `notice`, `placeholder`. No other styles, scripts, images or links to external files.

- **Navigation:** every button, link or row that leads somewhere has `data-go="{target id}"`; nothing is a dead link.
- **Traceability:** after each element that serves a requirement, `<span class="req-tag">REQ-005</span>` (several IDs separated by `, `). The toolbar's "Show requirements" toggle reveals them.
- **Assumptions:** add `class="assumption"` and `<span class="req-tag">assumption</span>`.
- **Sample data:** realistic names, dates and amounts that fit the client's domain; 3 to 6 rows per list.
- **Coverage screen** (`id="coverage"`, last): a table `Requirement | Screen(s)`, then "Not shown as a screen" and "Assumptions" as in the map.

## Screen spec (Google Doc for designers)

HTML for `create_file` (`text/html`):

```html
<h1>{project} — Screen spec v{N}</h1>
<p><b>Date:</b> {YYYY-MM-DD} · <b>Wireframe:</b> {file name} · <b>Register read on:</b> {YYYY-MM-DD}</p>
<h2>Flows</h2>
<ul><li><b>{flow}</b> ({role}): {Screen} → {Screen} → {Screen}</li></ul>
<h2>Screens</h2>
<h3>{n}. {Screen} ({id})</h3>
<p><b>For:</b> {role} · <b>Reached from:</b> {screens} · <b>Leads to:</b> {screens}</p>
<table border="1"><tr><td><b>Element</b></td><td><b>Behaviour</b></td><td><b>Requirements</b></td></tr>
<tr><td>{element}</td><td>{what it shows or does}</td><td>{REQ IDs, or "assumption"}</td></tr></table>
<p><b>States:</b> {empty, error, success, as shown}</p>
<h2>Not shown as a screen</h2><ul><li>{REQ-ID}: {why}</li></ul>
<h2>Assumptions to confirm with the client</h2><ul><li>{screen}: {assumption}</li></ul>
<h2>Changes in this version</h2><ul><li>{screen}: {old} → {new} ({REQ-ID or feedback source})</li></ul>
```

"Changes in this version" is left out for v1. The spec is what update mode reads, so keep its headings exactly.

## Update proposal (chat, first gate in update mode)

Group by screen. For each: `{Screen}: {old} → {new}`, with the reason: the REQ ID and its change (new, changed v{n}, rejected), or the feedback quote with speaker and timestamp. List new screens and removed screens separately. Unaffected screens: one line, "unchanged".
