# `role`

> A role in the organization, held by one or more people. A role is distinct from the
> person who keeps it — people change, the role persists.

**Serialized `type`:** `role`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `role` | Entity type |
| `role-keeper` / `role_keeper` | no | wikilink or list | The individual(s) holding the role — a list means a **shared** role |
| `for-domain` / `for_domain` | no | wikilink | The domain the role is scoped to — a work system or a unit (a site, a department); a role is itself a domain for `for-domain` — an entity scoped to a role shows up on every keeper |
| `version` | no | string | Version of the description |
| `decision_date` | no | date | When this version was decided |
| `review_date` | no | date | When it is due for review |

Plus the shared optionals from [conventions](../conventions.md).

> The **title** is the filename. **Date/Version** and **Review Date** live in the
> frontmatter and render as properties; the body starts at *Purpose*.

## Relationships

- **`role-keeper`** — who currently holds the role. Multiple keepers = a role shared
  across several people.
- **`for-domain`** — the domain the role operates in: a work system, or a unit such as a site
  or a department that decides something for itself. The role is in turn a
  **domain** other entities can name: an agreement, interaction, ODR, driver, proposal or AI
  agent with `for-domain: "[[This Role]]"` shows up on every keeper of the role — one hop;
  the role's own `for-domain` is not followed further.
- **Flight routes** — every [flight route](flight-route.md) whose `for-domain` names this
  role; the route lists it as the domain responsible for it.

## Body

| Section | Holds |
|---|---|
| `## Purpose` → `### Driver` | Why the role exists — the motive (optionally a `[[driver]]`) |
| `## Purpose` → `### Requirement` | What the role must fulfill |
| `## Description` | What the role is |
| `## Concerns` | What the role looks after / cares about — its areas of attention |
| `## Accountabilities` | What the role *must* do — obligations and deliverables; a list, prose, or a table `Name \| Mandate of` whose rows with a locator show as mandate chips |
| `## Decision Rights` | What the role *may* decide — its authority (optionally hinted via RACI or delegation levels, not necessarily a full matrix); a list or a table |
| `## Mandates` | Optional — the general form for either; see [conventions](../conventions.md#mandates--what-a-holder-must-or-may-do) |
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

## Reading it

- **The question:** who takes care of what, and in which domain?
- **Look first:** `role-keeper` (who holds it now) and `for-domain` (where it operates); in
  the body, `## Accountabilities` and `## Decision Rights` carry the gist.
- **Go next:** up via `for-domain` to the work system or unit; across to each keeper's file.
- **Backlinks:** the agreements, interactions, ODRs, drivers, proposals and AI agents scoped
  `for-domain` to the role say what is decided, met about and agreed for whoever keeps it;
  the flight routes whose `for-domain` names it are the routes it is responsible for; a
  signal or insight that `observes` it says where it is under strain.
- **Pictured in:** the role shows through its keepers: in the org chart, every entity scoped
  `for-domain` to it lands on the box of each keeper (one hop).

## Notes

- Body section headings are a convention, not enforced by the parser — use what fits.
- **Roles are individual.** There is no role-template or role-class that instances inherit
  from — five POs means five standalone role files. Any shared basis is prose in the body,
  not a maintained link.
- A role under strain is captured as a [`signal`](signal.md) or [`insight`](insight.md)
  that `observes` the role — not as a body section.
