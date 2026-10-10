---
type: flight-route
created_at: "2026-10-10"
---

How an [[Epic]] travels top-down: it enters the [[Portfolio]] as a strategic bet, is
accepted into the [[Charger ART]] at PI planning, and is split there by
[[Product Management]] into [[Feature]]s — the item type that travels the
[[Feature Route]] from here on. Two bands only, FL3 and FL2: the epic itself never reaches
a team; what reaches a team is a feature. PI results flow back up at the monthly
[[Portfolio Sync]], and the epic is delivered when its business outcome is in the market —
tracked at FL3, where it lives.

```dwsd.flightroute
title: Epic Route
for: "[[Epic]]"
bands:
  - name: Portfolio
    fl: 3
  - name: Train
    fl: 2
triggers:
  - name: strategic bet, major fleet contract or regulatory change
    generates:
      - epic @ Portfolio
path:
  # an epic accepted at PI planning is picked up by the train
  - epic @ Portfolio --> epic @ Train
  # Product Management splits it into features for one or more PIs
  - epic @ Train -> feature @ Train
  # PI results flow back up at the Portfolio Sync
  - feature @ Train ..> epic @ Portfolio
  # the epic is done when its business outcome is in the market
  - epic @ Portfolio ..> ()
bound-to:
  - band: Portfolio
    boards:
      - board: "[[Portfolio Board]]"
        stages:
          - epic: "col:Implementing"
  - band: Train
    boards:
      - board: "[[Charger ART Board]]"
        stages:
          - feature: "lane:Feature/group:Preparation/col:Program Backlog"
```
