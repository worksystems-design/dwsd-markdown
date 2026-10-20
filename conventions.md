# Conventions

Rules that apply to **every** entity, regardless of type. Each type's spec page only
adds what is specific to it.

## One file, one entity

An organization is a folder of Markdown files. Each `.md` file is exactly one entity.
Files are grouped into per-type subfolders, but the folder is a convenience — the
**`type:` field decides the type**, not the folder.

Entities fall into four **categories** — but these are conceptual, **not folders**. Each
type keeps its own flat plural folder (`individuals/`, `roles/`, …, `signals/`, …); the
category is a way of thinking about an entity, not a directory.

- **Structure** — the organization's makeup (who, and how they're organized): individual,
  role, unit, work-system, ai-agent.
- **Flow** — how work is coordinated and flows: interaction, meeting, agreement,
  flight-item-type, flight-route, visualization.
- **Change** — working *on* the system: signal, insight, driver, proposal,
  organizational-decision-record. These **look at** the organization and decide about it; they
  are not part of it. The category spans two phases of that work (see below).

### The Change category spans two phases

The five Change types divide by the phase of change work they belong to — the middle two of the
four MADE phases (Map · **Assess** · **Design** · Elevate):

| Phase | Types | What it does |
|---|---|---|
| **Assess** | `signal` · `insight` · `driver` | Reads the organization as it is — selected data, its interpretation, and the need that follows |
| **Design** | `proposal` · `organizational-decision-record` | Says what should be instead — a proposed response, and the decision once taken |

**Map** is the topology itself (the as-is picture), and **Elevate** — actually moving from as-is
toward to-be — is deliberately **not** modeled here: it is facilitation work (experiments, guides,
katas), a practice artifact rather than a record, and it belongs elsewhere.

The phases are a way of *thinking* about these five types. They are **not** how a reader filters
them: what matters when working is whether something is still **in flux** (signal → proposal) or
**decided** (the ODR, and the agreements that follow). Those two cuts run across each other on
purpose — `proposal` is Design by phase but still in flux by status.

```yaml
---
type: individual
---
```

A file with **no frontmatter**, or with an **unknown/missing `type`**, is silently
skipped by the parser. It is not an entity.

**The org's README.** A `README.md` at the org root is such a file. For lack of anything
better, its first `#` heading serves as the organization's name and its first paragraph
as its description — a tool that shows the org reads them from there, as written. There
is no frontmatter and no extra key for this, and nothing else in the README is read.

**Notes.** Such files — a README, a tour, any page without a `type:` — are **notes**. A
wikilink may point at a note and then resolves (it is not broken), but a note is not a node
in the organization's graph, and the wikilinks inside it are not relationships.

## Filename = label = slug

The filename without extension is both the **display label** and the source of the
**slug** (the stable id used in wikilinks and internally).

- `individuals/Aaron Turner.md` → label `Aaron Turner`, slug `aaron-turner`
- Spaces and non-ASCII are allowed in filenames; the slug is normalized.

**A wikilink finds its target by label, never by slug.** Cut the target at `|`, trim the
surrounding whitespace, and compare **keys**: `key = NFC(lowercase(NFC(label)))`, with
plain Unicode lowercasing (no locale rules, no full case folding), and no character
dropped or transliterated. The same rule holds for every wikilink — frontmatter and body.

| Target | File | Match? |
|---|---|---|
| `[[café]]` | `Café.md` | yes — case |
| `[[Café]]` (`e` + combining accent) | `Café.md` (`é`) | yes — NFC |
| `[[STRAẞE]]` | `Straße.md` | yes — `ẞ` lowercases to `ß` |
| `[[STRASSE]]` | `Straße.md` | **no** — `ß` is not folded to `ss` |
| `[[Mueller]]` | `Müller.md` | **no** — no transliteration |
| `[[Bakery  Ops]]` (two spaces) | `Bakery Ops.md` | **no** |

Two files with the same key in one organization are an error — labels are unique. The slug
(`aaron-turner`, umlauts spelled out) serves URLs and internal ids only; it is lossy, so it
is never used to match a link.

Because the filename is the identity, **renaming a file renames the entity** — update
the wikilinks that point at it.

## Relationships are wikilinks

Connections between entities are expressed in the frontmatter as Obsidian-style
wikilinks pointing at the **label** of the target:

```yaml
member-of: "[[Sales Team]]"          # single
role-keeper:                          # or a list
  - "[[Head of 3P]]"
  - "[[Head of 4P]]"
```

- `[[Target]]` and `[[Target|Alias]]` both resolve to `Target`.
- A field can hold a single wikilink or a list of them.
- The target is a label, matched as above. An unresolved target is kept as a dangling
  reference.
- **Every wikilink in the frontmatter is a relationship** — under any key, single or in a
  list. The keys in the table below carry a defined meaning (structure or flow, up or into
  the detail, a locator). Any other key — `derived-from`, `delegator`, `decision-makers`,
  or a key of the author's own like `mentor:` — is a plain **link** named by its key: it
  connects the two entities, but no view draws a marker from it. Wikilinks in the body
  are references, not relationships.

### Relationship fields

Both hyphen and underscore spellings are accepted (`reports-to` = `reports_to`).

| Field (variants) | Meaning |
|---|---|
| `reports-to` / `reports_to` | Reporting line — **individuals only** (individual → individual) |
| `member-of` | Belongs to a unit / work system — an **individual** or a **unit** can be a member |
| `contributes-to` | A work system contributes to a higher-level work system |
| `role-keeper` / `role_keeper` | Who holds this role |
| `for-domain` / `for_domain` | The **domain** — a work system, a role or a unit — that a role, agreement, interaction (or meeting), AI agent, ODR, driver or proposal is scoped to, and that a flight route (in its `dwsd.flightroute` block) names as the domain **responsible** for the route — points *up*. Naming a role lands the entity on every keeper of that role |
| `interaction-of` | The **board (position)** an interaction is of — points *into the detail*: a board **locator** `[[Board]]#BoardName/col:Column::in` (or `[[Board]]#BoardName::in` for the whole board), or a bare `[[entity]]` — a work system, a unit or a person |
| `agreement-of` | The **board (position)** an agreement is of — the same board **locator** as `interaction-of` (or a bare `[[entity]]`); coexists with `for-domain` |
| `bound-to` | Where an **AI agent**'s surface appears — the same **locator** as `interaction-of` / `agreement-of` (or a bare `[[entity]]` — a work system, a unit or a person) |
| `observes` | The entity a **signal** or **insight** observes — what was seen / interpreted — a work system, a unit, a person, or another entity |
| `derived-from` / `derived_from` | What this entity **emerged from** — the shared lineage key, see below |
| `uses-route` | The flight route an entity uses |
| `defined-for` | The entity something is defined for |
| `visualization-of` / `visualization_of` | The work system a visualization renders |

> **Up vs. into the detail.** `for-domain` names the **domain** (points *up*);
> `interaction-of` / `agreement-of` name a **board position** (a locator — points
> *into the detail*). A domain is a work system, a role or a unit — any named grouping that
> decides something for itself: a department, a site, a circle that governs without running a
> flow. `for-domain` never names a person — a decision about a person is anchored through the
> role the person keeps, and it then shows on the box of every keeper of that role (one hop:
> the role's own `for-domain` is not followed further). A board is **not** a work system, so
> the two coexist and neither field
> is overloaded to mean both. A board renders exactly one work system (`visualization-of`), so
> the work system is **inferable** from the board — `for-domain` is therefore optional, and
> stating it is just clearer. If both are present and the board's work system differs from
> `for-domain`, that mismatch is something a validator can flag. On a flight route,
> `for-domain` says who takes care when the route changes; the work systems the route flows
> through are derived (`bound-to` → board → `visualization-of`), never authored there.
>
> **The locator** (`interaction-of` / `agreement-of` / `bound-to`) is **value-polymorphic**: a
> bare `[[…]]` wikilink anchors to the **entity** it names — a work system, a unit, or a person
> (a 1:1, a personal working agreement) — wherever that entity is drawn (the topology, the org
> chart, the units view); a unit that is also a work system shows the same anchors in both
> pictures. A same-named person and unit both receive the bare link; the path form
> `[[individuals/Name]]` / `[[units/Name]]` names one of them. A value carrying a `#BoardName`
> and/or a `/kind:Name` path is a **board-position** locator. The path drills in with
> `/`-chained `col:` · `lane:` · `group:` · `split:` · `stage:` segments and an optional
> trailing `::before` · `::in` · `::after` (bare = `::in`), e.g.
> `[[Sprint Board]]#Sprint Board/col:Build/split:QA::before`. This is the **outside-in**
> direction; the board may also declare relationships **inside-out** with inline `agreements:` /
> `interactions:` keys on a column/lane/group (see [Embedded DSL fences](#embedded-dsl-fences)).
>
> **`stage:` anchors into a route, not a board.** The same locator can point at a **route
> stage**: `[[Route]]/stage:<itemType> @ <Band>::before|in|after`, where the name after
> `stage:` is the full `itemType @ Band` pair (single space each side of `@`), e.g.
> `[[Daily Replenishment Flow]]/stage:order @ Shops::before`. A `#Route Name` fragment
> disambiguates when one file hosts several routes. A stage whose item type is a wikilink
> is named by its link target, without brackets: `[[Feature Route]]/stage:Feature @ Train::in`
> for the stage `[[Feature]] @ Train`.

### `derived-from` — the shared emergence key

`derived-from` says **what an entity emerged from**. It is a **shared key, not a per-type
field**: any entity may carry it, and it is documented here once rather than repeated on each
type page.

It traces the design conversation and what follows from it:

```
signal → insight → driver → proposal → organizational-decision-record → agreement(s)
```

Each step may name its origin — an insight the signal(s) it interprets, a driver the insight(s)
it answers to, a proposal the driver, an ODR the proposal, and an **agreement the ODR it
operationalizes**. That last link is what makes an ODR's *bundle* expressible: the agreements
belonging to a decision are exactly those whose `derived-from` names it. No separate bundle
field is needed — the bundle is the reverse reading of this key.

- **Optional everywhere.** An entity without `derived-from` is complete; the key adds lineage,
  it does not gate validity.
- **Single or list.** `derived-from: "[[X]]"` or a list, like every other relationship field.
- **Metadata only.** There is no `derived-from` relationship *type* — it is preserved and
  readable, but it resolves to no marker and creates no typed edge. Read backwards ("what did
  this come from?") it sits in the document; read forwards ("what came of this?") it needs a
  reverse index over the key.

> **Why a shared key and not a per-type field.** It used to be documented on each type that
> happened to use it, and the type that most needed it — `agreement`, the one that answers
> "why does this rule apply?" — never got it, because a per-type field has to be remembered at
> every new type and eventually is not. Documented once, that whole class of omission goes away.

### Shared optional fields

Like `derived-from`, these are documented once and may appear on any entity; no type page
repeats them.

| Field | Meaning |
|---|---|
| `tags` | Descriptive chips on **any** entity type — a list of short words, e.g. `tags: [core, pilot]`. The renderers read them from the entity's frontmatter wherever the entity is drawn (the topology, the org chart, the units view); the view documents (board, flight-route, topology, org chart, units) carry a document-level `tags:` as well. A tag is a label, not a relationship — it resolves to nothing |

## Structure vs. flow

Two orthogonal views of the organization, modeled with two different relationships. Keep
them apart — an entity can sit very differently in each.

- **`reports-to` → structure** (the formal reporting line — "who reports to whom").
  **Individuals only.**

- **`member-of` → flow, optionally** (value creation — how work flows). `member-of`
  expresses *belonging* to a unit or work system; an **individual or a unit** can be a
  member. That belonging *can* describe the flow side — but need not. Use the membership
  that matters in context.

A **`unit`** sits **between** the two: a named grouping that one or more people, teams, or
other units belong to. It need not be a team — it can be an R&D department, a SAFe ART, or
any other named unit, and units can nest. A unit that also participates in flow is a work
system (its `unit-type` includes `work-system`, and it carries a `flightlevel`). See
[`types/unit.md`](types/unit.md) and [`types/work-system.md`](types/work-system.md).

The unit tree **need not mirror the topology.** `contributes-to` already says how work
systems feed each other; `member-of` between work systems that only repeats it adds a
second copy of the same picture. Cut the units by whatever dimension the organization
actually groups by — departments, disciplines, sites — and let a work system carry
`member-of` only where it really sits inside such a unit. A person can be `member-of` a
unit and a work system at once (a list).

## Work systems are marked on `unit-type`

`unit` is the base structural type. **A unit is a work system when its `unit-type`
includes `work-system`** — it then carries the full domain description (Purpose …
Evaluation Schedule; see [`types/work-system.md`](types/work-system.md)) and a
`flightlevel` recording its flight level. A unit *without* `work-system` in its
`unit-type` is purely structural — e.g. a plain `unit-type: team`.

The marker is **explicit on `unit-type`**, not inferred from the presence of a
`flightlevel`. `flightlevel` is an attribute a work system carries — required on every
work system — but it is not what *makes* a unit one. This lets a single unit declare both
of its hats at once: a team that is also a work system is `unit-type: [team, work-system]`.

This is a deliberate simplification: a unit and "its" work system are modeled as **one
entity** wearing two hats — now stated literally by the multi-valued `unit-type` — not as
two linked entities. The cleaner two-entity model — where a work system can span several
teams, or a team can have none — was considered and dropped for simplicity.

> **`flightlevel`** is written as one word — no underscore, no hyphen.

### Reserved and descriptive `unit-type` values

`unit-type` holds two kinds of value, and they behave differently:

- **Reserved** — today **`work-system`** and **`team`**. A reserved value carries meaning
  in the model. It is part of the format, like a field name: it is always written in
  English, and tools match it without regard to case. A view may draw it as a mark of its
  own and may label it in the reader's language.
  - **`work-system`** makes the unit a work system, with everything that follows (flight
    level, topology, `contributes-to`, validation).
  - **`team`** marks a stable group of people who work together. Its **members** are the
    individuals whose `member-of` names it, and a view may show the team's size as their
    number — the members the org folder models, which can be fewer than the real
    headcount. Units that are `member-of` a team are not counted. `team` and
    `work-system` combine freely: `[team, work-system]` is a team that is also a work
    system; a plain `team` is not.
- **Descriptive** — every other value: `site`, `department`, `company`, `ART`, `Werk`, …
  An open vocabulary in the author's words and language. No tool derives anything from
  it. Views show it **exactly as written** — no capitalization, no label lookup — so an
  acronym is spelled the way the author spelled it (`ART`, not `art`).

A descriptive value becomes reserved only by a change to this spec, when the model gives
it a meaning (a mark in a view, a rule in validation). Until then it is description.

## Subtypes and kinds — the `<base>-type` key

Where a type has subtypes or kinds, the discriminator key is **named after the
base type** (`<base>-type`), not a generic `subtype`, so it reads unambiguously for both
humans and tools:

- `type: visualization` + **`visualization-type: board`**
- `type: unit` + **`unit-type: team`**

A `<base>-type` discriminator holds a **single token or a YAML list** — a list when the
entity is several kinds at once. This is what lets a unit wear two hats:

- `type: unit` + **`unit-type: [team, work-system]`** — a team that is also a work system.

Every `<base>-type` (`unit-type`, `visualization-type`, `agreement-type`,
`interaction-type`) accepts a list; in practice only `unit-type` uses it today.

**A meeting is an interaction** whose `interaction-type` holds the token `meeting` (alone
or in a list, matched without regard to case). There is no `type: meeting`; a reader may
accept it as an old spelling of the same thing, and a validator warns.

## Tracking fields

Optional provenance/timestamps. Hyphen and underscore spellings both accepted:

```yaml
created_at: "2026-03-15"
updated_at: "2026-03-20"
created_by: "thomas"
```

## `sources` block (discovered / synced entities)

Entities pulled in from an external system carry a `sources:` block recording where
they came from (one key per source system, each with an `id` and `url`):

```yaml
sources:
  atlassian:
    id: "00000000-0000-0000-0000-000000000000"
    url: "https://example.atlassian.net/o/<org-id>/people/team/00000000-0000-0000-0000-000000000000"
  discovery:
    id: discovery-00000000
    url: "https://www.notion.so/00000000000000000000000000000000"
```

Some synced entities instead carry flat `atlassian_id` / `atlassian_url` fields — both
patterns are valid.

## Modeling notes in the body

Body text tells the organization's story. Where a file explains how it is **modeled** — why
it is anchored here, why a field is set or left out, which locator it uses — put that in
**one callout at the end of the file** (after any `## In context` view), as a GitHub alert:

```markdown
> [!NOTE]
> **Modeling note.** Anchored on the [[Daily Replenishment Flow]] where the dispatch
> stands on the shelf (`dispatch @ Shops::in`).
```

Readers can skip it; tools can tell it apart from content. Place it next to a passage only
when it explains that one passage and would lose its meaning at the end. Wikilinks inside the callout
are ordinary wikilinks. A file with nothing to explain about its modeling has no callout.

## Reading guide

How the model is meant to be used and read — by people and by agents. Nothing here adds a
field; it settles how existing structure is interpreted.

### How do I refer to an interaction from a meeting table?

A meeting's `## Interactions` table names small interactions inline, one per row. When one
of them gains weight — it needs its own description, someone wants to anchor something to
it or link to it — **pull it out into its own interaction file** and name that file in the
row's `Name` column:

```markdown
| Name                       | Outcome | Interaction of |
|----------------------------|---------|----------------|
| [[Where is each feature]]  |         |                |
```

- **There is no locator for a table row.** Locators say *where something hangs* (a board
  position, a route stage, an entity); they never point at a line in a document. To make
  a row addressable, give it its own file.
- **The file is the source.** For a `[[…]]` row, `Outcome` and `Interaction of` stay empty;
  the outcome is in the file's body, the anchor in its `interaction-of`. If a cell is
  filled anyway, it is a copy: the file wins, and a validator reports any difference.
  Values from row and file are never merged and never silently dropped.
- **The way back needs no field.** The table links the file, so its backlinks name the
  meeting that embeds it.
- **Readers read the table in reverse:** meeting → row → anchor. For a `[[…]]` row they
  take outcome and anchor from the file.
- The same holds for an agreement container: `## Agreements` with its `Agreement of`
  column.

## Anchors and around

Two ideas carry every picture of the organization, and they point in opposite directions.

- **An anchor says where an entity sits.** It is written in the entity's own file:
  `for-domain` anchors it up, to the domain that decides about it; a locator
  (`interaction-of`, `agreement-of`, `bound-to`) anchors it into the detail — an entity, a
  board position or a route stage; `observes` anchors a signal or an insight to what was
  seen. Every view finds an entity through its anchors and shows it on the box, column or
  stage it is anchored to.
- **`around:` says from where the organization is looked at.** Each inferred view —
  topology, org chart, units, change trail — takes `around:`, a wikilink or `self` (the
  entity whose file hosts the fence), and draws the organization from that entity outward,
  as far as `radius:` reaches. `around:` belongs to the view, not to the model: changing it
  changes what is shown, never what is true.

Anchors are written once, from each entity outward; `around:` reads them back from any
point. An org chart with `around: self` in a person's file shows that person's line; the
change trail with `around: self` in a decision record shows where the decision came from
and where its agreements landed. Same files, read from a different place.

## Embedded DSL fences

Six fence tags are parsed and rendered by the app. All six DSLs are **plain YAML**,
and all fence tags use the dot form. The first two are tied to a type and are **authored**;
the other four are **inferred views** that may appear in any entity body — the topology,
org chart and units view may also stand alone as a file (see below):

- `visualization` (boards) → ```` ```dwsd.board ```` — columns, lanes, groups, and inline
  inside-out `agreements:` / `interactions:`; no inline sugar; the board name is the
  shared `title:` header key. See [`types/visualization.md`](types/visualization.md).
- `flight-route` → ```` ```dwsd.flightroute ```` — `title:`, `for:`, `bands:`,
  `triggers:`, glyph-typed `path:` edges, and a `bound-to:` layer that maps bands onto
  boards via wikilinks and the **locator** above. The old `@`-handle references
  (`@work-system#Column`) are retired. See
  [`types/flight-route.md`](types/flight-route.md).
- **any entity** (optional) → ```` ```dwsd.topology ```` — an inline **flight-level
  context map**, inferred from the org's relationships rather than authored. Keys:
  `mode: infer` (the only mode so far), `around:` (a wikilink naming the entity to center
  on; when omitted, the map centers on the entity hosting the block), and `radius:` (how
  many relationship hops the map reaches). Purely a view — it declares no relationships
  and is never part of a type's required body structure.
- **any entity** (optional) → ```` ```dwsd.orgchart ```` — the **line organization**:
  every `individual` and its `reports-to` chain, drawn top-down as a tree of person boxes.
  A person without `reports-to` is a root; a vacancy is an individual with the position in
  `role:` (the Goldcrust and Voltfeld examples name theirs `NA1`). Keys: `mode: infer`,
  `around:` (a person), `radius:` (a number or `{ up, down }`), and `notes:` — a note
  written on a box, naming it with a bare wikilink. Nothing else is listed in the fence:
  rename a file or move a `reports-to`, and the chart follows.
- **any entity** (optional) → ```` ```dwsd.units ```` — the **unit structure**: every
  `unit` (work systems included) nested by its **first** `member-of`; a unit without
  `member-of` is a root. `layout: nested` (default) draws children inside the parent box,
  `layout: tree` the same containment as a tree; each box wears its `unit-type` values as
  chips, so a `[team, work-system]` is told from a plain `team` at a glance. Units only —
  no people (that is the org chart), no flow between work systems (that is the topology).
  Same `mode:` / `around:` / `radius:` / `notes:` keys as the org chart.
- **any entity** (optional) → ```` ```dwsd.change-trail ```` — the **change trail**: the
  org's change entities as one network, left to right — signal → insight → driver →
  proposal → decision record → agreement, one rung back along `derived-from` (an agreement
  may derive from the proposal directly) — and where each agreement **lands**: the units
  and work systems it names in `for-domain` or in a bare `agreement-of` (a board position
  or a role does not count). A signal or insight that `observes` a decision record or an
  agreement draws a **loop-back**. An entity nothing derives from yet is an **open end**
  and shows its next step; agreements are never open, and a `status` of `declined`,
  `rejected`, `withdrawn` or `superseded` closes an entity. `created_at` (fallback `date:`)
  dates each entry. Keys: `around:` (a wikilink, or `self` — the entity whose file hosts
  the fence), `show:` (`all`, the default, `open` or `recent`) and `radius:` (a number or
  `inf`); an empty body is the whole trail. With `around:` the trail keeps that entity's own
  line: back along `derived-from` to the signals, forward to what derives from it and where
  that lands. A decision record carries one this way (`around: self`), so its file shows
  where the decision came from and where its agreements apply.

The topology, org chart and units view are **annotated from the entity files**, never
from the fence: a
signal or insight that `observes` a person or unit pins on that box; an interaction,
agreement or AI agent whose locator names an entity shows on it (a unit that is also a work
system shows the marker on its unit box *and* its topology node); an entity scoped
`for-domain` to a role reaches the box of every keeper of that role — one hop; one scoped
to a plain unit shows on that unit's box in the units view. They declare
no relationships and are never part of a type's required body structure. All four take
`around:` as described in [Anchors and around](#anchors-and-around); `focus:` is its earlier
name and is still read as an alias — when both are written, `around:` wins. ⚠ **Preliminary**
— the key sets of the four inferred views may still change.

**Fence ids.** Any of the six fences may carry an id after its tag:
```` ```dwsd.board id=intake ````. The id names the diagram within its file, so a mark or an
address that points at it survives when other diagrams are inserted, moved or removed
around it. `id=` is the first and so far only attribute after the tag; the value is
kebab-case (`[a-z0-9][a-z0-9-]*`), unquoted, unique within the file, and stays as it is
when the fence's `title:` or the enclosing heading changes. The id is optional — a fence
without one is valid — and tools that create a fence should assign one. It is a plain
name, not a wikilink, and not part of the YAML, so the key sets above are unaffected; a
board's `title:` still names it in locators (`#BoardName`). Readers recognize a fence by
its tag, the first word of the info string, and ignore attributes they do not know. A
standalone view file (below) has no fence and no id; its filename names it.

**Standalone view files.** The topology, org chart and units view may also live as a
standalone file at the org root — `.dwsd-topology`, `.dwsd-orgchart`, `.dwsd-units` — holding the same YAML
without a fence (the examples keep one org chart and one units file each, e.g.
`Goldcrust Org Chart.dwsd-orgchart`). Such a file is **not an entity**: no frontmatter, no
`type:`, skipped by the entity parser — a picture of the organization, not a part of it.

## Markwhen siblings (`.mw`)

A scheduled `interaction` (e.g. a recurring meeting) may have a sibling file with the same
basename and a `.mw` extension holding a one-line [Markwhen](https://markwhen.com) timeline
entry:

```
interactions/3P Coordination.md
interactions/3P Coordination.mw
```

The `.mw` file is not an entity on its own; it is attached to the interaction.

An org folder may additionally keep **one consolidated timeline file** (e.g.
`operating-rhythm.mw`) that aggregates the sibling lines — a pragmatic workaround while
Markwhen viewers operate on a single file. It is not an entity either; the per-interaction
siblings remain the source of truth.
