---
type: unit
unit-type: [team, work-system]
flightlevel: 1
member-of: "[[Charger ART]]"
contributes-to: "[[Charger ART]]"
delegator: "[[Marit Solberg]]"
version: "1.0"
decision_date: "2026-01-12"
review_date: "2027-01-11"
created_at: "2026-10-10"
---

## In context

```dwsd.topology id=topology
mode: infer
radius: 2
```

```dwsd.units id=units
mode: infer
around: self
radius: { up: 1, down: inf }
```

## Purpose

Integrate what the teams build into one system release and prove that it is safe and
compliant: system and HIL test rigs, EMC and safety pre-tests, and the certification
dossiers for IEC 61851 and regional approvals. The ART's system team.

## Key Responsibilities

- Run the system and HIL rigs; integrate every PI's release candidate.
- Pre-test EMC and safety; prepare and track the certification dossiers.
- Hand a buildable, certified release to [[Manufacturing]] with its production test
  firmware.

## Customers and Deliverables

- [[Charger ART]] — an integrated, certified system release per PI.
- [[Manufacturing]] — the production test specification and firmware.

## Dependencies

Depends on all four product and platform teams delivering to the integration dates, and on
external test houses for certification slots.

## Key Challenges

- The DC test rig is one; two product lines and the platform queue for it.
- A certification finding late in the PI can hold the whole release.

## Key Metrics and Monitoring

- Integration defects per release; certification findings; rig utilization and queue time.
