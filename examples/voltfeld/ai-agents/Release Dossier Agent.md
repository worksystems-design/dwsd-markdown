---
type: ai-agent
platform: internal-assistant
status: active
for-domain: "[[System Integration]]"
bound-to:
  - "[[Charger ART Board]]#Charger ART/lane:Feature/group:Release::in"
  - "[[Marek Novotny]]"
description: Compiles release notes, the certification evidence index and the production hand-over package from the PI's released features.
created_at: "2026-10-10"
---

The Release Dossier Agent works the `Release` group of the [[Charger ART Board]] — the
sub-process from `Demoed` through `Certified` to `Released`. As features move through the
group it assembles what the release has to carry with it: release notes for
[[Field Service]] and the operators, the index of certification evidence [[Marek Novotny]]
files with the test house, and the hand-over package [[Manufacturing]] receives —
drawings, BOM, production test firmware from [[System Integration]]. [[Marek Novotny]]
owns the dossier; the agent drafts it.

> [!NOTE]
> **Modeling note.** The agent is bound to the `Release` **column group**, a group inside a
> lane: `#Charger ART/lane:Feature/group:Release::in` — the locator path drills lane →
> group, and the agent marker sits on the group bar.
>
> `ai-agent` is a preliminary type and the `bound-to` anchor convention may still change.
