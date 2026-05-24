# `signal`

> A *selected* piece of data or information — an observation, **before interpretation**.
> In Ladder-of-Inference terms a signal sits low on the ladder: something was observed
> and selected as worth noting, but no meaning is attached yet. Interpreting one or more
> signals is what produces an [`insight`](insight.md).

**Serialized `type`:** `signal`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `signal` | Entity type |
| `observes` | no | wikilink or list | The entity the signal is about |

Plus the shared optionals from [conventions](../conventions.md).

## Relationships

- **`observes`** — the entity the signal concerns (an individual, work system, …).

## Body

Just the selected datum — often a single line. **No interpretation, no suggested
actions.** The moment you add meaning, it has become an [`insight`](insight.md).

## Example

```markdown
---
type: signal
observes:
  - "[[Emma Design Lead]]"
created_at: "2026-03-29"
---
# Schmidt kommt um halb sechs

Schmidt kommt um 17:30 Uhr vorbei.
```

## Notes

- A signal stays a signal as long as it carries no interpretation. When it is
  interpreted, the interpretation is recorded as an [`insight`](insight.md) that points
  back at the signal(s) it came from via `derived-from`.
