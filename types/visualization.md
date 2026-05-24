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

The body holds one ```` ```board ```` fenced block. Columns are listed one per line;
indented modifiers (2 spaces) refine them. The essentials:

- **Column:** a name on its own line.
- **Status tag:** `#todo` `#in-progress` `#done` `#waiting` `#blocked` — sets the header color.
- **WIP limit:** `Name [5]` (max) or `Name [2..5]` (min..max).
- **Modifiers** (indented): `aging: 3d`, `returns: 2`, `check: "…"`.
- **Split:** `split: a | b | c` (vertical), `split horizontal: …`.
- **Group:** `group Development` with indented columns under it.
- **Lane / swimlane:** `lane Expedite !expedite`, declared *before* the columns.

## Example

```markdown
---
type: visualization
visualization-type: board
title: "3P FL2 Coordination"
visualization-of: "[[3P]]"
---

```board
Backlog
Selected #todo
In Progress #in-progress
Review #waiting
Done #done
```
```

## Notes

- `board` is the only visualization kind so far; the type is general enough to host other
  view kinds later via additional `visualization-type` values.
