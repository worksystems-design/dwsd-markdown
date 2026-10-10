---
type: unit
unit-type: company
created_at: "2026-10-10"
---

Voltfeld is the company as a whole — the structural root everything else belongs to. Its
`unit-type` is just `company`: no `work-system`, no `flightlevel`. It groups; it does not
coordinate a flow of work.

Voltfeld builds EV charging hardware: an AC [[Wallbox]] line for homes and workplaces and a
[[DC Charger]] line for depots and public sites, both connected to a fleet backend. About
120 people; founded 2019. Since January 2026 product development runs as one Agile Release
Train, the [[Charger ART]], on a ten-week PI cadence — one of several ideas borrowed from
SAFe without adopting the whole framework.

Two trees hang off this root, and they are **not the same tree**:

- **The line** (`reports-to`, drawn by the org chart): [[Henrik Dahl]] at the top, four
  C-level leaders under him, and the engineers reporting to the heads of
  [[Hardware Engineering]] and [[Software Engineering]].
- **The work** (`member-of`, drawn by the units view): the [[Portfolio]] (FL3), the
  [[Charger ART]] (FL2) with its six teams (FL1), and [[Operations]] and [[Commercial]]
  with their teams.

The same engineer appears in both — reporting to a department head in one picture, a
member of a cross-functional team in the other. The standalone views are
`Voltfeld Org Chart.dwsd-orgchart` and `Voltfeld Units.dwsd-units` at the org root.

## In context

```dwsd.units
mode: infer
focus: self
radius: { up: 1, down: inf }
```
