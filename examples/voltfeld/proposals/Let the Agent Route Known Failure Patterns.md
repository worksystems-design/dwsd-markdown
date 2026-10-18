---
type: proposal
for-domain: "[[Charger ART]]"
derived-from: "[[Triage Time Goes to Calls Already Made]]"
status: consented
created_at: "2026-10-05"
---

## Proposal

A failure pattern the [[Field Issue Triage]] has decided the same way three times becomes a
**known pattern**. When the [[Field Issue Triage Agent]] matches a new report to a known
pattern, it routes the report itself: the cause goes as a [[Feature]] to the backlog of the
team that owns it, the customer gets the known workaround the same day, and the case does
not wait for Tuesday. The triage sees known patterns only as one weekly count, and takes a
pattern back the moment it changes (a new serial range, a safety impact, a fleet down).

## Objections

- [[Sofia Marques]]: an agent deciding on its own — addressed: it decides nothing new, it
  applies a call the people already made, and every routing is in the weekly count.
- [[Mateo Ruiz]]: a pattern can drift — accepted; anything outside the known pattern goes
  back to the triage.

## Outcome

Consented at the [[Field Issue Triage]] on 2026-10-06. Recorded as
[[Known Failure Patterns Skip the Weekly Triage]]; operationalized by version 2.0 of the
[[Expedite Lane Policy]].
