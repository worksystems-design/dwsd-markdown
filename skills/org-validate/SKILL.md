---
name: org-validate
description: >-
  Validate a DWSD organization folder — frontmatter, wikilink, @handle, and ladder
  integrity. Use when asked to validate, check, or lint a DWSD org.
argument-hint: "[org-folder] (defaults to the current folder)"
---

# org-validate

Validate the DWSD organization rooted at **$ARGUMENTS** (default: the current working
directory). You are the validator — use Glob, Grep, and Read; no parser needed. The
authoritative type list and contracts are bundled with this plugin
(`${CLAUDE_PLUGIN_ROOT}/conventions.md`, `${CLAUDE_PLUGIN_ROOT}/types/`). This is
**read-only** — do not modify files; offer fixes only after reporting.

Report findings as `file:line — issue`, grouped, with a final **PASS / FAIL** summary:

1. **Frontmatter sanity** — every `.md` entity has a valid `type:` and any required
   discriminator. Folder placement follows the *conceptual* type, not the bare `type:`:
   - `type: unit` **with** `flightlevel` → `work-systems/`; without → `units/`.
   - `type: interaction` (including `interaction-type: meeting`) → `interactions/`.
   - every other type → its plural folder (`signal` → `signals/`, …).
   Flag a `visualization` missing `visualization-type`, an `agreement` missing
   `agreement-type`, or an `interaction` missing `interaction-type`.
2. **Wikilink integrity** — collect every `[[Target]]` (frontmatter and body) and confirm a
   file `Target.md` exists somewhere in the org (labels are unique). Report danglers.
3. **Handle integrity** — for every `@handle` in ` ```board ` / ` ```flightroute ` fences,
   confirm it maps to an entity slug (kebab-case of a filename); for every `@handle#Column`,
   confirm the column exists in that work system's board.
4. **Ladder integrity** — every `derived-from` resolves; trace
   signal → insight → driver → proposal → agreement chains and report breaks.
5. **Type coverage** (informational) — list which of the 16 types are present / absent
   (remember: work systems are `unit`+`flightlevel`; meetings are
   `interaction`+`interaction-type: meeting`).
