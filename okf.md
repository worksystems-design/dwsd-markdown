# OKF compatibility

DWSD is conformant with the **Open Knowledge Format (OKF)** — the open specification
Google Cloud published in June 2026 for representing knowledge as a folder of Markdown
files. DWSD is an **organizational profile** of that format: OKF gives the substrate,
DWSD supplies the vocabulary for describing organizations.

## Shared ancestry

OKF, [`agents.md`](https://agents.md/), and DWSD descend from the same idea — Andrej
Karpathy's LLM-wiki sketch: a folder of plain Markdown files, one file per concept, that
both people and AI agents can read directly. OKF formalizes the substrate; DWSD specializes
it for organizations.

## Conformance

OKF v0.1 defines three requirements for a conformant bundle. DWSD meets all three by
construction:

| OKF requirement | DWSD |
|---|---|
| Every non-reserved `.md` file has a parseable YAML frontmatter block | Every entity is one `.md` file with frontmatter — see [`conventions.md`](conventions.md) |
| Every frontmatter block has a non-empty `type` field | `type:` is DWSD's core discriminator — required on every entity |
| Reserved filenames (`index.md`, `log.md`) follow their structure when present | DWSD uses neither, so the requirement is satisfied vacuously |

An OKF consumer can therefore read a DWSD org folder as a valid OKF bundle: each entity is
an OKF *concept*, its file path is the concept identity, and the `type` field carries over
unchanged.

## DWSD as an OKF profile

OKF is deliberately minimal — only `type` is required, and producers define the rest. DWSD
fills that open space with an organizational vocabulary:

- a fixed set of entity **types** (`individual`, `role`, `work-system`, `flight-route`, …)
  grouped into three categories — structure, flow, change;
- **relationship** conventions (`reports-to`, `member-of`, `contributes-to`, …) expressed
  as `[[wikilinks]]` in the frontmatter;
- per-type **frontmatter** and **body** schemas (one spec page per type).

Where OKF's own reference examples profile the format for data assets (BigQuery tables,
datasets, metrics), DWSD profiles it for organizations.

## Field mapping

OKF *recommends* — but never requires — five frontmatter fields beyond `type`. DWSD's
equivalents:

| OKF field | DWSD |
|---|---|
| `type` | `type` — same field, required (e.g. `work-system`) |
| `title` | the **filename** is the label (`Head Baker.md`); no separate field |
| `description` | the Markdown body (often a `## Purpose` or intro line) |
| `resource` | the `sources:` block for discovered/synced entities; otherwise omitted |
| `tags` | not used by default |
| `timestamp` | the `updated_at` / `created_at` tracking fields |

Every one of these is OKF-optional, so the differences cost nothing for conformance. A
consumer that wants OKF's canonical field names can map them; DWSD does not duplicate them.

## Two honest differences

DWSD is a **superset** of the OKF baseline, not a reduction of it. Two places carry more
than a generic OKF reader will interpret:

1. **Relationships live in frontmatter, not body links.** OKF builds its knowledge graph
   from Markdown links in the *body*; DWSD's typed relationships are `[[wikilinks]]` in the
   *frontmatter*. OKF requires consumers to preserve unknown frontmatter keys, so a generic
   reader keeps DWSD's relationships intact but does not read them as edges — a DWSD-aware
   tool does. Conformance is unaffected: OKF never requires body links.

2. **Documentation files.** A few files in an org folder are not entities (for example an
   `examples/.../README.md`). OKF would have these either carry `type` frontmatter or use
   the reserved `index.md` name; DWSD currently skips frontmatter-less files as
   non-entities. Aligning them to OKF's `index.md` convention is a planned, low-cost
   refinement.

## Why it matters

Two independent efforts — one inside Google Cloud, one here — converged on the same
foundation: an organization, or any body of knowledge, is best described as a folder of
plain Markdown that humans and agents read alike. OKF validates the substrate; DWSD shows
what it looks like for the hardest domain to make legible — how an organization actually
works.

## References

- OKF specification and reference implementations —
  [GoogleCloudPlatform/knowledge-catalog/okf](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
- [`conventions.md`](conventions.md) — the DWSD rules that satisfy OKF's requirements
