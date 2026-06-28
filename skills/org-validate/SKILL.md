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
   - `type: unit` whose `unit-type` **includes `work-system`** → `work-systems/`; otherwise
     → `units/`.
   - `type: interaction` (including `interaction-type: meeting`) → `interactions/`.
   - every other type → its plural folder (`signal` → `signals/`, …).
   Flag a `visualization` missing `visualization-type`, an `agreement` missing
   `agreement-type`, or an `interaction` missing `interaction-type`.
   - **Work-system integrity:** a unit whose `unit-type` includes `work-system` **must**
     have a `flightlevel` (flag if missing). Conversely, **warn** on a unit that has a
     `flightlevel` but does *not* list `work-system` in `unit-type` — `flightlevel` no
     longer makes a unit a work system, so this is likely an authoring slip.
2. **Wikilink integrity** — collect every `[[Target]]` (frontmatter and body) and confirm a
   file `Target.md` exists somewhere in the org (labels are unique). Report danglers.
3. **Handle & locator integrity** — two distinct reference forms:
   - **Route `@handle`** — for every `@handle` in ` ```flightroute ` fences, confirm it maps to
     an entity slug (kebab-case of a filename); for every `@work-system#Column`, confirm the
     column exists in that work system's board (its ` ```dwsd-board ` fence, found via
     `visualization-of`).
   - **Board locator** — `interaction-of` / `agreement-of` carry a locator
     `[[Board]]#BoardName/col:Column::in` (or `[[Board]]#BoardName::in` for the whole board, or
     a bare `[[Work System]]` for a work-system anchor). Confirm the `[[Board]]` file exists and
     that any `col:` / `lane:` / `group:` / `split:` segment names a unit present in that board's
     ` ```dwsd-board ` YAML. Inline inside-out `agreements:` / `interactions:` keys on a
     column/lane/group are valid board content, not references to resolve.
   - **Board-binding consistency:** when an entity carries both `for-domain` (a work system)
     and a board-position `interaction-of` / `agreement-of`, **warn** if the anchored board's
     work system (its `visualization-of`) differs from `for-domain`.
4. **Ladder integrity** — every `derived-from` resolves; trace
   signal → insight → driver → proposal → agreement chains and report breaks.
5. **Type coverage** (informational) — list which of the 16 types are present / absent
   (remember: work systems are `unit` whose `unit-type` includes `work-system`; meetings are
   `interaction`+`interaction-type: meeting`).
