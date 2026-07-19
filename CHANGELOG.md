# Changelog — model & convention decisions

Notable changes to the DWSD model and its Markdown conventions, recorded **from the first
commit onward**. The current model is described by the reference itself — `README.md`,
`conventions.md`, and the pages under `types/`; this log tracks how it changes over time.

## 2026-07-19

- **The topology fence is documented — and joins the dot form (` ```dwsd.topology `).**
  The inferred flight-level context map used in the Goldcrust example (`mode: infer`,
  optional `focus:`, `radius:`) is now the documented third embedded DSL fence in
  [`conventions.md`](conventions.md); the previously undocumented `wsd-topology` tag is
  renamed to `dwsd.topology`. The block is **optional** — a view any entity body may
  carry (the Goldcrust work systems use it as an "In context" demo), never part of a
  type's required body structure. ⚠ Preliminary: the key set may still change.
- **Item types point at their route with `uses-route`.** The
  flight-item-type ↔ flight-route pair is now bidirectional: the route names its primary
  item type in the fence's `for:` key, and the item type points back with a frontmatter
  `uses-route` wikilink — documented on both type pages and exercised by all four
  Goldcrust item types.
- **Scheduling generalizes to every interaction.** `start` / `end` / `rrule` are now
  documented on `types/interaction.md` (previously only on the `meeting` page) — any
  interaction may be scheduled, and a recurring one usually carries a `.mw` sibling. An
  org folder may additionally keep one **consolidated timeline file** (e.g.
  `operating-rhythm.mw`) aggregating the sibling lines — Markwhen viewers operate on a
  single file; the siblings stay the source of truth.
- **Goldcrust gets a clock.** The day now runs contradiction-free: the 13:30 Daily
  Production Sync frames tomorrow on *yesterday's* closing counts and today's
  sell-through; the 18:30 Evening Stock Count sets final quantities within that frame;
  sourdough's 24-hour lead is named in the Bakehouse. All five recurring interactions
  carry `start`/`end`/`rrule` plus `.mw` siblings, aggregated in `operating-rhythm.mw`.
- **Goldcrust gets a door.** A guided `TOUR.md` (six stops: a person, a domain, a
  meeting, the sourdough decision thread, the agreement, a board — then "your first
  three files" from `templates/`) is now the first entry point: linked at the top of the
  example README and as the first bullet of the root "Start here" (before
  `conventions.md` — concrete before abstract). The tour is a guide, not an entity (no
  `type:`), and uses plain relative links so it works on GitHub too. The example
  README's plain-text map fallback is collapsed into a `<details>` block, and the
  flight-level map now states that levels are altitudes on the work, not ranks.
- **One range decision, one answer.** The range decision rights read consistently across
  Head Baker, Daily Range Cap, and Shop Manager Mandate: the Head Baker *curates* the
  standing range and decides recipes and the daily bake sequence; *changing* the range
  is a Bakery Strategy bet under the Daily Range Cap, with Mara Holt holding the final
  call — today both hats sit on the same person, and the files say so.
- **An open thread.** A fresh, uninterpreted signal (`Two Wholesale Enquiries Waiting at
  the Cap`, observing the Wholesale Capacity Cap) shows navigation with the ladder still
  unclimbed — change in the example now has a future, not only a past. The tour points
  at it as its closing question.

## 2026-07-18

- **Route DSL is now YAML (` ```dwsd.flightroute `).** The route fence moved from the old
  line-based form (`route "Name"`, `for: @handle`, `path:` FL chains, `flow:` edges with
  `-[action: @item]->` arrows) to **plain YAML** with a closed key set: `title:`, `tags:`,
  `for:` (the primary flight-item-type, as a wikilink), `bands:` (named bands with
  `fl: 1|2|3` or a span), `triggers:` (`{name, generates}` — external start events), and a
  glyph-typed `path:`: `->` generate (same band), `-->` copy (across bands), `..>` feedback,
  `..> ()` delivery to the outside sink (⊙). A route is authored **unbound**; the separate
  `bound-to:` layer maps bands onto boards via wikilinks and the locator, with per-stage
  pins (`lane:X/col:Y`) under the one hard rule **Flow ⊆ Path**. The `@`-handle references
  (`@work-system#Column`), the `flow:` section, and the `deliver` edge are retired.
- **Fence tags converge on the dot form.** Renderable fences are ` ```dwsd.board ` and
  ` ```dwsd.flightroute ` — the hyphenated `dwsd-board` tag and the bare `flightroute` tag
  are retired (they may still highlight, but do not render). The board name key `board:` is
  retired in favor of the shared document header `title:` (same key on both DSLs).
- **Route-stage anchoring.** The locator gains a `stage:` segment: an interaction or
  agreement can anchor onto a route stage via
  `[[Route]]/stage:itemType @ Band::before|in|after` (with `#Route Name` disambiguating a
  multi-route file).
- **Goldcrust Bakery: four flight routes, one per flight-item-type.** A new
  `New Product Introduction` item type joins the three existing ones, and each type now has
  a route with a distinct pattern: `Daily Replenishment Flow` (operational closed loop,
  migrated to the YAML DSL), `Wholesale Contract Route` (acquisition — a contract
  *generates* a standing order), `New Shop Launch Route` (top-down strategic), and
  `New Product Introduction Route` (bottom-up, FL1 → FL3 → FL2 → FL1).

## 2026-06-28

- **Board DSL is now YAML (` ```dwsd-board `).** The board fence moved from the old
  line-based form (`Column #status`, `[wip]`, indented `aging:` lines) to **plain YAML** with
  spelled-out keys: a board header (`board`, `flightlevel: FL1|FL2|FL3`, `timebox`, `tags`,
  `agreements`, `interactions`), `columns:`, `lanes:`, and `groups:`. There is **no inline
  sugar** — status is `status-category: to-do|in-progress|done|waiting|assess` (no `blocked`;
  a stuck column is `waiting`), WIP is `wip: N` (column max) or `wip: [min, max]`, plus
  `aging:`, `max-returns:`, `check:`, `split:`. The parser is tolerant (a `board.*` diagnostic
  + clamp/skip, never a throw).
- **Inside-out / outside-in anchoring.** A board node may declare relationships **inside-out**
  via inline `agreements:` / `interactions:` keys on a board / column / lane / group / split.
  External entities anchor **outside-in** via a **locator** in `interaction-of` /
  `agreement-of`: `[[Board]]#BoardName/col:Column::in` (path of `/`-chained
  `col:` · `lane:` · `group:` · `split:` segments + optional `::before|in|after`, bare = `in`),
  or `[[Board]]#BoardName::in` for the whole board. The keys are **value-polymorphic** — a bare
  `[[Work System]]` still anchors to a work system. The old `@board#Column` anchor is retired
  for boards.
- **Lanes** are `named | assignee | expedite`; they are **not** bound to a flight-item-type. A
  "swimlane per item type" is authored as a `named` lane named after the type.
- **The route DSL is unchanged** — ` ```flightroute ` still references work systems and item
  types by `@`-handle (`@work-system#Column`), distinct from the board locator above.

## 2026-06-20

- **OKF compatibility documented.** DWSD is stated **conformant with the Open Knowledge
  Format** (OKF v0.1, Google Cloud, June 2026) as an *organizational profile* of it. The
  new [`okf.md`](okf.md) records the conformance — OKF's three requirements (parseable
  frontmatter, a required non-empty `type`, reserved-filename handling) are met by
  construction — plus the DWSD ↔ OKF field mapping and two honest supersets (relationships
  live in frontmatter rather than body links; non-entity docs are skipped rather than named
  `index.md`). This is **descriptive, not a model change**: nothing in the format changes,
  and the alignment is backward-compatible. OKF, `agents.md`, and DWSD share the same
  Karpathy LLM-wiki lineage.

## 2026-05-29

- **Work systems are marked on `unit-type`, not by `flightlevel`.** A unit is a work
  system when its `unit-type` includes the reserved value `work-system` (e.g.
  `unit-type: [team, work-system]`). Previously a work system was recognized implicitly by
  the *presence of a `flightlevel`*. `flightlevel` stays — it remains **required** on every
  work system and records the flight level — but it is no longer the discriminator. This
  makes a unit's two hats (a **team** of people and a **work system** in the flow) explicit
  on one field instead of inferred.
- **`<base>-type` discriminators may be lists.** Any discriminator named `<base>-type`
  (`unit-type`, `visualization-type`, `agreement-type`, `interaction-type`) may hold a
  single token or a YAML list, so an entity can declare several kinds at once. In practice
  only `unit-type` uses this today.
- **Meetings are containers of interactions.** A `meeting` (an `interaction` of
  `interaction-type: meeting`) now bundles a **list of interactions** — each with its outcome
  — in a `## Interactions` body section. The earlier step/agenda table (with its
  `discover-plan / deliver / improve` categories) and the "Meeting Canvas" label are removed;
  the four framing questions stay as plain body sections. Entries may be inline or
  `[[wikilinks]]` to an interaction or another meeting, so larger events compose from smaller
  meetings. Any interaction may optionally use the same four framing questions.
