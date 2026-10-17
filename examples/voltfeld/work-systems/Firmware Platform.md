---
type: unit
unit-type: [team, work-system]
flightlevel: 1
member-of: "[[Charger ART]]"
contributes-to:
  - "[[Wallbox]]"
  - "[[DC Charger]]"
  - "[[Connectivity]]"
delegator: "[[Marit Solberg]]"
tags: [platform]
version: "1.0"
decision_date: "2026-06-29"
review_date: "2026-12-28"
created_at: "2026-10-10"
---

## In context

```dwsd.topology id=topology
mode: infer
radius: 2
```

```dwsd.units id=units
mode: infer
focus: self
radius: { up: 1, down: inf }
```

## Purpose

Provide the firmware every charger runs on: the real-time OS layer, bootloader and OTA
client, the charging-protocol stack (ISO 15118, OCPP client), and the hardware abstraction
for the [[HW Base]] control board. One firmware base serves three teams.

## Key Responsibilities

- Own the firmware base, its release train and its security updates.
- Provide the protocol stack to [[Wallbox]] and [[DC Charger]], and the device side of OTA
  and telemetry to [[Connectivity]].
- Keep the hardware abstraction in step with [[HW Base]] control-board revisions.

## Customers and Deliverables

- [[Wallbox]] and [[DC Charger]] — a versioned firmware base to build product firmware on.
- [[Connectivity]] — the device-side protocol and OTA client the backend talks to.

## Dependencies

Depends on [[HW Base]] for control-board revisions and test hardware, and on
[[System Integration]] for protocol conformance test slots.

## Key Challenges

- Three customers: the product lines want features, Connectivity wants protocol stability,
  and a security fix has to reach all of them in one OTA wave.

## Key Metrics and Monitoring

- Base firmware releases per PI; protocol conformance findings; time to patch a security
  issue across the fleet.

## Evaluation Schedule

Reviewed at the end of every second PI; next review 2026-12-28.
