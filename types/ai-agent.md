# `ai-agent`

> An **AI agent** present in the organization. Conceptually this is less about *what an
> agent is* and more about a **surface** — where an AI surfaces at a point in the
> workflow. Today that is e.g. a Jira/Rovo agent on a board column; other platforms
> (including managed agents) will follow.

> ⚠ **Preliminary.** An early sketch — the surface concept is still evolving across
> platforms, so the fields below (especially `bound-to`) will likely change.

**Serialized `type`:** `ai-agent`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `ai-agent` | Entity type |
| `platform` | no | string | Host platform, e.g. `jira-rovo` |
| `description` | no | string | What the agent is / does |
| `status` | no | `active` \| `deactivated` \| … | Lifecycle (e.g. `deactivated` when switched off) |
| `for-domain` / `for_domain` | no | wikilink or list | The domain — a work system, a role or a unit — the agent belongs to (as for a role). Naming a role lands the agent on every keeper of that role |
| `bound-to` | no | board locator or list (or a bare `[[entity]]` — a work system, a unit or a person) | Where the agent's surface appears — a board-position anchor, the same locator as `interaction-of` / `agreement-of` (e.g. `[[Board]]#BoardName/col:Column::in`), or the entity whose box carries the agent. Preliminary convention, to be revisited. |

Plus the shared optionals from [conventions](../conventions.md).

Optional `## Accountabilities` and `## Decision Rights` in the body (or one `## Mandates`
section) say what the agent must do, what it may do on its own and where it must ask
("on its own", "after consulting [[…]]") — see
[conventions](../conventions.md#mandates--what-a-holder-must-or-may-do). Preliminary, like
the type.

## Example

```markdown
---
type: ai-agent
created_at: "2026-04-01"
platform: jira-rovo
description: Rovo agent surfacing on a board column
status: active
for-domain: "[[Customer Support]]"
bound-to:
  - "[[Support Board]]#Support Board/col:Triage::in"
---
```

## Reading it

- **The question:** where does an AI surface in the work, and which domain does it belong to?
- **Look first:** `bound-to` (where the surface appears), then `description`, `platform`
  and `status`.
- **Go next:** into the detail via `bound-to`: a board position, or the entity whose box
  carries the agent; up via `for-domain` (a role there reaches each keeper).
- **Pictured in:** on the board at its `bound-to` position, or on the box of a bare-named
  entity in the topology, org chart or units view. Like the type, `bound-to` is preliminary.

## Notes

- An ai-agent is really a **surface**: use `bound-to` when it appears at a specific point
  in the workflow (a board column), and/or `for-domain` for the work system it belongs to.
- `bound-to` is a **board-position anchor** and uses the same board **locator** as
  `interaction-of` / `agreement-of` (`[[Board]]#BoardName/col:Column::in`), so it resolves and
  renders as a link. Value-polymorphic like them: a bare `[[entity]]` — a work system, a unit
  or a person — puts the agent on that entity's box wherever it is drawn. This preliminary
  convention is still being settled.
