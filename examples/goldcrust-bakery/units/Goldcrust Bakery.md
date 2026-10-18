---
type: unit
unit-type: company
created_at: "2026-05-24"
---

Goldcrust Bakery is the company as a whole — the structural root of its units. It groups;
it does not itself coordinate a flow of work.

Its units are cut by **site** — where people work:

- [[Mill Lane]] — the bakehouse, the office and the van yard; home of the two plain teams
  [[Deliveries]] (the morning dispatch) and [[Wholesale]] (the standing daily orders).
- [[Market Street]] and [[Station Road]] — the two shops.

How the work *flows* is a different picture, drawn by the work systems:

- [[Bakery Strategy]] — FL3, sets direction.
- [[Bakery Operations]] — FL2, coordinates production and retail.
- [[Bakehouse]] — FL1, production.
- [[Market Street Shop]] and [[Station Road Shop]] — FL1, retail.

The units show where people sit, the work systems show how the work moves. People belong
to both — a shop assistant works at the shop's site and in its work system.

## In context

```dwsd.units id=units
mode: infer
focus: self
radius: { up: 1, down: inf }
```

## Change trail

```dwsd.change-trail id=change-trail
```

Every change entity of the bakery in one picture, from what was seen to where the
agreement landed. The sourdough shortfall runs from the sold-out shelf to an agreement in
the [[Bakehouse]]. The dispatch insight looks back at the decision that made
[[Jonas Keller]] Head of Operations and, like the van and the wholesale enquiries, is
still open.

> [!NOTE]
> **Modeling note.** Its `unit-type` is just `company` — it does **not** include
> `work-system` (and it has no `flightlevel`), so it is a plain structural `unit`, not a
> work system. The flow picture is drawn by the work systems and their `contributes-to` in
> the flight-level map. The work systems carry no `member-of`, so the unit tree does not
> draw them a second time; the topology shows how the work moves. A shop assistant is
> `member-of` the shop's site and its work system.
>
> The org chart of the people who work in them is the standalone
> `Goldcrust Org Chart.dwsd-orgchart` at the org root; the unit tree is
> `Goldcrust Units.dwsd-units`.
