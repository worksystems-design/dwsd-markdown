---
type: ai-agent
platform: cad-assistant
status: active
for-domain: "[[HW Base]]"
bound-to:
  - "[[HW Base Board]]#HW Base/group:Verification::in"
  - "[[Bastian Lorenz]]"
description: Runs design-for-manufacturing rules on every drawing entering Verification and drafts the findings list for the DFM Review.
created_at: "2026-10-10"
---

An agent working **inside a sub-process**: the DFM Check Agent is bound to the whole
`Verification` **column group** of the [[HW Base Board]] — not to a single column. Every
drawing that enters the group (Design Review, DFM Check, Lab Test) is checked against the
plant's design-for-manufacturing rules — draft angles, wall thickness, fastener count,
tolerances the end-of-line test can hold — and the agent drafts the findings list the
[[DFM Review]] works from. People decide; the agent prepares.

`bound-to` is a list: the group locator, and [[Bastian Lorenz]] — the Manufacturing Lead
who reviews the findings, so the agent shows on his box in the org chart too. The group
locator uses the same grammar as a column locator, one segment shorter:
`#HW Base/group:Verification::in`.

> `ai-agent` is a preliminary type and the `bound-to` anchor convention may still change.
