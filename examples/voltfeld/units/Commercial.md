---
type: unit
unit-type: department
member-of: "[[Voltfeld]]"
created_at: "2026-10-10"
---

Commercial is [[Rolf Steinbach]]'s department: [[Sales]] sells chargers and fleet contracts,
[[Field Service]] installs, commissions and repairs them. Both are plain teams. Field
Service is where most field issues enter the company.

## In context

```dwsd.units id=units
mode: infer
focus: self
radius: { up: 1, down: inf }
```

> [!NOTE]
> **Modeling note.** Both teams have no `flightlevel` and no `work-system`. Field Service
> being the entry point for field issues makes it the start of a route in the flow section
> of this example.
