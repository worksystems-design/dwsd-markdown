"""Build the agent guide for one contract: contracts/<version>.guide.md.

    python contracts/build-guide.py            # write the guide for the newest contract
    python contracts/build-guide.py 1.8        # for a named contract
    python contracts/build-guide.py --check    # fail if the committed guide differs

The guide is generated from contracts/<version>.json (folders, required keys, fields with
kind, values and targets) plus contracts/guide-source.yaml (meaning, rules, examples), so it
cannot drift from the contract. Needs PyYAML. Output is LF-only and under 8 KB.
"""
import json
import pathlib
import sys

import yaml

root = pathlib.Path(__file__).resolve().parent.parent
cdir = root / "contracts"
LIMIT = 8 * 1024

args = [a for a in sys.argv[1:] if not a.startswith("--")]
check = "--check" in sys.argv

contracts = sorted(cdir.glob("*.json"), key=lambda p: tuple(int(n) for n in p.stem.split(".")))
path = (cdir / f"{args[0]}.json") if args else contracts[-1]
version = path.stem
contract = json.loads(path.read_text(encoding="utf-8"))
source = yaml.safe_load((cdir / "guide-source.yaml").read_text(encoding="utf-8"))
if "fields" not in next(iter(contract["types"].values())):
    sys.exit(f"{path.name} has no fields; the guide starts at 1.4 (use 1.8 or newer)")

RELATION = {"wikilink", "locator", "text-or-wikilink"}


def field(name, spec):
    kind = spec["kind"]
    if kind in RELATION:
        t = "|".join(spec.get("targets", ["any"]))
        head = {"wikilink": "→", "locator": "locator →", "text-or-wikilink": "text or →"}[kind]
        return f"`{name}` {head} {t}"
    if kind in ("enum", "token-or-list") and spec.get("values"):
        vals = "|".join(spec["values"])
        return f"`{name}` {vals}" + (" (or other)" if spec.get("open") else "")
    if kind == "enum":
        return f"`{name}`"
    return f"`{name}` ({kind})" if kind not in ("string", "token-or-list") else f"`{name}`"


shared = ", ".join(f"`{n}`" for n, s in contract["shared-fields"].items() if "earlier-form-of" not in s)
out = [f"# DWSD format {version} — guide for agents", "", source["intro"].strip(), "", "## Rules", ""]
out += [f"- {r}" for r in source["rules"]]
out += ["", f"Any entity may also carry: {shared}.", "", "## Types", ""]

for name, entry in contract["types"].items():
    if not entry.get("entity"):
        continue
    folders = " / ".join(f"`{f}/`" for f in entry["folders"])
    req = ", ".join(f"`{r}`" for r in entry["required"])
    out.append(f"### {name} — {folders}")
    out.append(source["meaning"][name])
    line = "Fields: " + "; ".join(field(n, s) for n, s in entry["fields"].items()) if entry["fields"] else ""
    if req:
        out.append(f"Required: {req}.")
    if line:
        out.append(line + ".")
    out.append("")

for rule in contract.get("rules", []):
    w = rule["when"]
    out.append(f"Rule: a `{rule['type']}` whose `{w['field']}` contains `{w['contains']}` "
               f"needs `{rule['require']['field']}` ({'|'.join(rule['require']['oneOf'])}).")
out += ["", "## Minimal examples", ""]
for name, text in source["examples"].items():
    out += [f"`{source['example-paths'][name]}`", "```markdown", text.rstrip(), "```", ""]

text = "\n".join(out).rstrip() + "\n"
size = len(text.encode("utf-8"))
target = cdir / f"{version}.guide.md"

if check:
    ok = target.exists() and target.read_bytes() == text.encode("utf-8")
    print(f"{target.name}: {'ok' if ok else 'differs from the generated guide'} ({size} bytes)")
    sys.exit(0 if ok else 1)

target.write_bytes(text.encode("utf-8"))
print(f"{target.name}: {size} bytes" + ("" if size <= LIMIT else f" — over the {LIMIT} limit!"))
sys.exit(0 if size <= LIMIT else 1)
