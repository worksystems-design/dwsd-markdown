---
type: flight-route
---
```dwsd.flightroute
title: <Route name>
for: "[[<Flight Item Type>]]"
bands:
  - name: <Band>
    fl: <1|2|3>
  - name: <Band>
    fl: <1|2|3>
triggers:
  - name: <what sets this route in motion>
    generates:
      - <item-type> @ <Band>
path:
  - <item-type> @ <Band> -> <item-type> @ <Band>
  - <item-type> @ <Band> --> <item-type> @ <Band>
  - <item-type> @ <Band> ..> ()
bound-to:
  - band: <Band>
    boards:
      - board: "[[<Board>]]"
        stages:
          - <item-type>: "col:<Column>"
```
