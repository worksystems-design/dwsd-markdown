# `design-record`

> A **Design Record** — the org-design analogue of an Architecture Decision Record (ADR).
> It captures a single design decision: what was decided, why, and the consequences
> expected. Minimal by design. Category: **change**.

**Serialized `type`:** `design-record`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `design-record` | Entity type |
| `for-domain` / `for_domain` | no | wikilink | The domain / work system the decision concerns |
| `status` | no | `proposed` \| `accepted` \| `superseded` \| `deprecated` | Lifecycle of the decision |
| `date` | no | date | When the decision was recorded / last updated |
| `decision-makers` | no | wikilink or list | Who made the decision |

Plus the shared optionals from [conventions](../conventions.md). Optionally
`derived-from` the [`proposal`](proposal.md) or [`driver`](driver.md) it records.

## Body

| Section | Holds |
|---|---|
| `## Context` | The situation and forces — why a decision was needed |
| `## Decision` | What was decided, and what we will do |
| `## Consequences` | What we expect to follow — benefits and trade-offs |

## Example

```markdown
---
type: design-record
for-domain: "[[Strategic Direction]]"
status: accepted
date: "2026-05-11"
decision-makers:
  - "[[COO]]"
---
## Context
The 3P and 4P work systems duplicate coordination and compete for the same teams; standard
production keeps stalling.

## Decision
Merge 3P and 4P into one FL2 work system; retire the separate 4P coordination.

## Consequences
Fewer hand-offs and one priority queue (benefit); a larger coordination scope for the
merged work system, watched via lead-time metrics (trade-off).
```

## Notes

- Modeled on the ADR (Michael Nygard) minimal form — Status / Context / Decision /
  Consequences. Kept minimal on purpose.
- A design record is the initial member of the **change** category (records of decided
  organizational change).
