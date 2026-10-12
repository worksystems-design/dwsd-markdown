---
type: agreement
agreement-type: work
for-domain: "[[Bakery Operations]]"
agreement-of:
  - "[[Bakery Operations Coordination Board]]#Bakery Operations Coordination/lane:Wholesale Contract::in"
  - "[[Wholesale]]"
  - "[[Wholesale Contract Route]]/stage:standing-order @ Coordination::before"
version: "1.0"
decision_date: "2026-07-19"
review_date: "2027-01-19"
created_at: "2026-07-19"
---

## Driver and Requirement

Every signed [[Wholesale Contract]] permanently claims a slice of the [[Bakehouse]]'s
nightly capacity — dependable base load, but unchecked it crowds out the shops' morning
range. The wholesale book needs a cap that protects the [[Daily Replenishment Flow]].

## Who is responsible for what?

- [[Bakery Operations]] — signs new contracts only while the wholesale book stays under
  the cap; sequences enquiries that would exceed it.
- [[Head Baker]] — flags when nightly utilization approaches the limit.
- [[Wholesale]] — keeps the standing orders inside the cap.

## Description

Standing wholesale volume stays at or below **40% of nightly bake capacity**. Each new
contract counts its standing order against the cap at signing. At the cap, new enquiries
wait, or an existing account is renegotiated first.

The cap is the gate a signed contract passes before it may spawn its standing daily order
and claim nightly capacity.

> [!NOTE]
> **Modeling note.** On the [[Wholesale Contract Route]] the cap sits `::before` the
> `standing-order` stage. The agreement is also anchored to the team itself
> (`agreement-of: [[Wholesale]]`), so it shows on the team's box in the units view.

## Evaluation Criteria

- No shop replenishment order is cut short in favor of a wholesale delivery.
- Morning dispatch on-time rate holds as the wholesale book grows.
