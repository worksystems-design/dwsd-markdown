---
type: agreement
agreement-type: work
for-domain: "[[Bakehouse]]"
agreement-of: "@bakehouse-production-board#Mixing-Proofing"
version: "1.0"
decision_date: "2026-05-26"
review_date: "2026-08-26"
created_at: "2026-06-28"
---

## Driver and Requirement

The proofers and mixer are the [[Bakehouse]]'s tightest constraint in the morning window.
When too many batches enter mixing and proofing at once, dough over-proofs while it waits
for an oven, and quality drops. The flow needs a cap that protects the bottleneck.

## Who is responsible for what?

- [[Bakehouse]] — keeps no more than three batches in `Mixing-Proofing` at any time and
  pulls the next batch only when a slot frees up.
- [[Head Baker]] — decides batch sequence and which line takes a freed slot.
- [[Bakery Operations]] — reviews the limit if dispatch on-time rates slip.

## Description

The `Mixing-Proofing` column on the [[Bakehouse Production Board]] carries a WIP limit of
three (`[3]`). It is a pull policy, not a target: a new batch starts only when an in-flight
batch moves on to `Baking`.

## Evaluation Criteria

- No batch over-proofs while waiting for an oven.
- Morning dispatch on-time rate holds with the limit in place.

## Concerns

If demand spikes, three concurrent batches may be too few to clear the morning range — the
review exists to retune the number against real throughput.
