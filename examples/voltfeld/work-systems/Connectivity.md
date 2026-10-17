---
type: unit
unit-type: [product-line, work-system]
flightlevel: 2
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
focus: self
radius: { up: 1, down: inf }
```

## Purpose

Build and run the cloud side of every Voltfeld charger: the fleet backend, the OCPP
connection to charge-point operators, the operator and end-user apps, and over-the-air
updates.

An FL2 **product line**: it coordinates two teams, [[Charge Point Backend]] and
[[Driver App]], at PI planning and the [[ART Sync]], and contributes to the
[[Charger ART]], which coordinates across all three product lines on the same level.

## Key Responsibilities

- Develop and operate the backend and apps; keep the OCPP integration certified.
- Ship OTA packages for every system release and roll them out to the fleet.
- Provide the device-side counterpart together with the [[Firmware Platform]], whose
  protocol stack the backend talks to.

## Customers and Deliverables

- [[Charger ART]] — backend features released in step with device releases.
- Charge-point operators and fleet managers — the connected service.
- [[Field Service]] — remote diagnostics and firmware recovery.

## Dependencies

Depends on the [[Firmware Platform]] for the device protocol and OTA client, and on
[[Wallbox]] and [[DC Charger]] for product-specific telemetry.

## Key Metrics and Monitoring

- Backend availability; OTA success rate; time from device release to fleet rollout.

> [!NOTE]
> **Modeling note.** The example draws no board for Connectivity.
