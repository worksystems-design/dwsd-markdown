---
type: visualization
visualization-type: board
title: "Market Street Shop"
visualization-of: "[[Market Street Shop]]"
created_at: "2026-06-28"
---

The FL1 retail board for the [[Market Street Shop]] — the morning dispatch arrives, sells
through the day, and the closing count becomes tomorrow's [[Daily Replenishment Order]]. The
`Sold-Out` column is where the [[Sourdough Sold Out Before 9am]] signal shows up. `Incoming`
carries an inline (inside-out) pointer to the [[Counter Handover]], which also anchors here
from its own file (outside-in).

```dwsd-board
board: Market Street Shop
flightlevel: FL1
columns:
  - name: Incoming
    status-category: to-do
    interactions:
      - "[[Counter Handover]]"
  - name: On-Shelf
    status-category: in-progress
  - name: Low-Stock
    status-category: waiting
  - name: Sold-Out
    status-category: waiting
  - name: Reorder
    status-category: done
```
