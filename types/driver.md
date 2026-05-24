# `driver`

> An *organizational driver* — the motive for acting: a current situation together with
> the effect it has and the need that arises from it. On the Ladder of Inference it is
> the rung above an [`insight`](insight.md): **signal → insight → driver → response**. A
> driver is what a response (a proposal, an agreement, an action) answers to.

**Serialized `type`:** `driver`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `driver` | Entity type |
| `for-domain` / `for_domain` | no | wikilink | The domain / work system whose team has the need |
| `derived-from` | no | wikilink or list | The [insight(s)](insight.md) this driver is built on (see note) |
| `status` | no | string | Lifecycle, e.g. `new`, `addressed` |

Plus the shared optionals from [conventions](../conventions.md).

## Relationships

- **`for-domain`** — the domain the driver belongs to (whose team has the need).
- **`derived-from`** — the [insight(s)](insight.md) the driver was distilled from, and
  through them the [signals](signal.md) beneath. Continues the Ladder of Inference.
  *Metadata only:* the parser has no `derived-from` relationship type, so it is not a
  typed edge.

## Body — driver description

Open with the **condensed driver** — 1–2 sentences — then four parts:

| Section | Holds |
|---|---|
| `## Current Situation` | The essential aspects of the situation — observations, not judgments |
| `## Effect` | Why the organization should care; note whether the effect is evidenced or assumed |
| `## Need` | What the team needs to manage its domain — and **who** has the need |
| `## Consequences` | The intended result, plus potential benefits or opportunities |

## Example

```markdown
---
type: driver
for-domain: "[[Strategic Direction]]"
status: new
derived-from:
  - "[[Cross-Team Alignment Gap]]"
---
# Standard-order hand-off has no owner

Standard orders stall between Sales and Assembly because no one owns the hand-off; the
Standard PMs need a clear acknowledgement protocol.

## Current Situation

Orders flow Sales → Standard PMs → Assembly with no agreed acknowledgement step. Several
recent orders waited days before anyone picked them up.

## Effect

Delivery promises slip and Sales loses visibility. Evidenced by the 2026-Q1 review.

## Need

The Standard PMs need a dependable acknowledgement and slot-confirmation protocol to
manage standard-order flow.

## Consequences

A clear protocol cuts idle wait time and restores Sales' visibility into intake capacity.
```

## Notes

- The four-part structure is DWSD's own, inspired by — not copied from — Sociocracy 3.0's
  [*Describe Organizational Drivers*](https://patterns.sociocracy30.org/describe-organizational-drivers.html).
  Other influences: Flight Levels.
- A driver is typically answered by a response — often an [`agreement`](agreement.md).
