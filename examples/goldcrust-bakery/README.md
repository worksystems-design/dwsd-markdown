# Goldcrust Bakery — example organization

A small, fictional bakery described in DWSD: a production **Bakehouse**, two retail shops,
a delivery team, a coordination layer, and a strategy layer. It is a **worked example** —
every DWSD entity type appears at least once, wired together into one self-consistent
organization.

> Fictional and public-safe. Names and numbers are invented.

## Flight-level map

```wsd-topology
mode: infer
focus: "[[Bakery Operations]]"
radius: 1
```

<!-- The same flight-level map as plain text (renders everywhere, even without the
     DWSD renderer): -->

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
- Boards and flight routes carry embedded DSL (` ```board `, ` ```flightroute `).

## Entry points

- **Structure** — [`work-systems/`](work-systems/): `Bakehouse.md` carries the fullest
  domain description (and is a `[team, work-system]`). [`units/`](units/) holds the root
  `Goldcrust Bakery.md` and the plain-team `Deliveries.md`.
- **Flow** — [`visualizations/`](visualizations/) (a board per operational work system —
  Bakehouse, Bakery Operations, and both shops), [`flight-routes/`](flight-routes/) (the
  `Daily Replenishment Flow` route that closes the loop across those boards — demand up,
  plan down, product across), [`interactions/`](interactions/) (the `Daily Production Sync`
  meeting + its `.mw` sibling).
- **Navigation ladder** — follow the morning-sourdough thread:
  [`signals/`](signals/) → [`insights/`](insights/) → [`drivers/`](drivers/) →
  [`proposals/`](proposals/) → [`agreements/`](agreements/).
- **Change** — [`design-records/`](design-records/) records the decision to run a single
  daily sync.
