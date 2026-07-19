---
type: interaction
interaction-type: review
for-domain: "[[Bakery Operations]]"
start: "2026-07-21T14:00:00"
end: "2026-07-21T14:30:00"
rrule: "RRULE:FREQ=WEEKLY;BYDAY=TU"
interaction-of:
  - "[[Bakery Operations Coordination Board]]#Bakery Operations Coordination/lane:Wholesale Contract/col:Running::in"
  - "[[Wholesale Contract Route]]/stage:standing-order @ Coordination::in"
created_at: "2026-07-19"
---

## Purpose

The weekly look at every running wholesale account: delivered volumes, delivery
punctuality, complaints, and whether the standing order still fits the [[Bakehouse]]'s
nightly capacity. Standing orders get adjusted here; contracts that drift get flagged for
renegotiation.

This is where delivery experience flows back into the contract world — the review anchors
both to the `Running` column of the wholesale lane and to the
[[Wholesale Contract Route]]'s `standing-order @ Coordination` stage. [[Bakery Operations]]
runs it; the [[Head Baker]] joins when capacity is the question.
