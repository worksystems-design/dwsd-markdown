---
type: ai-agent
platform: internal-assistant
status: active
for-domain: "[[Order to Delivery]]"
bound-to:
  - "[[Customer Order Route]]/stage:order @ ERP::in"
  - "[[Order Studio Board]]#Order Studio/col:Flagged::before"
description: Watches every order in the ERP, flags the ones that will not go through, prepares each case with what is missing and the options, and groups reason codes for the monthly review.
tags: [factory-studio]
created_at: "2026-10-11"
---

The Order Exception Agent sits **in the factory**: it reads every order as the ERP
processes it. When an order will not go through — a configuration with no price, a date
the plant's schedule cannot meet, a credit limit — it pulls the [[Order Andon]]: the order
appears in `Flagged` on the [[Order Studio Board]], with the case already prepared.

It does not decide. [[Paula Weiss]] and the people she pulls in do. What the agent adds at
the end is the memory: it groups the month's reason codes for the
[[Order Exceptions Review]], so the loop starts from data instead of from whoever shouts
loudest.

> [!NOTE]
> **Modeling note.** The agent is bound to the `order @ ERP` stage of the
> [[Customer Order Route]]; its second anchor is the slot `::before` the `Flagged` column
> on the [[Order Studio Board]].
>
> `ai-agent` is a preliminary type and the `bound-to` anchor convention may still change.
