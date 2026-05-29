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
| `interaction-of` | no | wikilink or list | The work system(s) it coordinates |

Plus the shared optionals from [conventions](../conventions.md). The `meeting` kind adds
scheduling and a **list of interactions** it bundles — see [`meeting.md`](meeting.md).

## Relationships

- **`interaction-of`** — the work system(s) the interaction belongs to.

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
interaction-of: "[[3P]]"
---
## Purpose
Ad-hoc alignment between [[Head of 3P]] and [[Head of Assembly]] on the next hand-off window.
```

## Notes

- Influence: Flight Levels' *agile interactions*.
