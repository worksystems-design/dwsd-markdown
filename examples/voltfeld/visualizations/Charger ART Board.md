---
type: visualization
visualization-type: board
title: "Charger ART"
visualization-of: "[[Charger ART]]"
created_at: "2026-10-10"
---

The FL2 board of the [[Charger ART]] — the train's program board for the PI. Two lanes, one
per flight-item-type in motion at FL2:

- The **`Feature`** lane carries the PI's [[Feature]]s through three **column groups** —
  `Preparation` (before PI planning), `In PI` (the ten weeks), `Release` (demoed, certified,
  released). The groups are the sub-processes of the train; the
  [[Release Dossier Agent]] works the `Release` group as a whole.
- The **`Field Issue`** lane is an **expedite lane**: a [[Field Issue]] that cannot wait for
  the PI is triaged here and fixed outside the cadence. The [[Field Issue Triage Agent]]
  pre-sorts what arrives at `Triage`, the people decide.

In `Certified` the train waits on an external test house; `Implementing` is where the
teams are, and the train's own work there is coordination.

```dwsd.board id=charger-art
title: Charger ART
flightlevel: FL2
timebox: 10w
agreements:
  - "Features enter the PI at PI planning; mid-PI changes need the Business Owners"
lanes:
  - name: Feature
    groups:
      - name: Preparation
        columns:
          - name: Program Backlog
            status-category: to-do
          - name: Refined
            status-category: to-do
            check: "Acceptance criteria, team assignment and platform dependencies named"
      - name: In PI
        interactions:
          - "[[ART Sync]]"
        columns:
          - name: Implementing
            wip: 8
            status-category: in-progress
          - name: Integrating
            status-category: in-progress
            agreements:
              - "Integration dates are set at PI planning; a slipped date is raised at the ART Sync, not discovered on the rig"
      - name: Release
        interactions:
          - "[[System Demo]]"
        columns:
          - name: Demoed
            status-category: assess
          - name: Certified
            status-category: waiting
          - name: Released
            status-category: done
  - name: Field Issue
    type: expedite
    columns:
      - name: Triage
        status-category: assess
      - name: Fix-in-Progress
        wip: 2
        status-category: in-progress
        agreements:
          - "One hotfix in progress per team; a second one waits or becomes a feature"
      - name: Hotfix-Released
        status-category: done
```

> [!NOTE]
> **Modeling note.** The board carries `timebox: 10w` for the PI. The
> [[Release Dossier Agent]] is bound to the `Release` group as a whole, not to one column.
> The `Field Issue` lane is marked `type: expedite`, and the [[Field Issue Triage Agent]]
> sits `::before` its `Triage` column. Status categories read from the train's
> perspective: `Certified` is `waiting`.
