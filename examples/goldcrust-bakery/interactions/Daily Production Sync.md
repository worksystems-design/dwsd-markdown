---
type: interaction
interaction-type: meeting
for-domain: "[[Bakehouse]]"
interaction-of: "@bakehouse-production-board"
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

| Name                               | Outcome                              | On board                                       |
|------------------------------------|--------------------------------------|------------------------------------------------|
| Confirm tomorrow's bake quantities | agreed [[Daily Replenishment Order]] | @bakehouse-production-board#Backlog            |
| Check the morning dispatch cleared | shared demand picture                | @bakehouse-production-board#Ready-for-Dispatch |
| Flag capacity or supply risks      | risks with owners                    | @bakehouse-production-board#Mixing-Proofing    |
