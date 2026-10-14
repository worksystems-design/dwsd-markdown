---
type: interaction
interaction-type: meeting
for-domain: "[[Charger ART]]"
interaction-of:
  - "[[Charger ART Board]]#Charger ART::in"
  - "[[Charger ART]]"
start: "2026-09-24T09:00:00"
end: "2026-09-25T17:00:00"
rrule: "RRULE:FREQ=WEEKLY;INTERVAL=10;BYDAY=TH"
version: "1.0"
created_at: "2026-10-10"
---

## Why are we doing this meeting?

Two days, every ten weeks, all teams of the [[Charger ART]] in one room with the
[[Business Owner]]s: the only moment the whole train plans together. Features become team
objectives, dependencies between the product lines and the platforms get owners and
integration dates, and the train commits to a PI it believes in.

## What is the outcome?

Committed PI objectives per team with business value assigned, a dependency board with
owners and dates, and a confidence vote the train stands behind.

## What decisions are we making, and who makes them?

PI content and feature ranking ([[Product Management]] with the [[Business Owner]]s);
team objectives and capacity ([[Product Owner Wallbox]], [[Product Owner DC Charger]] and
their teams); architectural runway ([[System Architect]]); scope cuts after the management
review (the Business Owners).

## What information do we need?

The [[Portfolio Board]] and the epics in `Implementing`; the refined feature backlog; each
team's capacity for five iterations; certification slots from [[System Integration]]; the
platform roadmaps of [[HW Base]] and the [[Firmware Platform]]. Not an input today: lead
times for long-lead parts and tooling — [[Supply Chain]] is not in the room, and
[[Manufacturing]] is represented only through [[Ingrid Halvorsen]] as Business Owner.

## Interactions

| Name                                          | Outcome                                             | Interaction of                                                                              |
|-----------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------|
| Business context and PI vision                | shared priorities; the epics in play                | [[Portfolio Board]]#Portfolio/col:Implementing::in                                          |
| Architecture vision and runway                | runway items the features need                      | [[Charger ART Board]]#Charger ART/lane:Feature/group:Preparation/col:Refined::in            |
| Team breakouts: features into stories         | draft PI objectives per team                        | [[Wallbox Board]]#Wallbox/col:PI Backlog::in                                         |
| Dependency board                              | cross-team dependencies with owners and dates       | [[Charger ART Board]]#Charger ART/lane:Feature/group:In PI/col:Implementing::before         |
| Management review and problem solving         | scope adjusted overnight                            | [[Charger ART Board]]#Charger ART::in                                                       |
| Business value and confidence vote            | committed PI objectives                             | [[Epic Route]]/stage:Epic @ Train::in                                                       |
