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
scheduling and an agenda of activities — see [`meeting.md`](meeting.md).

## Relationships

- **`interaction-of`** — the work system(s) the interaction belongs to.

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
