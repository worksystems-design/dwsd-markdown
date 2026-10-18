---
type: agreement
agreement-type: work
for-domain: "[[Charger ART]]"
agreement-of:
  - "[[Charger ART Board]]#Charger ART/lane:Field Issue::in"
  - "[[Field Issue Route]]/stage:hotfix @ Train::before"
derived-from: "[[Known Failure Patterns Skip the Weekly Triage]]"
version: "2.0"
decision_date: "2026-10-06"
review_date: "2027-04-06"
created_at: "2026-10-10"
---

## Driver and Requirement

In March 2026 a firmware fault left a depot of DC chargers dark for a weekend because the
fix "would go into the next PI". A charger that does not charge cannot wait ten weeks. The
train needs one lane that bypasses the cadence — and a strict gate on what may use it, or
the lane becomes the way everything gets done.

## Who is responsible for what?

- [[Field Service]] — reports every issue with its observed impact; does not rank.
- The [[Field Issue Triage]] (product owners with [[Mateo Ruiz]] and [[Ravi Anand]]) —
  decides hotfix or feature, weekly; a safety issue is decided the same day, in a
  [[Safety Issue Call]].
- The team that owns the affected component — takes the hotfix immediately, at most one at
  a time.
- [[Connectivity]] — ships the hotfix to the fleet over the air and confirms rollout.

## Description

The `Field Issue` lane of the [[Charger ART Board]] is an **expedite lane**. An issue enters
`Fix-in-Progress` only if it is a safety risk or a fleet is down — everything else becomes a
[[Feature]] and goes to PI planning. WIP in `Fix-in-Progress` is two across the train, one
per team: a second hotfix for the same team waits or is re-decided. Every hotfix is reported
at the next [[System Demo]].

**Known patterns** (since version 2.0). A failure pattern the triage has decided the same
way three times is a known pattern. The [[Field Issue Triage Agent]] routes a report that
matches one itself: the cause goes as a [[Feature]] to the backlog of the owning team, the
customer gets the known workaround the same day. The triage sees known patterns as one
weekly count and takes a pattern back when it changes — a new serial range, a safety
impact, a fleet down. The agent never opens a hotfix.

## Evaluation Criteria

- Safety or fleet-down issues fixed in the fleet within five working days.
- Fewer than one in five triaged issues enters the expedite lane — the rest travels as
  features.
- Customers with a known pattern hear back the same day; no triage slot goes to a repeat
  call.

## Appendix

### Previous Versions

- **2.0** (2026-10-06) — known patterns skip the weekly triage, from
  [[Known Failure Patterns Skip the Weekly Triage]].
- **1.0** (2026-04-07) — the expedite lane, its gate and its WIP limit.
