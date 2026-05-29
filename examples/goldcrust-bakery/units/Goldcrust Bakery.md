---
type: unit
unit-type: company
created_at: "2026-05-24"
---

Goldcrust Bakery is the company as a whole — the structural root that the work systems and
people belong to. Its `unit-type` is just `company` — it does **not** include `work-system`
(and it has no `flightlevel`), so it is a plain structural `unit`, not a work system: it
groups, it does not itself coordinate a flow of work.

Its operational reality is described by the work systems below (each a `unit` whose
`unit-type` includes `work-system`):

- [[Bakery Strategy]] — FL3, sets direction.
- [[Bakery Operations]] — FL2, coordinates production and retail.
- [[Bakehouse]] — FL1, production.
- [[Market Street Shop]] and [[Station Road Shop]] — FL1, retail.

And one plain team that is *not* a work system:

- [[Deliveries]] — `unit-type: team`, no flightlevel; carries the morning dispatch.
