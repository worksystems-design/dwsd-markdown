---
type: role
role-keeper: "[[Bastian Lorenz]]"
for-domain: "[[Charger ART]]"
derived-from: "[[Production Joins the Train's Planning]]"
version: "1.0"
decision_date: "2026-10-06"
review_date: "2027-02-24"
created_at: "2026-10-11"
---

## Purpose

### Driver

The decision [[Production Joins the Train's Planning]] brings the plant to the train's
planning without making it a team of the ART. Someone has to sit at that table for the
plant, and has to be able to say what the plant needs before the features exist.

### Requirement

One role inside the [[Charger ART]] that speaks for production at PI planning and the
System Demo, and carries what it hears back to the plant.

## Description

The Production Liaison is the plant's seat in the train. It is kept by
[[Bastian Lorenz]], who also keeps the [[Manufacturing Lead]] role: one person, two
contexts. As Manufacturing Lead he runs the plant inside [[Manufacturing]]; as Production
Liaison he works inside the [[Charger ART]], at its cadence and on its board. Each role
carries its own agreement: the [[Long-Lead Commitment at PI Planning]] is the train-side
one and lands here; the [[Ramp Readiness Review]] is the plant-side one and lands on the
Manufacturing Lead. In force from the PI 27.1 planning on 2026-12-03.

## Concerns

Fixture and test-equipment needs discovered after the features are planned; a seat at
the table without a standing slot on the agenda.

## Accountabilities

- At PI planning *n*, name the fixtures and production test equipment the features of
  PI *n+1* will need, next to the molds [[HW Base]] names.
- Bring ramp status to every [[System Demo]] in the standing slot.
- Carry release dates and design changes from the train back to the plant the same week.

## Decision Rights

- Decides which plant needs go on the train's dependency board (autonomous).
- Does not decide release dates or line sequencing; the [[Charger ART]] and the
  [[Manufacturing Lead]] do.

## Evaluation

### Metrics and Monitoring

- Plant needs raised at PI planning vs. raised later in the PI.
