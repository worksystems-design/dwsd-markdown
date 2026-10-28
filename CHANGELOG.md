# Changelog — model & convention decisions

Notable changes to the DWSD model and its Markdown conventions, recorded **from the first
commit onward**. The current model is described by the reference itself — `README.md`,
`conventions.md`, and the pages under `types/`; this log tracks how it changes over time.
An entry that changes the format names the new format version on a `Format: x.y.z` line
(`conventions.md` › Format versions).

## 2026-10-28

- **Example mandates carry review dates.** In the Goldcrust example each mandate file has
  `version`, `decision_date` and `review_date`, spread so that in early November 2026 one
  review is overdue (Shop Manager Mandate), one comes up soon and one is months away. The site's
  $1,000-a-day spending row on Market Street became its own file, Market Street Site
  Spend, because a new limit gets an early first review. No format change.
- **The README marks the organization's root.** A `README.md` with `dwsd-format` is where
  a tool stops when it looks for the organization a file belongs to, and wikilinks
  resolve within that folder. It keeps `type: readme`: the organization as an entity is
  its root unit, and a second "organization" outside the graph would be mistaken for it.
  No format change.
- **`dwsd-format` skill** no longer lists the keys that take a locator; it points to the
  field table in `conventions.md` and the type pages, so a new locator key (like
  `observes` in 1.3.0) needs no change there.
- **No path-form locator.** `conventions.md` still said a same-named person and unit both
  receive a bare link, with `[[individuals/Name]]` / `[[units/Name]]` to tell them apart.
  That predates unique labels (2026-10-17): two files with one key are an error, so the
  case cannot arise. A path form in an older file still resolves, by its last segment.

## 2026-10-27 (later)

Format: 1.3.0

- **`observes` may be a locator.** A signal or an insight may name, besides an entity, a
  place in the detail where it was seen: a board position or a route stage, in the same
  locator form as `interaction-of`. Driver, proposal and decision record keep
  `for-domain`. Goldcrust and Voltfeld each anchor two signals this way (a board column or
  lane, a route stage) and carry `"1.3.0"`.
- **`contracts/1.3.json`** is 1.2 with the new number; what changed is a value form, not
  a key the contract lists.
- **More mandates in the examples.** Mandates held directly by a person and by a plain
  team: in Goldcrust the Deliveries team and Pia Brandt, in Voltfeld Field Service and
  Keiko Tanaka. Voltfeld now has mandates, which its `"1.3.0"` covers.
- **A change trail around a unit or work system** starts from the change entities scoped
  to it: `for-domain` on a driver, proposal, decision record or agreement, `observes` on
  a signal or insight. A driver or proposal states a standpoint of its domain, not an
  observation at a place, so this is where it shows; an entity scoped to a role does not
  count. A reading rule for the view, no new key (the trail stays preliminary).

## 2026-10-27

Format: 1.2.0

- **Host files.** A host may keep files of its own in an org folder, in folders of its
  own and with any `type`. The contract now names each entity type's **model folders**
  (`folders`: `units` and `work-systems` for `unit`, `decision-records` for the decision
  record, …). Inside a model folder an unknown `type` is still reported as a likely
  typo; anywhere else such a file is a note, without a warning. The format lists no host
  types. New in `conventions.md` › Host files; `org-validate` follows it.
- **`contracts/1.2.json`** adds `folders` to every entity type and nothing else. A 1.1
  org stays valid unchanged; it gets the new rule once its README says `"1.2.0"`.

## 2026-10-26

Format: 1.1.0

- **Mandates, optional.** A mandate is what a holder must or may do; the holder is the
  file it is written in — an individual, a role, a unit or work system, and, preliminary,
  an AI agent. Mandates sit under `## Accountabilities` (must), `## Decision Rights` (may),
  a work system's `## Key Responsibilities` (must) or a general `## Mandates`, as a list,
  prose or a table `Name | Mandate of`. A row with a locator in `Mandate of` shows as a
  **mandate chip** where it points, as an interaction row does in a meeting's table. How
  free the holder is stands in the mandate's own words; there is no fixed scale, and John
  Cutler's Mandate Levels are named as an inspiration for one. A row has no identity of its
  own: a mandate that needs one becomes a file of the new type **`mandate`** (`for-domain`
  the holder, `delegator` who can change it, `mandate-of` where it hangs). Reading rule:
  an agreement is changed by its parties together, a mandate by its delegator alone. New
  section in `conventions.md`, `types/mandate.md`, `templates/mandate.md`, the mandate
  table in the role, individual, unit and work-system templates; `org-read` collects a
  person's mandates directly, through roles and through units; `org-validate` checks the
  tables and the files. Goldcrust: Ines Rossi, the Market Street Site Lead and the Market
  Street site; the Shop Manager Mandate and the Market Street Opening Hours become mandate
  files. Two authoring skills turn prose into rows: `extract-mandates` and
  `extract-interactions`. Goldcrust carries `"1.1.0"`, since it has mandate files;
  Voltfeld stays at `"1.0.0"` and is still correct.
- **`contracts/1.1.json`** adds the `mandate` type (an entity, no required key beyond
  `type`). A 1.0 org stays valid unchanged; a writer that adds a mandate file raises its
  README to `"1.1.0"` in the same commit.
- **MADE becomes D-MADE** (Define · Map · Assess · Design · Elevate). Define comes first:
  what you want to achieve or what bothers you, and who should have a say. No Change type
  belongs to it; Assess and Design keep their five types. Wording in `conventions.md` only,
  not part of the format.

## 2026-10-25

Format: 1.0.0

- **The format has a version of its own.** `dwsd-format` in an org's README now holds a
  semantic version, `"1.0.0"`, instead of a CHANGELOG date: a date says when the spec
  changed, not whether the change breaks existing files. Major: an existing file becomes
  incorrect, always with a migration. Minor: it only adds. Patch: a rule worded more
  precisely. The fence grammar counts, renderers do not. `conventions.md` › Format versions
  gives the steps with examples, and how tools handle them: readers tolerate, writers bring
  a file to the current form of its major and may raise the minor in the same commit, a
  major jump is offered as a proposal. **1.0.0 is the state of 2026-10-25**; `"2026-10-24"`
  and `"2026-10-25"` are its aliases, so nothing needs to migrate. `org-validate` checks the
  id, `org-new` writes the newest version. Both example orgs carry `"1.0.0"`.
- **`okf.md` follows OKF v0.2.** Conformance is stated against v0.2, the field mapping lists
  its four recommended fields, and a third difference names `status` and `sources`, which
  v0.2 defines differently. Each format version names its OKF version (1.0.0 → OKF 0.2), so
  an org declares no `okf_version` of its own. The OKF repository moved; the link follows.
- **The checkable part is data.** `contracts/1.0.json` lists the types (which are entities,
  which keys they require) and the one conditional rule (a work system needs a
  `flightlevel`), so tools stop copying the spec. Findings about the id share `format.*`
  codes across all tools; none is an error.
- **README and tour carry a `type` of their own.** The org's `README.md` gets `type:
  readme` next to `dwsd-format`, a `TOUR.md` gets `type: tour`. Neither is an entity type:
  DWSD reads both as notes, and no tool lists or counts them. They give each Markdown file
  in an org folder the non-empty `type` OKF asks for, which the README lost when it gained
  frontmatter and the tours never had. `org-validate` notes a README or tour without it;
  both example orgs carry it.

## 2026-10-24

- **An org folder names the spec state it is written to.** The root `README.md` may carry
  frontmatter with one key, `dwsd-format`, holding the date of a `CHANGELOG.md` entry
  (`dwsd-format: "2026-10-24"`). The README stays a note: no `type`, name and description
  still from the first heading and paragraph. The id moves with each migration commit, so
  it is where migration paths start; a reader that does not know it warns and reads on.
  The spec has no version number of its own, and the plugin version also moves when only
  the skills change, so neither serves as the id. `org-validate` reports the id and the
  entries since; `org-new` offers a README with it. Both example orgs carry it.
## 2026-10-23

- **Change trail fences may hold entries of their own.** `mode: mixed` lays `entries:` over
  the organization's trail, `mode: declared` draws only them (a sketch without an
  organization); `infer` stays the default. **Brackets point outward**: an item with a bare
  `name` is an **inline entry** — a change entity defined in the fence, carrying the
  frontmatter keys of its `type` in the file's own spelling (`type:`, not `stage:`; no
  `odr`); `"[[Name]]"` is a reference to the file. Inside the fence a bare link value
  (`derived-from: hh`) means an inline entry, a wikilink the file, and a file never holds a
  bare name. `delta: add | remove` is an annotation that lives only in the fence; a new
  inline entry needs none. The spec says "inline entry", not "draft" — a proposal's
  `status: draft` already means something else. Agreed with the DSL for its Phase 53.1.1.
  `org-validate` checks the new keys.

## 2026-10-20

- **`focus:` becomes `around:`** in all four inferred views — topology, org chart, units and
  change trail. Same values (a wikilink or `self`); `radius:` and `show:` are unchanged.
  `focus:` stays a valid alias, and when a fence carries both, `around:` wins. All example
  fences, the decision-record template, the type page and both skills use `around:`.
- **Anchors and around**, a new section in `conventions.md`, names the two ideas behind
  every picture: an anchor (`for-domain`, a locator, `observes`) says where an entity sits;
  `around:` says from where a view looks at the organization.

- **`for-domain` may name a unit.** A domain is a work system, a role or a unit — any named
  grouping that decides something for itself: a department, a site, a circle that governs
  without running a flow. `for-domain` still never names a person. An entity scoped to a
  plain unit shows on that unit's box in the units view. Changed in `conventions.md`, every
  type page that carries `for-domain`, and both skills (`org-validate` now warns only on a
  person). Goldcrust gains the role *Market Street Site Lead*, scoped to the Market Street
  site and kept by Ines Rossi.
- **Skills are host-neutral.** Each skill names its **spec root** once (the folder that
  holds `conventions.md`; `${CLAUDE_PLUGIN_ROOT}` in Claude Code) and says what to do in
  verbs rather than tool names, so another host can vendor a skill unchanged.
- **Reading an org.** A new skill, `org-read`, routes a question about an org to the right
  files and links. Every type page gains a `## Reading it` section: the question the entity
  answers, where to look first, which links and backlinks complete it, and which picture
  shows it. Small fixes on the way: the driver and agreement pages name a unit as a possible
  domain, the ODR note no longer calls the record the category's only member, and the
  signal example is in English.

## 2026-10-19

- **A decision record shows its own change trail.** `focus:` in a ` ```dwsd.change-trail `
  fence now also takes `self` — the entity whose file hosts the fence. A decision record
  carries one in an optional `## Change trail` section at the top of the body, before
  `## Context`: back to the signals it came from,
  forward to its agreements and where they land. Added to the type page, the template, and
  all four decision records in the example orgs; `org-validate` accepts `self`.
- **Goldcrust: both decision records have an origin.** Two short chains — signal, insight,
  driver, proposal — now lead to *Single Daily Production Sync* (separate shop calls) and
  to *Jonas Keller Leads Operations* (the owner as bottleneck of the day-to-day), so each
  record's change trail runs back to what was first seen.
- **What a decision produced, beyond agreements.** The role *Head of Operations* and the
  interaction *Daily Production Sync* now name the decision record they came from in
  `derived-from`, as Voltfeld's *Production Liaison* already does. `derived-from` was always
  open to every type; this makes the examples use it where a decision's result is a role or
  an interaction rather than an agreement.

## 2026-10-18

- **Voltfeld: a second change chain, from the field.** Two field signals ("not charging
  after the firmware update", the same pattern eleven times in September) → the insight that
  a known pattern is decided again every week → driver → proposal → decision record
  *Known Failure Patterns Skip the Weekly Triage* → version 2.0 of the Expedite Lane Policy,
  where the triage agent routes known patterns itself. A new monthly interaction, the
  *Failure Pattern Review*, is where the eleven-times signal came from. Two open ends sit
  beside it: a second insight on one firmware build, and a signal about a frozen cable lock
  that nobody has interpreted yet.

- **A fourth inferred view: the change trail.** ` ```dwsd.change-trail ` draws the change
  entities as one network — signal → insight → driver → proposal → decision record →
  agreement along `derived-from`, landing in the units and work systems an agreement names
  in `for-domain` or a bare `agreement-of`, with loop-backs where a signal or insight
  `observes` a decision or an agreement. Open ends show their next step. Keys `focus:`,
  `show:`, `radius:`; an empty body is the whole trail. No standalone file. Both example
  orgs carry one on their company unit; Goldcrust's dispatch insight now also observes the
  decision it questions. `org-validate` checks the keys.

## 2026-10-17

- **One graph: what a relationship is, what a meeting is, how a link finds its file.** Every
  wikilink in the frontmatter is a relationship; the keys in conventions › Relationship
  fields carry a meaning, any other key (`derived-from`, `delegator`, `decision-makers`, an
  author's own) is a plain link named by its key, with no marker. A meeting is an
  interaction whose `interaction-type` holds `meeting` (single or list, any case);
  `type: meeting` is an old spelling and warns. A wikilink — frontmatter or body — matches
  a file by label: NFC, plain lowercase, nothing dropped or transliterated (`café` finds
  `Café`, `STRASSE` does not find `Straße`); the slug is never used to match. Two labels with
  the same key are an error. Files without `type:` are notes: links may reach them, but they
  are not part of the graph. `org-validate` follows.

- **The org's README names the organization.** The first `#` heading of `README.md` at the
  org root serves as the organization's name, its first paragraph as its description — for
  lack of anything better, and without a new key. The README stays a non-entity; nothing
  else in it is read.

- **Fences may carry an id.** Any of the five DSL fences may name itself in the info
  string after its tag: ` ```dwsd.board id=intake `. The id is kebab-case, unquoted and
  unique within the file, and it stays put when the title or the enclosing heading
  changes, so marks and addresses that point at a diagram survive edits that insert, move
  or remove other diagrams on the page. Optional; tools that create a fence should assign
  one. Readers recognize a fence by its tag alone. `org-validate` flags duplicate ids in a
  file and warns on a malformed one. Every fence in the Goldcrust and Voltfeld examples carries one —
  the title as a slug for boards and routes (`id=epic-route`), the tag for the inferred
  views (`id=orgchart`).

## 2026-10-14

- **Route item types: text or wikilink, never matched by name.** A stage's item type and a
  route's `for:` are either plain text — a description local to the route, never looked
  up, never flagged — or a wikilink, a real connection to a flight-item-type file that
  resolves or is a broken link. The old lookup (`epic` finds `Epic.md`, exact name first,
  then case-insensitive) is gone. Lines holding a wikilink are quoted; aliases
  (`[[Customer Order|order]]`) keep a short label. A linked stage is named by its link
  target in locators and `bound-to` keys (`stage:Feature @ Train`, `Feature:`), so
  switching `feature` to `[[Feature]]` changes those spellings. Voltfeld's `epic` and
  `feature` stages — the only ones with item-type files — are now wikilinks; every other
  stage in both examples stays text. `org-validate` checks wikilink stages and `for:`,
  quoting, and stages in one band that differ only by case or link-vs-text.

- **`team` becomes the second reserved `unit-type` value.** Like `work-system`, it is
  English in the data and matched without regard to case. It marks a stable group of
  people who work together; its members are the individuals whose `member-of` names it,
  and a view may show their number as the team's size (the modeled members, not
  necessarily the headcount). It combines with `work-system` or stands alone. No example
  data changes: both examples already use `team` this way. `org-validate` notes a team
  without members.

- **Reading guide: interactions from meeting tables.** A new `conventions.md` section says
  how existing structure is read. First entry: there is no locator for a table row; an
  interaction in a meeting table that gains weight moves into its own file and is named in
  the row's `Name` column with `[[…]]`. The file is the source for outcome and anchor;
  filled cells are copies, the file wins, a validator reports differences. Same for
  `## Agreements`. `types/meeting.md` allows `[[…]]` in the table form.
- **Skills follow the board-locator rules of the shared host data layer.** `dwsd-format`:
  a locator without `#BoardName` lands on a titled board; `#BoardName::in` is the whole
  board; a bare `[[Board]]::in` is an entity anchor. `org-validate`: three miss reasons
  (`document-not-indexed`, `board-not-found`, `unit-not-found`) and the meeting-table copy
  check.

## 2026-10-12

- **org-validate names the retired route keys.** `fl-path:`, `fl-triggers:`, `fl-bands:`
  and `flow:` in a route fence are flagged as retired forms, matching renderers that now
  reject them.
- **`unit-type`: one reserved value, the rest is description.** `work-system` is the only
  value with meaning in the model; it stays English in the data, matches without regard to
  case, and a view may label it in any language. Every other value is descriptive — the
  author's words and language, shown exactly as written, never interpreted. Voltfeld's
  Charger ART now reads `unit-type: [ART, work-system]`. More values may become reserved
  later, by a spec change, once the model gives them a meaning.
- **Modeling notes go at the end of the file.** 36 notes that sat mid-body (before
  `## Evaluation Criteria`, `## Consequences`, `## Concerns`, `## Key Responsibilities` or
  `## In context`) moved to the end; none explained a single passage. conventions.md says
  so, with the exception for a note that only makes sense next to its passage.
- **Agreements and interactions on flight routes; interactions without a schedule.** Both
  examples now anchor agreements on route stages, not only on board positions (Goldcrust:
  Station Road Early Dispatch, Wholesale Capacity Cap; Voltfeld: Expedite Lane Policy, Ramp
  Readiness Review). Each gains an event-triggered interaction with no `rrule` and no `.mw`
  sibling — the Sell-Out Call and the Safety Issue Call — whose `## Trigger` section names
  the event and whose route-stage anchor names the place. `types/interaction.md` notes that
  an interaction may be triggered rather than scheduled; it and `types/agreement.md` now
  mention the route-stage locator. No new field.
- **Modeling notes as callouts.** Entity bodies tell the organization's story; text that
  explains how an entity is modeled (anchors, locators, fields set or left out) now sits in
  one `> [!NOTE]` callout headed `**Modeling note.**` at the end of the body.
  `conventions.md` gains the rule; both examples mark their modeling explanations this way.

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
