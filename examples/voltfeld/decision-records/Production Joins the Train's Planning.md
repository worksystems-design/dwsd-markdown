---
type: organizational-decision-record
status: accepted
date: "2026-10-06"
decision-makers:
  - "[[Henrik Dahl]]"
  - "[[Ingrid Halvorsen]]"
  - "[[Marit Solberg]]"
for-domain:
  - "[[Charger ART]]"
  - "[[Manufacturing]]"
derived-from: "[[Bring the Plant and Supply Chain into PI Planning]]"
created_at: "2026-10-06"
---

## Context

Since the [[Charger ART]] was chartered in January 2026, Voltfeld has had two planning
horizons that never meet: the train plans ten weeks of development; the plant and the
supply base plan tooling and ramps that take longer than that, and learn about releases
after the fact. [[Manufacturing]] contributes to the [[Portfolio]] directly — there is no
FL2 that coordinates development and production together. Two PIs in a row, a committed
objective slipped on a mold ([[PI Objectives Missed on Enclosure Tooling Twice]]); the
26.3 release shipped five weeks late because fixtures started at the release
([[Fixtures Built After the Release]]). The insight
[[Production Is Outside the Train's Horizon]] named the cause; the driver
[[Long-Lead Work Needs a Longer Horizon Than the PI]] named the need.

## Decision

[[Supply Chain]] and [[Manufacturing]] become **participants of the train's planning** —
PI planning and the System Demo — without becoming teams of the ART. Long-lead work is
planned one PI ahead of the features that need it; ramp readiness is reviewed inside the
PI, not after it. Operationalized by two agreements:
[[Long-Lead Commitment at PI Planning]] and [[Ramp Readiness Review]].

Explicitly **not** decided: no change to the structure. Manufacturing stays in
[[Operations]], the plant does not join the ART board, and the question of a shared FL2
for development and production is deferred until two PIs have run under this decision.

The decision concerns two domains and is anchored on both: the [[Charger ART]], whose
planning gains two participants, and [[Manufacturing]], whose ramp now starts earlier.

## Consequences

- The train commits to objectives whose tooling is already ordered — predictability
  should recover toward the 80% the [[PI Commitment]] asks for.
- The plant hears about a release at the demo and starts fixtures there: the five-week
  gap between release and first shipment should close.
- The [[Feature Route]] gains the edge it is missing today — ramp status flowing from the
  plant back into the train — once the agreements are in force.
- Trade-off: molds are committed a PI earlier, on designs frozen at the DFM review rather
  than fully integrated. [[Supply Chain]] carries that risk and said so.
- PI planning grows by two parties and about half a day.
