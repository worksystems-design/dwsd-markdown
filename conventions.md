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
- **Navigation** — working *on* the system, sensing and deciding (sense → respond):
  signal, insight, driver, proposal. These **look at** the organization; they are not part of it.
- **Change** — records of decided organizational change: design-record (more may follow).

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
| `interaction-of` | The **board (position)** an interaction is of — points *into the detail*: `@board#Column`, or `@board` for the whole board |
| `agreement-of` | The **board (position)** an agreement is of — the same `@board#Column` anchor as `interaction-of`; coexists with `for-domain` |
| `observes` | The entity an insight observes |
| `uses-route` | The flight route an entity uses |
| `defined-for` | The entity something is defined for |
| `visualization-of` / `visualization_of` | The work system a visualization renders |

> **Up vs. into the detail.** `for-domain` names the **work system** (the domain — points
> *up*); `interaction-of` / `agreement-of` name a **board position** (`@board#Column` — points
> *into the detail*). A board is **not** a work system, so the two coexist and neither field is
> overloaded to mean both. A board renders exactly one work system (`visualization-of`), so the
> work system is **inferable** from the board — `for-domain` is therefore optional, and stating
> it is just clearer. If both are present and the board's work system differs from `for-domain`,
> that mismatch is something a validator can flag. The `@board#Column` anchor is the same one
> the board / flight-route DSLs use (see [Embedded DSL fences](#embedded-dsl-fences)).

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

Two types carry a fenced code block that the app parses and renders:

- `visualization` (boards) → ```` ```board ```` — see
  [`types/visualization.md`](types/visualization.md)
- `flight-route` → ```` ```flightroute ```` — see
  [`types/flight-route.md`](types/flight-route.md)

## Markwhen siblings (`.mw`)

A scheduled `interaction` (e.g. a recurring meeting) may have a sibling file with the same
basename and a `.mw` extension holding a one-line [Markwhen](https://markwhen.com) timeline
entry:

```
interactions/3P Coordination.md
interactions/3P Coordination.mw
```

The `.mw` file is not an entity on its own; it is attached to the interaction.
