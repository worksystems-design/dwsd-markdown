---
type: visualization
visualization-type: board
title: "Wallbox"
visualization-of: "[[Wallbox]]"
created_at: "2026-10-11"
---

The FL2 board of the [[Wallbox]] product line — the PI's Wallbox [[Feature]]s on their way
from the train's backlog to the system rig. One lane per
team, [[Wallbox Home]] and [[Wallbox Fleet]]; the teams are not work systems and keep no
board of their own, so this is where their work is coordinated. A third lane, `Hotfix`, is
the expedite lane a [[Field Issue]] lands in when the train hands a fix to the product line.
The one rule worth writing on the board concerns the platforms: a feature that depends on
[[HW Base]] or the [[Firmware Platform]] is pulled only when that dependency is resolved or
has a named owner on the ART board. The [[DC Charger]] and [[Connectivity]] product lines
coordinate the same way.

```dwsd.board
title: Wallbox
flightlevel: FL2
timebox: 10w
columns:
  - name: PI Backlog
    status-category: to-do
  - name: Ready
    status-category: to-do
    check: "Feature split into team stories, platform dependency resolved or named"
  - name: In Progress
    wip: 4
    status-category: in-progress
    agreements:
      - "Pull a platform-dependent feature only with the dependency resolved or owned"
  - name: On the Rig
    status-category: assess
  - name: Done
    status-category: done
lanes:
  - Wallbox Home
  - Wallbox Fleet
  - name: Hotfix
    type: expedite
    wip: 1
```

> [!NOTE]
> **Modeling note.** The board carries `timebox: 10w`, like the train. The [[DC Charger]]
> and [[Connectivity]] product lines are not drawn as boards.
