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

A confirmed frame for tomorrow — line priorities, capacity, and bake plan — with owners
for anything unusual (events, weather, special orders). Final quantities are set at
closing by the [[Evening Stock Count]], within this frame.

## What decisions are we making, and who makes them?

Next-day quantities and bake sequence ([[Head Baker]]); trade-offs when capacity is tight
([[Bakery Operations]]).

## What information do we need?

The [[Bakehouse Production Board]], yesterday's closing counts and today's sell-through
so far from both shops, and any known events for tomorrow.

## Interactions

| Name                               | Outcome                              | Interaction of                                                                  |
|------------------------------------|--------------------------------------|---------------------------------------------------------------------------------|
| Pull together the shops' demand    | one shared demand picture            | [[Bakery Operations Coordination Board]]#Bakery Operations Coordination/lane:Daily Replenishment Order/col:Demand-In::in |
| Frame tomorrow's bake plan         | agreed priorities and capacity       | [[Bakery Operations Coordination Board]]#Bakery Operations Coordination/lane:Daily Replenishment Order/col:Planned::in   |
| Hand the plan to the Bakehouse     | next-day plan in production          | [[Bakehouse Production Board]]#Bakehouse Production/col:Backlog::in              |
| Check the morning dispatch cleared | dispatch status confirmed                | [[Bakehouse Production Board]]#Bakehouse Production/col:Ready-for-Dispatch::in   |
| Lift dispatch status into the order world | FL2 order cards current         | [[Daily Replenishment Flow]]/stage:dispatch @ Bakehouse::after                   |
| Flag capacity or supply risks      | risks with owners                    | [[Bakehouse Production Board]]#Bakehouse Production/col:Mixing-Proofing::in      |
