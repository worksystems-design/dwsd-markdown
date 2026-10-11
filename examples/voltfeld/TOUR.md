# The Voltfeld tour — one engineer, two trees, one missing edge

This folder describes a company that builds EV chargers the way DWSD describes any
organization: **one Markdown file per thing** — people, teams, boards, agreements. The
company runs its product development as an Agile Release Train, borrowing parts of SAFe
without adopting the framework; you do not need to know SAFe, Flight Levels, or YAML to take
this tour. Seven stops, about ten minutes. At each stop: open the linked file, read it, come
back. If this is your first DWSD example, take the [Goldcrust tour](../goldcrust-bakery/TOUR.md)
first — it is smaller, and this one builds on what it shows.

> This page is a guide, not part of the organization — it carries no `type:` and is skipped
> by the parser.

## Stop 1 — One engineer, two pictures

Open [Daria Novak](individuals/Daria%20Novak.md). Two lines matter: she **reports to**
[Kaspar Reinholt](individuals/Kaspar%20Reinholt.md), head of Hardware Engineering — and she is a
**member of** the [Wallbox](work-systems/Wallbox.md) team, inside the Charger ART.

Those two lines draw two different pictures. Her reporting line, two levels up:

```dwsd.orgchart
mode: infer
focus: "[[Daria Novak]]"
radius: { up: 2, down: 0 }
```

And the team she works in, inside the train:

```dwsd.units
mode: infer
focus: "[[Wallbox]]"
radius: { up: 1, down: 0 }
```

**Watch for:** nothing in either fence names a person or a team. Both pictures are read off
the files. In the first, Daria sits under a department; in the second, her team sits inside
the train and the department is not even in the frame. The whole company works like this —
open [Hardware Engineering](units/Hardware%20Engineering.md): a department with a head and a
reporting line, and nobody *working* in it. That is what an Agile Release Train does to a line
organization, and DWSD keeps both pictures without choosing one.

## Stop 2 — A platform that serves two

Open [HW Base](work-systems/HW%20Base.md). The power module, the control board, the enclosure
base — one hardware platform that both product lines are built on. Look at its frontmatter:
`contributes-to` is a **list** — [Wallbox](work-systems/Wallbox.md) *and*
[DC Charger](work-systems/DC%20Charger.md). The same for the
[Firmware Platform](work-systems/Firmware%20Platform.md), which serves three.

```dwsd.topology
mode: infer
focus: "[[HW Base]]"
radius: 1
```

**Watch for:** the edges run sideways. All three are FL1 teams; a platform does not sit
*above* the teams it serves, it sits *beside* them and feeds them. And read HW Base's *Key
Challenges*: two customers with different cadences, a mold that has to be ordered before the
design is finished. Keep that mold in mind — it comes back at stop 5.

## Stop 3 — The train's board

Open [Charger ART Board](visualizations/Charger%20ART%20Board.md). This is the FL2 board of the
train — ten weeks per Program Increment (`timebox: 10w`), two lanes. The `Feature` lane runs
through three **column groups**, `Preparation` → `In PI` → `Release`; the `Field Issue` lane is
an **expedite lane** for the one kind of work that cannot wait ten weeks.

**Watch for:** a group is a *sub-process* with a name — and names are what other files can
point at. The agreement [PI Commitment](agreements/PI%20Commitment.md) is anchored on the
whole `In PI` group (`agreement-of: …/lane:Feature/group:In PI::in`), not on a column. The
board also carries rules of its own, written inline on columns — "one hotfix in progress per
team". Two directions, one surface: the board reaches out, the files reach in.

## Stop 4 — A route that stops at the plant

Open [Feature Route](flight-routes/Feature%20Route.md). A feature travels from the train to a
team and back as stories; at the end of the PI the features bundle into a **release**, and the
release is copied to a third band, `Plant` — drawings, BOM and test firmware arrive at
[Manufacturing](work-systems/Manufacturing.md), who build the chargers that ship.

**Watch for:** read the `Plant` band twice. The release arrives (`-->`), the chargers leave
(`..> ()`) — and **no edge comes back**. Every other band has a dotted feedback line; the
plant has none. Now open the [Manufacturing Board](visualizations/Manufacturing%20Board.md):
nothing on the train's board points at it, nothing on it points back. And in the
[README](README.md)'s flight-level map, Manufacturing contributes straight up to the FL3
Portfolio: development and production have no shared FL2. Three files, one gap, drawn three
ways.

## Stop 5 — From two signals to a decision

Two things were observed, one sentence each:

1. [PI Objectives Missed on Enclosure Tooling Twice](signals/PI%20Objectives%20Missed%20on%20Enclosure%20Tooling%20Twice.md) —
   a mold takes fourteen weeks; a PI has ten.
2. [Fixtures Built After the Release](signals/Fixtures%20Built%20After%20the%20Release.md) —
   the plant started its ramp the day the release arrived.

Then the ladder, one small file per rung:

3. [Production Is Outside the Train's Horizon](insights/Production%20Is%20Outside%20the%20Train%27s%20Horizon.md) —
   what the two signals mean together.
4. [Long-Lead Work Needs a Longer Horizon Than the PI](drivers/Long-Lead%20Work%20Needs%20a%20Longer%20Horizon%20Than%20the%20PI.md) —
   the need behind it, and whose need it is.
5. [Bring the Plant and Supply Chain into PI Planning](proposals/Bring%20the%20Plant%20and%20Supply%20Chain%20into%20PI%20Planning.md) —
   the proposal, with the objections that were raised and how each was answered.
6. [Production Joins the Train's Planning](decision-records/Production%20Joins%20the%20Train%27s%20Planning.md) —
   the decision, recorded.

**Watch for:** two things in the decision record. It says what was **not** decided — no new
FL2, no restructuring of Operations; that question is parked for two PIs. And it is dated
2026-10-06 but in force from the next PI planning in December — which is why the pictures at
stop 4 are still true today. The organization has decided to change and has not yet changed.
DWSD can say both at once.

## Stop 6 — The decision, in two agreements and a role

Open [Long-Lead Commitment at PI Planning](agreements/Long-Lead%20Commitment%20at%20PI%20Planning.md)
and [Ramp Readiness Review](agreements/Ramp%20Readiness%20Review.md). Both carry
`derived-from: "[[Production Joins the Train's Planning]]"` — that one line is what makes the
decision's **bundle** readable: the agreements that belong to a decision are exactly the ones
that point back at it.

**Watch for:** where each is pinned. The decision sits at the *domains* (`for-domain`: the
train and the plant). The agreements sit *where the work happens*: on the `Preparation`
group of the train's board, `::before` the `Tooling Released` column of the HW Base board, on
the [Supply Chain](units/Supply%20Chain.md) team's box, on a column of the Manufacturing
board. One decision up at the system, its consequences down in the flow — and the second
agreement is, in route terms, the missing edge from stop 4 written down before it exists.

The decision also made a role: [Production Liaison](roles/Production%20Liaison.md), the
plant's seat in the train, again with `derived-from` the decision. It is kept by
[Bastian Lorenz](individuals/Bastian%20Lorenz.md), who already keeps the
[Manufacturing Lead](roles/Manufacturing%20Lead.md) role. **Watch for:** one person, two
roles, two contexts, and each role with its own agreement. The long-lead commitment names
the Liaison in its `for-domain` and lands on the train side of Bastian; the ramp review
names the Manufacturing Lead and lands on the plant side. It is the inverse of the
[Business Owner](roles/Business%20Owner.md) role, which one role shares across four people.

## Stop 7 — An agent that prepares, people who decide

Open [DFM Check Agent](ai-agents/DFM%20Check%20Agent.md). It is bound to the whole
`Verification` **column group** of the [HW Base Board](visualizations/HW%20Base%20Board.md):
every drawing that enters the group is checked against the plant's producibility rules, and
the agent drafts the findings list the [DFM Review](interactions/DFM%20Review.md) works from.
Then open [Field Issue Triage Agent](ai-agents/Field%20Issue%20Triage%20Agent.md): bound
`::before` the `Triage` column — the queue *in front of* the column, not the column.

**Watch for:** an AI agent in DWSD is a **surface** — a place in the flow where it appears —
and the locator says exactly where: a column, a group, the slot before one. Each agent here
is also anchored to a person or a team, so the same agent shows on a box in the org chart or
the units view. And in every case the pattern is the same: the agent prepares, the people in
the interaction decide.

## Now you — your first three files

Grab three skeletons from [`templates/`](../../templates/) and describe your own
organization for fifteen minutes:

1. **Your team** — a `unit`, with `member-of` pointing where its work goes and a
   one-paragraph purpose.
2. **The team you depend on** — another `unit`; add `contributes-to` from one to the other,
   and you have your first topology edge.
3. **The agreement between you** — an `agreement`, anchored on the board column where it
   bites.

That's it. You've started.

## Where to next

- The train's whole cadence at a glance: [operating-rhythm.mw](operating-rhythm.mw) — a PI
  from planning to inspect-and-adapt.
- The one flow that bypasses the cadence: the
  [Field Issue Route](flight-routes/Field%20Issue%20Route.md), starting in a band with no
  flight level and forking into hotfix or feature.
- An open thread no one has interpreted yet:
  [Variant Request Declined Three Times](signals/Variant%20Request%20Declined%20Three%20Times.md)
  — the [Platform Variant Rule](agreements/Platform%20Variant%20Rule.md) is doing what it was
  written to do, and a product team is quietly routing around it. The ladder from stop 5
  starts here, unclimbed. What would you do?
- The rules behind it all: [conventions](../../conventions.md) and the
  [type index](../../README.md#types).
