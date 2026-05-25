# dwsd-markdown

**DWSD** — *Dynamic Work Systems Design* — is an approach to designing how an organization
works; it is more than a folder of files. This repository is its **Markdown foundation**:
the essentials for laying a **semantic layer** over the messy reality of how organizations
are actually built — so that both humans and AI agents can read, navigate, and reason
about an organization.

Concretely, the format describes an organization as a folder of Markdown files. Every file
is one *entity* — a person, a role, a work system, a meeting, a board, a flight route, and
so on. The entity's type and its connections live in the YAML frontmatter; the body is
plain Markdown (sometimes with an embedded DSL block).

This repository is the **reference** for that format: one spec page per type, the shared
conventions that apply across all of them, and bare copy-paste templates.

## Why this exists

Organizations are messy: their structure, roles, and how work actually flows are scattered
across heads, slides, and tools. DWSD captures the essentials in plain text so they become
**legible** — to people and to AI agents alike. Every page is written for a model to read
directly: explicit field tables, clear rules, and self-contained examples, so an agent can
generate, validate, and reason about entities without guesswork. The result is
version-controlled like code and editable in any editor.

Think of it as the organizational counterpart to [`agents.md`](https://agents.md/): where
`agents.md` tells a coding agent *how to work* in a codebase, DWSD describes *how an agent
(or a new colleague) finds its way around an organization* — what it is, where the work
happens, and how it flows.

DWSD draws inspiration from [Sociocracy 3.0](https://sociocracy30.org) and
[Flight Levels](https://flightlevels.io), among other models — adapted to fit, never
followed slavishly.

> **Canonical model, English-only.** The pages here are the canonical description of the
> format — explicit and self-contained.

## Start here

- **[conventions.md](conventions.md)** — the rules that apply to *every* entity:
  frontmatter, the `type` field, wikilink relationships, positions, tracking fields,
  DSL fences, and the structure vs. flow distinction.

> **Editing in VS Code.** `[[wikilinks]]` show as plain text in the default Markdown
> preview. Install [Foam](https://github.com/foambubble/foam) or **Markdown Memo** to make
> body wikilinks clickable; frontmatter relationships are resolved by the DWSD parser (and
> Obsidian) either way.

## Types

One file = one entity. The `type:` field in the frontmatter decides what it is. Entities
fall into four **categories** — **structure** (the org's makeup), **flow** (how work is
coordinated and flows), **navigation** (sensing and deciding — looking *on* the system),
and **change** (records of decided change). These are conceptual, **not folders**.

| Type | Category | Spec | One-liner |
|---|---|---|---|
| `individual` | structure | [spec](types/individual.md) | A person |
| `role` | structure | [spec](types/role.md) | A role, held by one or more people |
| `unit` | structure | [spec](types/unit.md) | A named grouping (people, teams, or units) — between structure and flow |
| `work-system` | structure | [spec](types/work-system.md) | A flow / value-creation system (a unit with a flightlevel) |
| `ai-agent` | structure | [spec](types/ai-agent.md) | An AI-agent surface — where an AI appears in the workflow (preliminary) |
| `interaction` | flow | [spec](types/interaction.md) | People acting in relation across work systems |
| `meeting` | flow | [spec](types/meeting.md) | A scheduled interaction — Meeting Canvas + activities table |
| `agreement` | flow | [spec](types/agreement.md) | A working agreement between work systems |
| `flight-item-type` | flow | [spec](types/flight-item-type.md) | A class of work item |
| `flight-route` | flow | [spec](types/flight-route.md) | A path of work through the flight levels |
| `visualization` | flow | [spec](types/visualization.md) | A board (or other view) of a work system |
| `signal` | navigation | [spec](types/signal.md) | A selected piece of data — before interpretation |
| `insight` | navigation | [spec](types/insight.md) | An interpretation drawn from signals |
| `driver` | navigation | [spec](types/driver.md) | The motive to act — situation, effect, need |
| `proposal` | navigation | [spec](types/proposal.md) | A proposed response to a driver — before consent |
| `design-record` | change | [spec](types/design-record.md) | An ADR-style record of an org-design decision (what · why · consequences) — minimal |

## Templates

Bare, copy-paste skeletons for each type live in [`templates/`](templates/). Each spec
page also embeds its own annotated example.

## Examples

Worked example organizations live in [`examples/`](examples/) — complete, self-consistent
instances that show the types wired together. Start with
[`examples/goldcrust-bakery/`](examples/goldcrust-bakery/), a small bakery that exercises
every type once.

## Claude Code plugin

This repo also ships a thin Claude Code plugin, **`dwsd-md`**, that teaches an agent the
format and validates an org folder. Its skill points back at the files above, so there is
nothing to keep in sync. Add this repo as a plugin marketplace and install `dwsd-md`; the
commands are `/dwsd-md:org-validate` and `/dwsd-md:org-new`.

See [`CHANGELOG.md`](CHANGELOG.md) for model and convention decisions.
