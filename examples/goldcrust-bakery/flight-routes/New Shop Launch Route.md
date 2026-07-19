---
type: flight-route
created_at: "2026-07-18"
---

How a [[New Shop Launch]] travels from a strategic bet to an open door: the bet is decided
at [[Bakery Strategy]] (FL3), a copy moves to [[Bakery Operations]] (FL2) which
**generates** the concrete launch work — site, fit-out, hiring, range planning — worked by
a temporary launch crew at the operational level. Progress lifts back into the bet, which
is tracked — and finally lands — on the strategy board; the weekly [[Launch Check-in]] is
the interaction that carries that feedback edge. The `Launch Crew` band is
deliberately **unbound**: a temporary crew with no standing board of its own. This is the
top-down strategic route: months, not days, and the delivery is a new work system — from
its first trading day the shop joins the [[Daily Replenishment Flow]].

```dwsd.flightroute
title: New Shop Launch Route
for: "[[New Shop Launch]]"
bands:
  - name: Strategy
    fl: 3
  - name: Coordination
    fl: 2
  - name: Launch Crew
    fl: 1
triggers:
  - name: expansion bet
    generates:
      - shop-launch @ Strategy
path:
  # the decided bet is handed to operations coordination
  - shop-launch @ Strategy --> shop-launch @ Coordination
  # coordination breaks the launch into concrete work
  - shop-launch @ Coordination -> launch-task @ Coordination
  # launch tasks are worked at the operational level
  - launch-task @ Coordination --> launch-task @ Launch Crew
  # coordination progress lifts back into the strategic bet
  - shop-launch @ Coordination ..> shop-launch @ Strategy
  # opening day — the bet lands, tracked on the strategy board
  - shop-launch @ Strategy ..> ()
bound-to:
  - band: Strategy
    boards:
      - board: "[[Bakery Strategy Board]]"
        stages:
          - shop-launch: "col:In-Flight"
  - band: Coordination
    boards:
      - board: "[[Bakery Operations Coordination Board]]"
        stages:
          - shop-launch: "lane:New Shop Launch"
```
