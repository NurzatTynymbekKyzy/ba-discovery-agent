#!/usr/bin/env python3
"""Turn the human-edited templates in templates-source/ into the files a skill
uses to build Google Docs and Sheets.

BAs edit ordinary files:
  templates-source/<skill>/<name>.xlsx   a Sheet template (Excel or Google Sheets export)
  templates-source/<skill>/<name>.docx   a Doc template   (Word or Google Docs export)

This script converts all of a skill's templates into one compact file:
  plugins/ba-discovery/skills/<skill>/references/templates.json

  { "<name>": {"type": "sheet", "requests": [...], "fallback_csv": "..."},
    "<name>": {"type": "doc", "html": "..."} }

One file, no whitespace, nothing the skill doesn't use: the skill reads it
once per run, and Claude copies the requests into tool calls, so every
character here costs tokens on every run.

Nobody edits the generated file by hand. CI regenerates it on main.

Sheet templates carry: tabs, header row (names, bold, background colour),
column widths, frozen rows, dropdowns with typed values, and static text in
the rows below the header. Anything else (formulas, merged cells, conditional
formatting, dropdowns that point to a range) is reported as unsupported, so
no one believes a feature was carried over when it was not.

Doc templates carry headings, paragraphs, bold and italic text, lists and
tables. Images and unusual styles are reported.

Usage:
  build_templates.py             build every template, write changed files
  build_templates.py --check     exit 1 if the generated file is missing or stale
  build_templates.py --summary   print a Markdown summary of every template (for CI)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOURCE_ROOT = REPO / "templates-source"
SKILLS = REPO / "plugins" / "ba-discovery" / "skills"
DEFAULT_WIDTH_CHARS = 8.43
DROPDOWN_ROWS = 1000
GENERATED_NOTE = (
    "Generated from {source} by tools/templates/build_templates.py. "
    "Do not edit by hand: change the source file instead."
)


class Problems(list):
    def add(self, where: str, msg: str) -> None:
        self.append(f"{where}: {msg}")


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else str(path)


# ---------------------------------------------------------------- sheets

def _hex(cell) -> str | None:
    fill = cell.fill
    if fill is None or fill.fill_type != "solid" or fill.fgColor is None:
        return None
    rgb = fill.fgColor.rgb
    if not isinstance(rgb, str) or len(rgb) < 6 or rgb in ("00000000",):
        return None
    return "#" + rgb[-6:].upper()


def _rgb(hex_value: str) -> dict:
    v = hex_value.lstrip("#")
    return {k: round(int(v[i:i + 2], 16) / 255, 4) for k, i in (("red", 0), ("green", 2), ("blue", 4))}


def _list_values(formula: str | None) -> list[str] | None:
    f = (formula or "").strip()
    if len(f) >= 2 and f[0] == '"' and f[-1] == '"':
        return [v.strip() for v in f[1:-1].split(",") if v.strip()]
    return None


def read_sheet_template(path: Path, problems: Problems) -> dict:
    from openpyxl import load_workbook
    from openpyxl.utils import get_column_letter
    from openpyxl.utils.cell import range_boundaries

    wb = load_workbook(path)
    tabs = []
    for ws in wb.worksheets:
        where = f"{path.name} / tab '{ws.title}'"
        header = []
        for cell in ws[1]:
            if cell.value is not None and str(cell.value).strip():
                header.append((cell.column, str(cell.value).strip()))
        if not header:
            problems.add(where, "row 1 needs column names")
            continue
        if [c for c, _ in header] != list(range(1, len(header) + 1)):
            problems.add(where, "column names must start in A1 with no empty columns between them")
        ncols = len(header)

        rows = []
        for row in ws.iter_rows(min_row=2, max_col=max(ncols, ws.max_column)):
            values = []
            for cell in row:
                v = cell.value
                if isinstance(v, str) and v.startswith("="):
                    problems.add(where, f"{cell.coordinate} has a formula; formulas are not supported")
                    v = None
                if v not in (None, "") and cell.column > ncols:
                    problems.add(where, f"{cell.coordinate} is outside the named columns")
                values.append(v)
            values = values[:ncols]
            rows.append({
                "values": ["" if v is None else v for v in values],
                "bold": [bool(c.font and c.font.bold) for c in row[:ncols]],
            })
        while rows and all(v == "" for v in rows[-1]["values"]):
            rows.pop()

        if ws.merged_cells.ranges:
            problems.add(where, "merged cells are not supported")
        if len(ws.conditional_formatting) > 0:
            problems.add(where, "conditional formatting is not supported")

        options: dict[int, list[str]] = {}
        for dv in ws.data_validations.dataValidation:
            if dv.type != "list":
                problems.add(where, f"validation type '{dv.type}' is not supported, only dropdown lists")
                continue
            values = _list_values(dv.formula1)
            if values is None:
                problems.add(where, f"dropdown {dv.sqref} points to cells; type the values into the dropdown instead")
                continue
            for rng in str(dv.sqref).split():
                c1, _, c2, _ = range_boundaries(rng)
                for col in range(c1, c2 + 1):
                    if col > ncols:
                        problems.add(where, f"dropdown in column {get_column_letter(col)} has no column name")
                    elif options.get(col, values) != values:
                        problems.add(where, f"column {get_column_letter(col)} has two different dropdowns")
                    else:
                        options[col] = values

        frozen = 0
        if ws.freeze_panes:
            digits = "".join(ch for ch in ws.freeze_panes if ch.isdigit())
            letters = "".join(ch for ch in ws.freeze_panes if ch.isalpha())
            frozen = int(digits) - 1 if digits else 0
            if letters and letters != "A":
                problems.add(where, "frozen columns are not supported, only frozen rows")

        first = ws.cell(row=1, column=1)
        columns = []
        for col, name in header:
            dim = ws.column_dimensions.get(get_column_letter(col))
            width = dim.width if dim is not None and dim.width else DEFAULT_WIDTH_CHARS
            column = {"name": name, "width": int(round(width * 7 + 5))}
            if col in options:
                column["options"] = options[col]
            columns.append(column)

        tab = {
            "name": ws.title,
            "freeze_rows": frozen,
            "header": {"bold": bool(first.font and first.font.bold)},
            "columns": columns,
        }
        if _hex(first):
            tab["header"]["background"] = _hex(first)
        if rows:
            tab["rows"] = rows
        tabs.append(tab)
    return {"tabs": tabs}


def _value(value) -> dict:
    if isinstance(value, bool):
        return {"boolValue": value}
    if isinstance(value, (int, float)):
        return {"numberValue": value}
    return {"stringValue": str(value)}


def sheet_requests(spec: dict) -> list[dict]:
    """Exact batchUpdate requests for a spreadsheet created empty (first tab id 0).

    Kept as short as the API allows: header names in one request, header style
    in one request, one width request per run of equal-width columns."""
    reqs: list[dict] = []
    for i, tab in enumerate(spec["tabs"]):
        sid = 0 if i == 0 else 1000 + i
        cols = tab["columns"]
        n = len(cols)
        props = {"sheetId": sid, "title": tab["name"],
                 "gridProperties": {"frozenRowCount": tab["freeze_rows"]}}
        if i == 0:
            reqs.append({"updateSheetProperties": {
                "properties": props, "fields": "title,gridProperties.frozenRowCount"}})
        else:
            reqs.append({"addSheet": {"properties": props}})

        rows = [{"values": [{"userEnteredValue": _value(c["name"])} for c in cols]}]
        any_bold = False
        for row in tab.get("rows", []):
            cells = []
            for v, b in zip(row["values"], row["bold"]):
                cell = {} if v == "" else {"userEnteredValue": _value(v)}
                if v != "" and b:
                    cell["userEnteredFormat"] = {"textFormat": {"bold": True}}
                    any_bold = True
                cells.append(cell)
            rows.append({"values": cells})
        fields = "userEnteredValue,userEnteredFormat.textFormat.bold" if any_bold else "userEnteredValue"
        reqs.append({"updateCells": {"start": {"sheetId": sid, "rowIndex": 0, "columnIndex": 0},
                                     "rows": rows, "fields": fields}})

        fmt: dict = {}
        if tab["header"].get("bold"):
            fmt["textFormat"] = {"bold": True}
        if tab["header"].get("background"):
            fmt["backgroundColorStyle"] = {"rgbColor": _rgb(tab["header"]["background"])}
        if fmt:
            # Full field paths: the Sheets connector rejects the "a(b,c)" mask shorthand.
            parts = (["userEnteredFormat.textFormat.bold"] if "textFormat" in fmt else []) + \
                    (["userEnteredFormat.backgroundColorStyle"] if "backgroundColorStyle" in fmt else [])
            reqs.append({"repeatCell": {
                "range": {"sheetId": sid, "endRowIndex": 1, "endColumnIndex": n},
                "cell": {"userEnteredFormat": fmt},
                "fields": ",".join(parts)}})

        ci = 0
        while ci < n:
            cj = ci
            while cj + 1 < n and cols[cj + 1]["width"] == cols[ci]["width"]:
                cj += 1
            reqs.append({"updateDimensionProperties": {
                "range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": ci, "endIndex": cj + 1},
                "properties": {"pixelSize": cols[ci]["width"]}, "fields": "pixelSize"}})
            ci = cj + 1

        for ci, col in enumerate(cols):
            if col.get("options"):
                reqs.append({"setDataValidation": {
                    "range": {"sheetId": sid, "startRowIndex": 1, "endRowIndex": DROPDOWN_ROWS,
                              "startColumnIndex": ci, "endColumnIndex": ci + 1},
                    "rule": {"condition": {"type": "ONE_OF_LIST",
                                           "values": [{"userEnteredValue": v} for v in col["options"]]},
                             "strict": True, "showCustomUi": True}}})
    return reqs


def build_sheet(path: Path, problems: Problems) -> tuple[dict, dict] | None:
    spec = read_sheet_template(path, problems)
    if problems:
        return None
    first = spec["tabs"][0]
    csv_line = ",".join('"' + c["name"].replace('"', '""') + '"' if "," in c["name"] or '"' in c["name"]
                        else c["name"] for c in first["columns"])
    entry = {"type": "sheet", "requests": sheet_requests(spec), "fallback_csv": csv_line + "\n"}
    return entry, spec


# ------------------------------------------------------------------ docs

def build_doc(path: Path, problems: Problems) -> tuple[dict, dict] | None:
    import mammoth

    with path.open("rb") as fh:
        result = mammoth.convert_to_html(fh)
    for msg in result.messages:
        text = str(getattr(msg, "message", msg))
        if "image" in text.lower():
            problems.add(path.name, "images are not supported")
        elif getattr(msg, "type", "") == "warning":
            problems.add(path.name, text)
    if problems:
        return None
    # Google's HTML import draws table borders only when the table asks for them.
    body = result.value.replace("<table>", '<table border="1">')
    html = "<html><body>" + body + "</body></html>"
    return {"type": "doc", "html": html}, {"html": html}


# ------------------------------------------------------------------ main

def bundle_path(skill: str) -> Path:
    return SKILLS / skill / "references" / "templates.json"


def build_all():
    """Returns ({skill: {name: entry}}, [(source, spec)], [errors])."""
    bundles: dict[str, dict] = {}
    specs, errors = [], []
    for source in sorted(SOURCE_ROOT.glob("*/*")):
        if source.name.startswith(("~$", ".")):
            continue
        problems = Problems()
        if source.suffix == ".xlsx":
            res = build_sheet(source, problems)
        elif source.suffix == ".docx":
            res = build_doc(source, problems)
        else:
            if source.suffix.lower() != ".md":
                errors.append(f"{rel(source)}: only .xlsx and .docx templates are supported")
            continue
        if problems or res is None:
            errors.append(f"{rel(source)}:\n" + "\n".join(f"    - {p}" for p in problems))
            continue
        entry, spec = res
        skill = source.parent.name
        bundles.setdefault(skill, {"_generated": GENERATED_NOTE.format(source=f"templates-source/{skill}/")})
        bundles[skill][source.stem] = entry
        specs.append((source, spec))
    return bundles, specs, errors


def render(bundle: dict) -> str:
    return json.dumps(bundle, ensure_ascii=False, separators=(",", ":")) + "\n"


def summary(specs) -> str:
    import re
    lines = ["| Template | Type | Content |", "|---|---|---|"]
    for source, spec in specs:
        if "tabs" in spec:
            parts = []
            for tab in spec["tabs"]:
                cols = ", ".join(c["name"] + (f" ▾({'/'.join(c['options'])})" if c.get("options") else "")
                                 for c in tab["columns"])
                rows = f" · {len(tab['rows'])} preset rows" if tab.get("rows") else ""
                parts.append(f"**{tab['name']}**: {cols}{rows}")
            lines.append(f"| `{source.name}` | Sheet | {'<br>'.join(parts)} |")
        else:
            heads = re.findall(r"<h[1-3]>(.*?)</h[1-3]>", spec["html"])
            lines.append(f"| `{source.name}` | Doc | {' · '.join(re.sub('<[^>]+>', '', h) for h in heads)} |")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--summary", action="store_true")
    args = ap.parse_args(argv)

    bundles, specs, errors = build_all()
    for e in errors:
        print(f"✗ {e}")

    if args.summary:
        print(summary(specs))
        return 1 if errors else 0
    if errors:
        print("Nothing written: fix the templates above first.")
        return 1

    stale = False
    for skill, bundle in bundles.items():
        out = bundle_path(skill)
        text = render(bundle)
        current = out.read_text(encoding="utf-8") if out.exists() else None
        if current == text:
            print(f"= {rel(out)} ({len(bundle) - 1} templates)")
        elif args.check:
            print(f"✗ {rel(out)} is out of date")
            stale = True
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text, encoding="utf-8")
            print(f"✓ {rel(out)} ({len(bundle) - 1} templates)")
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
