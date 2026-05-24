# `proposal`

> A proposed response to a [`driver`](driver.md), before it is consented. On the design
> loop: **signal → insight → driver → proposal → agreement**. When consented, a proposal
> yields an [`agreement`](agreement.md).

**Serialized `type`:** `proposal`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `proposal` | Entity type |
| `derived-from` | no | wikilink or list | The [`driver`](driver.md) (and rungs below it) this responds to (see note) |
| `for-domain` / `for_domain` | no | wikilink | The domain the proposal concerns |
| `status` | no | `draft` \| `in-consent` \| `consented` \| `declined` | Where the proposal is in its decision |

Plus the shared optionals from [conventions](../conventions.md).

## Body

| Section | Holds |
|---|---|
| `## Proposal` | What is proposed — the change, or the agreement-to-be |
| `## Objections` | Objections / concerns raised during consent *(optional)* |
| `## Outcome` | Consented or declined; a link to the resulting [`agreement`](agreement.md) |

## Example

```markdown
---
type: proposal
derived-from: "[[Standard-order hand-off has no owner]]"
for-domain: "[[Strategic Direction]]"
status: consented
---
## Proposal
Introduce a Standard Order Fulfillment protocol: Sales acknowledges within 24h; Assembly
confirms a slot on intake.

## Objections
Capacity contention with custom orders may break the slot promise in peak weeks.

## Outcome
Consented 2026-05-11 → [[Standard Order Fulfillment Protocol]].
```

## Notes

- `derived-from` is metadata (the parser has no such relationship type yet), as on
  [`driver`](driver.md) and [`insight`](insight.md).
- **Out of scope:** *how* the change is accompanied — the facilitation workflow, who acts
  when, how consent is run — is an application concern, not part of this spec. The spec
  defines the artifacts (proposal, agreement); the process around them lives in the tooling.
