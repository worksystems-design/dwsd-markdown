---
type: agreement
agreement-type: work
for-domain:
  - "[[Charger ART]]"
  - "[[HW Base]]"
agreement-of:
  - "[[Charger ART Board]]#Charger ART/lane:Feature/group:Preparation::in"
  - "[[HW Base Board]]#HW Base/group:Release/col:Tooling Released::before"
  - "[[Supply Chain]]"
derived-from: "[[Production Joins the Train's Planning]]"
version: "1.0"
decision_date: "2026-10-06"
review_date: "2027-02-24"
created_at: "2026-10-06"
---

## Driver and Requirement

Answers [[Long-Lead Work Needs a Longer Horizon Than the PI]] through the decision
[[Production Joins the Train's Planning]]: a fourteen-week mold cannot be ordered inside a
ten-week PI and arrive in time. Long-lead items must be committed one PI before the
features that need them.

## Who is responsible for what?

- [[HW Base]] — at PI planning *n*, names every mold and long-lead part the features
  planned for PI *n+1* will need, with the feature it serves.
- [[Supply Chain]] — attends PI planning; orders each named item within one week; puts
  the confirmed delivery date on the dependency board.
- [[Release Train Engineer]] — tracks tooling dates as dependencies at the [[ART Sync]];
  a slipped tooling date is raised there, not discovered at integration.
- [[System Architect]] — confirms at planning that the platform interface the mold
  depends on is frozen enough to order; geometry freezes at the [[DFM Review]].

## Description

The `Preparation` group of the [[Charger ART Board]] gains a standing question for every
feature: *does it need tooling or a long-lead part?* If yes, the item is named at the PI
planning **before** the PI the feature is planned for, and Supply Chain orders it. On the
[[HW Base Board]] nothing enters `Tooling Released` without an order date already on the
dependency board — the agreement sits `::before` that column. In force from the PI 27.1
planning on 2026-12-03.

## Evaluation Criteria

- No PI objective moved for a tooling date in PI 27.1 and 27.2.
- Every mold ordered at least fourteen weeks before the integration date it serves.

## Concerns

Ordering a PI ahead means some molds are ordered for features the Business Owners later
cut — the cost of a cancelled mold is the price of predictability, and the review in
February looks at how often it was paid.
