# Changelog — model & convention decisions

Notable changes to the DWSD model and its Markdown conventions, recorded **from the first
commit onward**. The current model is described by the reference itself — `README.md`,
`conventions.md`, and the pages under `types/`; this log tracks how it changes over time.

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
