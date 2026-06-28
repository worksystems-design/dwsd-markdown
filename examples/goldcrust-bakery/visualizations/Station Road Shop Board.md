---
type: visualization
visualization-type: board
title: "Station Road Shop"
visualization-of: "[[Station Road Shop]]"
created_at: "2026-06-28"
---

The FL1 retail board for the [[Station Road Shop]] — same retail flow as Market Street, but
the early commuter rush drains the shelves first, so the morning dispatch has to land before
the peak. The closing count becomes tomorrow's [[Daily Replenishment Order]].

```dwsd-board
board: Station Road Shop
flightlevel: FL1
columns:
  - name: Incoming
    status-category: to-do
  - name: On-Shelf
    status-category: in-progress
  - name: Low-Stock
    status-category: waiting
  - name: Sold-Out
    status-category: waiting
  - name: Reorder
    status-category: done
```
