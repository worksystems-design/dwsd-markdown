# `visualization`

> A visualization of a work system. The kind in use today is **`board`** — a
> Kanban-style board defined with the Board DSL and rendered live.

**Serialized `type`:** `visualization`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `visualization` | Entity type |
| `visualization-type` | yes | `board` | The kind of visualization (the `<base>-type` discriminator) |
| `title` | no | string | Board title |
| `visualization-of` / `visualization_of` | no | wikilink | The work system this board renders |

Plus the shared optionals from [conventions](../conventions.md).

## Relationships

- **`visualization-of`** — the work system the board belongs to.

## Body — the `board` DSL

The body holds one ```` ```dwsd.board ```` fenced block. The board DSL is **plain YAML** —
every modifier is a spelled-out key, there is **no inline sugar** (no `#status` suffix, no
`[wip]` brackets, no bare-modifier line). A viewer that recognizes the `dwsd.board` fence id
renders it live; in plain Markdown the same block still reads as a YAML document.

**Board header fields** (all optional):

| Field | Shape | Meaning |
|---|---|---|
| `title` | string | The board name (the shared document header; the old `board:` key is retired — a hard error) |
| `flightlevel` | `FL1` \| `FL2` \| `FL3` | The band the board sits in |
| `timebox` | string (e.g. `5d`) | The cadence/timebox |
| `aging` | string (e.g. `3d`) | Board-level aging duration |
| `tags` | string list | Descriptive category chips (rendered visibly; no color) |
| `agreements` | string \| string list | Working agreements — inline rule, or `[[wikilink]]` to an entity |
| `interactions` | string \| string list | Meeting / interaction pointers |
| `columns` | list | The columns (see below) |
| `lanes` | list | The swimlanes (see below) |
| `groups` | list | Group blocks banding columns together |

**Columns** — each entry is a bare name (`- Backlog`) or an object:

- `name` — the column name.
- `status-category` — one of `to-do` `in-progress` `done` `waiting` `assess` (sets the
  header tint). There is **no `blocked`** — a stuck column is `waiting`.
- `wip` — a number (the **max**) or `[min, max]`.
- `aging` — duration string, e.g. `3d`. `max-returns` — escalation threshold.
- `check` — a Definition-of-Done string. `tags` — descriptive chips.
- `agreements` / `interactions` — **inside-out** declarations on the column (see below).
- `split` — `{ direction?: horizontal, of: [ {name, status-category?, wip?, …} ] }`.
- `group` — back-reference to a group (a string, or a path array for nested groups).

**Lanes** — each entry is a bare name (a `named` lane) or an object with `name`, an explicit
`type` (`named` \| `assignee` \| `expedite`), and optional `wip` (a single number binds
**both** min and max), `status-category`, `tags`, `agreements`, `interactions`, and
lane-local `columns` / `groups`. Lanes are **not** bound to a flight-item-type; a
"swimlane per item type" is just a `named` lane named after the type.

**Inside-out / outside-in.** A board node can reach *outward* with inline `agreements:` /
`interactions:` (the **inside-out** direction — terse relationships that live and die with
the board). External entities (an interaction/agreement/meeting file) point *into* a board
position with a [locator](../conventions.md) in their `interaction-of:` / `agreement-of:`
(the **outside-in** direction). Both render through one surface; when both target the same
position they blend with a provenance badge.

## Example

````markdown
---
type: visualization
visualization-type: board
title: "3P FL2 Coordination"
visualization-of: "[[3P]]"
---

```dwsd.board
title: 3P FL2 Coordination
flightlevel: FL2
agreements:
  - "[[Team Working Agreements]]"
  - "WIP per lane: 3"
columns:
  - Backlog
  - name: Selected
    status-category: to-do
  - name: In-Progress
    wip: 3
    status-category: in-progress
    agreements:
      - "Pull only when a slot frees up"
  - name: Review
    status-category: assess
  - name: Done
    status-category: done
```
````

## Notes

- `board` is the only visualization kind so far; the type is general enough to host other
  view kinds later via additional `visualization-type` values.
- The parser is tolerant: unknown or malformed fields produce a `board.*` diagnostic and a
  clamp/skip rather than an error.
