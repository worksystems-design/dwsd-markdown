---
type: organizational-decision-record
status: accepted
date: "2026-10-06"
decision-makers:
  - "[[Lukas Weber]]"
  - "[[Sofia Marques]]"
  - "[[Mateo Ruiz]]"
for-domain: "[[Charger ART]]"
derived-from: "[[Let the Agent Route Known Failure Patterns]]"
created_at: "2026-10-06"
---

## Context

Every field issue of the [[Charger ART]] has gone through the weekly
[[Field Issue Triage]] since the [[Expedite Lane Policy]] came into force in April 2026. The
[[Failure Pattern Review]] at the end of September found one pattern that came in eleven
times and was decided the same way each time
([[Same Failure Pattern Eleven Times in September]]). The insight
[[A Known Failure Pattern Is Decided Again Every Week]] named the cost; the driver
[[Triage Time Goes to Calls Already Made]] named the need.

## Decision

A pattern the triage has decided the same way three times is a **known pattern**. The
[[Field Issue Triage Agent]] routes reports that match one without waiting for the triage:
the cause goes to the owning team's backlog, the customer gets the known workaround the
same day. The triage reviews the known patterns as one weekly count and takes a pattern
back when it changes. Operationalized by version 2.0 of the [[Expedite Lane Policy]].

Explicitly **not** decided: the agent does not open hotfixes. Safety risks and fleets down
stay with the people, the same day, as before.

## Consequences

- The triage's half hour goes to issues that are new.
- Customers with a known fault hear back the same day instead of after Tuesday.
- Trade-off: a pattern that drifts may be routed wrongly for up to a week, until the count
  shows it.

## Change trail

```dwsd.change-trail id=change-trail
focus: self
```
