---
type: unit
unit-type: team
member-of: "[[Mill Lane]]"
tags: [pilot]
created_at: "2026-09-17"
---

Wholesale is the one-person team ([[Noor Haddad]]) that keeps the standing daily bread
orders from cafés and restaurants. Like [[Deliveries]] it is a **plain team**, not a work
system: `unit-type: team`, no `flightlevel`, no `work-system`. It sits at the
[[Mill Lane]] site, next to the bakehouse that bakes its orders.

The wholesale flow itself is modeled as a route, the [[Wholesale Contract Route]] — a
contract *generates* a standing order that the [[Bakehouse]] then bakes into every
morning's dispatch.

## In context

```dwsd.units
mode: infer
focus: self
radius: { up: 1, down: inf }
```
