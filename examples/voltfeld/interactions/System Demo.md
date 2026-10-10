---
type: interaction
interaction-type: meeting
for-domain: "[[Charger ART]]"
interaction-of:
  - "[[Charger ART Board]]#Charger ART/lane:Feature/group:Release/col:Demoed::in"
  - "[[Charger ART]]"
start: "2026-10-08T14:00:00"
end: "2026-10-08T15:30:00"
rrule: "RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=TH"
version: "1.0"
created_at: "2026-10-10"
---

## Why are we doing this meeting?

Every two weeks the integrated increment runs on the system rig at [[System Integration]] —
hardware, firmware and backend together, not three slide decks. The [[Business Owner]]s
see what the PI has produced so far and accept or challenge it. [[Bastian Lorenz]] attends
as a guest: today the demo is the first place the plant learns what the next release
contains.

## What is the outcome?

Accepted features move on toward certification; challenged ones go back with a reason;
and the plant has heard the release outlook — ten weeks before the release, sometimes
less.

## What decisions are we making, and who makes them?

Feature acceptance ([[Product Management]]); PI objective status (the [[Business Owner]]s);
whether a finding is a hotfix or waits for the next PI (the product owners with the
[[Release Train Engineer]]).

## What information do we need?

The increment on the rig; the `Release` group of the [[Charger ART Board]]; open
certification findings from [[Marek Novotny]].

## Interactions

| Name                                      | Outcome                                                 | Interaction of                                                                        |
|-------------------------------------------|---------------------------------------------------------|---------------------------------------------------------------------------------------|
| Demo the integrated increment              | features shown end to end on the rig                    | [[Charger ART Board]]#Charger ART/lane:Feature/group:Release/col:Demoed::in           |
| Business Owners accept or challenge        | accepted features move toward certification             | [[Charger ART Board]]#Charger ART/lane:Feature/group:Release/col:Demoed::after        |
| Release outlook for the plant              | Manufacturing hears the release scope                   | [[Manufacturing Board]]#Manufacturing/col:Release Received::before                    |
| Demo results back into the feature         | feature cards current at FL2                            | [[Feature Route]]/stage:story @ Teams::after                                          |
