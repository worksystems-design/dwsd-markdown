---
type: unit
unit-type: [department, work-system]
flightlevel: 2
member-of: "[[Bakery Strategy]]"
contributes-to: "[[Bakery Strategy]]"
delegator: "[[Mara Holt]]"
version: "1.0"
decision_date: "2026-05-20"
review_date: "2026-08-20"
created_at: "2026-05-24"
---

## In context

```dwsd.topology
mode: infer
radius: 2
```

## Purpose

Coordinate the flow of work between the [[Bakehouse]] and the shops so that daily demand
and daily production stay in balance.

## Key Responsibilities

- Translate shop demand into a prioritized next-day production plan.
- Resolve cross-team conflicts (capacity, dispatch windows, special orders).
- Run the [[Daily Production Sync]] and steward the [[Daily Replenishment Flow]].

## Customers and Deliverables

- [[Bakehouse]] — a clear, prioritized daily plan.
- [[Market Street Shop]] / [[Station Road Shop]] — dependable replenishment.

## Dependencies

Depends on timely evening stock counts from the shops and honest capacity signals from the
[[Bakehouse]].

## Key Metrics and Monitoring

- Plan-vs-actual production accuracy; replenishment lead time; stockout incidents.
