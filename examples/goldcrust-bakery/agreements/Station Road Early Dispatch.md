---
type: agreement
agreement-type: work
for-domain: "[[Bakehouse]]"
agreement-of: "[[Bakehouse Production Board]]#Bakehouse Production/col:Ready-for-Dispatch::in"
version: "1.0"
decision_date: "2026-05-26"
review_date: "2026-08-26"
created_at: "2026-06-28"
---

## Driver and Requirement

The [[Station Road Shop]] sits at a commuter location where an early rush drives a sharp
morning peak. If its dispatch arrives on the same run as the other shops, the shelves are
half-empty when the peak hits. Station Road needs its dispatch to clear `Ready-for-Dispatch`
first.

## Who is responsible for what?

- [[Bakehouse]] — finishes and releases the [[Station Road Shop]] dispatch ahead of the
  Market Street run, into the first delivery slot.
- [[Deliveries]] — runs the early Station Road drop before the commuter peak.
- [[Bakery Operations]] — reviews the ordering against actual peak times.

## Description

In the morning `Ready-for-Dispatch` queue, the [[Station Road Shop]] order is sequenced
first so the early delivery leaves in time for the commuter rush. The [[Market Street Shop]]
follows on the standard run.

## Evaluation Criteria

- Station Road shelves are stocked before the commuter peak begins.
- The earlier sequencing does not push the Market Street dispatch past opening time.

## Concerns

The sourdough quota for [[Market Street Shop]] (see [[Morning Sourdough Replenishment]])
must still be honored despite Station Road leaving first — both promises share the same
first-dispatch window.
