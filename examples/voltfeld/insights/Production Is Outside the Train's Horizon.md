---
type: insight
observes:
  - "[[Charger ART]]"
  - "[[Manufacturing]]"
  - "[[Supply Chain]]"
derived-from:
  - "[[PI Objectives Missed on Enclosure Tooling Twice]]"
  - "[[Fixtures Built After the Release]]"
status: acknowledged
acknowledged_at: "2026-10-02"
created_at: "2026-10-01"
---

The [[Charger ART]] plans in ten-week increments; a mold takes fourteen weeks and a ramp
five more. The two work systems that hold those lead times — [[Supply Chain]] and
[[Manufacturing]] — are not at PI planning and have no place on the ART board. The missed
objectives are not an execution problem of [[HW Base]]: the train commits to dates its
planning horizon cannot see, and the plant learns about releases when they are already
released.

**Category:** flow | **Severity:** warning

## Observations

- PI planning takes capacity, runway and certification slots as inputs — not tooling or
  parts lead times ([[PI Planning]], "What information do we need").
- [[Manufacturing]] contributes to the [[Portfolio]], not to the train; development and
  production share no FL2. The [[Feature Route]] has no edge from the plant back.
- The only recurring contact is the [[System Demo]], where [[Bastian Lorenz]] attends as a
  guest — after the design is frozen.
- Both molds were ordered in week 3 of the PI they were needed in; fourteen weeks cannot
  fit into the seven that remain.

## Suggested Actions

- Plan tooling and long-lead parts one PI ahead of the features that need them.
- Bring Supply Chain and the plant into PI planning as participants.
- Give ramp status a path back into the train before the release, not after.
