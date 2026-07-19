---
type: interaction
interaction-type: routine
start: "2026-05-25T18:30:00"
end: "2026-05-25T18:45:00"
rrule: "RRULE:FREQ=DAILY"
interaction-of:
  - "[[Market Street Shop Board]]#Market Street Shop/col:Reorder::in"
  - "[[Station Road Shop Board]]#Station Road Shop/col:Reorder::in"
  - "[[Daily Replenishment Flow]]/stage:order @ Shops::before"
created_at: "2026-06-28"
---

## Purpose

The close-of-day routine at each shop: count the closing stock, compare it against the
day's sell-through, and place tomorrow's [[Daily Replenishment Order]]. This is where demand
enters the flow — each shop's `Reorder` column feeds the [[Daily Replenishment Flow]] up to
[[Bakery Operations]].

A short, recurring interaction — the shop manager at each location
([[Market Street Shop Manager]], [[Station Road Shop Manager]]) counts, records, and
submits the order under the standing authority of the [[Shop Manager Mandate]]. The
afternoon [[Daily Production Sync]] has already set the frame — priorities and capacity;
the count fixes tonight's final quantities within it.

Besides the two board positions, this interaction also anchors to the
[[Daily Replenishment Flow]] itself — `::before` the `order @ Shops` stage, since the
count is what brings tomorrow's order into existence (a route-stage locator, see
`conventions.md`).
