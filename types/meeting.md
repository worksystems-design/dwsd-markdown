# `meeting` (an `interaction` of type `meeting`)

> A scheduled [`interaction`](interaction.md), described by the **Meeting Canvas** and
> made up of a sequence of activities. The canvas describes the meeting; the activities
> are listed in a compact table.

**Serialized `type`:** `interaction` + `interaction-type: meeting`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `interaction` | Base type |
| `interaction-type` | yes | `meeting` | Marks it a meeting |
| `interaction-of` | no | wikilink or list | The work system(s) it coordinates |
| `start` | no | ISO datetime | First occurrence start |
| `end` | no | ISO datetime | First occurrence end |
| `rrule` | no | iCal RRULE | Recurrence, e.g. `RRULE:FREQ=WEEKLY;BYDAY=TU` |
| `version` | no | string | Version of the canvas |

Plus the shared optionals from [conventions](../conventions.md).

## Body — Meeting Canvas

| Section | Holds |
|---|---|
| `## Why are we doing this meeting?` | The reason it exists |
| `## What is the outcome?` | The result it should produce |
| `## What decisions are we making, and who makes them?` | Decisions in scope and who is needed |
| `## What information do we need?` | The inputs required |
| `## Activities` | The activities the meeting runs, as a table (its step-by-step process) |

The **Activities** table — one row per activity, in order:

| Activity | Category | Outcome |
|---|---|---|
| … | `discover-plan` \| `deliver` \| `improve` | … |

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

## Activities

| Activity | Category | Outcome |
|---|---|---|
| Review Progress | deliver | Shared status |
| Blocker Clustering | improve | Grouped blockers, owners |
| Sequence | discover-plan | Next sprint order |
```

`interactions/3P Coordination.mw`:

```
May 12 2026 10:00-11:00 every week on Tuesday: 3P Coordination
```

## Notes

- A meeting consists of multiple activities; an activity is not necessarily a meeting.
- Activity categories follow the Flight Levels FL2 groups (Discover & Plan, Deliver,
  Improve).
- The Meeting Canvas adapts the Flight Levels Activity Canvas (Flight Levels GmbH,
  CC BY-SA 4.0).
