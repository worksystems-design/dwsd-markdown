# `individual`

> A person in the organization.

**Serialized `type`:** `individual`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `individual` | Entity type |
| `role` | no | string | Job title / function as **free text** (not a link to a `role` entity) |
| `level` | no | string | Seniority marker, e.g. `Lead` |
| `reports-to` | no | wikilink | Reporting line → **structure** (individuals only) |
| `member-of` | no | wikilink | Unit / work system the person belongs to → **flow** |
| `position_key` | no | string | Internal position id |
| `external_position_key` | no | string | Source-system position id |

Plus the shared optionals from [conventions](../conventions.md).

## Relationships

- **`reports-to`** — the formal manager (structure / reporting line).
- **`member-of`** — the unit/work system the person works in. Often the flow side, but
  not necessarily (see [structure vs. flow](../conventions.md#structure-vs-flow)).

## Body

Free Markdown — a short profile or notes. Wikilinks in prose are fine.

## Example

```markdown
---
type: individual
role: "Sales Representative"
level: Lead
member-of: "[[Sales Team]]"
reports-to: "[[Daljit Singh]]"
position_key: P-64
external_position_key: P3278
---
# Aaron Turner

Sales Representative (Lead) — member of [[Sales Team]], reports to [[Daljit Singh]].
```

## Notes

- `role:` here is a **string**, a job title. It is *not* a wikilink to a `role` entity.
  The two concepts (a person's title vs. a modeled `role`) are separate.
- A minimal individual is valid — only `type` is required.
