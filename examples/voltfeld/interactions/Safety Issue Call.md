---
type: interaction
interaction-type: conversation
for-domain: "[[Charger ART]]"
interaction-of:
  - "[[Field Issue Route]]/stage:issue @ Train::before"
  - "[[Field Service]]"
created_at: "2026-10-12"
---

## Trigger

[[Field Service]] reports a [[Field Issue]] with a safety risk — a charger that runs hot, a
cable that stays live — or a fleet that is down. The weekly [[Field Issue Triage]] is too
late for that, so the report itself is the trigger.

## Purpose

[[Mateo Ruiz]] calls the product owner of the affected product line and
[[Greta Vossberg]] within the hour. The call makes the same decision the triage would make
— hotfix or feature — and nothing else: no root cause, no planning. A hotfix goes straight
into `Fix-in-Progress` under the [[Expedite Lane Policy]]; the issue card notes who decided
and when. The next triage reviews the call, not the issue.

Anchored on the [[Field Issue Route]] *before* the issue reaches the train
(`issue @ Train::before`), where the weekly triage sits *in* the same stage — one by the
calendar, one by the event. And on [[Field Service]], which starts it.
