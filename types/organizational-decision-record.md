# `organizational-decision-record`

> An **Organizational Decision Record (ODR)** — the org-design analogue of an Architecture
> Decision Record (ADR). It captures a single organizational design decision: what was decided,
> why, and the consequences expected. Minimal by design. Category: **change**.

**Serialized `type`:** `organizational-decision-record`

## What earns one

The **`organizational`** in the name is a threshold, not decoration. Plenty gets decided about a
product, about a team's way of working, about this sprint — none of that is an ODR. An ODR is for
decisions about **the organization**: how it is structured, how work flows through it, who is in
it, what it rewards.

The practical test: **if you cannot name one of those levers, it is not an ODR.** Day-to-day
operational and tactical changes are agreements, or nothing.

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `organizational-decision-record` | Entity type |
| `for-domain` / `for_domain` | no | wikilink | The domain / work system the decision concerns |
| `status` | no | `proposed` \| `accepted` \| `superseded` \| `deprecated` | Lifecycle of the decision |
| `date` | no | date | When the decision was recorded / last updated |
| `decision-makers` | no | wikilink or list | Who made the decision |

Plus the shared optionals from [conventions](../conventions.md), including
[`derived-from`](../conventions.md#derived-from--the-shared-emergence-key) — typically the
[`proposal`](proposal.md) or [`driver`](driver.md) this record captures.

## Body

| Section | Holds |
|---|---|
| `## Context` | The situation and forces — why a decision was needed |
| `## Decision` | What was decided, and what we will do |
| `## Consequences` | What we expect to follow — benefits and trade-offs |

## Example

```markdown
---
type: organizational-decision-record
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

## What follows from a decision

An ODR is the **recorded decision**; what follows lives on as its own entities. The most common
continuation is one or more [`agreement`](agreement.md)s — the operational and tactical rules the
decision produced, each anchored where it applies. They name the record they came from via
[`derived-from`](../conventions.md#derived-from--the-shared-emergence-key), which is what makes a
decision's **bundle** readable: the agreements belonging to a decision are exactly those pointing
back at it.

The decision itself is pinned at the **domain** (`for-domain` — the work system it concerns); its
agreements are pinned **where the work happens** (`agreement-of` — a board position). One decision
up at the system, its consequences down in the flow.

Not every continuation is an agreement: a decision about structure shows up as a changed topology,
one about people as changed roles or membership. Only the process / way-of-working branch produces
agreements.

## Notes

- Modeled on the ADR (Michael Nygard) minimal form — Status / Context / Decision /
  Consequences. Kept minimal on purpose.
- An ODR is the initial member of the **change** category (records of decided organizational
  change).
- **It is a Decision Record, not a Design Record.** The ADR lineage it is named after is
  *Architecture **Decision** Record*, and the body section is `## Decision`. "Design" names the
  phase a decision is usually taken in, not the artifact — keeping the two apart stops one word
  from carrying two roles.
