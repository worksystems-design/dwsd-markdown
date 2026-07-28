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

## Filename = label = slug

The filename without extension is both the **display label** and the source of the
**slug** (the stable id used in wikilinks and internally).

- `individuals/Aaron Turner.md` → label `Aaron Turner`, slug `aaron-turner`
- Spaces and non-ASCII are allowed in filenames; the slug is normalized.

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
- The target is a label; the parser resolves it to a slug. An unresolved target is
  kept as a dangling reference.

### Relationship fields

Both hyphen and underscore spellings are accepted (`reports-to` = `reports_to`).

| Field (variants) | Meaning |
|---|---|
| `reports-to` / `reports_to` | Reporting line — **individuals only** (individual → individual) |
| `member-of` | Belongs to a unit / work system — an **individual** or a **unit** can be a member |
| `contributes-to` | A work system contributes to a higher-level work system |
| `role-keeper` / `role_keeper` | Who holds this role |
| `for-domain` / `for_domain` | The **work system** (domain) a role, agreement, or interaction is scoped to — points *up* |
| `interaction-of` | The **board (position)** an interaction is of — points *into the detail*: a board **locator** `[[Board]]#BoardName/col:Column::in` (or `[[Board]]#BoardName::in` for the whole board) |
| `agreement-of` | The **board (position)** an agreement is of — the same board **locator** as `interaction-of`; coexists with `for-domain` |
| `observes` | The entity a **signal** or **insight** observes — what was seen / interpreted |
| `derived-from` / `derived_from` | What this entity **emerged from** — the shared lineage key, see below |
| `uses-route` | The flight route an entity uses |
| `defined-for` | The entity something is defined for |
| `visualization-of` / `visualization_of` | The work system a visualization renders |

> **Up vs. into the detail.** `for-domain` names the **work system** (the domain — points
> *up*); `interaction-of` / `agreement-of` name a **board position** (a locator — points
> *into the detail*). A board is **not** a work system, so the two coexist and neither field is
> overloaded to mean both. A board renders exactly one work system (`visualization-of`), so the
> work system is **inferable** from the board — `for-domain` is therefore optional, and stating
> it is just clearer. If both are present and the board's work system differs from `for-domain`,
> that mismatch is something a validator can flag.
>
> **The locator** (`interaction-of` / `agreement-of`) is **value-polymorphic**: a bare
> `[[Work System]]` wikilink anchors to a whole **work system**; a value carrying a `#BoardName`
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
> disambiguates when one file hosts several routes.

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

## Embedded DSL fences

Three fence tags are parsed and rendered by the app. All three DSLs are **plain YAML**,
and all fence tags use the dot form. The first two are tied to a type; the third may
appear in any entity body:

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
  `mode: infer` (the only mode so far), `focus:` (a wikilink naming the entity to center
  on; when omitted, the map centers on the entity hosting the block), and `radius:` (how
  many relationship hops the map reaches). Purely a view — it declares no relationships
  and is never part of a type's required body structure. ⚠ **Preliminary** — the key set
  may still change.

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
