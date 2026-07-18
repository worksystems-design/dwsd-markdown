---
type: interaction
interaction-type: meeting
for-domain: "[[Bakery Operations]]"
interaction-of: "[[Bakery Operations Coordination Board]]#Bakery Operations Coordination::in"
start: "2026-05-25T13:30:00"
end: "2026-05-25T13:45:00"
rrule: "RRULE:FREQ=DAILY"
version: "1.0"
created_at: "2026-05-24"
---

## Why are we doing this meeting?

Keep the [[Bakehouse]] and the two shops in sync each afternoon, so the next-day bake plan
matches real demand before production starts.

## What is the outcome?

A confirmed next-day [[Daily Replenishment Order]] and bake plan, with owners for anything
unusual (events, weather, special orders).

## What decisions are we making, and who makes them?

Next-day quantities and bake sequence ([[Head Baker]]); trade-offs when capacity is tight
([[Bakery Operations]]).

## What information do we need?

The [[Bakehouse Production Board]], today's sell-through and closing-stock counts from both
shops, and any known events for tomorrow.

## Interactions

| Name                               | Outcome                              | Interaction of                                                                  |
|------------------------------------|--------------------------------------|---------------------------------------------------------------------------------|
| Pull together the shops' demand    | one shared demand picture            | [[Bakery Operations Coordination Board]]#Bakery Operations Coordination/col:Demand-In::in |
| Confirm tomorrow's bake quantities | agreed [[Daily Replenishment Order]] | [[Bakery Operations Coordination Board]]#Bakery Operations Coordination/col:Planned::in   |
| Hand the plan to the Bakehouse     | next-day plan in production          | [[Bakehouse Production Board]]#Bakehouse Production/col:Backlog::in              |
| Check the morning dispatch cleared | shared demand picture                | [[Bakehouse Production Board]]#Bakehouse Production/col:Ready-for-Dispatch::in   |
| Lift dispatch status into the order world | FL2 order cards current         | [[Daily Replenishment Flow]]/stage:dispatch @ Bakehouse::after                   |
| Flag capacity or supply risks      | risks with owners                    | [[Bakehouse Production Board]]#Bakehouse Production/col:Mixing-Proofing::in      |
