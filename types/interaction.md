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
| `interaction-of` | no | `@board#Column` or `@board` | The **board (position)** it is of — points *into the detail*, e.g. `@sprint-board#Doing` |
| `for-domain` / `for_domain` | no | wikilink | The **work system** it is scoped to — points *up*, e.g. `[[Strategic Direction]]` |

Plus the shared optionals from [conventions](../conventions.md). The `meeting` kind adds
scheduling and a **list of interactions** it bundles — see [`meeting.md`](meeting.md).

## Relationships

- **`interaction-of`** — the **board (position)** the interaction is of: `@board#Column` (a
  specific column) or `@board` (the whole board). Points *into the detail*.
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
interaction-of: "@3p-board#Doing"  # the board position it's of (detail)
---
## Purpose
Ad-hoc alignment between [[Head of 3P]] and [[Head of Assembly]] on the next hand-off window.
```

## Notes

- Influence: Flight Levels' *agile interactions*.
