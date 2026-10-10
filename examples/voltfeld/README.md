# Voltfeld — example organization

A fictional maker of EV charging hardware, described in DWSD: an AC **Wallbox** line and a
**DC Charger** line, developed by one Agile Release Train of six teams, built in a plant,
sold and serviced by a commercial department — about 120 people, of whom this folder models
the thirty that carry the structure. It is the second worked example next to the
[Goldcrust Bakery](../goldcrust-bakery/); where Goldcrust is small enough that the line and
the work almost coincide, Voltfeld is the example where they **do not**.

> **New here? [Take the tour](TOUR.md)** — seven stops, ten minutes: one engineer in two
> pictures, a platform that serves two teams, the train's board, a route that stops at the
> plant, two signals and a decision, the decision in two agreements, and an agent that
> prepares while people decide. If this is your first DWSD example, start with the
> [Goldcrust tour](../goldcrust-bakery/TOUR.md) instead — it is smaller.

> Fictional and public-safe. Names and numbers are invented.

## Partially SAFe-inspired

Voltfeld has borrowed several ideas from SAFe without adopting the framework: product
development runs as one **Agile Release Train** ([[Charger ART]]) on a ten-week **Program
Increment** cadence, facilitated by a [Release Train Engineer](roles/Release%20Train%20Engineer.md);
[Product Management](roles/Product%20Management.md) ranks a feature backlog that two
[product owners](roles/Product%20Owner%20Wallbox.md) split into team backlogs; a
[System Architect](roles/System%20Architect.md) keeps the runway; four
[Business Owners](roles/Business%20Owner.md) represent the portfolio at PI planning. The
rest of the company — the plant, the supply base, sales, field service — works outside the
train, and that seam is where this example is interesting.

DWSD describes this the way it describes any organization: the ART is a `unit` with
`unit-type: [art, work-system]` at FL2; the teams are units at FL1; the portfolio is the FL3
work system above. SAFe terms appear where Voltfeld uses them; nothing in the format depends
on them.

*SAFe® and Scaled Agile Framework® are registered trademarks of Scaled Agile, Inc.*

## Flight-level map

```dwsd.topology
mode: infer
focus: "[[Charger ART]]"
radius: 2
```

<details>
<summary>The same map as plain text (renders everywhere, even without the DWSD renderer)</summary>

```
FL3  Portfolio ◄────────────────────────────────────────────────┐
        ▲ contributes-to                                        │
FL2  Charger ART            plans, syncs, releases per PI       │
        ▲          ▲            ▲              ▲                │
FL1  Wallbox    DC Charger   Connectivity   System Integration  Manufacturing
        ▲  ▲       ▲  ▲          ▲                              contributes straight up
        │  └───────┼──┘          │                              to FL3: development and
     HW Base       │             │                              production share no FL2
     Firmware Platform ──────────┘

     Supply Chain · Sales · Field Service — plain teams (no flightlevel)
```

</details>

Two things to notice:

- **Two platform work systems contribute to more than one.** [HW Base](work-systems/HW%20Base.md)
  feeds both product teams; the [Firmware Platform](work-systems/Firmware%20Platform.md)
  feeds both product teams *and* Connectivity. `contributes-to` is a list, and the edges
  run laterally at FL1 — allowed, as long as nothing contributes *downward*.
- **Manufacturing has no FL2.** The [plant](work-systems/Manufacturing.md) is a work
  system — it coordinates a flow every day — but it is not in the ART. Its output is
  steered from the Portfolio directly. The ART coordinates development; the COO coordinates
  production; they meet at FL3. That gap is the as-is this example describes, and it is
  the one that `member-of` and `contributes-to` disagree about: Manufacturing *belongs to*
  [Operations](units/Operations.md) and *contributes to* the Portfolio.

## Two trees, not one

The line and the work are two different pictures here, drawn from two different frontmatter
keys of the same files.

**The org chart** — `reports-to`, individuals only. Engineers report to the heads of
[Hardware Engineering](units/Hardware%20Engineering.md) and
[Software Engineering](units/Software%20Engineering.md), who hire, develop and review them:

```dwsd.orgchart
mode: infer
```

**The units** — `member-of`, units only. The same engineers are members of the six
cross-functional ART teams; the two engineering departments appear as boxes with no team
inside them, because nobody *works* there — their `line` chip says so:

```dwsd.units
mode: infer
layout: nested
```

Follow one person through both: [Daria Novak](individuals/Daria%20Novak.md) reports to
[Kaspar Reinholt](individuals/Kaspar%20Reinholt.md) (org chart, under Hardware
Engineering) and works in [Wallbox](work-systems/Wallbox.md) (units, inside the Charger
ART). Both standalone views live at the org root:
[Voltfeld Org Chart.dwsd-orgchart](Voltfeld%20Org%20Chart.dwsd-orgchart) and
[Voltfeld Units.dwsd-units](Voltfeld%20Units.dwsd-units).

In [Operations](units/Operations.md) and [Commercial](units/Commercial.md) the two trees
agree — people work where they report. The difference is confined to engineering, which is
exactly what an ART does to a line organization.

## Agents at sub-process level

Three [`ai-agents/`](ai-agents/) work *inside* the flow, each bound to a part of a board
rather than to a single column. The [DFM Check Agent](ai-agents/DFM%20Check%20Agent.md)
is bound to the whole `Verification` **column group** of the HW Base board
(`group:Verification::in`); the [Release Dossier Agent](ai-agents/Release%20Dossier%20Agent.md)
to the `Release` group inside the ART board's feature lane
(`lane:Feature/group:Release::in`); the
[Field Issue Triage Agent](ai-agents/Field%20Issue%20Triage%20Agent.md) sits `::before`
the `Triage` column of the expedite lane — the queue in front of the column, not the column.
Each also anchors to a person or a unit, so the same agent shows on a box in the org chart
or the units view. In every case the agent prepares and the people decide.

## How to read this folder

- One file = one entity; the `type:` in the frontmatter decides what it is.
- Files are grouped into flat per-type folders (`individuals/`, `roles/`, `work-systems/`,
  …) — the folder is a convenience, the `type:` is authoritative.
- Relationships are `[[wikilinks]]` to other entities.
- The ` ```dwsd.topology `, ` ```dwsd.orgchart ` and ` ```dwsd.units ` blocks are
  **inferred views** — they name nothing; rename a file or move a `reports-to` and the
  pictures follow. All three are optional extras; an entity is complete without them.

## Entry points

- **Structure** — [`work-systems/`](work-systems/): nine work systems; the
  [Charger ART](work-systems/Charger%20ART.md) and [HW Base](work-systems/HW%20Base.md)
  carry the fullest domain descriptions. [`units/`](units/) holds the company root, four
  departments and three plain teams. [`roles/`](roles/) holds the ART roles and the
  Manufacturing Lead — including [Business Owner](roles/Business%20Owner.md), a role
  **shared** by four keepers. [`individuals/`](individuals/): thirty people, one of them the
  vacancy [NA1](individuals/NA1.md).
- **Flow** — [`visualizations/`](visualizations/): five boards. The
  [Charger ART Board](visualizations/Charger%20ART%20Board.md) is the train's program board
  (`timebox: 10w`) with a feature lane in three **column groups** and an **expedite lane**
  for field issues; the [HW Base Board](visualizations/HW%20Base%20Board.md) runs hardware
  work through `Design` → `Verification` → `Release`; the
  [Portfolio Board](visualizations/Portfolio%20Board.md) is the FL3 epic kanban; a team
  board and the [Manufacturing Board](visualizations/Manufacturing%20Board.md) — which
  nothing on the ART board points at — complete the set.
  [`flight-routes/`](flight-routes/) holds **three routes, one per item type, each a
  different pattern**: the [Epic Route](flight-routes/Epic%20Route.md) (top-down, FL3 → FL2),
  the [Feature Route](flight-routes/Feature%20Route.md) (one PI, ending with a release
  copied to the plant — and no edge back), and the
  [Field Issue Route](flight-routes/Field%20Issue%20Route.md) (bottom-up from a band with
  no flight level, forking into hotfix or feature);
  [`flight-item-types/`](flight-item-types/) defines what flows.
  [`interactions/`](interactions/) holds the ART's cadence — [PI Planning](interactions/PI%20Planning.md),
  [ART Sync](interactions/ART%20Sync.md), [System Demo](interactions/System%20Demo.md),
  [Inspect and Adapt](interactions/Inspect%20and%20Adapt.md) — the monthly
  [Portfolio Sync](interactions/Portfolio%20Sync.md), the weekly
  [Field Issue Triage](interactions/Field%20Issue%20Triage.md), the unscheduled
  [DFM Review](interactions/DFM%20Review.md) and a 1-1; each scheduled one has a `.mw`
  sibling, aggregated in [operating-rhythm.mw](operating-rhythm.mw).
  [`agreements/`](agreements/) holds four standing agreements, anchored on board positions
  ([PI Commitment](agreements/PI%20Commitment.md) on a column group,
  [Expedite Lane Policy](agreements/Expedite%20Lane%20Policy.md) on a lane) or on entities
  ([Platform Variant Rule](agreements/Platform%20Variant%20Rule.md) on the two platforms and
  the System Architect role, [DC Rig Booking](agreements/DC%20Rig%20Booking.md) on a team
  without a board).
- **Change** — the ladder climbs from two [`signals/`](signals/)
  ([PI Objectives Missed on Enclosure Tooling Twice](signals/PI%20Objectives%20Missed%20on%20Enclosure%20Tooling%20Twice.md),
  [Fixtures Built After the Release](signals/Fixtures%20Built%20After%20the%20Release.md))
  through the [insight](insights/Production%20Is%20Outside%20the%20Train%27s%20Horizon.md),
  the [driver](drivers/Long-Lead%20Work%20Needs%20a%20Longer%20Horizon%20Than%20the%20PI.md)
  and the [proposal](proposals/Bring%20the%20Plant%20and%20Supply%20Chain%20into%20PI%20Planning.md)
  to the decision record
  [Production Joins the Train's Planning](decision-records/Production%20Joins%20the%20Train%27s%20Planning.md),
  which two agreements operationalize via `derived-from`:
  [Long-Lead Commitment at PI Planning](agreements/Long-Lead%20Commitment%20at%20PI%20Planning.md)
  and [Ramp Readiness Review](agreements/Ramp%20Readiness%20Review.md). Decided 2026-10-06,
  in force from the next PI planning — so the as-is pictures above are still true today. A
  third signal, [Variant Request Declined Three Times](signals/Variant%20Request%20Declined%20Three%20Times.md),
  is uninterpreted: the ladder starts there, unclimbed.
