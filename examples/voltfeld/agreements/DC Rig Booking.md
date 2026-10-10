---
type: agreement
agreement-type: work
for-domain: "[[System Integration]]"
agreement-of: "[[System Integration]]"
version: "1.0"
decision_date: "2026-03-23"
review_date: "2027-03-22"
created_at: "2026-10-10"
---

## Driver and Requirement

There is one high-power test rig. The [[DC Charger]] team needs it for every product
feature, [[HW Base]] for every power-module revision, [[System Integration]] for the release
candidate and the certification pre-tests. In PI 26.1 it was booked by whoever walked in
first, and the release candidate waited behind a platform experiment.

## Who is responsible for what?

- [[System Integration]] — owns the rig schedule; publishes it at PI planning and keeps it
  current at the [[ART Sync]].
- [[DC Charger]] and [[HW Base]] — book slots at PI planning for the PI; ad-hoc requests go
  through [[Priya Raman]].
- [[Release Train Engineer]] — arbitrates when two bookings collide.

## Description

Rig slots are allocated at PI planning for the whole PI. The last iteration of every PI is
reserved for the release candidate and certification pre-tests; product and platform work
on the rig stops there. A hotfix under the [[Expedite Lane Policy]] may take a slot at any
time and displaces platform work first.

Anchored on [[System Integration]] as an entity — the team has no board of its own in this
example, so the agreement shows on its topology node and its unit box.

## Evaluation Criteria

- Release candidate on the rig on the planned date every PI.
- Rig queue time per request under three working days outside the last iteration.
