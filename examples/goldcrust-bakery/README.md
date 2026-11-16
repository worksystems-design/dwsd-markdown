---
type: readme
dwsd-format: "1.6.0"
---

# Goldcrust Bakery

A small, fictional bakery described in DWSD: a production **Bakehouse**, two retail shops,
a delivery team, a coordination layer, and a strategy layer. It is a **worked example** —
every DWSD entity type appears at least once, wired together into one self-consistent
organization.

> **New here? [Take the tour](TOUR.md)** — seven stops, ten minutes, no prior knowledge
> needed: one person, one domain, one meeting, one decision, one board, and the structure
> behind the flow.

> Fictional and public-safe. Names and numbers are invented.

## Flight-level map

```dwsd.topology id=topology
mode: infer
around: "[[Bakery Operations]]"
radius: 1
```

The levels are **altitudes on the work, not ranks**: the same fourteen people fly all
three — Mara bakes at FL1 in the morning and decides range bets at FL3 in the afternoon.

<details>
<summary>The same map as plain text (renders everywhere, even without the DWSD renderer)</summary>

```
FL3  Bakery Strategy        sets direction
        ▲ contributes-to
FL2  Bakery Operations      coordinates production + retail
        ▲                ▲                  ▲
FL1  Bakehouse        Market Street Shop   Station Road Shop
     (production)     (retail)             (retail)

     Deliveries  — a plain team (no flightlevel) that carries the morning dispatch;
                   participates in the flow Bakery Operations coordinates
```

</details>

## Who reports to whom

**The org chart** — `reports-to`, individuals only. Nothing is listed here: edit a person's
file and the chart follows. Mara has no `reports-to`, so she is the root; `NA1` is an open
position.

```dwsd.orgchart id=orgchart
mode: infer
around: "[[Mara Holt]]"
radius: { up: 0, down: inf }
notes:
  - on: "[[NA1]]"
    text: "Interviews in October"
```

## Which unit sits inside which

**The units** — `member-of`, units only: Goldcrust Bakery contains three sites (Mill Lane
with Deliveries and Wholesale, Market Street, Station Road). The work systems carry no
`member-of`; they are the flow, drawn in the map above, not a second time here.

```dwsd.units id=units
mode: infer
layout: nested
around: "[[Goldcrust Bakery]]"
radius: { up: 0, down: inf }
notes:
  - on: "[[Deliveries]]"
    text: "Second van budgeted for Q4"
```

(`around` + `radius: { up: 0, down: inf }` scope each picture to this organization: the
renderer indexes the whole workspace, and a workspace with several example orgs would
otherwise show every root side by side.)

A unit is a **work system** when its `unit-type` includes `work-system` (it then also
carries a `flightlevel`). This example shows the shapes of `unit`:

- **Plain unit** — `Goldcrust Bakery` (in `units/`), `unit-type: company`, no `flightlevel`:
  the structural root that groups everything; it does not coordinate a flow.
- **Site** — `Mill Lane`, `Market Street`, `Station Road` (in `units/`), `unit-type: site`:
  the unit tree is cut by *where people work*. It does not redraw the topology — the work
  systems carry no `member-of` and appear only in the flight-level map, and people are
  `member-of` both their site and their work system.
- **Plain team** — `Deliveries` (in `units/`), `unit-type: team`, no `flightlevel`: a real
  team of people that is *not* a work system.
- **Team that is also a work system** — `Bakehouse` (in `work-systems/`),
  `unit-type: [team, work-system]`, `flightlevel: 1`: the two hats on one unit. The other
  four work systems carry `work-system` the same way.

## How to read this folder

- One file = one entity; the `type:` in the frontmatter decides what it is.
- Files are grouped into flat per-type folders (`individuals/`, `roles/`, `work-systems/`,
  …) — the folder is a convenience, the `type:` is authoritative.
- Relationships are `[[wikilinks]]` to other entities (rendered by the DWSD parser or
  Obsidian; plain VS Code preview shows them as text).
- Boards and flight routes carry embedded DSL (` ```dwsd.board ` and ` ```dwsd.flightroute `,
  both plain YAML). The ` ```dwsd.topology ` blocks (the map above, and the "In context"
  section in each work system) are the **optional** third fence — an inferred flight-level
  context map, used here as a demo extra; a work system is complete without one. The org
  chart and the units view above are two more inferred pictures (` ```dwsd.orgchart `,
  ` ```dwsd.units `); they also exist as standalone files at the org root.

## Entry points

- **Structure** — [`work-systems/`](work-systems/): `Bakehouse.md` carries the fullest
  domain description (and is a `[team, work-system]`). [`units/`](units/) holds the root
  `Goldcrust Bakery.md`, the three sites and the plain teams `Deliveries.md` and
  `Wholesale.md`. [`roles/`](roles/) keeps one
  shop-manager role file per location — roles are individual and evolve independently; a
  role *shared* by several people would instead list them all as `role-keeper`s. The
  *Market Street Site Lead* is scoped to the site, a plain unit, not to the shop's work
  system: keys, opening hours and the back door belong to the building.
- **Flow** — [`visualizations/`](visualizations/): a board per work system, in the YAML
  ` ```dwsd.board ` DSL. The Bakehouse and shop boards run the daily flow; the
  `Bakery Operations Coordination` board is end-to-end with a **swimlane per
  flight-item-type**; the `Bakery Strategy` board (FL3) holds the few strategic bets. Boards
  carry **inside-out** working agreements inline (e.g. the Bakehouse `Mixing-Proofing` WIP
  rule); entities also anchor **outside-in** via locators in `interaction-of` /
  `agreement-of`. [`flight-routes/`](flight-routes/) holds **four routes, one per
  flight-item-type, each a different pattern**: the `Daily Replenishment Flow` (operational
  closed loop — demand up, plan down, product across), the `Wholesale Contract Route`
  (acquisition — the contract *generates* a standing order), the `New Shop Launch Route`
  (top-down strategic, FL3 → FL2), and the `New Product Introduction Route` (bottom-up,
  FL1 → FL3 → FL2 → FL1); [`flight-item-types/`](flight-item-types/) defines what flows.
  [`interactions/`](interactions/) holds the `Daily Production Sync` meeting + its `.mw`
  sibling, and a review interaction per item type (`Wholesale Account Review`,
  `Launch Check-in`, `Trial Bake Tasting`) — each anchored to both a board position and
  a route stage. Not every interaction has a time slot: the
  [Sell-Out Call](interactions/Sell-Out%20Call.md) has no `rrule` and no `.mw` sibling — it
  happens when a shop runs out, and its `## Trigger` says so. Agreements anchor on routes
  too: [Station Road Early Dispatch](agreements/Station%20Road%20Early%20Dispatch.md) sits
  where the dispatch leaves the Bakehouse, the
  [Wholesale Capacity Cap](agreements/Wholesale%20Capacity%20Cap.md) before a signed
  contract becomes a standing order.
- **Navigation ladder** — follow the morning-sourdough thread:
  [`signals/`](signals/) → [`insights/`](insights/) → [`drivers/`](drivers/) →
  [`proposals/`](proposals/) → [`agreements/`](agreements/).
- **Change** — [`decision-records/`](decision-records/) records the decision to run a single
  daily sync.
