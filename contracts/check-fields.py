"""Check that the newest contract's fields match the Frontmatter tables on the type pages.

Run from the repo root: python contracts/check-fields.py
Exits 1 and lists each key that is on a page but not in the contract, or the other way round.
"""
import json
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
contracts = sorted((root / "contracts").glob("*.json"),
                   key=lambda p: tuple(int(n) for n in p.stem.split(".")))
contract = json.loads(contracts[-1].read_text(encoding="utf-8"))
shared = set(contract.get("shared-fields", {}))

# A page that describes a kind of entity rather than a type of its own.
PAGE_TYPE = {"work-system": "unit", "meeting": "interaction"}

def page_keys(path):
    keys, inside = set(), False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            inside = line.strip() == "## Frontmatter"
            continue
        if inside and line.startswith("| `"):
            first = line.split("|")[1]
            keys |= set(re.findall(r"`([^`]+)`", first))
    return keys

problems = []
seen = {}
for page in sorted((root / "types").glob("*.md")):
    name = PAGE_TYPE.get(page.stem, page.stem)
    entry = contract["types"].get(name)
    if entry is None or "fields" not in entry:
        problems.append(f"{page.name}: no type '{name}' with fields in {contracts[-1].name}")
        continue
    fields = entry["fields"]
    known = {"type"} | set(fields) | shared
    for f in fields.values():
        known |= set(f.get("aliases", []))
    for f in contract.get("shared-fields", {}).values():
        known |= set(f.get("aliases", []))
    keys = page_keys(page)
    for key in sorted(keys - known):
        problems.append(f"{page.name}: '{key}' is on the page but not in the contract")
    seen.setdefault(name, set()).update(keys)

for name, entry in contract["types"].items():
    for key in sorted(set(entry.get("fields", {})) - seen.get(name, set())):
        problems.append(f"{contracts[-1].name}: {name}.{key} is in the contract but on no type page")

for p in problems:
    print(p)
print(f"{contracts[-1].name}: {'ok' if not problems else f'{len(problems)} problem(s)'}")
sys.exit(1 if problems else 0)
