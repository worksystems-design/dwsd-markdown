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
| `observes` | no | wikilink, locator or list | The entity the signal is about — an individual, a unit, a work system, or another entity — or, as a locator, the board position or route stage where it was seen (since format 1.3.0) |

Plus the shared optionals from [conventions](../conventions.md).

## Relationships

- **`observes`** — the entity the signal concerns (an individual, a unit, a work system, …).
  A bare wikilink names that entity wherever it is drawn — a unit that is also a work system
  shows the signal in both pictures.

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
# Schmidt comes by at half past five

Schmidt comes by at 5:30 pm.
```

## Reading it

- **The question:** what was observed, and about what?
- **Look first:** the body, the selected datum itself (often one line); then `observes` and
  `created_at`.
- **Go next:** via `observes` to the entity the signal is about.
- **Backlinks:** the insights whose `derived-from` names it: what was made of the signal.
  Until one does, the signal is an open end.
- **Pictured in:** pinned on the box of the observed person or unit (topology, org chart,
  units view). In the change trail it is the first rung; one that `observes` a decision
  record or an agreement draws a loop-back. A `dwsd.change-trail` fence with
  `around: self` shows what came of it.

## Notes

- A signal stays a signal as long as it carries no interpretation. When it is
  interpreted, the interpretation is recorded as an [`insight`](insight.md) that points
  back at the signal(s) it came from via `derived-from`.
