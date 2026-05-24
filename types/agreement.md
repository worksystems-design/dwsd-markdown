# `agreement`

> A working agreement — a protocol, SLA, or contract between work systems. The parties
> and who is responsible for what are spelled out in the body.

**Serialized `type`:** `agreement`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `agreement` | Entity type |
| `agreement-type` | yes | `organizational` \| `work` | What it governs — see *Kinds* below |
| `for-domain` / `for_domain` | no | wikilink | The domain / strategy layer the agreement is scoped to |
| `derived-from` | no | wikilink | The [`proposal`](proposal.md) it was consented from (metadata) |
| `version` | no | string | Version of the agreement, e.g. `1.2` |
| `decision_date` | no | date | When this version was decided |
| `review_date` | no | date | When it is due for review |

Plus the shared optionals from [conventions](../conventions.md).

> The **title** is the filename. **Date/Version** and **Review Date** live in the
> frontmatter (`version` + `decision_date`, and `review_date`) and render as properties;
> the body starts at *Driver and Requirement*.

## Kinds

`agreement-type` marks which loop the agreement belongs to — the point where working
*on* the system and working *in* the system meet:

- **`organizational`** — an agreement *on* the system (Work Systems Design): about
  domains, roles, and how the organization is structured.
- **`work`** — an agreement *in* the system (Work Management): about how work flows and
  is coordinated — WIP limits, Definition of Ready, hand-off protocols.

Both kinds share the body structure below.

## Relationships

- **`for-domain`** — the higher domain the agreement is scoped to.

## Body — recommended structure

A standard structure for agreements. Sections in parentheses are optional.

| Section | Heading | Holds |
|---|---|---|
| Driver and Requirement | `## Driver and Requirement` | Why the agreement exists — the need it answers |
| Who is responsible for what? | `## Who is responsible for what?` | Responsibilities as a list, linking the parties (`[[…]]`) |
| Description | `## Description` | What the agreement actually says — rules, flow, SLAs |
| Evaluation Criteria | `## Evaluation Criteria` | How we know it is working |
| (Concerns) | `## Concerns` | Open questions / dissent raised when deciding *(optional)* |
| Appendix | `## Appendix` | Supporting material, in `###` subsections (below) |

The **Appendix** groups three subsections:

- `### Background Information` — context that informed the agreement
- `### Previous Versions` — version history
- `### References` — links to related entities (`[[…]]`) and external documents

## Example

```markdown
---
type: agreement
agreement-type: work
for-domain: "[[Strategic Direction]]"
version: "1.2"
decision_date: "2026-05-11"
review_date: "2026-08-11"
---
## Driver and Requirement

Standard orders kept stalling between Sales intake and Assembly because no one owned the
hand-off timing. This agreement fixes who acknowledges what, and by when.

## Who is responsible for what?

- [[Sales]] — acknowledges every standard order within 24h and tags the target variant.
- [[Assembly]] — confirms a delivery slot on intake, or escalates within 48h.

## Description

Orders flow Sales → Standard PMs → Assembly. Standard delivery target: 4–6 weeks.
Acknowledgement SLA: 24h.

## Evaluation Criteria

- 95% of standard orders acknowledged within 24h.
- No standard order waiting > 48h without a confirmed slot.

## Concerns

- Capacity contention with custom orders may break the 48h slot promise in peak weeks.

## Appendix

### Background Information

Raised during the 2026-Q1 delivery-bottleneck review.

### Previous Versions

- v1.1 (2026-03-01) — first coordination protocol, no escalation path.

### References

- [[Standard Order Fulfillment Protocol]]
- [[Sales]]
```

## Notes

- The body structure is a **recommendation**. A discovered / imported agreement may start
  sparse — imported metadata plus free body text — until it is filled in.
