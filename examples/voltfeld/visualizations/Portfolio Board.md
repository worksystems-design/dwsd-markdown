---
type: visualization
visualization-type: board
title: "Portfolio"
visualization-of: "[[Portfolio]]"
created_at: "2026-10-10"
---

The FL3 portfolio kanban of the [[Portfolio]] — the few [[Epic]]s Voltfeld has in motion.
Two **column groups** band the columns: `Exploring` (an epic is understood before it is
decided) and `Committed` (decided, funded, in flight). Kept deliberately small: three
epics implementing at once is the limit for a company with one ART and one plant.

```dwsd.board
title: Portfolio
flightlevel: FL3
agreements:
  - "Only epics that change a product line, a market or the plant enter here"
groups:
  - name: Exploring
    status-category: assess
    columns:
      - Funnel
      - Reviewing
      - name: Analyzing
        agreements:
          - "An epic leaves Analyzing with a lean business case and a named Business Owner"
  - name: Committed
    columns:
      - name: Portfolio Backlog
        status-category: to-do
      - name: Implementing
        wip: 3
        status-category: in-progress
        agreements:
          - "An epic enters Implementing only with a PI it is funded for"
      - name: Done
        status-category: done
```
