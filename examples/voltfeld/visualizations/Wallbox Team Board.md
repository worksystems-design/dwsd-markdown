---
type: visualization
visualization-type: board
title: "Wallbox Team"
visualization-of: "[[Wallbox]]"
created_at: "2026-10-10"
---

The FL1 team board of the [[Wallbox]] team — stories from the PI's features, two-week
iterations (`timebox: 2w`). A plain flow; the one rule worth writing on the board concerns
the platforms: a story that depends on [[HW Base]] or the [[Firmware Platform]] is pulled
only when that dependency is resolved or has a named owner on the ART board. The
[[DC Charger]] team runs the same board shape and is not modeled separately.

```dwsd.board
title: Wallbox Team
flightlevel: FL1
timebox: 2w
columns:
  - Backlog
  - name: Ready
    status-category: to-do
    check: "Story sized, platform dependency resolved or named"
  - name: In Progress
    wip: 4
    status-category: in-progress
    agreements:
      - "Pull a platform-dependent story only with the dependency resolved or owned"
  - name: Review
    status-category: assess
  - name: Done
    status-category: done
```
