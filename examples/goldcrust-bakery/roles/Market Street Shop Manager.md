---
type: role
role-keeper: "[[Lena Frei]]"
for-domain: "[[Market Street Shop]]"
version: "1.0"
decision_date: "2026-05-20"
review_date: "2026-11-20"
created_at: "2026-05-24"
---

## Purpose

### Driver

The [[Market Street Shop]] needs someone accountable for daily trading and for feeding
accurate demand back to production.

### Requirement

A role that owns opening and closing, sell-through, and the next-day replenishment order
for the Market Street location.

## Description

The Market Street Shop Manager runs the [[Market Street Shop]] end to end: staffing the
counter, selling the range, counting closing stock, and placing the
[[Daily Replenishment Order]].

A standalone role, deliberately separate from the [[Station Road Shop Manager]] — roles
are individual in DWSD, so each location's role evolves on its own. (A role *shared* by
several people would instead list them all as `role-keeper`s.)

## Concerns

Morning availability — sourdough through the morning peak in particular (see
[[Morning Sourdough Replenishment]]) — customer experience at peak, and demand-signal
accuracy.

## Accountabilities

- Open and close the shop; staff the counter.
- Place an accurate next-day [[Daily Replenishment Order]].
- Report stockouts and demand patterns to [[Bakery Operations]].

## Decision Rights

- Decides daily counter staffing and replenishment quantities (autonomous).
- Escalates range changes to the [[Head Baker]].

## Evaluation

### Metrics and Monitoring

- Morning stockout incidents; sell-through rate; replenishment accuracy.
