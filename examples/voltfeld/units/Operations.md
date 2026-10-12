---
type: unit
unit-type: department
member-of: "[[Voltfeld]]"
created_at: "2026-10-10"
---

Operations is [[Ingrid Halvorsen]]'s department: the plant and the supply base. It contains
one work system — [[Manufacturing]], which builds and tests every charger — and one plain
team, [[Supply Chain]], which sources parts and manages suppliers.

Unlike the engineering departments, Operations *is* where its people work. Manufacturing's
output, though, goes to customers and is steered from the [[Portfolio]], not from the
[[Charger ART]].

> [!NOTE]
> **Modeling note.** The `member-of` and `reports-to` trees agree here. What does **not**
> agree is the flow — see the topology map in the [README](../README.md).

## In context

```dwsd.units
mode: infer
focus: self
radius: { up: 1, down: inf }
```
