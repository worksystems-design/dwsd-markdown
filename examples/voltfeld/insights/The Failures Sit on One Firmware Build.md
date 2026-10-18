---
type: insight
observes: "[[Firmware Platform]]"
derived-from: "[[Not Charging After the Firmware Update]]"
status: new
created_at: "2026-10-03"
---

Every "not charging" ticket since September is a unit from WB-H 2407–2412 running build
4.2.0. Units from the same range on 4.1 do not show it, and neither do newer ranges on 4.2.
The fault sits where one hardware batch meets one firmware build — a question for the
[[Firmware Platform]] and [[HW Base]] together, not for the triage.

**Category:** structural | **Severity:** info

## Observations

- [[Ravi Anand]] matched the ticket serials against the OTA rollout log: all on 4.2.0.
- The serial range shares one charge-controller revision.

## Suggested Actions

- Hold 4.2.0 for the range until the cause is known.
