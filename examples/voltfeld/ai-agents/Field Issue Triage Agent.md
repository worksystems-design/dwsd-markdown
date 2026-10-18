---
type: ai-agent
platform: internal-assistant
status: active
for-domain: "[[Connectivity]]"
bound-to:
  - "[[Charger ART Board]]#Charger ART/lane:Field Issue/col:Triage::before"
  - "[[Field Service]]"
description: Clusters incoming field reports and telemetry into candidate issues with a proposed severity and suspected subsystem, ahead of the weekly triage.
created_at: "2026-10-10"
---

The Field Issue Triage Agent works **before** the people do. Through the week it reads
service tickets from [[Field Service]] and the fleet telemetry [[Connectivity]] collects,
clusters them into candidate [[Field Issue]]s, and proposes a severity and a suspected
subsystem — power stage, firmware, backend. The [[Field Issue Triage]] on Tuesday starts
from that list and makes the call the [[Field Issue Route]] forks on: hotfix, or feature
for the next PI.

Since version 2.0 of the [[Expedite Lane Policy]] the agent also routes **known
patterns** — calls the triage has made the same way three times — straight to the owning
team's backlog, and reports them to the triage as one weekly count.

> [!NOTE]
> **Modeling note.** The agent is bound `::before` the `Triage` column of the expedite lane
> on the [[Charger ART Board]]. The `::before` slot is the point: the agent's surface is
> the queue *in front of* the column, not the column itself. The second anchor,
> [[Field Service]], is a plain team — the agent marker shows on its box in the units view.
>
> `ai-agent` is a preliminary type and the `bound-to` anchor convention may still change.
