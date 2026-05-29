# `unit`

> The base structural unit — a **named grouping** that one or more people, teams, or other
> units belong to. It need not be a team: an R&D department or a SAFe ART is a unit too,
> and units can nest. A unit belongs to the **structure** (the reporting line). A unit
> whose **`unit-type` includes `work-system`** is also a [work system](work-system.md)
> (and carries a `flightlevel`); without it the unit is purely structural.

**Serialized `type`:** `unit`

## The concept

`unit` is the base type — deliberately general. A unit is **any named grouping with
members**: a team, an R&D department, a SAFe ART, a tribe, and so on. Units can contain
other units (they nest). What makes it a unit is a name plus members (people, teams, or
other units) — not any particular level. The `unit-type` names the kind of unit, and can
carry more than one value. On top of the bare unit:

1. **`unit-type` includes `work-system`** → the unit is also a **work system** (see
   [`work-system.md`](work-system.md)); it then carries a `flightlevel`. `unit-type` is the
   marker — e.g. `unit-type: [team, work-system]` is a team that is also a work system.
2. **No `work-system` in `unit-type`** → the unit is purely structural (e.g.
   `unit-type: team`). That is fine and common.

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `unit` | Entity type (base) |
| `unit-type` | no | token **or** list — `team` \| `art` \| `[team, work-system]` \| … | Kind(s) of unit (open vocabulary). Include `work-system` to mark it a **work system** |
| `flightlevel` | no | `1` \| `2` \| `3` | Required **when `unit-type` includes `work-system`**; the work system's flight level |
| `member-of` | no | wikilink | The parent unit / work system this one belongs to → **flow** |
| `contributes-to` | no | wikilink | The higher work system this unit feeds |

Plus the shared optionals from [conventions](../conventions.md). A unit that *is* a work
system also carries the work-system frontmatter (`delegator`, `version`,
`decision_date`, `review_date`) and the domain-description body — see
[`work-system.md`](work-system.md).

## Body

- **Plain unit (no `work-system` in `unit-type`):** light — a line or two of description
  is enough.
- **Unit that is also a work system (`unit-type` includes `work-system`):** use the full
  domain-description body from [`work-system.md`](work-system.md) (Purpose, Key
  Responsibilities, Customers and Deliverables, … Evaluation Schedule).

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

A unit that is *also* a work system carries `unit-type: [team, work-system]` (or
`[department, work-system]`, …) plus a `flightlevel` — see the example in
[`work-system.md`](work-system.md).

## Notes

- A unit becomes a work system by including `work-system` in its `unit-type` — not by its
  folder. The folder (`units/` vs `work-systems/`) is organizational only.
- `unit-type` is an open vocabulary (`team`, `art`, `department`, …) and may hold several
  values. Alongside the *kind*, the reserved value **`work-system`** is what marks the unit
  as a work system; `flightlevel` is then required but is not itself the marker.
