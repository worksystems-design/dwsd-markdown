---
type: flight-route
---
```flightroute
route "<Route name>"
  for: @<flight-item-type-handle>
  triggers: <what sets this route in motion>
  path: FL2: @<work-system> -> FL1: @<work-system>
  flow:
    FL2: @<work-system>#<Column>
      -[generate: @<flight-item-type>]-> FL2: @<work-system>#<Column>
    FL1: @<work-system>#Done
      -[copy: @<flight-item-type>]-> FL1: @<work-system>#To-Do
```
