---
type: unit
unit-type: [art, work-system]
flightlevel: 2
member-of: "[[Voltfeld]]"
contributes-to: "[[Portfolio]]"
delegator: "[[Henrik Dahl]]"
version: "1.0"
decision_date: "2026-01-12"
review_date: "2027-01-11"
created_at: "2026-10-10"
---

## In context

```dwsd.topology
mode: infer
radius: 2
```

## Purpose

Coordinate the six teams that develop Voltfeld's chargers so that features land in
releases together — hardware, firmware and backend in step — on a ten-week Program
Increment cadence. The ART is Voltfeld's one FL2 work system: it plans, syncs and
demonstrates across teams; the teams build.

## Key Responsibilities

- Run PI planning, the weekly ART sync, the system demo and the inspect-and-adapt
  workshop, facilitated by the [[Release Train Engineer]].
- Turn portfolio epics into a ranked feature backlog ([[Product Management]]) and an
  architectural runway ([[System Architect]]).
- Resolve cross-team dependencies — above all between the two product teams and the
  two platform teams they draw on, [[HW Base]] and [[Firmware Platform]].
- Release: integrate, certify and ship a system release at the end of each PI.

## Customers and Deliverables

- [[Portfolio]] — delivered epics, a PI predictability measure, an honest capacity signal.
- [[Manufacturing]] — a release that can be built: drawings, BOM, test firmware.
- [[Field Service]] — release notes, recovery procedures, OTA packages via [[Connectivity]].

## Dependencies

Depends on [[Supply Chain]] for long-lead parts and tooling, on [[Manufacturing]] for ramp
capacity and design-for-manufacturing feedback, and on [[System Integration]] for
certification slots.

## External Constraints

- Certification cycles (IEC 61851, EMC, regional approvals) that take longer than a PI.
- Component availability and tooling lead times set by suppliers.

## Key Challenges

- Enclosure and tooling lead times exceed one PI; the ART plans in ten-week increments
  while Supply Chain works on fourteen-week lead times and is not in the room at PI planning.
- Two product teams pull on the same two platform teams with different priorities.
- Hardware integration happens late — the first time a new power stage meets production
  firmware is on the system rig, not before.

## Key Resources

- Six teams: [[Wallbox]], [[DC Charger]], [[Connectivity]], [[HW Base]],
  [[Firmware Platform]], [[System Integration]]; the ART roles [[Release Train Engineer]],
  [[Product Management]], [[System Architect]]; the HIL and system test rigs.

## Delegator Responsibilities

- [[Henrik Dahl]] chartered the ART and keeps it funded per PI through the [[Portfolio]].

## Competencies, Qualities and Skills

- Cross-team planning under hardware lead times, systems thinking across power
  electronics, firmware and cloud, facilitation of thirty-plus engineers at once.

## Key Metrics and Monitoring

- PI predictability (committed vs. delivered objectives); feature lead time; release
  cadence held; cross-team dependencies open at PI planning.

## Evaluation Schedule

Inspect-and-adapt at the end of every PI; domain description reviewed yearly, next
2027-01-11.
