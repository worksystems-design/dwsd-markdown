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
   `agreement-type`, or an `interaction` missing `interaction-type`. **Warn** on
   `type: meeting` (→ `type: interaction` + `interaction-type: meeting`).
   - **Team integrity:** a unit whose `unit-type` includes `team` should have at least one
     individual with `member-of` naming it — **note** a team without members (its size
     would read as zero).
   - **Work-system integrity:** a unit whose `unit-type` includes `work-system` **must**
     have a `flightlevel` (flag if missing). Conversely, **warn** on a unit that has a
     `flightlevel` but does *not* list `work-system` in `unit-type` — `flightlevel` no
     longer makes a unit a work system, so this is likely an authoring slip.
2. **Wikilink integrity** — collect every `[[Target]]` (frontmatter and body) and confirm a
   file whose label matches it exists somewhere in the org, by key: cut at `|`, trim,
   `NFC(lowercase(NFC(label)))` — no `ß`→`ss`, no transliteration, never by slug (see
   `conventions.md` › Filename = label = slug). A note (a file without `type:`) is a valid
   target. Report danglers. Flag two files in one org whose labels share a key.
3. **DSL fence & locator integrity** — three checks:
   - **Route fences** (` ```dwsd.flightroute `) — only the closed key set `title:` /
     `tags:` / `for:` / `for-domain:` / `bands:` / `triggers:` / `path:` / `bound-to:`.
     Flag retired forms: a `route "…"` header or a root `route:` key (→ `title:`), the
     legacy keys `fl-path:` (→ `path:`), `fl-triggers:` (→ `triggers:`), `fl-bands:`
     (→ `bands:`) and a `flow:` section (→ `bound-to:`), `@`-handle references, a `deliver` edge (→ `..> ()`), a bare
     `flightroute` fence tag. A wikilink `for:` resolves like any wikilink (broken link
     otherwise) and should name a flight-item-type file — **warn** when it names another
     type; a plain-text `for:` is a description and is not checked.
     `for-domain:` (a quoted wikilink or a list of them) must resolve to a **work system
     or a role** — **warn** otherwise, including when it names a person or a plain unit
     (see `conventions.md` › Up vs. into the detail). A stage item type is text or a wikilink:
     text is **never** looked up or flagged, even when a file of that name exists; a
     wikilink stage resolves like any wikilink (broken link otherwise) and should name a
     flight-item-type file — **warn** when it names another type. (The DSL package
     reports the same cases as `route.unresolved-item-type-ref` and
     `route.item-type-ref-kind`, both warnings: "'[[X]]' is a <kind>, not a
     flight-item-type — link a flight-item-type or write the stage as plain text".) Flag
     an unquoted path / `generates:` line that contains `[[` (YAML reads it as a list).
     **Warn** when one band holds two stages whose names differ only by case or by
     link-vs-text (`[[Feature]] @ Train` and `feature @ Train`). Every band named in a `path:`
     edge or a trigger's `generates:` must be declared in `bands:` (`fl` ∈ 1..3 or a
     numeric span; a pure custom band omits `fl` — never flag that). Edge sanity: one hop per line; `()` reached only via `..>`; `->`
     stays inside one band, `-->` crosses bands (warn otherwise). **Flow ⊆ Path:** every
     `bound-to:` `band` is declared in `bands:`, and every pinned item type lives in that
     band per `path:`; each `board:` wikilink resolves to a visualization file, and each
     pinned locator segment (`lane:` / `col:` / …) names a unit present in that board's
     YAML.
   - **Board fences** (` ```dwsd.board `) — the name key is `title:` (a root `board:`
     key is retired); flag a hyphenated `dwsd-board` fence tag (it highlights but does
     not render). Inline inside-out `agreements:` / `interactions:` keys on a
     column/lane/group are valid board content, not references to resolve.
   - **Change trail fences** (` ```dwsd.change-trail `) — the body may be empty; the only
     keys are `focus:` (a wikilink that must resolve), `show:` (`all` | `open` | `recent`)
     and `radius:` (a whole number or `inf`). **Warn** on any other key or value.
   - **Fence ids** (any of the six fences, e.g. ` ```dwsd.board id=intake `) — optional,
     never flag a fence without one. Flag two fences in one file with the same id; **warn**
     when the value is not kebab-case (`[a-z0-9][a-z0-9-]*`), is quoted, or follows another
     attribute. Match a fence by its tag only — text after the tag never hides a fence.
   - **Locator** — `interaction-of` / `agreement-of` carry a locator
     `[[Board]]#BoardName/col:Column::in` (or `[[Board]]#BoardName::in` for the whole
     board, a bare `[[entity]]` — a work system, a **unit** or a **person** (two persons
     make a 1:1) — for an entity anchor, or
     `[[Route]]/stage:itemType @ Band::in` for a **route stage**). Confirm the target
     file exists (a bare entity anchor that names a plain unit or a person is valid —
     never flag it); any `col:` / `lane:` / `group:` / `split:` segment names a unit present
     in that board's YAML — a board locator that lands nowhere is reported with one of three
     reasons: `document-not-indexed` (the board file is not in the org), `board-not-found`
     (no board of that title in the file, or a wrong `#BoardName`), `unit-not-found` (the
     board exists but has no unit at that path); a `stage:` segment names an `itemType @ Band` pair — the token, or a linked stage's
     target without brackets, matched exactly — the route's
     `path:` (or a trigger's `generates:`) actually places in that band.
   - **Meeting tables** — in a meeting's `## Interactions` (or `## Agreements`) table, a
     row whose `Name` is a `[[…]]` link must resolve to an interaction (or meeting /
     agreement) file. Its `Outcome` and `Interaction of` (`Agreement of`) cells should be
     empty; if filled, they are a copy — **warn** when the anchor cell differs from the
     file's `interaction-of` (`agreement-of`), and note a differing outcome. The file wins;
     never merge the two.
   - **`for-domain`** on any entity names a **work system or a role** (a list may mix
     them) — both are valid; **warn** only when it names a person or a plain unit.
   - **Board-binding consistency (informational):** when an entity carries both
     `for-domain` (a work system) and a board-position `interaction-of` / `agreement-of`,
     **note** — not warn — if the anchored board's work system (its `visualization-of`)
     differs from `for-domain`. Cross-level on purpose is common (an FL2 domain meeting at
     an FL1 board); list it so the author can confirm, but it never affects PASS/FAIL.
4. **Ladder integrity** — every `derived-from` resolves; trace
   signal → insight → driver → proposal → organizational-decision-record → agreement(s)
   chains and report breaks. Steps may be skipped: an agreement whose `derived-from`
   names the **proposal** it was consented from (no ODR in between) is valid, and so is
   an ODR without `derived-from` — report those as informational, not as breaks. A break
   is a `derived-from` that does not resolve, or one that points *down* the ladder. `derived-from` is the shared emergence key (any entity may carry
   it); reading it in reverse from an ODR yields that decision's **bundle** of agreements.
5. **Type coverage** (informational) — list which of the 16 types are present / absent
   (remember: work systems are `unit` whose `unit-type` includes `work-system`; meetings are
   `interaction`+`interaction-type: meeting`).
