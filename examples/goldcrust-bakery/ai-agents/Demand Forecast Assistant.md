---
type: ai-agent
platform: internal-assistant
status: active
for-domain: "[[Bakehouse]]"
bound-to:
  - "[[Bakehouse Production Board]]#Bakehouse Production/col:Backlog::in"
  - "[[Mara Holt]]"
  - "[[Bakehouse]]"
description: Suggests next-day quantities from recent sell-through and weather.
created_at: "2026-05-24"
---

A preliminary AI-agent surface. The Demand Forecast Assistant proposes next-day quantities
into the Backlog of the [[Bakehouse Production Board]], drawing on recent sell-through and
the weather forecast. The [[Head Baker]] reviews and adjusts before the plan is confirmed
at the [[Daily Production Sync]].

`bound-to` is a list: the board column where the suggestions appear, the person who
reviews them ([[Mara Holt]] — the agent shows on her box in the org chart), and the
[[Bakehouse]] itself — a team that is also a work system, so the agent marker appears
both on the topology node and on the unit's box.

> `ai-agent` is a preliminary type and the `bound-to` anchor convention may still change.
