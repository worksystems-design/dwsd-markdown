---
type: role
role-keeper: "[[Elias Moreau]]"
for-domain: "[[Charger ART]]"
version: "1.0"
decision_date: "2026-01-12"
review_date: "2027-01-11"
created_at: "2026-10-10"
---

## Purpose

### Driver

A charger is one system across power electronics, firmware and cloud. Four teams each
owning a piece will drift apart unless someone holds the whole.

### Requirement

One role that owns the system architecture of the [[Charger ART]] and the line between
platform and product.

## Description

The System Architect defines the system architecture and the architectural runway, decides
what [[HW Base]] and the [[Firmware Platform]] provide versus what [[Wallbox]], [[DC Charger]]
and [[Connectivity]] build on top, and reviews designs before tooling and certification
commit them.

## Concerns

Interface stability between platform and product; variant proliferation that splits the
platform; certification scope creep from a seemingly small change.

## Accountabilities

- Maintain the system architecture and the runway backlog.
- Review platform/product interface changes before they are committed to tooling.
- Advise [[Product Management]] on technical sequencing of features.

## Decision Rights

- Decides interfaces between platform and product (autonomous, after consulting the teams).
- Decides what is platform and what is product — **agrees** with [[Marit Solberg]].

## Evaluation

### Metrics and Monitoring

- Interface changes after tooling release; platform reuse share; runway items ready before
  the features that need them.
