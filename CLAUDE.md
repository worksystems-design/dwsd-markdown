# CLAUDE.md — working on dwsd-markdown

This repository is the **DWSD reference** — a Markdown spec for describing an
organization as a folder of Markdown files. It is a **public** repo, written for both
**humans and AI agents**.

## Hard rules

- **Public repo — keep everything publishable.** No secrets, no internal or customer
  project names. **DWSD** = *Dynamic Work Systems Design*.
- **English (US) only.** Translations, if ever, are a deliberate future restructuring —
  not a parallel tree maintained now.
- Inspirations (Sociocracy 3.0, Flight Levels, Ladder of Inference,
  Management 3.0, ADR/MADR) are cited as **inspiration, not dogma** — adapted, not copied.
- Keep it **crisp and technical**.

## Layout

- `README.md` — landing + type index.
- `conventions.md` — rules for every entity (authoritative).
- `types/<type>.md` — one spec page per type.
- `templates/<type>.md` — bare copy-paste skeletons (+ `meeting.mw` Markwhen sibling).
- `examples/<org>/` — worked example organizations (full instances; e.g. `goldcrust-bakery/`).
- `CHANGELOG.md` — model & convention decisions.
- `.claude-plugin/`, `skills/` — the **`dwsd-md`** Claude Code plugin: thin
  authoring + validation skills (`dwsd-format`, `org-validate`, `org-new`) that point back
  at the files above via `${CLAUDE_PLUGIN_ROOT}` (no duplication). Heavier tooling (parser,
  rendering, the change-accompaniment workflow) stays out of scope.

## The model (summary — `conventions.md` is authoritative)

- **One file = one entity.** The `type:` field decides the type, not the folder. Each type
  lives in a flat plural folder (`individuals/`, `signals/`, …).
- **Three conceptual categories — NOT folders:** `structure` (individual, role, unit,
  work-system, ai-agent), `flow` (interaction, meeting, agreement, flight-item-type,
  flight-route, visualization), `change` (signal, insight, driver, proposal,
  organizational-decision-record — these *look at* the org and decide about it). The change
  category spans two phases: **Assess** (signal/insight/driver) and **Design**
  (proposal/ODR).
- **Keys are kebab-case.** `flightlevel` is one word. Subtype/kind discriminators are
  named `<base>-type` (`visualization-type`, `unit-type`, `agreement-type`,
  `interaction-type`) and may hold a single token **or a YAML list** (e.g.
  `unit-type: [team, work-system]`).
- **Relationships are wikilinks** (`[[Target]]`). `reports-to` (individuals only) =
  structure; `member-of` (individuals + units) = flow. `derived-from` and `delegator` are
  **metadata** (no parser relationship type yet), not typed edges.
- **Ladder of Inference (through the change category):** signal → insight → driver →
  proposal → `organizational-decision-record` → agreement(s). The ODR (ADR-style) is the
  recorded decision; the agreements it produces carry on operationally and name it via
  `derived-from`, which makes a decision's bundle readable in reverse.
- **`unit`** is the base structural type; a unit whose `unit-type` includes `work-system`
  (and which carries a `flightlevel`) is a **work system**. A unit is any named grouping
  (team, R&D dept, SAFe ART, …), nestable.
- **`meeting`** is an `interaction` of `interaction-type: meeting`; it bundles a **list of
  interactions** (a meeting "container"), each with its outcome. Any interaction may
  optionally use the same four framing questions.
- **`sources`** is documented only in `conventions.md` — don't repeat it on type pages.
- **Out of scope:** the change-accompaniment *workflow* (facilitation, consent process) is
  an application concern, not this spec.

## Spec page shape (keep consistent)

Intro one-liner → `**Serialized type:**` → `## Frontmatter` table (Field / Required /
Format / Meaning) → `## Relationships` → `## Body` (often a section table) → `## Example`
(self-contained markdown) → `## Notes`. **No folder line** on pages — the folder/category
convention lives in `conventions.md`.

## Open / preliminary

- `ai-agent` is **preliminary** — a "surface" concept, still evolving; `bound-to` anchor
  convention to be revisited.
- `action` (the to-do that falls out of a design decision) — parked.
- "Concerns" means *attention areas* on `role` but *objections* on `agreement` — align or
  leave context-dependent (open).
- `organizational-decision-record` placement may still evolve.
- An interaction **board-related / supporting** classifier (and a pointer to a specific board
  column), plus a meeting **`participants`** field, are **deferred** — may emerge later.
