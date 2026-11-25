# `automation`

> An **automation** present in the organization: something that acts in the workflow **by
> fixed rules** — a rule in an issue tracker, an integration workflow, a script, or a whole
> system such as an ERP. An [`ai-agent`](ai-agent.md) judges; an automation does what it
> was set up to do.

> ⚠ **Preliminary.** Deliberately minimal, modeled on `ai-agent`.

**Serialized `type`:** `automation`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `automation` | Entity type |
| `platform` | no | string | What it runs on, as the organization calls it |
| `description` | no | string | What the automation is / does |
| `status` | no | `active` \| `deactivated` \| … | Lifecycle (e.g. `deactivated` when switched off) |
| `for-domain` / `for_domain` | no | wikilink or list | The domain — a work system, a role or a unit — the automation belongs to |
| `bound-to` | no | board locator or list (or a bare `[[entity]]` — a work system, a unit or a person) | Where it acts — a board-position anchor, the same locator as on an [`ai-agent`](ai-agent.md), or the entity whose box carries it. Preliminary convention, as there. |

Plus the shared optionals from [conventions](../conventions.md), among them `same-as` for
the rule, workflow or system it is over there.

The body is free text: what starts it (a `## Trigger` section, as on an
[`interaction`](interaction.md), where it needs more than a sentence), what it does, what it
leaves to people.

## Example

```markdown
---
type: automation
platform: issue tracker
description: Moves an order to Ready when stock is confirmed
status: active
for-domain: "[[Customer Support]]"
bound-to: "[[Support Board]]#Support Board/col:Ready::before"
---
```

## Reading it

- **The question:** what happens here by itself, and which domain does it belong to?
- **Look first:** `bound-to` (where it acts), then `description`, `platform` and `status`.
- **Go next:** into the detail via `bound-to`; up via `for-domain`; out via `same-as`.
- **Pictured in:** on the board at its `bound-to` position, or on the box of a bare-named
  entity, where a renderer supports it.

## Notes

- **Size is free.** One rule on one column and a whole ERP are both one file; a list in
  `bound-to` names every place it acts. Split it when two parts need their own description.
- **Not a holder of mandates.** It decides nothing it could be accountable for; whoever
  answers for it is found through `for-domain`, and what people agreed about it is an
  [`agreement`](agreement.md).
- **Automation or ai-agent?** Fixed rules: automation. Judgment by a model: ai-agent. A
  workflow that calls a model is named for what matters to the people working with it.
- **No credentials** — no token, key or secret in the file.
