# Goldcrust Bakery — example organization

A small, fictional bakery described in DWSD: a production **Bakehouse**, two retail shops,
a coordination layer, and a strategy layer. It is a **worked example** — every DWSD entity
type appears at least once, wired together into one self-consistent organization.

> Fictional and public-safe. Names and numbers are invented.

## Flight-level map

```
FL3  Bakery Strategy        sets direction
        ▲ contributes-to
FL2  Bakery Operations      coordinates production + retail
        ▲                ▲                  ▲
FL1  Bakehouse        Market Street Shop   Station Road Shop
     (production)     (retail)             (retail)
```

`Goldcrust Bakery` (in `units/`) is the structural root — a plain `unit` with **no**
`flightlevel`. The five work systems are `unit`s **with** a `flightlevel`.

## How to read this folder

- One file = one entity; the `type:` in the frontmatter decides what it is.
- Files are grouped into flat per-type folders (`individuals/`, `roles/`, `work-systems/`,
  …) — the folder is a convenience, the `type:` is authoritative.
- Relationships are `[[wikilinks]]` to other entities (rendered by the DWSD parser or
  Obsidian; plain VS Code preview shows them as text).
- Boards and flight routes carry embedded DSL (` ```board `, ` ```flightroute `).

## Entry points

- **Structure** — [`work-systems/`](work-systems/): `Bakehouse.md` carries the fullest
  domain description. [`units/`](units/) holds the root `Goldcrust Bakery.md`.
- **Flow** — [`visualizations/`](visualizations/) (the production board),
  [`flight-routes/`](flight-routes/) (the replenishment route),
  [`interactions/`](interactions/) (the `Daily Production Sync` meeting + its `.mw` sibling).
- **Navigation ladder** — follow the morning-sourdough thread:
  [`signals/`](signals/) → [`insights/`](insights/) → [`drivers/`](drivers/) →
  [`proposals/`](proposals/) → [`agreements/`](agreements/).
- **Change** — [`design-records/`](design-records/) records the decision to run a single
  daily sync.
