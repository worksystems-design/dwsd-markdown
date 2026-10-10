---
type: interaction
interaction-type: meeting
for-domain: "[[Charger ART]]"
interaction-of:
  - "[[Charger ART Board]]#Charger ART::in"
  - "[[Charger ART]]"
start: "2026-09-23T09:00:00"
end: "2026-09-23T16:00:00"
rrule: "RRULE:FREQ=WEEKLY;INTERVAL=10;BYDAY=WE"
version: "1.0"
created_at: "2026-10-10"
---

## Why are we doing this meeting?

The PI's closing day, the day before the next PI planning: the whole increment is shown,
the numbers are looked at — above all PI predictability — and the train picks the few
problems it will actually work on. Facilitated by the [[Release Train Engineer]]; the
[[Business Owner]]s attend the first half.

## What is the outcome?

A PI system demo seen by everyone, the predictability measure for the PI, and improvement
items with owners that enter the next PI's backlog as work — not as good intentions.

## What decisions are we making, and who makes them?

Which problems the train takes on next PI (the train, by vote); which improvement items
become backlog items (the [[Release Train Engineer]] with [[Product Management]]).

## What information do we need?

The whole [[Charger ART Board]], the PI objectives with their business value, the
predictability measure, and the root causes gathered through the PI. The last two
workshops both landed on the same cause — tooling lead times that outrun the PI — without
an item that reached outside the train.

## Interactions

| Name                          | Outcome                                           | Interaction of                                                                           |
|-------------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------|
| PI system demo                | the whole PI's increment shown                    | [[Charger ART Board]]#Charger ART/lane:Feature/group:Release/col:Demoed::in              |
| Quantitative measurement      | predictability and flow metrics for the PI        | [[Charger ART Board]]#Charger ART::in                                                    |
| Problem-solving workshop      | root causes and improvement items with owners     | [[Charger ART Board]]#Charger ART/lane:Feature/group:Preparation/col:Program Backlog::before |
