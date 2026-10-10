---
type: visualization
visualization-type: board
title: "Manufacturing"
visualization-of: "[[Manufacturing]]"
created_at: "2026-10-10"
---

The FL1 board of [[Manufacturing]] — not the daily line (that runs on the plant's own
system) but the **ramp** of each new variant the [[Charger ART]] releases: from the release
arriving to stable production. `Release Received` is the column where the
[[Feature Route]] ends for the train and begins for the plant; nothing on this board points
back at the ART board, and no ART board column points here. Two boards, one hand-over, no
loop — the picture the change ladder starts from.

```dwsd.board
title: Manufacturing
flightlevel: FL1
columns:
  - name: Release Received
    status-category: to-do
    agreements:
      - "A release is accepted only with production test firmware from System Integration"
  - name: Fixtures and Instructions
    status-category: in-progress
  - name: Pilot Build
    wip: 1
    status-category: in-progress
    check: "First-article inspection passed"
  - name: Ramp
    status-category: in-progress
  - name: Stable Production
    status-category: done
```
