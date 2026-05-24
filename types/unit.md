# `unit`

> The base structural unit — a **named grouping** that one or more people, teams, or other
> units belong to. It need not be a team: an R&D department or a SAFe ART is a unit too,
> and units can nest. A unit belongs to the **structure** (the reporting line). A unit that
> also has a **`flightlevel`** is implicitly a [work system](work-system.md); without one
> it is purely structural.

**Serialized `type`:** `unit`

## The concept

`unit` is the base type — deliberately general. A unit is **any named grouping with
members**: a team, an R&D department, a SAFe ART, a tribe, and so on. Units can contain
other units (they nest). What makes it a unit is a name plus members (people, teams, or
other units) — not any particular level. On top of the bare unit:

1. **A `flightlevel`** → the unit is also a **work system** (see
   [`work-system.md`](work-system.md)). The presence of `flightlevel` is the marker.
2. **No `flightlevel`** → the unit is purely structural. That is fine and common.

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `unit` | Entity type (base) |
| `unit-type` | no | `team` \| `art` \| … | Kind of unit (open vocabulary) |
| `flightlevel` | no | `1` \| `2` \| `3` | If present, the unit is **also a work system** |
| `member-of` | no | wikilink | The parent unit / work system this one belongs to → **flow** |
| `contributes-to` | no | wikilink | The higher work system this unit feeds |

Plus the shared optionals from [conventions](../conventions.md). A unit that *is* a work
system also carries the work-system frontmatter (`delegator`, `version`,
`decision_date`, `review_date`) and the domain-description body — see
[`work-system.md`](work-system.md).

## Body

- **Plain team (no `flightlevel`):** light — a line or two of description is enough.
- **Unit with a `flightlevel`:** use the full domain-description body from
  [`work-system.md`](work-system.md) (Purpose, Key Responsibilities, Customers and
  Deliverables, … Evaluation Schedule).

## Example — a plain team

```markdown
---
type: unit
unit-type: team
member-of: "[[3P]]"
---
# 3P body

A 3P body team. No own work system — contributes to the [[3P]] work system.
```

A unit *with* a `flightlevel` looks like the example in
[`work-system.md`](work-system.md).

## Notes

- A unit becomes a work system purely by having a `flightlevel` — not by its folder or
  `unit-type`. The folder (`units/` vs `work-systems/`) is organizational only.
- `unit-type` is an open vocabulary (`team`, `art`, …); it names the *kind* of unit and
  does **not** carry work-system-ness.
