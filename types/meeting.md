# `meeting` (an `interaction` of type `meeting`)

> A scheduled [`interaction`](interaction.md) that bundles a **list of interactions**
> (each with an outcome). It is a lightweight container: when people meet, and the
> interactions they run. Flight Levels calls this pattern a *meeting container*; we keep
> the term **meeting**.

**Serialized `type`:** `interaction` + `interaction-type: meeting`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `interaction` | Base type |
| `interaction-type` | yes | `meeting` | Marks it a meeting |
| `interaction-of` | no | board locator (or `[[Work System]]`) | The **board (position)** it is of — points *into the detail* |
| `for-domain` / `for_domain` | no | wikilink | The **work system** it is scoped to — points *up* |
| `start` | no | ISO datetime | First occurrence start |
| `end` | no | ISO datetime | First occurrence end |
| `rrule` | no | iCal RRULE | Recurrence, e.g. `RRULE:FREQ=WEEKLY;BYDAY=TU` |
| `version` | no | string | Version of the meeting |

Plus the shared optionals from [conventions](../conventions.md).

## Body

| Section | Holds |
|---|---|
| `## Why are we doing this meeting?` | The reason it exists |
| `## What is the outcome?` | The result it should produce |
| `## What decisions are we making, and who makes them?` | Decisions in scope and who is needed |
| `## What information do we need?` | The inputs required |
| `## Interactions` | The interactions this meeting bundles — as a list **or** as a 3-column table that also **anchors each interaction to a board position** |

The **Interactions** section takes one of two forms:

**Bullet-list form** — one line per interaction, in order, each naming the
interaction and its outcome. Reference a standalone interaction or another meeting
with `[[…]]` when one exists; otherwise an inline line is enough:

```markdown
## Interactions

- Review progress → shared status
- Blocker clustering → grouped blockers with owners
```

**Table form** — a 3-column table whose third column anchors each interaction to a **board
position** with a locator, so one meeting pins several board positions at once (one row =
one anchor):

```markdown
## Interactions

| Name         | Outcome             | Interaction of                                |
|--------------|---------------------|-----------------------------------------------|
| What's done? | Items moved to Done | [[Sprint Board]]#Sprint Board/col:Done::in    |
| Where stuck? | Blockers visible    | [[Sprint Board]]#Sprint Board/col:Blocked::in |
```

Each row's locator may be **relative** (`#col:Done::in` or `col:Done::in`, no `[[file]]`) —
it then inherits the meeting's frontmatter `interaction-of` head. For an
agreement container the heading is `## Agreements` and the column is `Agreement of`, read
the same way.

## Markwhen sibling (`.mw`)

A recurring meeting usually has a `.mw` sibling (same basename) with one
[Markwhen](https://markwhen.com) line. Attached to the meeting, not a separate entity.

## Example

`interactions/3P Coordination.md`:

```markdown
---
type: interaction
interaction-type: meeting
interaction-of: "[[3P]]"
start: "2026-05-12T10:00:00"
end: "2026-05-12T11:00:00"
rrule: "RRULE:FREQ=WEEKLY;BYDAY=TU"
version: "1.0"
---
## Why are we doing this meeting?

Keep [[3P]] sub-teams synchronized so blockers surface weekly, not at hand-off.

## What is the outcome?

A current picture of 3P status and agreed next steps with owners.

## What decisions are we making, and who makes them?

Sprint re-sequencing ([[Head of 3P]]); escalation of cross-product conflicts
([[Standard Drones PM]]).

## What information do we need?

The 3P board, current blockers, upcoming hand-off windows with [[Assembly]].

## Interactions

- Review progress → shared status
- Blocker clustering → grouped blockers with owners
- Sequence next sprint → agreed sprint order
```

A meeting that anchors its interactions to board positions uses the **table form** instead
(one row → one board position):

```markdown
---
type: interaction
interaction-type: meeting
for-domain: "[[Standard Production]]"
interaction-of: "[[Sprint Board]]#Sprint Board::in"
---
## Interactions

| Name         | Outcome             | Interaction of                                |
|--------------|---------------------|-----------------------------------------------|
| What's done? | Items moved to Done | [[Sprint Board]]#Sprint Board/col:Done::in    |
| Where stuck? | Blockers visible    | [[Sprint Board]]#Sprint Board/col:Blocked::in |
```

`interactions/3P Coordination.mw`:

```
May 12 2026 10:00-11:00 every week on Tuesday: 3P Coordination
```

## Notes

- A meeting **bundles interactions** — each a small, named interaction with its own outcome.
- **Interactions** entries can be inline, or `[[wikilinks]]` to an interaction or meeting.
  Because a meeting *is* an interaction, larger events (e.g. a quarterly review + planning +
  retro) can be composed from smaller meetings.
- Influence: Flight Levels — the *meeting container* bundles interactions and their outcomes.
