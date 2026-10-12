---
type: flight-route
created_at: "2026-10-10"
---

How a [[Feature]] travels through one PI — and where it leaves the train. At PI planning
the train hands it to a product line, which gives it to one of its teams; the team breaks it
into stories; progress and demo results flow back into the
feature at the weekly [[ART Sync]] and the biweekly [[System Demo]]; at the end of the PI
the features bundle into one system **release**, a second item type the route generates.
The release is then **copied to the plant**: drawings, BOM and production test firmware land
at [[Manufacturing]], which builds the chargers that ship.

At the plant, the release arrives, the chargers leave — and **nothing goes back**. Ramp
status, fixture problems, a drawing the line cannot build — none of it has a path into the
train today.

```dwsd.flightroute
title: Feature Route
for: "[[Feature]]"
for-domain: "[[Charger ART]]"
bands:
  - name: Train
    fl: 2
  - name: Product Lines
    fl: 2
  - name: Teams
    fl: 1
  - name: Plant
    fl: 1
triggers:
  - name: epic split by Product Management, or a market request
    generates:
      - feature @ Train
path:
  # a product line takes the feature at PI planning
  - feature @ Train --> feature @ Product Lines
  # the product line gives it to one of its teams
  - feature @ Product Lines --> feature @ Teams
  # the team breaks it into stories
  - feature @ Teams -> story @ Teams
  # story progress flows back into the product line's feature
  - story @ Teams ..> feature @ Product Lines
  # feature progress and demo results flow back to the train (ART Sync, System Demo)
  - feature @ Product Lines ..> feature @ Train
  # the PI's features bundle into one system release
  - feature @ Train -> release @ Train
  # the release lands at the plant as drawings, BOM and production test firmware
  - release @ Train --> release @ Plant
  # built chargers ship to customers
  - release @ Plant ..> ()
  # (no edge from Plant back to Train — the gap the change ladder addresses)
bound-to:
  - band: Train
    boards:
      - board: "[[Charger ART Board]]"
        stages:
          - feature: "lane:Feature/group:In PI/col:Implementing"
          - release: "lane:Feature/group:Release/col:Released"
  - band: Product Lines
    boards:
      - board: "[[Wallbox Board]]"
        stages:
          - feature: "lane:Wallbox Home/col:In Progress"
  - band: Teams
    boards:
      - board: "[[HW Base Board]]"
  - band: Plant
    boards:
      - board: "[[Manufacturing Board]]"
        stages:
          - release: "col:Release Received"
```

> [!NOTE]
> **Modeling note.** Read the `Plant` band carefully: **no edge carries anything back**.
> The feedback edges stop at the teams. That missing edge is the as-is this example's
> change ladder starts from.
