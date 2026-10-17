---
type: flight-route
created_at: "2026-10-10"
---

How a [[Field Issue]] travels bottom-up — the mirror of the [[Epic Route]]. It starts
outside the flight levels, at [[Field Service]]. The week's issues are brought to the
[[Field Issue Triage]], where the route **forks**: a safety or fleet-down issue becomes a
**hotfix** in the ART board's expedite lane, goes to the expedite lane of the product line
concerned, and bypasses the PI; everything else becomes a
[[Feature]] and waits for PI planning like any other. The hotfix reaches the fleet over the
air; what happened to each report flows back to Field Service, who close it with the
customer.

The fork is the point: one cadence for the planned work, one lane for what cannot wait,
and a named place where the decision between them is made.

```dwsd.flightroute id=field-issue-route
title: Field Issue Route
for: "[[Field Issue]]"
for-domain: "[[Charger ART]]"
bands:
  - name: Field
  - name: Train
    fl: 2
  - name: Product Lines
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
  - "issue @ Train -> [[Feature]] @ Train"
  # the product line takes the hotfix into its expedite lane
  - hotfix @ Train --> hotfix @ Product Lines
  # one of its teams fixes it immediately
  - hotfix @ Product Lines --> hotfix @ Teams
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
          - Feature: "lane:Feature/group:Preparation/col:Program Backlog"
  - band: Product Lines
    boards:
      - board: "[[Wallbox Board]]"
        stages:
          - hotfix: "lane:Hotfix/col:In Progress"
```

> [!NOTE]
> **Modeling note.** `Field` is a **custom band without a flight level**, because
> [[Field Service]] is a plain team, not a work system.
