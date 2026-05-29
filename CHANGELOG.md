# Changelog — model & convention decisions

Notable changes to the DWSD model and its Markdown conventions, recorded **from the first
commit onward**. The current model is described by the reference itself — `README.md`,
`conventions.md`, and the pages under `types/`; this log tracks how it changes over time.

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
