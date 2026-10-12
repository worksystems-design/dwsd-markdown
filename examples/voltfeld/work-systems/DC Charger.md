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

Develop the DC fast-charger product line — 50 to 150 kW systems for depots and public
sites — including the power cabinet, the dispenser and the product firmware on top of the
shared platforms.

An FL2 **product line**: it coordinates two teams, [[DC Power Stage]] and
[[DC Site Controller]], at PI planning and the [[ART Sync]], and contributes to the
[[Charger ART]], which coordinates across all three product lines on the same level.

## Key Responsibilities

- Own the DC Charger variants and their certification scope.
- Deliver committed features into each PI's system release.
- Integrate the shared power module from [[HW Base]] and the firmware base from the
  [[Firmware Platform]]; coordinate payment and fleet features with [[Connectivity]].

## Customers and Deliverables

- [[Charger ART]] — release-ready DC Charger features and variants.
- Fleet operators and site owners, through [[Sales]] and [[Field Service]].

## Dependencies

Depends on [[HW Base]], the [[Firmware Platform]] and [[Connectivity]], and on
[[System Integration]] for high-power test slots — the DC rig is the ART's scarcest
resource.

## Key Metrics and Monitoring

- Features delivered per PI; certification findings per release; commissioning time per
  site.

> [!NOTE]
> **Modeling note.** The example draws no board for DC Charger.
