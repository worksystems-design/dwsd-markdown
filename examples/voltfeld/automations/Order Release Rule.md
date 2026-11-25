---
type: automation
platform: erp
status: active
for-domain: "[[Order to Delivery]]"
bound-to: "[[Order Studio Board]]/col:Back in the ERP::in"
description: Releases a clarified order again when its case carries a reason code.
tags: [factory-studio]
created_at: "2026-11-25"
---

## Trigger

A case reaches `Back in the ERP` with its reason code set.

## What it does

It lifts the hold and releases the order again, so the factory carries on where it stopped.
Without a reason code nothing happens, and the case stays visible. The rule judges nothing:
whether the order is right was settled in the studio. That is what sets it apart from the
[[Order Exception Agent]], which reads each order and prepares a case.

> [!NOTE]
> **Modeling note.** Bound to the one column where the rule acts. It holds no mandates;
> `for-domain` names the work system that answers for it.
