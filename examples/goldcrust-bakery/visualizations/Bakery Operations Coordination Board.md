---
type: visualization
visualization-type: board
title: "Bakery Operations Coordination"
visualization-of: "[[Bakery Operations]]"
created_at: "2026-06-28"
---

The FL2 end-to-end coordination board for [[Bakery Operations]] — one **swimlane per
flight-item-type**. Lanes are plain `named` lanes named after the item type (the board DSL
has no typed item-type binding), one per type currently in motion. The types flow
differently, so **each lane carries its own columns** (lane-local `columns:`): the daily
[[Daily Replenishment Order]] runs the demand–plan–produce–deliver cycle, a
[[Wholesale Contract]] goes from enquiry to a running account, a [[New Shop Launch]] is
accepted, prepared, and opened, and a [[New Product Introduction]] rolls out via trial
bakes into the range.

Status categories read from FL2's perspective: in the replenishment lane, `Planned` is
`done` (the coordination work on the order is finished) while `In-Production` is
`waiting` — the order sits with the [[Bakehouse]] at FL1, and FL2 is waiting on it.

```dwsd.board
title: Bakery Operations Coordination
flightlevel: FL2
lanes:
  - name: Daily Replenishment Order
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
  - name: Wholesale Contract
    columns:
      - name: Enquiry
        status-category: to-do
      - name: Negotiation
        status-category: in-progress
      - name: Signed
        status-category: done
      - name: Running
        status-category: in-progress
  - name: New Shop Launch
    agreements:
      - "Strategic launches need FL3 sign-off before capacity is committed"
    columns:
      - name: Accepted
        status-category: to-do
      - name: In-Prep
        status-category: in-progress
      - name: Open
        status-category: done
  - name: New Product Introduction
    columns:
      - name: Rollout-Planning
        status-category: to-do
      - name: Trial-Bakes
        status-category: in-progress
      - name: In-Range
        status-category: done
```
