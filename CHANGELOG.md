# Changelog — model & convention decisions

Notable changes to the DWSD model and its Markdown conventions, recorded **from the first
commit onward**. The current model is described by the reference itself — `README.md`,
`conventions.md`, and the pages under `types/`; this log tracks how it changes over time.

## 2026-10-12

- **Agreements and interactions on flight routes; interactions without a schedule.** Both
  examples now anchor agreements on route stages, not only on board positions (Goldcrust:
  Station Road Early Dispatch, Wholesale Capacity Cap; Voltfeld: Expedite Lane Policy, Ramp
  Readiness Review). Each gains an event-triggered interaction with no `rrule` and no `.mw`
  sibling — the Sell-Out Call and the Safety Issue Call — whose `## Trigger` section names
  the event and whose route-stage anchor names the place. `types/interaction.md` notes that
  an interaction may be triggered rather than scheduled; it and `types/agreement.md` now
  mention the route-stage locator. No new field.

## 2026-10-11

- **Voltfeld: an order process with a factory and a studio.** A new FL2 work system,
  Order to Delivery, owns the Customer Order Route. Two bands without a flight level stand
  for two work modes: `ERP` (factory — the stages run by the system of record, which the
  route's `sources:` block points at, bound to no board) and `Studio` (studio — the orders
  that need people, on the Order Studio Board). The edge into the studio is an andon (the
  Order Andon agreement), the edge back carries a reason code, and the monthly Order
  Exceptions Review turns the codes into a signal that meets the train's own unclimbed
  variant signal. One new person, an agent bound to the factory stage, a daily huddle. No
  new type and no new field: transactional processes are described with what the model
  already has.

- **Voltfeld's flight-level map shows the whole company.** The README topology now starts at
  the Portfolio (`focus: "[[Portfolio]]"`, `radius: { up: 0, down: inf }`) instead of the
  train, so Manufacturing appears where the example's point is: contributing straight to
  FL3, beside the train, not inside it.
- **One person, two roles, two contexts.** The decision record "Production Joins the
  Train's Planning" now also produces a role, the Production Liaison (`derived-from` the
  record, `for-domain` the Charger ART), kept by the Manufacturing Lead's keeper. Each role
  carries its own agreement through `for-domain`: the long-lead commitment lands on the
  Liaison, the ramp-readiness review on the Manufacturing Lead. It is the inverse of the
  shared Business Owner role (one role, four people). A role may carry `derived-from` like
  any entity; nothing in the spec changes.
- **Product lines on FL2, teams that are not work systems.** Voltfeld's Wallbox, DC Charger
  and Connectivity become FL2 product lines (`unit-type: [product-line, work-system]`),
  `member-of` and `contributes-to` the Charger ART on the same level: the train coordinates
  across them, each coordinates two teams of its own. The six teams are plain
  `unit-type: team` units with `member-of` and `contributes-to` the product line — no
  flightlevel, no board; `contributes-to` on a plain unit was always allowed
  (`types/unit.md`). The platforms now feed the product lines from FL1 upward. The Wallbox
  Team Board becomes the FL2 Wallbox Board with one lane per team and an expedite lane;
  the Feature and Field Issue routes gain a `Product Lines` band and bind it there, using
  the lane × column cell form (`lane:Wallbox Home/col:In Progress`). Six new people.
- **Goldcrust's units are cut by site, not by flow.** The unit tree used to nest the work
  systems the way `contributes-to` already does (Strategy ⊃ Operations ⊃ Bakehouse and
  shops), so the units view only redrew the topology. Now the company holds three
  `unit-type: site` units — Mill Lane (bakehouse, office, van yard; home of the plain teams
  Deliveries and Wholesale), Market Street and Station Road — and the five work systems
  carry no `member-of`. People are `member-of` their site and their work system (a list).
  `conventions.md` (Structure vs. flow) now says it outright: the unit tree need not mirror
  the topology; cut it by the dimension the organization actually groups by.
- **Board groups documented on the spec page.** `types/visualization.md` now lists the
  group fields (`name`, `columns` / `lanes` / `groups`, `agreements`, `interactions`,
  `tags`, `status-category`), the three-deep limit, what `groups:` means at board, lane
  and group scope, and how locators reach into a group (flattened column-only groups vs.
  lane-hosting groups, and the lane × column cell). No change to the DSL itself.
- **`org-validate` follows the spec.** The skill no longer warns on what the spec allows:
  an agreement `derived-from` a proposal (no ODR in between) and an ODR without
  `derived-from` are informational; a bare unit or person anchor in `interaction-of` /
  `agreement-of` is valid; `for-domain` may name a role (warn only on a person or plain
  unit); a board whose work system differs from `for-domain` is a note, never a warning.
- **Plugin `dwsd-md` 0.5.0.**

## 2026-10-10

- **A second worked example: Voltfeld.** A fictional EV-charging hardware maker that has
  borrowed parts of SAFe — one Agile Release Train on a ten-week PI, a Release Train Engineer,
  Product Management, Business Owners — without adopting the framework. About 110 files, every
  type at least once, with its own `TOUR.md`. Where Goldcrust is small enough that the line and
  the work almost coincide, Voltfeld is the example where they **do not**: engineers report into
  two line departments (`reports-to`) and work in six cross-functional ART teams (`member-of`),
  so the org chart and the units view draw two different trees from the same files.
- **`contributes-to` as a list, lateral at FL1.** Two platform work systems (HW Base, Firmware
  Platform) feed two and three teams respectively — the first example of a work system
  contributing to more than one, and the first where `member-of` and `contributes-to`
  disagree: Manufacturing belongs to Operations and contributes straight to the FL3 Portfolio.
  Development and production share no FL2 — the as-is the example's change ladder addresses
  (two signals → insight → driver → proposal → ODR → two agreements, dated October 2026 and in
  force from the next PI, so the as-is pictures stay true today).
- **Agents at sub-process level.** An `ai-agent`'s `bound-to` may name a **column group**
  (`[[Board]]#Board/group:Verification::in`, `…/lane:Feature/group:Release::in`) or the
  `::before` slot of a column. The locator grammar always allowed it; the example now exercises
  it, and the pattern it shows is: the agent prepares, the people decide.
- **The org-chart and units views are documented.** ` ```dwsd.orgchart ` (individuals over
  `reports-to`) and ` ```dwsd.units ` (units over their first `member-of`, `layout: nested |
  tree`) join the topology as the **three inferred views** in `conventions.md` — five fences in
  total — together with the standalone file forms (`.dwsd-topology`, `.dwsd-orgchart`,
  `.dwsd-units`), which are pictures, not entities. Goldcrust had used both since September
  (its tour's seventh stop) without the spec naming them. ⚠ Preliminary, like the topology.
- **A role as `for-domain` on an organizational agreement, exercised.** Voltfeld's Platform
  Variant Rule names the System Architect role alongside two work systems, so it lands on the
  keeper's box in the org chart — the Goldcrust Shop Manager Mandate pattern, now on an
  `organizational` agreement anchored on entities rather than a board.
- **Plugin skills caught up.** `dwsd-format` lists all five fences and the full ladder
  (signal → insight → driver → proposal → ODR → agreement); `explore-example-org` knows two
  examples.
- **`for-domain` on flight routes.** A route names the **domain responsible** for it — the
  work system or role that has to take care when the route changes — with `for-domain:`, a
  key inside the ` ```dwsd.flightroute ` block next to `for:` and `bound-to:` (a quoted
  wikilink or a list of them). It is responsibility, not flow: the work systems a route flows
  through stay **derived** (`bound-to` → board → `visualization-of`) and are never authored on
  the route. An unresolved target is a warning, never an error. `for:` is unchanged.
- **Stage item types resolve to entities.** A stage's item-type token resolves to a
  `flight-item-type` entity of that name — the exact name first, otherwise a case-insensitive
  match when exactly one entity matches. A resolved stage is a reference a renderer can make
  navigable; an unresolved one stays a local token, never an error, so a route stays
  authorable without any org model. Edge item-type references (`-[action: @item]->`) stay
  retired.
- The `org-validate` and `dwsd-format` skills and the flight-route template follow:
  `for-domain:` joins the closed route key set, and the validator checks it names a work
  system or a role.

- **Every person and unit page carries its own cut-out.** All 44 individuals of both examples
  end with a ` ```dwsd.orgchart ` fence (`mode: infer`, `focus: self`, `radius: { up: 1,
  down: 1 }`), all 25 units and work systems with a ` ```dwsd.units ` fence (`focus: self`,
  `radius: { up: 1, down: inf }`) — on work systems as a second block in the existing
  "In context" section, elsewhere in a new trailing one. `focus: self` is the page itself, so
  the fence is identical on every page and the picture follows the frontmatter. The Goldcrust
  tour's fourth stop now introduces the organizational decision record with the bakery's one
  existing record.
- **Plugin `dwsd-md` 0.3.0** — for-domain on routes, the cut-outs, the tour changes.

## 2026-07-28

- **`design-record` → `organizational-decision-record`.** The type is a *Decision* Record, not
  a Design Record: the ADR lineage it is named after is *Architecture **Decision** Record*, and
  its body section is `## Decision`. "Design" names the **phase** a decision is usually taken
  in, and letting one word carry both the phase and the artifact was the source of the drift —
  the same artifact was shipping under five different names downstream. The `organizational`
  qualifier is kept deliberately: it is a **threshold**, not decoration. Plenty gets decided
  about a product or a team's practice; none of that is an ODR. Folder convention in the
  examples follows as `decision-records/`.
- **The `navigation` category is folded into `change`.** All five types — `signal`, `insight`,
  `driver`, `proposal`, `organizational-decision-record` — are one category: working *on* the
  system. Four conceptual categories become three. The category **spans two phases** of change
  work, the middle two of MADE (Map · **Assess** · **Design** · Elevate): Assess =
  signal/insight/driver, Design = proposal/ODR. **Map** is the topology itself; **Elevate** is
  deliberately not modeled here — moving from as-is toward to-be is facilitation work
  (experiments, guides, katas), a practice artifact rather than a record.
- **The phases are for thinking, not for filtering.** What matters while working is whether
  something is still **in flux** (signal → proposal) or **decided** (the ODR, and the agreements
  that follow). That cut runs *across* the phase cut on purpose — `proposal` is Design by phase
  but still in flux by status.
- **`derived-from` is documented once, as a shared key.** It says what an entity **emerged
  from** and may sit on any entity; it was previously described per type, which is exactly why
  the type that needed it most kept missing it downstream. Its most load-bearing use: an
  `agreement` names the ODR it operationalizes, which makes a decision's **bundle** expressible
  as the reverse reading of the key — no bundle field needed — and answers *why does this rule
  apply?* long after the people who agreed it have moved on. It stays **metadata only**: no
  relationship type, no typed edge; readable backwards in the document, walkable forwards only
  via a reverse index.

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
