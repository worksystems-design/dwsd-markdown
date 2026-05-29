# `work-system` (a unit whose `unit-type` includes `work-system`)

> A work system is the **flow** / value-creation view. In the
> target model it is **not a separate type**: it is a [`unit`](unit.md) whose
> **`unit-type` includes `work-system`** and which carries a **`flightlevel`**. The
> `work-system` value on `unit-type` is the marker; a unit can declare both hats at once,
> e.g. `unit-type: [team, work-system]` — a frontline team that is also a work system. In
> Flight Levels terms a work system is a **domain** of work, which is why roles point at it
> with `for-domain`.

**Serialized `type`:** `unit` + `unit-type` containing `work-system` (+ `flightlevel`)

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `unit` | Base type — a work system is a unit |
| `unit-type` | yes | must include `work-system` — e.g. `[team, work-system]`, `[department, work-system]` | **What marks it a work system**, alongside the kind of unit |
| `flightlevel` | yes | `1` \| `2` \| `3` | The flight level — required on a work system (carried, not the marker) |
| `contributes-to` | no | wikilink | The higher work system this one feeds |
| `member-of` | no | wikilink | The work system / strategy layer this belongs to |
| `delegator` | no | wikilink | Who delegated this domain (see note — metadata, not a typed edge) |
| `version` | no | string | Date/Version of the description, e.g. `1.2` |
| `decision_date` | no | date | When this version was decided |
| `review_date` | no | date | When it is due for review |
| `term` | no | string | Term of office — only when the template is used for a role |

Plus the shared optionals from [conventions](../conventions.md).

> The **title** is the filename. **Date/Version**, **Review Date**, **Delegator** and
> **Term** live in the frontmatter and render as properties; the body starts at
> *Purpose*.

## Relationships

- **`contributes-to`** — flow upward: this work system's output feeds the named one.
- **`member-of`** — structural belonging within the flow organization.

## Body — domain description

Describe the work system as a domain. All sections are `##` headings.

| Section | Holds |
|---|---|
| `## Purpose` | Why this domain exists |
| `## Key Responsibilities` | What the domain is accountable for *(list)* |
| `## Customers and Deliverables` | Who it serves and what it delivers *(list)* |
| `## Dependencies` | What it depends on — link work systems with `[[…]]` |
| `## External Constraints` | Constraints from outside the domain *(list)* |
| `## Key Challenges` | Current challenges / strain *(list)* |
| `## Key Resources` | People, budget, tools available to the domain *(list)* |
| `## Delegator Responsibilities` | What the delegator stays accountable for *(list)* |
| `## Competencies, Qualities and Skills` | What it takes to keep this domain *(list)* |
| `## Key Metrics and Monitoring` | How performance is observed *(list)* |
| `## Evaluation Schedule` | When and how the domain is reviewed |

## Example

```markdown
---
type: unit
unit-type: [department, work-system]
flightlevel: 2
contributes-to: "[[Strategic Direction]]"
member-of: "[[Strategic Direction]]"
delegator: "[[COO]]"
version: "1.0"
decision_date: "2026-05-11"
review_date: "2026-08-11"
---
## Purpose

Coordinate standard 3P / 4P / 5P production above the contributing teams and protect the
baseline revenue stream.

## Key Responsibilities

- Hold the standard-order delivery promise across the three product lines.
- Resolve cross-team dependencies and shared-platform release conflicts.

## Customers and Deliverables

- [[Sales]] — a predictable standard-order throughput.
- Customer — assembled, tested standard drones.

## Dependencies

Depends on [[Procurement]] for components and [[Assembly]] for final build.

## External Constraints

- Component lead times from external suppliers.

## Key Challenges

- Standard production blocked by custom / innovation pull.

## Key Resources

- [[3P body]], [[3P pm]], [[3P sw]] contributing teams.

## Delegator Responsibilities

- [[COO]] secures cross-domain capacity and arbitrates portfolio priority.

## Competencies, Qualities and Skills

- Production planning, dependency management, cross-team facilitation.

## Key Metrics and Monitoring

- Standard-order lead time; % delivered within 4–6 weeks.

## Evaluation Schedule

Reviewed quarterly; next review 2026-08-11.
```

## Notes

- A work system is **not its own type** — it is a `unit` whose `unit-type` includes
  `work-system`. The folder (`work-systems/`) is organizational only.
- One-entity model: a unit and "its" work system are the same entity. The cleaner
  two-entity alternative — a work system that can span several teams — was considered and
  dropped for simplicity.
- **`delegator`** is shown as a wikilink, but it is read as plain metadata: there is no
  `delegator` relationship type, so it is not a typed edge.
- The same domain template fits a **role** (hence *Delegator*, *Term (for a role)*,
  *Competencies…*). [`role.md`](role.md) keeps a lighter structure.
