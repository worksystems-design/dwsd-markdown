---
type: interaction
interaction-type: review
for-domain: "[[Bakery Strategy]]"
start: "2026-07-24T14:00:00"
end: "2026-07-24T14:45:00"
rrule: "RRULE:FREQ=WEEKLY;BYDAY=FR"
interaction-of:
  - "[[Bakery Operations Coordination Board]]#Bakery Operations Coordination/lane:New Product Introduction/col:Trial-Bakes::in"
  - "[[New Product Introduction Route]]/stage:new-product @ Bakehouse::after"
created_at: "2026-07-19"
---

## Purpose

The tasting that follows a round of trial bakes: the [[Head Baker]] presents the candidate,
the shop managers ([[Market Street Shop Manager]], [[Station Road Shop Manager]]) bring
what customers actually ask for at the counter, and
[[Mara Holt]] holds the range decision. The outcome is a clear call — into the range,
another trial round with changes, or dropped.

This interaction carries the [[New Product Introduction Route]]'s feedback edge: trial
results flow back into the range decision at [[Bakery Strategy]], anchored `::after` the
route's `new-product @ Bakehouse` stage and on the `Trial-Bakes` column of the FL2 lane.
