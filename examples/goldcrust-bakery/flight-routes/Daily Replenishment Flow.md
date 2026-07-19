---
type: flight-route
created_at: "2026-05-24"
updated_at: "2026-07-18"
---

How a [[Daily Replenishment Order]] moves as a closed loop: **demand up** (each shop's
closing count flows to [[Bakery Operations]]), **plan down** (the confirmed order is
handed to the [[Bakehouse]]), and **product across** — overnight baking turns the order
into the morning **dispatch**, a second item type the route generates, which is delivered
to both shops, where fresh stock reaches the customers. This is the bakery's operational
heartbeat — it runs every day, entirely between FL1 and FL2, and never touches strategy.

The order → dispatch transition happens operationally in the Bakehouse, but the *order*
stays a coordination object: the dotted feedback edge is what lifts dispatch status back
into the order world at FL2, and the interaction that carries it is the
[[Daily Production Sync]] — its afternoon "check the morning dispatch cleared" step
anchors both to the Bakehouse board and to this route's `dispatch @ Bakehouse` stage.
The `bound-to:` layer maps the three bands onto [[Market Street Shop Board]],
[[Station Road Shop Board]], [[Bakery Operations Coordination Board]] and
[[Bakehouse Production Board]].

```dwsd.flightroute
title: Daily Replenishment Flow
for: "[[Daily Replenishment Order]]"
bands:
  - name: Coordination
    fl: 2
  - name: Shops
    fl: 1
  - name: Bakehouse
    fl: 1
triggers:
  - name: evening stock count
    generates:
      - order @ Shops
path:
  # demand up — each shop's closing count becomes the next-day order
  - order @ Shops --> order @ Coordination
  # plan down — the confirmed order is handed to the Bakehouse
  - order @ Coordination --> order @ Bakehouse
  # overnight baking turns the order into the morning dispatch
  - order @ Bakehouse -> dispatch @ Bakehouse
  # product across — the morning dispatch is delivered to both shops
  - dispatch @ Bakehouse --> dispatch @ Shops
  # fresh stock on the shelf reaches the customers
  - dispatch @ Shops ..> ()
  # dispatch status is lifted back into the order world at FL2
  # (carried by the Daily Production Sync)
  - dispatch @ Bakehouse ..> order @ Coordination
bound-to:
  - band: Shops
    boards:
      - board: "[[Market Street Shop Board]]"
        stages:
          - order: "col:Reorder"
          - dispatch: "col:Incoming"
      - board: "[[Station Road Shop Board]]"
        stages:
          - order: "col:Reorder"
          - dispatch: "col:Incoming"
  - band: Coordination
    boards:
      - board: "[[Bakery Operations Coordination Board]]"
        stages:
          - order: "lane:Daily Replenishment Order/col:Demand-In"
  - band: Bakehouse
    boards:
      - board: "[[Bakehouse Production Board]]"
        stages:
          - order: "col:Backlog"
          - dispatch: "col:Ready-for-Dispatch"
```
