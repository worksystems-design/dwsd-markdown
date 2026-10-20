# `flight-route`

> How one type of work flows through the flight levels, end to end — the **bands** it
> moves through, the **stages** (an item type at a band) it passes, and the typed
> **edges** between them. Defined with the Route DSL and rendered live.

**Serialized `type`:** `flight-route`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `flight-route` | Entity type |

Plus the shared optionals from [conventions](../conventions.md). The route definition
itself lives in the body, not the frontmatter.

## Relationships

- Other entities point at a route with **`uses-route`** (a wikilink) — typically the
  [flight-item-type](flight-item-type.md) that travels it, pointing back at the route
  named in its `for:` key.
- The route names its primary [flight-item-type](flight-item-type.md) in the fence's
  `for:` key, and maps onto boards via `bound-to:` — both are part of the DSL below.
- The route names its **responsible domain** — a [work system](work-system.md), a
  [role](role.md) or a [unit](unit.md) — in the fence's `for-domain:` key. This is responsibility, not flow:
  the work systems a route flows through are **derived** (`bound-to` → board →
  `visualization-of`) and never authored on the route. A work system, role or unit can list the
  routes it is responsible for.
- External entities (interactions, agreements) can anchor **onto a route stage** with a
  locator: `"[[Route]]/stage:<itemType> @ <Band>::before|in|after"` — see
  [conventions](../conventions.md).

## Body — the `dwsd.flightroute` DSL

The body holds one ```` ```dwsd.flightroute ```` fenced block. The route DSL is **plain
YAML**; the only inline sugar is the edge line itself. A route is authored **unbound** —
`path:` references no board; a separate `bound-to:` layer maps bands onto concrete
boards. In plain Markdown the block still reads as a YAML document.

**Keys** (a closed set — nothing else is a key):

| Key | Shape | Meaning |
|---|---|---|
| `title` | string | The route name (shared document header; the old `route:` key is retired) |
| `tags` | string list | Descriptive chips, document scope only |
| `for` | wikilink or string | The primary flight-item-type the route describes — a wikilink to its file, or plain text when it has none |
| `for-domain` | wikilink or list of wikilinks | The **domain** — a work system, a role or a unit — **responsible** for the route: who has to take care when it changes. Points *up*. An unresolved target is a warning, never an error |
| `bands` | list of `{ name, fl }` | The named bands work moves through; `fl` is `1`/`2`/`3` or a span like `[1, 2]`; omit `fl` for a pure custom band |
| `triggers` | list of `{ name, generates }` | External start events outside the bands; `generates` is one stage or a list (fan-out) |
| `path` | edge list | The route itself — typed edges between stages |
| `bound-to` | list of band→board bindings | Optional binding of bands to boards (see below) |

**Stages** are never declared — a stage is an `itemType @ Band` pair (single space each
side of `@`, e.g. `order @ Shops`), and the parser infers the set of stages from the edge
endpoints and trigger targets.

**A stage's item type is text or a wikilink.** Text (`order @ Shops`) describes the item
locally to the route: it is never looked up and never flagged. A wikilink
(`[[Feature]] @ Train`) is a real connection to a [flight-item-type](flight-item-type.md)
entity — it resolves like any wikilink, and one that resolves to nothing is a broken link.
A link that resolves to an entity of another type is still a link; a validator warns.
An alias keeps a short label (`[[Customer Order|order]] @ ERP`). Both forms mix freely,
also on one line. A line that holds a wikilink is **quoted**, as everywhere in YAML:

```yaml
path:
  - "[[Epic]] @ Train -> [[Feature]] @ Train"
  - "[[Feature]] @ Train -> story @ Teams"
```

A stage is **named** by its token, or for a wikilink by its link target (not the alias):
`stage:Feature @ Train` in a locator, `Feature:` as a `bound-to` key. The match is exact
within the route; a locator never nests `[[…]]`. Switching a stage from text to a wikilink
therefore changes its name (`feature` → `Feature`) — update the locators and keys with it.

**Edges** — each `path:` line is one hop, `LEFT <glyph> RIGHT`; the glyph selects the
kind:

| Kind | Glyph | Bands | Meaning |
|---|---|---|---|
| `generate` | `->` | same band | One item type is created from another |
| `copy` | `-->` | different bands | The same item is copied across bands (fan-out capable) |
| `feedback` | `..>` | unconstrained | Backward information flow to an earlier stage |
| `delivery` | `..> ()` | terminates outside | Delivery to the reserved outside sink (rendered as a ⊙ ring) |

Band constraints (`generate` = same band, `copy` = across bands) are teaching nudges —
warnings, never hard blocks. `()` is reachable **only** via the dotted `..>` glyph, and a
line holds exactly one hop. Every edge also has an expanded object form
`{ from, to, kind }`; both forms mix freely.

**Binding — `bound-to:`.** Each entry names one `band` (which must be declared in
`bands:`) and a list of `boards`. A **coarse** binding is a bare `board:` wikilink; a
**fine** binding adds `stages:` — a list of `{ <stage name>: <locator> }` pinning a stage
to a board position (`lane:Name/col:Name`). The relation is N:M — one band may bind to
several boards and vice versa; an entirely unbound route is valid. The one hard rule is
**Flow ⊆ Path**: every bound band must exist in `bands:`, and every pinned item type must
live in that band per `path:`.

## Example

````markdown
---
type: flight-route
---
A customer order enters at Sales, is broken into component specs, and the finished
component ships to the customer.

```dwsd.flightroute
title: Standard Order Fulfillment
for: "[[Standard Order]]"
for-domain: "[[Sales]]"
bands:
  - name: Sales
    fl: 2
  - name: Assembly
    fl: 1
triggers:
  - name: customer order placement
    generates:
      - standard-order @ Sales
path:
  - standard-order @ Sales -> component-spec @ Sales
  - component-spec @ Sales --> component-spec @ Assembly
  - component-spec @ Assembly ..> standard-order @ Sales
  - component-spec @ Assembly ..> ()
bound-to:
  - band: Assembly
    boards:
      - board: "[[Assembly 1 Board]]"
        stages:
          - component-spec: "col:To-Do"
```
````

Reading the path: Sales is the domain responsible for the route (`for-domain`); the
order *generates* component specs (same band, solid `->`); the
specs are *copied* down into the Assembly band (dashed `-->`); build status *feeds back*
to the order (dotted `..>`); the finished component is *delivered* to the customer
(`..> ()`, the ⊙ ring).

## Notes

- `for-domain:` and `bound-to: … board:` take wikilinks — the target entity's name, like
  every other relationship in the model. `for:` and a stage's item type take a wikilink
  **or** plain text: the wikilink is a connection, the text a description. Nothing is
  matched by name — `epic` stays text even when an `Epic` file exists — so a route stays
  authorable without any org model.
- Retired forms (all hard errors or rejected): the `route "Name"` header and the root
  `route:` key (→ `title:`), the `flow:` section and `@`-handle column references
  (→ `path:` + `bound-to:`), the `deliver` edge (→ `..> ()`), `-[action: @item]->`
  arrows (→ the glyph vocabulary), and the bare `flightroute` fence tag
  (→ `dwsd.flightroute`).
- The parser is tolerant: malformed entries produce a `route.*` diagnostic and are
  skipped; the two structural errors are a retired key and a `bound-to:` entry that
  violates Flow ⊆ Path.
