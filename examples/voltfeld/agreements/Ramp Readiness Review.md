---
type: agreement
agreement-type: work
for-domain:
  - "[[Manufacturing]]"
  - "[[Manufacturing Lead]]"
  - "[[Charger ART]]"
agreement-of:
  - "[[Manufacturing Board]]#Manufacturing/col:Fixtures and Instructions::in"
  - "[[Charger ART Board]]#Charger ART/lane:Feature/group:Release/col:Certified::in"
  - "[[Feature Route]]/stage:release @ Plant::before"
derived-from: "[[Production Joins the Train's Planning]]"
version: "1.0"
decision_date: "2026-10-06"
review_date: "2027-02-24"
created_at: "2026-10-06"
---

## Driver and Requirement

Answers [[Long-Lead Work Needs a Longer Horizon Than the PI]] through the decision
[[Production Joins the Train's Planning]]: the plant must start its ramp when a feature is
demoed, not when the release package arrives — and the train must hear how the ramp is
going while the release is still in its hands.

## Who is responsible for what?

- [[Manufacturing]] — starts fixtures and work instructions for a feature when it reaches
  `Demoed`; brings ramp status to every [[System Demo]].
- [[Manufacturing Lead]] — accepts a release as producible before it leaves `Certified`.
- [[Production Liaison]] — brings ramp status to every [[System Demo]] in a standing slot.
- [[Release Train Engineer]] — adds the ramp-readiness check as a standing row of the
  System Demo and carries blockers to the [[ART Sync]].
- [[System Integration]] — delivers production test firmware with the release candidate,
  not after certification.

## Description

Two columns, one loop. On the [[Manufacturing Board]], `Fixtures and Instructions` is
entered at the demo of the feature, from the demo material and the drawings as they
stand. On the [[Charger ART Board]], a feature leaves `Certified` only with the plant's
producibility acceptance. With the ramp-readiness check at every [[System Demo]], ramp
status flows from the plant back into the train while the feature is still in the
`Release` group. In force from the PI 27.1 planning on 2026-12-03.

## Evaluation Criteria

- Time from release date to first customer shipment under two weeks (today: five).
- Every release leaves `Certified` with a recorded producibility acceptance.

## Concerns

Fixtures started at the demo may need rework when certification forces a design change —
accepted; rework on a fixture is cheaper than five weeks of waiting.

> [!NOTE]
> **Modeling note.** The ramp-readiness check is the feedback edge the [[Feature Route]]
> has been missing.
