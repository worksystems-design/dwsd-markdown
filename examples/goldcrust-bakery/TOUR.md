# The Goldcrust tour — one day, one loaf, one decision

This folder describes a small bakery the way DWSD describes any organization: **one
Markdown file per thing** — people, teams, meetings, agreements, boards. You don't need
to know Flight Levels, YAML, or anything else to take this tour. Six stops, about ten
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

## Now you — your first three files

Grab three skeletons from [`templates/`](../../templates/) and describe your own
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
  ranks** — the same eight people fly all three.)
- An open thread no one has interpreted yet:
  [Two Wholesale Enquiries Waiting at the Cap](signals/Two%20Wholesale%20Enquiries%20Waiting%20at%20the%20Cap.md)
  — the ladder from stop 4 starts here, unclimbed. What would you do?
- The rules behind it all: [conventions](../../conventions.md) and the
  [type index](../../README.md#types)
