---
type: flight-route
created_at: "2026-07-18"
---

How a [[Wholesale Contract]] goes from first enquiry to a running account: a café or
restaurant asks for a standing daily bread order, [[Bakery Operations]] negotiates and
plans it, and the signed contract **generates** a standing order that joins nightly
production at the [[Bakehouse]]. This is the acquisition route — one flight item type
creating another: the contract lives on at FL2 while the standing order it spawned runs
the daily delivery. The Bakehouse bakes each night's batch, but the delivery is tracked
on the standing order at FL2. Delivery experience feeds the contract world through the
weekly [[Wholesale Account Review]], and the [[Wholesale Capacity Cap]] limits how much
of the Bakehouse's night a growing wholesale book may claim.

```dwsd.flightroute
title: Wholesale Contract Route
for: "[[Wholesale Contract]]"
bands:
  - name: Coordination
    fl: 2
  - name: Bakehouse
    fl: 1
triggers:
  - name: wholesale enquiry
    generates:
      - contract @ Coordination
path:
  # a signed contract spawns its standing daily order
  - contract @ Coordination -> standing-order @ Coordination
  # the standing order joins nightly production
  - standing-order @ Coordination --> standing-order @ Bakehouse
  # the recurring early-morning delivery — tracked on the standing order at FL2
  - standing-order @ Coordination ..> ()
bound-to:
  - band: Coordination
    boards:
      - board: "[[Bakery Operations Coordination Board]]"
        stages:
          - contract: "lane:Wholesale Contract/col:Negotiation"
          - standing-order: "lane:Wholesale Contract/col:Running"
  - band: Bakehouse
    boards:
      - board: "[[Bakehouse Production Board]]"
```
