# `role`

> A role in the organization, held by one or more people. A role is distinct from the
> person who keeps it — people change, the role persists.

**Serialized `type`:** `role`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `role` | Entity type |
| `role-keeper` / `role_keeper` | no | wikilink or list | The individual(s) holding the role — a list means a **shared** role |
| `for-domain` / `for_domain` | no | wikilink | The work system / domain the role is scoped to |
| `version` | no | string | Version of the description |
| `decision_date` | no | date | When this version was decided |
| `review_date` | no | date | When it is due for review |

Plus the shared optionals from [conventions](../conventions.md).

> The **title** is the filename. **Date/Version** and **Review Date** live in the
> frontmatter and render as properties; the body starts at *Purpose*.

## Relationships

- **`role-keeper`** — who currently holds the role. Multiple keepers = a role shared
  across several people.
- **`for-domain`** — the work system or domain the role operates in.

## Body

| Section | Holds |
|---|---|
| `## Purpose` → `### Driver` | Why the role exists — the motive (optionally a `[[driver]]`) |
| `## Purpose` → `### Requirement` | What the role must fulfill |
| `## Description` | What the role is |
| `## Concerns` | What the role looks after / cares about — its areas of attention |
| `## Accountabilities` | What the role *should* do — obligations and deliverables |
| `## Decision Rights` | What the role *may* decide — its authority (optionally hinted via RACI or delegation levels, not necessarily a full matrix) |
| `## Evaluation` → `### Metrics and Monitoring` | How the role's performance is observed |

## Example

```markdown
---
type: role
role-keeper:
  - "[[Head of 3P]]"
  - "[[Head of 4P]]"
for-domain: "[[3P]]"
version: "1.0"
decision_date: "2026-05-11"
review_date: "2026-08-11"
---
## Purpose

### Driver
Standard production keeps stalling against custom and innovation pull; someone must own
the baseline revenue stream.

### Requirement
Protect standard 3P / 4P / 5P throughput and arbitrate cross-product priority.

## Description
A shared coordination role across the three product Heads.

## Concerns
Standard-order flow across 3P / 4P / 5P, and the hand-off to [[Assembly]].

## Accountabilities
- Hand the monthly production forecast to [[Head of Assembly]].
- Arbitrate cross-product priority conflicts and surface delivery risks early.

## Decision Rights
- Re-sequence production within a quarter — **delegated**.
- Reallocate teams across products — **agree** with the [[Product Heads]].

## Evaluation

### Metrics and Monitoring
- Standard-order lead time within target.
- No standard order delayed > 1 sprint by custom / innovation pull.
```

## Notes

- Body section headings are a convention, not enforced by the parser — use what fits.
- **Roles are individual.** There is no role-template or role-class that instances inherit
  from — five POs means five standalone role files. Any shared basis is prose in the body,
  not a maintained link.
- A role under strain is captured as a [`signal`](signal.md) or [`insight`](insight.md)
  that `observes` the role — not as a body section.
