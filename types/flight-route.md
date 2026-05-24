# `flight-route`

> A path that work takes through the flight levels — which work systems it passes
> through, in what order, and how items move between them. Defined with the Route DSL and
> rendered live.

**Serialized `type`:** `flight-route`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `flight-route` | Entity type |

Plus the shared optionals from [conventions](../conventions.md). The route definition
itself lives in the body, not the frontmatter.

## Body — the `flightroute` DSL

The body holds one ```` ```flightroute ```` fenced block. A block starts with
`route "Name"` and then sections:

- **`triggers:`** — comma-separated list of what sets the route in motion.
- **`for:`** — the flight-item-type the route carries, by `@`-handle.
- **`path:`** — the path across flight levels (e.g. `FL2 -> FL1`), each step optionally
  bound to a work system by `@`-handle.
- **`flow:`** — the operational flow through concrete work systems. Edges carry an action
  and a flight-item-type and move items between columns.
- Lines starting with `#` are comments.

Work systems are referenced by `@`-handle and bound to a flight level and column:

```flightroute
route "Standard Order Fulfillment"
  for: @standard-order
  triggers: Customer order placement (3P / 4P / 5P standard config)
  path: FL2: @sales-fl2 -> FL2: @3p-fl2 -> FL1: @3p-sw-fl1 -> FL1: @assem-1-fl1
  flow:
    FL2: @sales-fl2#Backlog
      -[generate: @standard-order]-> FL2: @3p-fl2#Backlog
    FL2: @3p-fl2#In Progress
      -[copy: @component-spec]-> FL1: @3p-sw-fl1#To Do
    FL1: @3p-sw-fl1#Done
      -[copy: @component-spec]-> FL1: @assem-1-fl1#To Do
```

Reading an edge: `FL2: @sales-fl2#Backlog -[generate: @standard-order]-> FL2: @3p-fl2#Backlog`
= from the Backlog column of `@sales-fl2` on FL2, *generate* a `@standard-order` into the
Backlog column of `@3p-fl2`.

## Notes

- A flight route references [flight-item-types](flight-item-type.md) and work systems by
  `@`-handle. The handle is the target entity's slug.
