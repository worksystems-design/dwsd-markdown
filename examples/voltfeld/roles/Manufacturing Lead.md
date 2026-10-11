---
type: role
role-keeper: "[[Bastian Lorenz]]"
for-domain: "[[Manufacturing]]"
version: "1.0"
decision_date: "2025-11-03"
review_date: "2026-11-02"
created_at: "2026-10-10"
---

## Purpose

### Driver

The plant builds what the [[Charger ART]] designs, to volumes the [[Portfolio]] sets, from
parts [[Supply Chain]] delivers — three inputs, none of them under its control. Someone has
to hold the line steady in the middle.

### Requirement

One role accountable for output, yield and ramps at the plant.

## Description

The Manufacturing Lead runs the [[Manufacturing]] work system day to day: the line, the
end-of-line test, the ramp of every new variant. Kept by [[Bastian Lorenz]]. The role is
not part of the ART; it meets the ART's output at the system demo and as drawings. From the
PI 27.1 planning on, the same person also keeps the [[Production Liaison]] role inside the
train; the [[Ramp Readiness Review]] stays with this role.

## Concerns

Ramp dates set without the plant in the room; design changes that arrive as revised
drawings; parts shortages that stop the line.

## Accountabilities

- Deliver the volume plan at target yield.
- Ramp every new variant: fixtures, work instructions, production test.
- Feed design-for-manufacturing findings back to [[HW Base]].

## Decision Rights

- Decides line sequencing and shift plan (autonomous).
- Accepts or rejects a release as producible — **agrees** with the [[System Architect]].
- Does not decide release dates; the [[Charger ART]] does.

## Evaluation

### Metrics and Monitoring

- Output vs. plan; first-pass yield; ramp time per variant.
