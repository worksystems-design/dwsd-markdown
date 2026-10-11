---
type: unit
unit-type: company
created_at: "2026-05-24"
---

Goldcrust Bakery is the company as a whole — the structural root of its units. Its `unit-type` is just `company` — it does **not** include `work-system`
(and it has no `flightlevel`), so it is a plain structural `unit`, not a work system: it
groups, it does not itself coordinate a flow of work.

Its units are cut by **site** — where people work:

- [[Mill Lane]] — the bakehouse, the office and the van yard; home of the two plain teams
  [[Deliveries]] (the morning dispatch) and [[Wholesale]] (the standing daily orders).
- [[Market Street]] and [[Station Road]] — the two shops.

How the work *flows* is a different picture, drawn by the work systems and their
`contributes-to` in the flight-level map:

- [[Bakery Strategy]] — FL3, sets direction.
- [[Bakery Operations]] — FL2, coordinates production and retail.
- [[Bakehouse]] — FL1, production.
- [[Market Street Shop]] and [[Station Road Shop]] — FL1, retail.

The work systems carry no `member-of`, so the unit tree does not draw them a second time:
the units show where people sit, the topology shows how the work moves. People belong to
both — a shop assistant is `member-of` the shop's site and its work system. The org chart of the people who work in them is the standalone
`Goldcrust Org Chart.dwsd-orgchart` at the org root; the unit tree is `Goldcrust Units.dwsd-units`.

## In context

```dwsd.units
mode: infer
focus: self
radius: { up: 1, down: inf }
```
