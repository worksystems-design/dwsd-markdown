---
type: unit
unit-type: team
member-of: "[[Commercial]]"
created_at: "2026-10-10"
---

Field Service, led by [[Mateo Ruiz]], installs and commissions DC chargers, supports the
installer partners for wallboxes, and handles repairs and firmware recoveries in the field.
A plain team. It sees every product first when it fails — which makes it the richest source
of signals in the company and the starting point of the field-issue flow.

## Accountabilities

| Name                                                                   | Mandate of                                    |
|------------------------------------------------------------------------|-----------------------------------------------|
| Log every failure seen on site as a field issue within one working day | [[Field Issue Route]]/stage:issue @ Field::in |

## Decision Rights

| Name                                                                                                   | Mandate of |
|--------------------------------------------------------------------------------------------------------|------------|
| Power-cycle a charger or roll its firmware back on site to restore charging, before triage has seen it |            |

## In context

```dwsd.units id=units
mode: infer
around: self
radius: { up: 1, down: inf }
```
