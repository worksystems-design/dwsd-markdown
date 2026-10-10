---
type: unit
unit-type: [team, work-system]
flightlevel: 1
member-of: "[[Charger ART]]"
contributes-to:
  - "[[Wallbox]]"
  - "[[DC Charger]]"
delegator: "[[Marit Solberg]]"
tags: [platform]
version: "1.0"
decision_date: "2026-06-29"
review_date: "2026-12-28"
created_at: "2026-10-10"
---

## In context

```dwsd.topology
mode: infer
radius: 2
```

```dwsd.units
mode: infer
focus: self
radius: { up: 1, down: inf }
```

## Purpose

Provide the hardware platform both product lines are built on: the power and metering
module, the control board, and the enclosure base with its tooling. One platform, two
products — so that a power-stage improvement reaches the [[Wallbox]] and the [[DC Charger]]
in the same release instead of being built twice.

## Key Responsibilities

- Own the shared power module, metering, control board and enclosure base.
- Keep a variant roadmap that serves both product teams' PI commitments.
- Run design-for-manufacturing reviews with [[Manufacturing]] before a tooling release.
- Specify long-lead parts and tooling early enough for [[Supply Chain]] to source them.

## Customers and Deliverables

- [[Wallbox]] — the power and metering module in its 7–22 kW variants, the enclosure base.
- [[DC Charger]] — the power module stacked for 50–150 kW, the dispenser enclosure base.
- [[Manufacturing]] — producible designs: drawings, BOM, test specifications.

## Dependencies

Depends on [[Supply Chain]] for power semiconductors and enclosure tooling, on
[[Manufacturing]] for producibility feedback, and on [[System Integration]] for EMC and
safety pre-tests.

## External Constraints

- Injection-mold tooling: about fourteen weeks from release to first parts — longer than
  one PI.
- Power-semiconductor allocation from suppliers, set quarterly.

## Key Challenges

- Two customers with different cadences and priorities pull on one team; the ART decides
  the order, but every PI planning is a negotiation.
- A platform change ripples into both product lines' certification scope.
- Tooling has to be released before the product teams have finished integrating — the
  team commits to a mold while the design is still moving.

## Key Resources

- [[Yara Ben Salem]] (power electronics) and [[Ole Brekke]] (mechanics); the power lab.

## Delegator Responsibilities

- [[Marit Solberg]] decides what is platform and what is product, and arbitrates when the
  two product teams' needs collide.

## Competencies, Qualities and Skills

- Power electronics, thermal and mechanical design, design for manufacturing, saying no
  to variant requests that split the platform.

## Key Metrics and Monitoring

- Platform reuse: share of each product's BOM that is platform; tooling releases on time
  for the PI they serve; DFM findings caught before tooling release.

## Evaluation Schedule

Reviewed at the end of every second PI; next review 2026-12-28.
