---
type: role
role-keeper: "[[Greta Vossberg]]"
for-domain: "[[Charger ART]]"
version: "1.0"
decision_date: "2026-01-12"
review_date: "2027-01-11"
created_at: "2026-10-10"
---

## Purpose

### Driver

Six teams, two of them platforms serving the other four, cannot keep their dependencies
straight by talking in corridors. The [[Charger ART]] needs someone whose job is the train
itself, not any one wagon.

### Requirement

One role that owns the ART's cadence and events, makes dependencies visible, and removes
what blocks the teams between them.

## Description

The Release Train Engineer is the servant-leader of the [[Charger ART]]: facilitates PI
planning, the weekly ART sync, the system demo and inspect-and-adapt; keeps the program
board of cross-team dependencies current; escalates risks to the [[Business Owner]]s.
Borrowed from SAFe, where the role has the same name.

## Concerns

Cross-team dependencies — above all between the two product teams and [[HW Base]] and the
[[Firmware Platform]]; PI predictability; the integration dates [[System Integration]]
plans around; and lately, the lead times from [[Supply Chain]] that no ART event covers.

## Accountabilities

- Prepare and facilitate every ART event; publish PI objectives and the program board.
- Track dependencies and risks across the PI; escalate what the teams cannot resolve.
- Run inspect-and-adapt and follow through on its improvement items.

## Decision Rights

- Decides the ART's event schedule and planning format (autonomous).
- Re-sequences cross-team work within a PI — **agrees** with the affected teams.
- Does not rank the backlog ([[Product Management]]) and does not decide architecture
  ([[System Architect]]).

## Evaluation

### Metrics and Monitoring

- PI predictability; dependencies still open at the end of PI planning; improvement items
  closed per PI.
