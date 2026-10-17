---
type: visualization
visualization-type: board
title: "HW Base"
visualization-of: "[[HW Base]]"
created_at: "2026-10-10"
---

The FL1 board of the [[HW Base]] platform team — hardware work from concept to tooling
release, in three **column groups**: `Design`, `Verification`, `Release`. The groups are
the sub-processes a hardware change goes through, and the `Verification` group is where
an agent works: the [[DFM Check Agent]] runs the design-for-manufacturing rules on every
drawing that enters it, and the [[DFM Review]] with [[Manufacturing]] decides on its
findings.

A card sitting in `Tooling Released` is not stuck: it is waiting out the fourteen weeks a
mold takes — the lead time this whole example turns on.

```dwsd.board id=hw-base
title: HW Base
flightlevel: FL1
timebox: 2w
groups:
  - name: Design
    columns:
      - Backlog
      - name: Concept
        status-category: in-progress
      - name: Detailed Design
        wip: 3
        status-category: in-progress
  - name: Verification
    status-category: assess
    interactions:
      - "[[DFM Review]]"
    columns:
      - name: Design Review
        check: "Interface to both product lines confirmed with the System Architect"
      - name: DFM Check
        agreements:
          - "No drawing goes to tooling without a DFM review with Manufacturing"
      - name: Lab Test
  - name: Release
    columns:
      - name: Tooling Released
        status-category: waiting
        aging: 98d
      - name: Handed Over
        status-category: done
        check: "Drawings, BOM and test specification received by Manufacturing"
```

> [!NOTE]
> **Modeling note.** The [[DFM Check Agent]] is bound to the whole `Verification` group.
> `Tooling Released` is `waiting` with a long `aging` — the fourteen weeks a mold takes.
