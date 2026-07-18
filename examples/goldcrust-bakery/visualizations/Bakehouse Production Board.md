---
type: visualization
visualization-type: board
title: "Bakehouse Production"
visualization-of: "[[Bakehouse]]"
created_at: "2026-05-24"
---

The daily production board for the [[Bakehouse]] — one column per stage from order to
dispatch. `Mixing-Proofing` carries both an inline (inside-out) agreement and an external
(outside-in) one — [[Mixing-Proofing WIP Limit]] anchors to the same column.

```dwsd.board
title: Bakehouse Production
flightlevel: FL1
columns:
  - Backlog
  - name: Mise-en-Place
    status-category: to-do
  - name: Mixing-Proofing
    wip: 3
    status-category: in-progress
    agreements:
      - "Pull a new batch only when a proofer frees up"
  - name: Baking
    status-category: in-progress
    aging: 1d
  - name: Cooling
    status-category: waiting
    agreements:
      - "Cool to room temperature before dispatch"
  - name: Ready-for-Dispatch
    status-category: done
```
