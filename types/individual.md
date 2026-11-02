# `individual`

> A person in the organization.

**Serialized `type`:** `individual`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `individual` | Entity type |
| `role` | no | string or wikilink | The person's **primary role**: free text, the way it is said today, or `"[[Role]]"` once that role is spelled out as a `role` entity (since format 1.6.0) |
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
- **`role`** as a link — which of the person's roles is the **primary** one. Who holds a
  role is said by the role's `role-keeper`, not here; the person named primary for a role
  belongs in its `role-keeper` too.

## Body

Free Markdown — a short profile or notes. Wikilinks in prose are fine. Optional
`## Accountabilities` and `## Decision Rights` (or one `## Mandates` section) say what the
person must or may do directly, outside any role; table rows with a locator show as mandate
chips — see
[conventions](../conventions.md#mandates--what-a-holder-must-or-may-do).

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

## Reading it

- **The question:** who is this person, whom do they report to, and where do they work?
- **Look first:** `role` (the primary role, as text or as a link to a `role`),
  `reports-to` and `member-of`.
- **Go next:** up via `reports-to` to the manager; into the units and work systems named in
  `member-of`.
- **Backlinks:** the roles whose `role-keeper` names the person, and through them every
  entity scoped `for-domain` to those roles; the individuals whose `reports-to` names them;
  interactions, agreements and AI agents anchored to them with a bare locator (a 1:1, a
  personal working agreement); signals and insights that `observes` them.
- **Pictured in:** the org chart; a `dwsd.orgchart` fence with `around: self` draws the
  person's line, with what is anchored to them on their box.

## Notes

- `role:` is the **primary role** — what people usually mean by "their role": the one agreed
  with HR, the one in the contract. As text it is a starting point, with implicit
  expectations about what the person may or should do; talking those through turns the
  text into a spelled-out `role` entity, and the text into a link to it. Both forms are
  valid side by side; text is not a defect.
- A link does not make anyone a keeper: the role's `role-keeper` does. A primary role whose
  `role-keeper` does not name the person is reported (`individual.primary-role-not-kept`).
- A vacancy keeps its position in `role:` as text (the examples name theirs `NA1`).
- A minimal individual is valid — only `type` is required.
