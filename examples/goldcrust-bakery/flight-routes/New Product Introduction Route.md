---
type: flight-route
created_at: "2026-07-18"
---

How a [[New Product Introduction]] travels bottom-up: an idea starts on the floor — a
customer request at the counter, a baker's experiment in the [[Bakehouse]] — is pitched
up to [[Bakery Strategy]] as a range bet (the strategy board only takes bets that change
the product range or footprint), and the decided product comes back down through
[[Bakery Operations]] for rollout and into the Bakehouse for trial bakes. The
introduction itself is delivered from the coordination band — the Bakehouse bakes, but
"the product stands in the daily range" is tracked where the flight item lives, on the
FL2 board's `New Product Introduction` lane. The mirror image of the
[[New Shop Launch Route]]: FL1 → FL3 → FL2 → FL1.

```dwsd.flightroute
title: New Product Introduction Route
for: "[[New Product Introduction]]"
bands:
  - name: Bakehouse
    fl: 1
  - name: Coordination
    fl: 2
  - name: Strategy
    fl: 3
triggers:
  - name: counter requests and bakers' ideas
    generates:
      - product-idea @ Bakehouse
path:
  # the idea is pitched up as a range bet
  - product-idea @ Bakehouse --> product-idea @ Strategy
  # the decided bet becomes a new product
  - product-idea @ Strategy -> new-product @ Strategy
  # rollout is coordinated at FL2
  - new-product @ Strategy --> new-product @ Coordination
  # trial bakes and recipe finalization in the Bakehouse
  - new-product @ Coordination --> new-product @ Bakehouse
  # trial results feed back into the range decision
  - new-product @ Bakehouse ..> new-product @ Strategy
  # the introduction is done when the product stands in the daily range —
  # delivered and tracked at the new-product level, not the operational one
  - new-product @ Coordination ..> ()
bound-to:
  - band: Strategy
    boards:
      - board: "[[Bakery Strategy Board]]"
        stages:
          - product-idea: "col:Discovery"
  - band: Coordination
    boards:
      - board: "[[Bakery Operations Coordination Board]]"
        stages:
          - new-product: "lane:New Product Introduction"
  - band: Bakehouse
    boards:
      - board: "[[Bakehouse Production Board]]"
```
