# `interaction`

> People acting in relation to each other across work systems. The structured, scheduled
> kind is a [`meeting`](meeting.md); others are informal conversations or bilateral
> alignments.

**Serialized `type`:** `interaction`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `interaction` | Entity type |
| `interaction-type` | yes | `meeting` \| `conversation` \| `bilateral` \| … | Kind of interaction (open vocabulary) |
| `interaction-of` | no | board locator (or `[[Work System]]`) | The **board (position)** it is of — points *into the detail*, e.g. `[[Sprint Board]]#Sprint Board/col:Doing::in` |
| `for-domain` / `for_domain` | no | wikilink | The **work system** it is scoped to — points *up*, e.g. `[[Strategic Direction]]` |
| `start` | no | ISO datetime | First occurrence start — **any** interaction may be scheduled |
| `end` | no | ISO datetime | First occurrence end |
| `rrule` | no | iCal RRULE | Recurrence, e.g. `RRULE:FREQ=DAILY` |

Plus the shared optionals from [conventions](../conventions.md). A scheduled interaction
usually has a `.mw` Markwhen sibling (see [conventions](../conventions.md)). The `meeting`
kind adds a **list of interactions** it bundles — see [`meeting.md`](meeting.md).

## Relationships

- **`interaction-of`** — the **board (position)** the interaction is of: a board **locator**
  `[[Board]]#BoardName/col:Column::in` (a specific column) or `[[Board]]#BoardName::in` (the
  whole board). Value-polymorphic: a bare `[[Work System]]` anchors to a work system instead.
  Points *into the detail*.
- **`for-domain`** — the **work system** the interaction is scoped to. Points *up*. Optional —
  inferable from the board, but clearer when stated (board ≠ work system). See
  [conventions](../conventions.md).

## Body

An interaction's body is free-form — often a one-line `## Purpose`. When more structure
helps, it may *optionally* use the same four framing questions a [`meeting`](meeting.md)
uses:

- `## Why are we doing this?`
- `## What is the outcome?`
- `## What decisions are we making, and who makes them?`
- `## What information do we need?`

## Example

```markdown
---
type: interaction
interaction-type: bilateral
for-domain: "[[3P]]"               # the work system (up)
interaction-of: "[[3P Board]]#3P Board/col:Doing::in"  # the board position it's of
---
## Purpose
Ad-hoc alignment between [[Head of 3P]] and [[Head of Assembly]] on the next hand-off window.
```

## Notes

- Influence: Flight Levels' *agile interactions*.
