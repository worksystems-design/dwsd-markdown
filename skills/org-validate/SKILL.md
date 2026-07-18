---
name: org-validate
description: >-
  Validate a DWSD organization folder — frontmatter, wikilink, DSL-fence, locator, and
  ladder integrity. Use when asked to validate, check, or lint a DWSD org.
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
3. **DSL fence & locator integrity** — three checks:
   - **Route fences** (` ```dwsd.flightroute `) — only the closed key set `title:` /
     `tags:` / `for:` / `bands:` / `triggers:` / `path:` / `bound-to:`. Flag retired
     forms: a `route "…"` header or a root `route:` key (→ `title:`), a `flow:` section,
     `@`-handle references, a `deliver` edge (→ `..> ()`), a bare `flightroute` fence tag.
     Confirm `for:` resolves to a flight-item-type file. Every band named in a `path:`
     edge or a trigger's `generates:` must be declared in `bands:` (`fl` ∈ 1..3 or a
     numeric span). Edge sanity: one hop per line; `()` reached only via `..>`; `->`
     stays inside one band, `-->` crosses bands (warn otherwise). **Flow ⊆ Path:** every
     `bound-to:` `band` is declared in `bands:`, and every pinned item type lives in that
     band per `path:`; each `board:` wikilink resolves to a visualization file, and each
     pinned locator segment (`lane:` / `col:` / …) names a unit present in that board's
     YAML.
   - **Board fences** (` ```dwsd.board `) — the name key is `title:` (a root `board:`
     key is retired); flag a hyphenated `dwsd-board` fence tag (it highlights but does
     not render). Inline inside-out `agreements:` / `interactions:` keys on a
     column/lane/group are valid board content, not references to resolve.
   - **Locator** — `interaction-of` / `agreement-of` carry a locator
     `[[Board]]#BoardName/col:Column::in` (or `[[Board]]#BoardName::in` for the whole
     board, a bare `[[Work System]]` for a work-system anchor, or
     `[[Route]]/stage:itemType @ Band::in` for a **route stage**). Confirm the target
     file exists; any `col:` / `lane:` / `group:` / `split:` segment names a unit present
     in that board's YAML; a `stage:` segment names an `itemType @ Band` pair the route's
     `path:` (or a trigger's `generates:`) actually places in that band.
   - **Board-binding consistency:** when an entity carries both `for-domain` (a work system)
     and a board-position `interaction-of` / `agreement-of`, **warn** if the anchored board's
     work system (its `visualization-of`) differs from `for-domain`.
4. **Ladder integrity** — every `derived-from` resolves; trace
   signal → insight → driver → proposal → agreement chains and report breaks.
5. **Type coverage** (informational) — list which of the 16 types are present / absent
   (remember: work systems are `unit` whose `unit-type` includes `work-system`; meetings are
   `interaction`+`interaction-type: meeting`).
