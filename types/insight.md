# `insight`

> An *interpretation* — meaning drawn from one or more [signals](signal.md). In
> Ladder-of-Inference terms: a signal is selected data; an insight is the next rung up,
> where interpretation (and often suggested actions) is added. What makes something an
> insight rather than a signal is precisely that interpretation.

**Serialized `type`:** `insight`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `insight` | Entity type |
| `observes` | no | wikilink, locator or list | The entity (or entities) the insight is about — an individual, a unit, a work system, or another entity — or, as a locator, a board position or route stage (since format 1.3.0) |
| `title` | no | string | Explicit title (otherwise the `#` heading / filename is the title) |
| `status` | no | `new` \| `acknowledged` | Lifecycle |
| `acknowledged_at` | no | ISO datetime | When it was acknowledged |
| `derived-from` | no | wikilink or list | The signal(s) this insight interprets (see note) |

Plus the shared optionals from [conventions](../conventions.md).

## Relationships

- **`observes`** — the entity (or entities) the insight is about (an individual, a unit, a
  work system, …). A bare wikilink names that entity wherever it is drawn.
- **`derived-from`** — the [signal(s)](signal.md) the interpretation is built on. Makes
  the Ladder of Inference visible: selected data → interpretation. *Metadata only:* the
  parser has no `derived-from` relationship type yet, so it is not a typed edge.

## Body

- The interpretation, in a sentence or two.
- Optional classification line: `**Category:** structural | **Severity:** warning`
- Optional `## Observations` and `## Suggested Actions`.

The body may be short, but an insight always carries interpretation — if it is only a
selected datum with no meaning attached, it is a [`signal`](signal.md), not an insight.

## Example

```markdown
---
type: insight
title: Cross-Team Alignment Gap
observes:
  - "[[Product Development]]"
  - "[[Platform Engineering]]"
status: acknowledged
acknowledged_at: "2026-03-25"
derived-from:
  - "[[diverging-okrs]]"
---
# Cross-Team Alignment Gap

**Category:** structural | **Severity:** warning

Product Development and Platform Engineering have diverging priorities causing friction.

## Observations
- Different OKRs with no shared metrics
- Communication mostly through tickets

## Suggested Actions
- Joint planning sessions
- Shared success metrics
```

## Reading it

- **The question:** what does it mean, and which signals is the interpretation built on?
- **Look first:** the interpretation that opens the body, and the optional
  `**Category:** … | **Severity:** …` line; `status` says whether it was acknowledged.
- **Go next:** back along `derived-from` to the signals; via `observes` to the entity the
  insight is about.
- **Backlinks:** the drivers whose `derived-from` names it.
- **Pictured in:** pinned on the box of the observed person or unit (topology, org chart,
  units view). In the change trail it is the second rung, read along `derived-from`; one
  that `observes` a decision record or an agreement draws a loop-back. A
  `dwsd.change-trail` fence with `around: self` keeps its own line.
