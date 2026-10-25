---
type: tour
---

# The Goldcrust tour — one day, one loaf, one decision

This folder describes a small bakery the way DWSD describes any organization: **one
Markdown file per thing** — people, teams, meetings, agreements, boards. You don't need
to know Flight Levels, YAML, or anything else to take this tour. Seven stops, about ten
minutes. At each stop: open the linked file, read it, come back.

> This page is a guide, not part of the organization — it carries no `type:` and is
> skipped by the parser, like a visitor walking through the bakery.

## Stop 1 — A person

Open [Mara Holt](individuals/Mara%20Holt.md). Three lines: the owner, still bakes most
mornings, reports to no one.

**Watch for:** the file has two layers. The block at the top (the *frontmatter*) holds
her connections to everything else; the text below it is written for you. That split is
the whole trick — and it repeats in every file here.

## Stop 2 — A domain, written down

Open [Bakehouse](work-systems/Bakehouse.md). The production team, described as a domain:
what it's for, who it serves, what it depends on, what keeps it up at night (sourdough
runs on a 24-hour lead).

**Watch for:** knowledge that usually lives in one person's head. Here it's written
down — so it survives vacations, hand-overs, and growth.

## Stop 3 — A meeting that knows why it exists

Open [Daily Production Sync](interactions/Daily%20Production%20Sync.md). Fifteen minutes
at 13:30, every day. Four questions: *why are we doing this meeting, what is the outcome,
what decisions are we making and who makes them, what information do we need.*

**Watch for:** the four questions — you could hang them over any meeting in your own
company tomorrow. And notice who runs it:
[Bakery Operations](work-systems/Bakery%20Operations.md) — the coordination between
bakehouse and shops is *work of its own* here, with a name, a purpose, and metrics,
instead of living in the owner's phone. (The table at the bottom of the sync is the
machine layer — skip it for now; stop 6 shows what it's for.)

## Stop 4 — From observation to decision

Sourdough sells out before 9am. Follow the thread, one small file per rung:

1. [Sourdough Sold Out Before 9am](signals/Sourdough%20Sold%20Out%20Before%209am.md) — the raw observation, one sentence.
2. [Market Street Morning Sourdough Shortfall](insights/Market%20Street%20Morning%20Sourdough%20Shortfall.md) — what it means.
3. [Dependable Morning Sourdough](drivers/Dependable%20Morning%20Sourdough.md) — the need behind it.
4. [Prioritize Morning Sourdough](proposals/Prioritize%20Morning%20Sourdough.md) — the proposal, consented.

**Watch for:** each rung points back at the one below it. Months later, anyone can trace
*why* the bakery changed — from decision all the way down to the observation.

A decision about how the organization itself works can earn one more file: an organizational decision record, which keeps the context, what was decided, and what the bakery expects to follow from it. The bakery keeps one from a different thread, [Single Daily Production Sync](decision-records/Single%20Daily%20Production%20Sync.md) — why the shops and the Bakehouse now coordinate in one daily afternoon sync. The type page says when a proposal earns one.

## Stop 5 — The decision, made operational

Open [Morning Sourdough Replenishment](agreements/Morning%20Sourdough%20Replenishment.md).
The consented proposal became a working agreement: who does what, how we know it's
working — and a `review_date`.

**Watch for:** the review date. The change isn't carved in stone; it comes back to the
table. That's how this format handles organizational change: small, written, revisited.

## Stop 6 — Seeing the work

Open [Bakehouse Production Board](visualizations/Bakehouse%20Production%20Board.md). The
Bakehouse's day as a board, order to dispatch. On the website it renders as an actual
board; the file itself is the recipe for it — roughly:

```
Backlog | Mise-en-Place | Mixing-Proofing [3] | Baking | Cooling | Ready-for-Dispatch
```

**Watch for:** the `[3]` on Mixing-Proofing. The agreement
[Mixing-Proofing WIP Limit](agreements/Mixing-Proofing%20WIP%20Limit.md) anchors to that
same column — one rule, two views: prose for humans, a position on the board for the
work. This is the machine layer from stop 3 paying off: files can point at *places on a
board*, and the board points back.

## Stop 7 — The structure behind the flow

Stops 2 to 6 were about the *work* — domains, meetings, boards. This stop is about the
*structure*: who reports to whom, and which unit sits inside which. Neither is written
down anywhere as a chart. Both are **inferred** from the files you have already seen —
the `reports-to` line in each person's file, the `member-of` line in each unit's.

The org chart of the fourteen people — one fence, and the only thing it says is where to
look:

```dwsd.orgchart id=orgchart
mode: infer
around: "[[Mara Holt]]"
radius: { up: 0, down: inf }
```

Mara at the top, [Jonas Keller](individuals/Jonas%20Keller.md) running operations under
her, and one box named `NA1` — an open position (the Delivery Coordinator), kept in the
chart as a person with no name yet so the reporting line and the seat stay visible. The
same chart lives as a standalone file, [Goldcrust Org Chart.dwsd-orgchart](Goldcrust%20Org%20Chart.dwsd-orgchart).

The units, cut by site:

```dwsd.units id=units
mode: infer
layout: nested
around: "[[Goldcrust Bakery]]"
radius: { up: 0, down: inf }
```

[Goldcrust Bakery](units/Goldcrust%20Bakery.md) ⊃ three sites:
[Mill Lane](units/Mill%20Lane.md), where the bread is made and the two plain teams
[Deliveries](units/Deliveries.md) and [Wholesale](units/Wholesale.md) sit, and the two shops,
[Market Street](units/Market%20Street.md) and [Station Road](units/Station%20Road.md). Each
box wears its `unit-type` as a chip — `company`, `site`, `team`. Standalone:
[Goldcrust Units.dwsd-units](Goldcrust%20Units.dwsd-units).

What is *not* in the tree: the five work systems. They carry no `member-of`, because the
flight-level map of stop 2 already draws them, by how the work flows. Units are another
cut of the same organization — here by place; elsewhere it might be departments or
disciplines — and a unit tree that only redraws the topology adds nothing. People belong
to both: [Lena Frei](individuals/Lena%20Frei.md) is `member-of` both the Market Street site
and the Market Street Shop work system.

The boxes are annotated, and the annotations come from the same files as everything
else. A signal that names a person — [Dispatch Mornings Double-Booked](signals/Dispatch%20Mornings%20Double-Booked.md)
`observes: "[[Jonas Keller]]"` — pins on Jonas's box; the insight that follows it does
too. A decision *about* Jonas is not anchored on him but through his role:
[Jonas Keller Leads Operations](decision-records/Jonas%20Keller%20Leads%20Operations.md)
carries `for-domain: "[[Head of Operations]]"`, and the record reaches the box of whoever
keeps that role — open it and the drawer says "via Head of Operations". The same bridge
puts the [Shop Manager Mandate](agreements/Shop%20Manager%20Mandate.md) on both shop
managers, because its `for-domain` lists both shop-manager roles. On the units side the
[Wholesale Capacity Cap](agreements/Wholesale%20Capacity%20Cap.md) names the
[Wholesale](units/Wholesale.md) team with a bare wikilink and shows on that box; the
[Demand Forecast Assistant](ai-agents/Demand%20Forecast%20Assistant.md) names the
[Bakehouse](work-systems/Bakehouse.md), a work system, so its marker appears on the
Bakehouse node in the flight-level map rather than in this tree. The little
chips — `founder`, `new-role`, `pilot`, `core` — are the `tags:` line of each entity's
frontmatter. One rule behind all of it: a bare wikilink means that entity, wherever it is
drawn.

**Watch for:** neither fence lists a person or a unit. Each names one entity — the root to
start from (`around`) — and says how far to go (`radius: { up: 0, down: inf }`: nothing
above it, everything below it). That scope is what keeps the picture to *this*
organization when the renderer's index spans a whole workspace — this repository holds a
second example org, and without it both roots would appear side by side. The dashed ring
around the outer box marks the entity the picture is drawn around. (The two standalone files each add one `notes:` entry — a note written on a box, and even that
names its box with a bare wikilink.) Rename a file, move someone's `reports-to`, and both
pictures follow. Structure and flow are two views over the same files — the flight-level
map in the [README](README.md) is the third.

## Now you — your first three files

Grab three skeletons from the DWSD templates and describe your own
organization for fifteen minutes:

1. **Yourself** — an `individual`, five lines.
2. **Your team** — a `unit`, with a one-paragraph purpose.
3. **Your Monday meeting** — a `meeting`, answering the four questions from stop 3.

That's it. You've started.

## Where to next

- The bakery's whole day at a glance: [operating-rhythm.mw](operating-rhythm.mw)
- How work travels between the flight levels:
  [Daily Replenishment Flow](flight-routes/Daily%20Replenishment%20Flow.md) — and three
  more routes, each a different pattern. (Flight levels are **altitudes on the work, not
  ranks** — the same fourteen people fly all three.)
  Each route names the domain responsible for it with `for-domain` — a renderer shows it
  as a chip next to the route's title.
- An open thread no one has interpreted yet:
  [Two Wholesale Enquiries Waiting at the Cap](signals/Two%20Wholesale%20Enquiries%20Waiting%20at%20the%20Cap.md)
  — the ladder from stop 4 starts here, unclimbed. What would you do?
- The rules behind it all: the DWSD conventions and the
  type pages
