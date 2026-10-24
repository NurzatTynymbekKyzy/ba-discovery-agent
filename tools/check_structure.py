#!/usr/bin/env python3
"""Check plugins/ba-discovery/skills/discovery-setup/references/structure.yaml.

The discovery-setup skill creates exactly what this file lists, and other
skills find items by their `key`. A mistake here would break every new
Discovery, so CI checks it on every change:

  - the root has a name containing {project}
  - every item has a key, a type and a name
  - keys are unique snake_case identifiers
  - types are folder, doc or sheet; only folders have `items`
  - every doc and sheet names a template that exists, both as source and built
  - names are unique within the same folder

Exit code 0 when the file is valid, 1 otherwise.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
STRUCTURE = REPO / "plugins/ba-discovery/skills/discovery-setup/references/structure.yaml"
TYPES = {"folder", "doc", "sheet"}
TEMPLATE_SOURCE = REPO / "templates-source/discovery-setup"
TEMPLATE_BUNDLE = REPO / "plugins/ba-discovery/skills/discovery-setup/references/templates.json"
KEY_RE = re.compile(r"^[a-z][a-z0-9_]*$")


def check(path: Path) -> list[str]:
    global BUNDLE
    BUNDLE = json.loads(TEMPLATE_BUNDLE.read_text(encoding="utf-8")) if TEMPLATE_BUNDLE.exists() else {}
    problems: list[str] = []
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return ["the file must be a mapping with `root` and `items`"]

    root_name = (data.get("root") or {}).get("name", "")
    if "{project}" not in str(root_name):
        problems.append("root.name must contain {project}")

    seen_keys: set[str] = set()

    def walk(items, where: str) -> None:
        if not isinstance(items, list) or not items:
            problems.append(f"{where}: `items` must be a non-empty list")
            return
        names: set[str] = set()
        for item in items:
            if not isinstance(item, dict):
                problems.append(f"{where}: every item must be a mapping")
                continue
            key, typ, name = item.get("key"), item.get("type"), item.get("name")
            label = f"{where}/{name or key or '?'}"
            if not key or not KEY_RE.match(str(key)):
                problems.append(f"{label}: key must be snake_case (got {key!r})")
            elif key in seen_keys:
                problems.append(f"{label}: duplicate key {key!r}")
            else:
                seen_keys.add(key)
            if typ not in TYPES:
                problems.append(f"{label}: type must be one of {sorted(TYPES)} (got {typ!r})")
            if not name or not str(name).strip():
                problems.append(f"{label}: missing name")
            elif name in names:
                problems.append(f"{label}: duplicate name in the same folder")
            else:
                names.add(name)
            extra = set(item) - {"key", "type", "name", "items", "template"}
            if extra:
                problems.append(f"{label}: unknown fields {sorted(extra)}")
            template = item.get("template")
            if typ in ("doc", "sheet"):
                if not template:
                    problems.append(f"{label}: every doc and sheet needs a template")
                else:
                    ext = {"doc": ".docx", "sheet": ".xlsx"}[typ]
                    if not (TEMPLATE_SOURCE / f"{template}{ext}").exists():
                        problems.append(f"{label}: template source {template}{ext} not found in templates-source/discovery-setup/")
                    entry = BUNDLE.get(template)
                    if entry is None:
                        problems.append(f"{label}: template {template} missing from templates.json; run tools/templates/build_templates.py")
                    elif entry.get("type") != typ:
                        problems.append(f"{label}: template {template} is a {entry.get('type')}, but the item is a {typ}")
            elif template:
                problems.append(f"{label}: folders don't take a template")
            if "items" in item:
                if typ != "folder":
                    problems.append(f"{label}: only folders can contain items")
                else:
                    walk(item["items"], label)

    walk(data.get("items"), "root")
    return problems


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else STRUCTURE
    problems = check(path)
    shown = path.relative_to(REPO) if path.is_relative_to(REPO) else path
    if problems:
        print(f"✗ {shown}")
        for p in problems:
            print(f"    - {p}")
        return 1
    print(f"✓ {shown} is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
