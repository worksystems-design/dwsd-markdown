---
type: visualization
visualization-type: board
title: "Order Studio"
visualization-of: "[[Order to Delivery]]"
tags: [factory-studio]
created_at: "2026-10-11"
---

The studio's board — and only the studio's. The orders that go through never appear here;
their state is in the ERP. What appears here are the cases: flagged, worked, waiting on
the customer, back in the factory. It is small on purpose, and it is the one place where
the people of [[Order to Delivery]] meet every morning ([[Order Studio Huddle]]).

```dwsd.board id=order-studio
title: Order Studio
flightlevel: FL2
aging: 2d
columns:
  - name: Flagged
    status-category: to-do
  - name: In Studio
    wip: 4
    status-category: in-progress
    check: "Cause understood, order corrected or customer asked"
  - name: Waiting on Customer
    status-category: waiting
  - name: Back in the ERP
    status-category: done
    check: "Order released again, reason code set"
lanes:
  - Configuration
  - Date
  - Credit
```
