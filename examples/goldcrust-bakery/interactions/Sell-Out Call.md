---
type: interaction
interaction-type: conversation
for-domain: "[[Bakery Operations]]"
interaction-of:
  - "[[Daily Replenishment Flow]]/stage:dispatch @ Shops::in"
  - "[[Bakehouse]]"
created_at: "2026-10-12"
---

## Trigger

A shop sells out of a bread before 11:00. No calendar entry: the call happens when the
shelf is empty, some weeks twice, some weeks never.

## Purpose

The shop manager ([[Lena Frei]] or [[Selin Aydin]]) phones the Bakehouse, and [[Mara Holt]]
decides on the spot: either what is left on the cooling racks goes out with a midday drop
by [[Deliveries]], or the gap waits, and the shop writes it into tonight's
[[Evening Stock Count]] so tomorrow's order grows. Five minutes, standing up.

> [!NOTE]
> **Modeling note.** Anchored on the [[Daily Replenishment Flow]] where the dispatch
> stands on the shelf (`dispatch @ Shops::in`), and on the [[Bakehouse]], the work system
> that picks up the phone. Compare the [[Evening Stock Count]] on the same route: that one
> runs at 18:30 every day; this one runs when something happens.
