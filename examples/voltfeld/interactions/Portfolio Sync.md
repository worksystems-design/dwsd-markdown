---
type: interaction
interaction-type: meeting
for-domain: "[[Portfolio]]"
interaction-of:
  - "[[Portfolio Board]]#Portfolio::in"
  - "[[Portfolio]]"
start: "2026-10-06T14:00:00"
end: "2026-10-06T15:30:00"
rrule: "RRULE:FREQ=MONTHLY;BYDAY=1TU"
version: "1.0"
created_at: "2026-10-10"
---

## Why are we doing this meeting?

The five leaders of the [[Portfolio]] look at the epics once a month: what moved, what the
train delivered, what the plant can build and when, and which bets in the funnel deserve a
business case. It is also — today — the only recurring place where development and
production are discussed in the same room: at FL3, monthly, through [[Marit Solberg]] and
[[Ingrid Halvorsen]].

## What is the outcome?

Epic decisions, ramp dates for the next release set with the plant, and funnel items moved
into `Reviewing` or dropped.

## What decisions are we making, and who makes them?

Epic go/stop and funding ([[Henrik Dahl]] with the group); ramp dates and volume
([[Ingrid Halvorsen]] with [[Niamh Byrne]]); market entry and pricing ([[Rolf Steinbach]]).

## What information do we need?

The [[Portfolio Board]]; the train's PI results from the [[Release Train Engineer]]; output,
yield and ramp status from the [[Manufacturing Board]]; pipeline from [[Sales]].

## Interactions

| Name                                 | Outcome                                       | Interaction of                                                   |
|--------------------------------------|-----------------------------------------------|------------------------------------------------------------------|
| Epic review                          | status and decisions per epic in flight       | [[Portfolio Board]]#Portfolio/col:Implementing::in               |
| PI results from the train            | predictability and scope changes understood   | [[Epic Route]]/stage:feature @ Train::after                      |
| Volume and ramp plan with the plant  | ramp dates set for the next release           | [[Manufacturing Board]]#Manufacturing/col:Ramp::in               |
| Funnel review                        | epics into Reviewing, or dropped              | [[Portfolio Board]]#Portfolio/col:Funnel::in                     |
