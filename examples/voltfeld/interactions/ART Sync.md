---
type: interaction
interaction-type: meeting
for-domain: "[[Charger ART]]"
interaction-of:
  - "[[Charger ART Board]]#Charger ART/lane:Feature/group:In PI::in"
  - "[[Charger ART]]"
start: "2026-09-30T10:00:00"
end: "2026-09-30T10:45:00"
rrule: "RRULE:FREQ=WEEKLY;BYDAY=WE"
version: "1.0"
created_at: "2026-10-10"
---

## Why are we doing this meeting?

Keep the product lines and teams in step inside the PI: where each feature stands, which integration
dates hold, where the two product lines are pulling on the same platform team at once. The
[[Release Train Engineer]] runs it; the product owners, the [[System Architect]] and one
person per team attend. Forty-five minutes, weekly — the train's heartbeat between PI
plannings.

## What is the outcome?

A current picture of every feature in the PI, slipped integration dates raised before they
reach the rig, and platform conflicts sequenced.

## What decisions are we making, and who makes them?

Re-sequencing within the PI ([[Release Train Engineer]], agreed with the teams); platform
priority conflicts ([[System Architect]], escalated to [[Marit Solberg]] when the teams
cannot agree); anything that changes a PI objective goes to the [[Business Owner]]s.

## What information do we need?

The `In PI` group of the [[Charger ART Board]], the team boards, the dependency board from
PI planning, and the rig schedule from [[System Integration]].

## Interactions

| Name                                   | Outcome                                                   | Interaction of                                                                           |
|----------------------------------------|-----------------------------------------------------------|------------------------------------------------------------------------------------------|
| Where is each feature                  | current picture per team                                  | [[Charger ART Board]]#Charger ART/lane:Feature/group:In PI/col:Implementing::in          |
| Dependencies and integration dates     | slipped dates raised with owners                          | [[Charger ART Board]]#Charger ART/lane:Feature/group:In PI/col:Integrating::before       |
| Platform pull conflicts                | sequence agreed between the platforms and product lines   | [[HW Base Board]]#HW Base/group:Design/col:Detailed Design::in                           |
| Lift story status into the feature     | FL2 feature cards current                                 | [[Feature Route]]/stage:story @ Teams::after                                             |
| Risks to the PI objectives             | risks owned, accepted or escalated                        | [[Charger ART Board]]#Charger ART::in                                                    |
