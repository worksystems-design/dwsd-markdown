---
type: flight-route
created_at: "2026-10-10"
---

How a [[Field Issue]] travels bottom-up — the mirror of the [[Epic Route]]. It starts
outside the flight levels: `Field` is a **custom band without a flight level**, because
[[Field Service]] is a plain team, not a work system. The week's issues are brought to the
[[Field Issue Triage]], where the route **forks**: a safety or fleet-down issue becomes a
**hotfix** in the ART board's expedite lane and bypasses the PI; everything else becomes a
[[Feature]] and waits for PI planning like any other. The hotfix reaches the fleet over the
air; what happened to each report flows back to Field Service, who close it with the
customer.

The fork is the point: one cadence for the planned work, one lane for what cannot wait,
and a named place where the decision between them is made.

```dwsd.flightroute
title: Field Issue Route
for: "[[Field Issue]]"
bands:
  - name: Field
  - name: Train
    fl: 2
  - name: Teams
    fl: 1
triggers:
  - name: a charger fails on site, an installer calls, telemetry flags a pattern
    generates:
      - issue @ Field
path:
  # Field Service brings the week's issues to triage
  - issue @ Field --> issue @ Train
  # safety or fleet-down: the issue becomes a hotfix in the expedite lane
  - issue @ Train -> hotfix @ Train
  # everything else becomes a feature for the next PI
  - issue @ Train -> feature @ Train
  # a team takes the hotfix immediately
  - hotfix @ Train --> hotfix @ Teams
  # the verified fix flows back into the issue
  - hotfix @ Teams ..> issue @ Train
  # the hotfix reaches the fleet over the air
  - hotfix @ Train ..> ()
  # Field Service hears back what happened to what it reported
  - issue @ Train ..> issue @ Field
bound-to:
  - band: Train
    boards:
      - board: "[[Charger ART Board]]"
        stages:
          - issue: "lane:Field Issue/col:Triage"
          - hotfix: "lane:Field Issue/col:Fix-in-Progress"
          - feature: "lane:Feature/group:Preparation/col:Program Backlog"
  - band: Teams
    boards:
      - board: "[[Wallbox Team Board]]"
        stages:
          - hotfix: "col:In Progress"
```
