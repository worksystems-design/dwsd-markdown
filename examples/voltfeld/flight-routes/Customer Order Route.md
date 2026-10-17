---
type: flight-route
sources:
  erp:
    id: "O2C-STD"
    url: "https://erp.example.com/process/O2C-STD"
created_at: "2026-10-11"
---

How a [[Customer Order]] travels — and what happens to the ones that do not go through. The
route has two bands without a flight level, and they are not places but **modes**:

- `ERP` is **factory mode**. Order entry, scheduling, the production order and the invoice
  are defined and run in the system of record. Nobody touches an order here: the ERP is
  where its state lives.
- `Studio` is **studio mode**. When the [[Order Exception Agent]] flags an order — a
  configuration the ERP cannot price, a date the plant cannot make, a credit block — the
  order leaves the factory as a **case**. People work it together with the agent on the
  [[Order Studio Board]], and the clarified order flows back into the ERP.

The edge from `ERP` to `Studio` is the **andon**: the defined trigger that stops one order,
not the line. The [[Order Andon]] agreement says who answers within what time. The edge
back is the part most order processes forget: a case is done when the order is back in
the factory, with a reason code that the [[Order Exceptions Review]] reads each month.

```dwsd.flightroute id=customer-order-route
title: Customer Order Route
for: "[[Customer Order]]"
for-domain: "[[Order to Delivery]]"
tags: [factory-studio]
bands:
  - name: ERP
  - name: Studio
  - name: Plant
    fl: 1
triggers:
  - name: a fleet operator, depot or installer places an order
    generates:
      - order @ ERP
path:
  # factory mode: scheduling turns the order into a production job, no hands
  - order @ ERP -> job @ ERP
  # the job is released to the line
  - job @ ERP --> job @ Plant
  # built and tested: the confirmation flows back into the order
  - job @ Plant ..> order @ ERP
  # the order is invoiced and closed
  - order @ ERP -> invoice @ ERP
  - invoice @ ERP ..> ()
  # the andon: an order that will not go through leaves the factory as a case
  - order @ ERP --> case @ Studio
  # clarified, with a reason code: the order flows back into the factory
  - case @ Studio ..> order @ ERP
bound-to:
  - band: Studio
    boards:
      - board: "[[Order Studio Board]]"
        stages:
          - case: "col:In Studio"
  - band: Plant
    boards:
      - board: "[[Manufacturing Board]]"
        stages:
          - job: "col:Stable Production"
```

> [!NOTE]
> **Modeling note.** The `sources:` block above points at the ERP process. The `ERP` band
> is bound to **no board** on purpose: the ERP is where its state lives. The
> [[Order Andon]] agreement sits on the edge from `ERP` to `Studio`.
