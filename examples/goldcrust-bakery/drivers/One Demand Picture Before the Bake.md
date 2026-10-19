---
type: driver
for-domain: "[[Bakery Operations]]"
derived-from: "[[Demand Reaches the Bakehouse in Separate Calls]]"
status: addressed
created_at: "2026-05-13"
---

[[Bakery Operations]] needs both shops' demand in one picture before the [[Bakehouse]]
sets tomorrow's bake.

## Current Situation

Each shop calls the Bakehouse separately and at no fixed time. The bake plan follows
whichever call came first.

## Effect

Lines are baked against partial numbers: one shop runs short while the other carries
leftovers.

## Need

One fixed point each day where the shops' demand and the Bakehouse's capacity meet.

## Consequences

A shared demand picture lets the Bakehouse plan against real numbers; it also gives
cross-team questions a home.
