---
type: role
role-keeper: "[[Selin Aydin]]"
for-domain: "[[Station Road Shop]]"
version: "1.0"
decision_date: "2026-05-20"
review_date: "2026-11-20"
created_at: "2026-07-19"
---

## Purpose

### Driver

The [[Station Road Shop]] trades against a sharp commuter peak: if the shop is not
stocked and open before the rush, the day's best window is gone.

### Requirement

A role that owns early opening, sell-through, and the next-day replenishment order for
the Station Road location.

## Description

The Station Road Shop Manager runs the [[Station Road Shop]] end to end: opening ahead
of the commuter rush, staffing the counter, counting closing stock, and placing the
[[Daily Replenishment Order]].

A standalone role, deliberately separate from the [[Market Street Shop Manager]] — the
two evolve independently as their locations diverge.

## Concerns

Early-peak availability (the dispatch must land before the rush — see
[[Station Road Early Dispatch]]), throughput at the counter, and demand-signal accuracy.

## Accountabilities

- Open the shop stocked before the commuter peak; staff the counter.
- Place an accurate next-day [[Daily Replenishment Order]].
- Report stockouts and demand patterns to [[Bakery Operations]].

## Decision Rights

- Decides daily counter staffing and replenishment quantities (autonomous).
- Escalates range changes to the [[Head Baker]].

## Evaluation

### Metrics and Monitoring

- Early-peak sell-through; morning stockout incidents; replenishment accuracy.
