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

Develop the AC wallbox product line — 7 to 22 kW chargers for homes, workplaces and
semi-public parking — from feature to release-ready variant.

An FL2 **product line**: it coordinates two teams, [[Wallbox Home]] and [[Wallbox Fleet]], on the [[Wallbox Board]],
and contributes to the [[Charger ART]], which coordinates across all three product lines
on the same level.

## Key Responsibilities

- Own the Wallbox variants: product-specific hardware, enclosure fit, product firmware.
- Deliver committed features into each PI's system release.
- Integrate what the platforms provide: the power and metering module from [[HW Base]],
  the firmware base and protocol stack from the [[Firmware Platform]].

## Customers and Deliverables

- [[Charger ART]] — release-ready Wallbox features and variants.
- Installers and home owners, through [[Sales]] and [[Field Service]].

## Dependencies

Depends on [[HW Base]] for the power module and enclosure base, on the
[[Firmware Platform]] for the OS, bootloader and charging protocol, and on
[[Connectivity]] for backend features that span device and cloud.

## Key Metrics and Monitoring

- Features delivered per PI; integration defects found on the system rig; field failure
  rate per thousand units.
