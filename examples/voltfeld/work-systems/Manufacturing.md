---
type: unit
unit-type: [team, work-system]
flightlevel: 1
member-of: "[[Operations]]"
contributes-to: "[[Portfolio]]"
delegator: "[[Ingrid Halvorsen]]"
version: "1.0"
decision_date: "2025-11-03"
review_date: "2026-11-02"
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

Build, test and ship every Voltfeld charger at the plant, and ramp production for each new
variant the [[Charger ART]] releases. Manufacturing is a work system of its own — it
coordinates a flow of work daily — but it is **not** part of the ART.

Structurally it belongs to [[Operations]], while its output goes to customers and is
steered from the [[Portfolio]] — FL1 straight to FL3. Development and production have no
shared FL2.
The ART coordinates development; the plant is coordinated by the COO.

## Key Responsibilities

- Build and end-of-line test wallboxes and DC chargers to the volume plan.
- Ramp each new variant: fixtures, work instructions, production test, first-article
  inspection.
- Feed design-for-manufacturing findings back to [[HW Base]] and the product lines.

## Customers and Deliverables

- Customers, through [[Sales]] — built, tested chargers on the committed dates.
- [[Portfolio]] — volume, yield and ramp status.

## Dependencies

Depends on [[Supply Chain]] for parts on time, on [[System Integration]] for the production
test firmware, and on the [[Charger ART]] for release dates it currently learns about at
the system demo.

## Key Challenges

- Ramp dates are set by ART releases without production in the room; a new enclosure
  variant means new fixtures, and those are planned after the fact.
- Design changes reach the plant late — first through a revised drawing, not a
  conversation.

## Key Resources

- [[Bastian Lorenz]] (lead) and [[Leyla Demir]] (planning); the line, the end-of-line
  testers, about forty operators.

## Key Metrics and Monitoring

- Output vs. plan; first-pass yield; ramp time from release to stable production;
  parts-shortage hours.

## Evaluation Schedule

Reviewed yearly; next review 2026-11-02.

> [!NOTE]
> **Modeling note.** Note where it sits in the two trees: `member-of` [[Operations]],
> `contributes-to` the [[Portfolio]]. The forty operators are not modeled individually
> here.
