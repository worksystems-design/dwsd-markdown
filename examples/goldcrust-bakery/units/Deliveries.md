---
type: unit
unit-type: team
member-of: "[[Mill Lane]]"
created_at: "2026-05-29"
---

Deliveries is the two-person team ([[Pia Brandt]], [[Nils Vogt]]) that runs the morning
run from the [[Bakehouse]] to the two shops, with one open seat — the Delivery
Coordinator ([[NA1]]) — reporting to [[Jonas Keller]]. It is a **plain team**, not a work
system.

It sits at the [[Mill Lane]] site, where the van leaves from. It participates in the flow
that [[Bakery Operations]] (FL2) coordinates — it carries the morning dispatch.

## In context

```dwsd.units id=units
mode: infer
focus: self
radius: { up: 1, down: inf }
```

> [!NOTE]
> **Modeling note.** Its `unit-type` is just `team`, with **no `flightlevel`** and **no
> `work-system`**: the delivery itself isn't a domain the bakery models as its own work
> system. Contrast it with the [[Bakehouse]], which *is* both a team **and** a work system
> (`unit-type: [team, work-system]`). The open seat is modeled as the vacancy [[NA1]].
