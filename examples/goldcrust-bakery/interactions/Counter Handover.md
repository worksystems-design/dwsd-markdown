---
type: interaction
interaction-type: handover
interaction-of:
  - "@bakehouse-production-board#Ready-for-Dispatch"
  - "@market-street-shop-board#Incoming"
  - "@station-road-shop-board#Incoming"
created_at: "2026-05-24"
---

## Purpose

The morning hand-off where the [[Bakehouse]] dispatch is received and checked in at each
shop counter before opening. A short, recurring interaction — not a meeting, just a defined
moment of contact between work systems, crossing from the Bakehouse's `Ready-for-Dispatch`
column to each shop's `Incoming` column.

The dispatch arrives, the shop counts it against the [[Daily Replenishment Order]], and any
shortfall is flagged immediately to [[Bakery Operations]].
