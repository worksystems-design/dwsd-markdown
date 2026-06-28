---
type: visualization
visualization-type: board
title: "Bakery Operations Coordination"
visualization-of: "[[Bakery Operations]]"
created_at: "2026-06-28"
---

The FL2 end-to-end coordination board for [[Bakery Operations]] — the columns are the shared
coordination flow; each **swimlane is one flight-item-type** that travels it. Lanes are plain
`named` lanes named after the item type (the board DSL has no typed item-type binding), one
per type currently in motion: the daily [[Daily Replenishment Order]], standing
[[Wholesale Contract]] orders, and the strategic [[New Shop Launch]].

```dwsd-board
board: Bakery Operations Coordination
flightlevel: FL2
columns:
  - name: Demand-In
    status-category: to-do
  - name: Planning
    wip: 3
    status-category: in-progress
  - name: Planned
    status-category: done
  - name: In-Production
    status-category: waiting
  - name: Delivered
    status-category: done
lanes:
  - Daily Replenishment Order
  - Wholesale Contract
  - name: New Shop Launch
    agreements:
      - "Strategic launches need FL3 sign-off before capacity is committed"
```
