---
type: flight-route
created_at: "2026-05-24"
---

How a [[Daily Replenishment Order]] moves from the afternoon plan through the [[Bakehouse]]
to the shops. (Only the [[Bakehouse]] has a board in this example, so the
`@bakery-operations` and `@market-street-shop` columns below are named but not yet
rendered.)

```flightroute
route "Daily Replenishment Flow"
  for: @daily-replenishment-order
  triggers: Evening stock count at the shops, next-day demand forecast
  path: FL2: @bakery-operations -> FL1: @bakehouse -> FL1: @market-street-shop
  flow:
    FL2: @bakery-operations#Planned
      -[generate: @daily-replenishment-order]-> FL1: @bakehouse#Backlog
    FL1: @bakehouse#Ready for Dispatch
      -[deliver: @daily-replenishment-order]-> FL1: @market-street-shop#Incoming
```
