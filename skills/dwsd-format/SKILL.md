---
name: dwsd-format
description: >-
  Read, write, and review DWSD organization entities — the Dynamic Work Systems Design
  markdown format (entity types, frontmatter contracts, wikilink relationships, the board
  and flight-route DSLs, and the flat per-type folder layout). Use whenever creating,
  editing, or reviewing files in a DWSD org folder, or when asked about the DWSD format.
---

# DWSD format

**Spec root** — the folder that holds `conventions.md`, `types/`, `templates/` and
`examples/`; paths below start there (`<spec-root>/…`). In Claude Code it is
`${CLAUDE_PLUGIN_ROOT}`; another host names its own.

DWSD describes an organization as a folder of Markdown files: **one file = one entity**,
and the `type:` field in the frontmatter decides what it is. Entities are grouped into flat
**plural per-type folders** (`individuals/`, `roles/`, `units/`, `work-systems/`,
`interactions/`, `agreements/`, `mandates/`, `signals/`, `insights/`, `drivers/`, `proposals/`,
`decision-records/`, `visualizations/`, `flight-item-types/`, `flight-routes/`,
`ai-agents/`) — the folder is a convenience; the `type:` is authoritative.

## The authoritative spec sits next to this skill — read it

This skill is a thin pointer; the **full contract lives in the spec** at the spec root (the
same files as the `dwsd-markdown` repo). Before authoring or validating, read:

- **`<spec-root>/conventions.md`** — rules for every entity: frontmatter, the
  `type` field, `[[wikilink]]` relationships, `reports-to` (structure) vs `member-of`
  (flow), tracking fields, the `sources` block, the embedded DSL fences, and `.mw` siblings.
- **The org root `README.md`** is a note (`type: readme`; a tour is `type: tour`). Its first `#` heading is the org's
  name, its first paragraph the description; its frontmatter holds `type: readme` and
  `dwsd-format: "1.0.0"`, the format version the folder is written to. When you write a
  file, use the current form of that major version; if what you write needs a newer minor
  (a type the README's version does not have yet), raise the id to that minor in the same
  change and say so; never cross a major — offer the migration instead
  (`<spec-root>/conventions.md` › Format versions).
- **`<spec-root>/types/<type>.md`** — the per-type contract (required vs optional
  frontmatter, relationships, body sections, a worked example). Always open the specific
  type page before authoring that type.
- **`<spec-root>/templates/<type>.md`** — a bare copy-paste skeleton per type.
- **`<spec-root>/examples/`** — two complete worked examples: `goldcrust-bakery/`
  (a small bakery) and `voltfeld/` (a hardware product company with an Agile Release Train).

## Subtypes: the `type:` value is not always the conceptual type

Two conceptual types are expressed as a **base `type:` plus a discriminator** — there is no
`type: work-system` or `type: meeting`. Recognize them by the discriminator, and place them
by the **conceptual** type, not the bare `type:`:

- **work system** = `type: unit` whose **`unit-type` includes `work-system`** (e.g.
  `unit-type: [team, work-system]`); it also carries a `flightlevel: 1|2|3`. Lives in
  `work-systems/` and carries the full domain description. A unit *without* `work-system` in
  its `unit-type` is just a structural unit (e.g. `unit-type: team`) and lives in `units/`.
  `work-system` and `team` are the **reserved** `unit-type` values (English, matched
  without regard to case). `team` marks a stable group of people; its members are the
  individuals whose `member-of` names it (their number is the team's modeled size). Every
  other value is **descriptive** — write it the way the organization spells it (`ART`,
  `Werk`), show it exactly as written, and never infer anything from it.
- **meeting** = `type: interaction` **with** `interaction-type: meeting`. Lives in
  `interactions/`, alongside non-meeting interactions.

When scanning an org, key off the discriminator (`unit-type` containing `work-system`,
`interaction-type`), not `type:` alone.

## Cross-cutting rules to keep in mind

- **Relationships are `[[wikilinks]]`** in frontmatter, pointing at the target's **label**
  (its filename without `.md`). `[[Target]]` and `[[Target|Alias]]` both resolve to
  `Target`. Hyphen and underscore field spellings are both accepted.
- **`reports-to`** = structure (individuals only). **`member-of`** = flow (individual or
  unit). `derived-from` and `delegator` are metadata, not typed edges.
- **Discriminators are named `<base>-type`**: `unit-type`, `interaction-type`,
  `agreement-type`, `visualization-type`. Each may hold a single token **or a YAML list**
  (e.g. `unit-type: [team, work-system]`). `flightlevel` is one word.
- **Two types carry embedded DSL — both plain YAML, dot-form fence tags:**
  `visualization` → ` ```dwsd.board ` (`title:`, `columns:` / `lanes:` / `groups:`, with
  inline inside-out `agreements:` / `interactions:` on any node — no inline sugar like
  `#status` or `[wip]`); `flight-route` → ` ```dwsd.flightroute ` (`title:`, `for:` as a
  wikilink or plain text, stage item types as text (`order @ Shops`) or a quoted wikilink
  (`"[[Feature]] @ Train"`) — never matched by name; a linked stage is named by its target
  in locators and `bound-to` keys (`stage:Feature @ Train`), `for-domain:` naming the work system, role or unit responsible for the route, `bands:`, `triggers:`, glyph-typed `path:` edges `->` / `-->` / `..>` /
  `..> ()`, and a `bound-to:` layer binding bands to boards). External entities anchor
  **into** a board or route via a **locator** (`interaction-of` / `agreement-of` /
  `bound-to`: `[[Board]]#BoardName/col:Column::in`, a column group
  `[[Board]]#BoardName/lane:Lane/group:Group::in`, the `::before` / `::after` slot of a
  position, or `[[Route]]/stage:itemType @ Band::in`); a bare `[[Entity]]` anchors to a work
  system, unit or person instead. A locator without `#BoardName` (`[[Board]]/col:Column::in`)
  lands on the column of a titled board, just as a route locator lands on a titled route;
  in a file with several titled board fences it lands on every fence that has the unit.
  `[[Board]]#BoardName::in` addresses the whole board and shows in the board header; a bare
  `[[Board]]::in` is an entity anchor, not a board anchor. A meeting's `## Interactions`
  table row may name a standalone interaction with `[[…]]` — the file is then the source
  for outcome and anchor (conventions.md › Reading guide). See `<spec-root>/types/visualization.md` and
  `<spec-root>/types/flight-route.md`.
- **Three more fences are inferred views any entity may host** (or standalone files at the
  org root): ` ```dwsd.topology ` (flight-level context over `contributes-to`),
  ` ```dwsd.orgchart ` (individuals over `reports-to`), ` ```dwsd.units ` (units over their
  first `member-of`, `layout: nested | tree`). `mode: infer` lists nothing — the pictures
  follow the entity files; `around:` names the entity to draw from (a wikilink or `self`),
  `radius:` how far. `focus:` is the earlier name of `around:`, still read as an alias.
  See `<spec-root>/conventions.md` › Embedded DSL fences and › Anchors and around.
- **A fourth inferred view, ` ```dwsd.change-trail `,** draws the change ladder as one
  network (along `derived-from`, landing via `for-domain` / bare `agreement-of`, loop-backs
  via `observes`); keys `around:` (a wikilink or `self`), `show: all | open | recent`,
  `radius:`, an empty body is the whole trail. No standalone file. A decision record carries
  one under `## Change trail`, first in the body, with `around: self`. `mode: mixed` lays
  the fence's own `entries:` over the organization's trail, `mode: declared` draws only
  them. Brackets point outward: an item with a bare `name` is an **inline entry** carrying
  its type's frontmatter keys (`type: insight`, never `stage:`); `"[[Name]]"` is a reference
  to the file. Inside the fence `derived-from: hh` means the inline entry, `"[[hh]]"` the
  file; a file never holds a bare name. `delta: add | remove` is an annotation on either.
- **Fence ids:** any of the six fences may name itself after the tag
  (` ```dwsd.board id=intake `) — kebab-case, unique within the file, kept when the title
  or heading changes. Optional; when you create a fence, give it one.
- **Change ladder:** `signal` → `insight` → `driver` → `proposal` →
  `organizational-decision-record` → `agreement`(s), each rung naming the one below with
  `derived-from`; an agreement names the ODR it operationalizes, which makes a decision's
  bundle readable in reverse.

## Authoring steps

1. Identify the conceptual type (mind the subtypes above) and open
   `<spec-root>/types/<type>.md` for its contract.
2. Start from `<spec-root>/templates/<type>.md`.
3. Name the file with the entity's human label (Title Case, spaces allowed — the filename
   *is* the label and the wikilink target). Put it in the matching plural folder.
4. Fill the frontmatter (required fields + discriminator) and wire relationships as
   `[[wikilinks]]`.

When in doubt, the spec wins — this skill never overrides it. To answer questions about an
existing org, use the `org-read` skill.
