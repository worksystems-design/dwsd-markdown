---
type: unit
unit-type: company
created_at: "2026-10-10"
---

Voltfeld is the company as a whole — the structural root everything else belongs to. It
groups; it does not coordinate a flow of work.

Voltfeld builds EV charging hardware: an AC [[Wallbox]] line for homes and workplaces and a
[[DC Charger]] line for depots and public sites, both connected to a fleet backend. About
120 people; founded 2019. Since January 2026 product development runs as one Agile Release
Train, the [[Charger ART]], on a ten-week PI cadence — one of several ideas borrowed from
SAFe without adopting the whole framework.

Two trees hang off this root, and they are **not the same tree**:

- **The line**: [[Henrik Dahl]] at the top, four C-level leaders under him, and the
  engineers reporting to the heads of [[Hardware Engineering]] and
  [[Software Engineering]].
- **The work**: the [[Portfolio]] (FL3), the [[Charger ART]] (FL2) with its three product
  lines (FL2, two teams each) and three FL1 work systems, and [[Operations]] and
  [[Commercial]] with their teams.

The same engineer appears in both — reporting to a department head in one picture, a
member of a cross-functional team in the other.

## In context

```dwsd.units id=units
mode: infer
around: self
radius: { up: 1, down: inf }
```

## Change trail

```dwsd.change-trail id=change-trail
```

Every change entity of Voltfeld in one picture. Two signals from the train and the plant
become one insight, one driver, one proposal and one decision, which lands in two
agreements. Two reports from the field — a wallbox that stops charging after an update, and
the same pattern eleven times in a month — end in version 2.0 of the
[[Expedite Lane Policy]]; one of them also opened a question about a firmware build that
nobody has taken up. The frozen cable lock, the studio's configuration cases and the
declined variant requests are still open.

> [!NOTE]
> **Modeling note.** Its `unit-type` is just `company`: no `work-system`, no `flightlevel`.
> The line is the `reports-to` tree, drawn by the org chart; the work is the `member-of`
> tree, drawn by the units view. The standalone views are
> `Voltfeld Org Chart.dwsd-orgchart` and `Voltfeld Units.dwsd-units` at the org root.
