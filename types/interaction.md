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
| `interaction-of` | no | board locator or list (or a bare `[[entity]]` — a work system, a unit or a person) | The **board (position)** it is of — points *into the detail*, e.g. `[[Sprint Board]]#Sprint Board/col:Doing::in`; two persons make a 1:1 |
| `for-domain` / `for_domain` | no | wikilink or list | The **domain** — a work system, a role or a unit — it is scoped to — points *up*, e.g. `[[Strategic Direction]]`. Naming a role lands the interaction on every keeper of that role |
| `start` | no | ISO datetime | First occurrence start — **any** interaction may be scheduled |
| `end` | no | ISO datetime | First occurrence end |
| `rrule` | no | iCal RRULE | Recurrence, e.g. `RRULE:FREQ=DAILY` |

Plus the shared optionals from [conventions](../conventions.md). A scheduled interaction
usually has a `.mw` Markwhen sibling (see [conventions](../conventions.md)). The `meeting`
kind adds a **list of interactions** it bundles — see [`meeting.md`](meeting.md).

## Relationships

- **`interaction-of`** — the **board (position)** the interaction is of: a board **locator**
  `[[Board]]#BoardName/col:Column::in` (a specific column) or `[[Board]]#BoardName::in` (the
  whole board). Value-polymorphic: a bare `[[entity]]` — a work system, a unit or a person —
  anchors to that entity instead, wherever it is drawn; a list of two persons is a 1:1.
  Points *into the detail*.
- **`interaction-of`** may also name a **route stage**:
  `[[Route]]/stage:<itemType> @ <Band>::before|in|after` — see
  [conventions](../conventions.md).
- **`for-domain`** — the **domain** — a work system, a role or a unit — the interaction is scoped to.
  Points *up*. Optional —
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

- **Not every interaction is scheduled.** Without `start` / `rrule` an interaction happens
  when something triggers it: an item reaching a route stage or a board column, a threshold
  (a WIP limit hit, a card aging past its limit), a call for help. Say what triggers it in
  the body — a `## Trigger` section works — and let the anchor say *where*: an interaction
  anchored `::before` a route stage reads as "when an item arrives here". No `.mw` sibling.
- Influence: Flight Levels' *agile interactions*.
