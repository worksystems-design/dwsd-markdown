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
| `for-domain` / `for_domain` | no | wikilink | The work system the agent belongs to (as for a role) |
| `bound-to` | no | board locator or list | Where the agent's surface appears — a board-position anchor, the same locator as `interaction-of` / `agreement-of` (e.g. `[[Board]]#BoardName/col:Column::in`). Preliminary convention, to be revisited. |

Plus the shared optionals from [conventions](../conventions.md).

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

## Notes

- An ai-agent is really a **surface**: use `bound-to` when it appears at a specific point
  in the workflow (a board column), and/or `for-domain` for the work system it belongs to.
- `bound-to` is a **board-position anchor** and uses the same board **locator** as
  `interaction-of` / `agreement-of` (`[[Board]]#BoardName/col:Column::in`), so it resolves and
  renders as a link. This preliminary convention is still being settled.
