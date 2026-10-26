---
type: role
role-keeper: "[[Ines Rossi]]"
for-domain: "[[Market Street]]"
version: "1.0"
decision_date: "2026-10-20"
review_date: "2027-04-20"
created_at: "2026-10-20"
---

## Purpose

### Driver

The [[Market Street]] site needs someone who looks after the building itself — keys,
opening hours, the back door — whoever runs the counter that day.

### Requirement

A role for the site, separate from the shop's flow: who opens up, who is called when the
alarm goes off, who takes the early delivery at the back door.

## Description

The Market Street Site Lead holds the keys to [[Market Street]], sets the posted opening
hours, and receives the early van at the back door. The role is scoped to the site, not to
the [[Market Street Shop]] work system: what is sold and how much is ordered stays with the
[[Market Street Shop Manager]].

## Concerns

The building and its access — keys, alarm, opening hours, the back-door delivery slot.

## Mandates

| Mandate                                                  | Level                       | Anchor |
|----------------------------------------------------------|-----------------------------|--------|
| Open and lock the building; hold the keys and alarm code | must                        |        |
| [[Market Street Opening Hours]]                          |                             |        |
| Receive the early delivery at the back door, sign for it | must                        |        |
| Decide who else holds a key                              | autonomous                  |        |
| Set the back-door delivery slot                          | agree with [[Deliveries]]   |        |

## Evaluation

### Metrics and Monitoring

- Late openings; missed back-door deliveries.

> [!NOTE]
> **Modeling note.** `for-domain` names the site, a plain unit: the site decides about its
> own building without running a flow. The role shows on the Market Street box in the
> units view; the shop's flow stays with the work system and its own role.
