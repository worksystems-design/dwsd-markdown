---
type: visualization
visualization-type: board
title: "Bakery Strategy"
visualization-of: "[[Bakery Strategy]]"
created_at: "2026-06-28"
---

The FL3 strategy board for [[Bakery Strategy]] — only a handful of strategic bets are ever in
motion at once (e.g. a [[New Shop Launch]]). A bet moves from `Discovery` through being
understood and decided, to `Ready-for-Flight`, `In-Flight`, and finally `Landed`. Kept
deliberately small: this is where the bakery looks at *what to take on*, not how to run it.

```dwsd.board
title: Bakery Strategy
flightlevel: FL3
agreements:
  - "Only bets that change the product range or footprint enter here"
columns:
  - name: Discovery
    status-category: to-do
  - Understood
  - name: Decided
    status-category: in-progress
    agreements:
      - "A bet enters flight only with an owner and a funded first step"
  - name: Ready-for-Flight
    status-category: in-progress
  - name: In-Flight
    status-category: in-progress
  - name: Landed
    status-category: done
```
