# Voltfeld — example organization

A fictional maker of EV charging hardware, described in DWSD: an AC **Wallbox** line and a
**DC Charger** line, developed by one Agile Release Train of six teams, built in a plant,
sold and serviced by a commercial department — about 120 people, of whom this folder models
the thirty that carry the structure. It is the second worked example next to the
[Goldcrust Bakery](../goldcrust-bakery/); where Goldcrust is small enough that the line and
the work almost coincide, Voltfeld is the example where they **do not**.

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
