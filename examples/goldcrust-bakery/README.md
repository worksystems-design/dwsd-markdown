# Goldcrust Bakery — example organization

A small, fictional bakery described in DWSD: a production **Bakehouse**, two retail shops,
a delivery team, a coordination layer, and a strategy layer. It is a **worked example** —
every DWSD entity type appears at least once, wired together into one self-consistent
organization.

> **New here? [Take the tour](TOUR.md)** — six stops, ten minutes, no prior knowledge
> needed: one person, one domain, one meeting, one decision, one board.

> Fictional and public-safe. Names and numbers are invented.

## Flight-level map

```dwsd.topology
mode: infer
focus: "[[Bakery Operations]]"
radius: 1
```

The levels are **altitudes on the work, not ranks**: the same eight people fly all
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

A unit is a **work system** when its `unit-type` includes `work-system` (it then also
carries a `flightlevel`). This example shows all three shapes of `unit`:

- **Plain unit** — `Goldcrust Bakery` (in `units/`), `unit-type: company`, no `flightlevel`:
  the structural root that groups everything; it does not coordinate a flow.
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
  context map, used here as a demo extra; a work system is complete without one.

## Entry points

- **Structure** — [`work-systems/`](work-systems/): `Bakehouse.md` carries the fullest
  domain description (and is a `[team, work-system]`). [`units/`](units/) holds the root
  `Goldcrust Bakery.md` and the plain-team `Deliveries.md`. [`roles/`](roles/) keeps one
  shop-manager role file per location — roles are individual and evolve independently; a
  role *shared* by several people would instead list them all as `role-keeper`s.
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
  a route stage.
- **Navigation ladder** — follow the morning-sourdough thread:
  [`signals/`](signals/) → [`insights/`](insights/) → [`drivers/`](drivers/) →
  [`proposals/`](proposals/) → [`agreements/`](agreements/).
- **Change** — [`decision-records/`](decision-records/) records the decision to run a single
  daily sync.
