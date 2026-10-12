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

The Demand Forecast Assistant proposes next-day quantities into the Backlog of the
[[Bakehouse Production Board]], drawing on recent sell-through and the weather forecast.
The [[Head Baker]] reviews and adjusts before the plan is confirmed at the
[[Daily Production Sync]].

> [!NOTE]
> **Modeling note.** A preliminary AI-agent surface. `bound-to` is a list: the board column
> where the suggestions appear, the person who reviews them ([[Mara Holt]] — the agent
> shows on her box in the org chart), and the [[Bakehouse]] work system itself, so the
> agent marker appears on its node in the flight-level map. (The units view stays out of
> it: Goldcrust's units are cut by site, and the work systems are not drawn there.)
>
> `ai-agent` is a preliminary type and the `bound-to` anchor convention may still change.
