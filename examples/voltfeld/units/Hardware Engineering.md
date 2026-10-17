---
type: unit
unit-type: department
member-of: "[[Voltfeld]]"
tags: [line]
created_at: "2026-10-10"
---

Hardware Engineering is a **line department**: the hardware, mechanical, test and
compliance engineers report to its head, [[Kaspar Reinholt]], who hires, develops and
reviews them. None of them *work* here — they sit in agile teams ([[Wallbox]],
[[DC Charger]], [[HW Base]], [[System Integration]]). The department is where the
reporting lines go, not where the work goes.

## In context

```dwsd.units id=units
mode: infer
focus: self
radius: { up: 1, down: inf }
```

> [!NOTE]
> **Modeling note.** The engineers' `member-of` points at the agile team they sit in. That
> is why this unit has a box in the units view but no members of its own. Compare the org
> chart, where the same people sit directly under Kaspar.
