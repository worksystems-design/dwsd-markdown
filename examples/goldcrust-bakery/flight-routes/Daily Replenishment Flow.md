---
type: flight-route
created_at: "2026-05-24"
---

How a [[Daily Replenishment Order]] moves as a closed loop across the boards: **demand up**
(each shop's closing count flows to [[Bakery Operations]]), **plan down** (the confirmed
plan is handed to the [[Bakehouse]]), and **product across** (the morning dispatch goes out
to both shops). Every column below is rendered by a board — the work-system handles resolve
to [[Bakery Operations Coordination Board]], [[Bakehouse Production Board]],
[[Market Street Shop Board]] and [[Station Road Shop Board]].

```flightroute
route "Daily Replenishment Flow"
  for: @daily-replenishment-order
  triggers: Evening stock count at the shops, next-day demand forecast
  path: FL1: @market-street-shop -> FL2: @bakery-operations -> FL1: @bakehouse -> FL1: @market-street-shop
  flow:
    # Demand up — each shop's closing count becomes the next-day order
    FL1: @market-street-shop#Reorder
      -[signal: @daily-replenishment-order]-> FL2: @bakery-operations#Demand-In
    FL1: @station-road-shop#Reorder
      -[signal: @daily-replenishment-order]-> FL2: @bakery-operations#Demand-In
    # Plan down — confirmed plan handed to the Bakehouse
    FL2: @bakery-operations#Planned
      -[generate: @daily-replenishment-order]-> FL1: @bakehouse#Backlog
    # Product across — morning dispatch to both shops
    FL1: @bakehouse#Ready-for-Dispatch
      -[deliver: @daily-replenishment-order]-> FL1: @market-street-shop#Incoming
    FL1: @bakehouse#Ready-for-Dispatch
      -[deliver: @daily-replenishment-order]-> FL1: @station-road-shop#Incoming
```
