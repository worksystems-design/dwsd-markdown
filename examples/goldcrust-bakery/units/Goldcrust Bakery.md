---
type: unit
unit-type: company
created_at: "2026-05-24"
---

Goldcrust Bakery is the company as a whole — the structural root that the work systems and
people belong to. Its `unit-type` is just `company` — it does **not** include `work-system`
(and it has no `flightlevel`), so it is a plain structural `unit`, not a work system: it
groups, it does not itself coordinate a flow of work.

Its operational reality is described by the work systems below (each a `unit` whose
`unit-type` includes `work-system`):

- [[Bakery Strategy]] — FL3, sets direction.
- [[Bakery Operations]] — FL2, coordinates production and retail.
- [[Bakehouse]] — FL1, production.
- [[Market Street Shop]] and [[Station Road Shop]] — FL1, retail.

And two plain teams that are *not* work systems:

- [[Deliveries]] — `unit-type: team`, no flightlevel; carries the morning dispatch.
- [[Wholesale]] — `unit-type: team`, no flightlevel; keeps the standing daily orders.

Read as a containment tree, the units nest three deep from this root: Goldcrust Bakery ⊃
[[Bakery Strategy]] ⊃ [[Bakery Operations]] ⊃ the three FL1 work systems and the two plain
teams. The org chart of the people who work in them is the standalone
`Goldcrust Org Chart.dwsd-orgchart` at the org root; the unit tree is `Goldcrust Units.dwsd-units`.

## In context

```dwsd.units
mode: infer
focus: self
radius: { up: 1, down: inf }
```
