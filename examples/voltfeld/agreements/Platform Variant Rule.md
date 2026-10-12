---
type: agreement
agreement-type: organizational
for-domain:
  - "[[HW Base]]"
  - "[[Firmware Platform]]"
  - "[[System Architect]]"
agreement-of:
  - "[[HW Base]]"
  - "[[Firmware Platform]]"
version: "1.0"
decision_date: "2026-06-29"
review_date: "2026-12-28"
created_at: "2026-10-10"
---

## Driver and Requirement

Before the platform teams existed, the [[Wallbox]] and [[DC Charger]] teams each kept their
own power board and their own firmware fork of what had once been one code base. Every
fix was made twice and certified twice. When [[HW Base]] and the [[Firmware Platform]] were
carved out in June 2026, the line between platform and product had to be written down, or
the forks would have come back within two PIs.

## Who is responsible for what?

- [[HW Base]] and the [[Firmware Platform]] — own the shared components and their variant
  roadmap; serve both product lines from one design.
- [[Wallbox]] and [[DC Charger]] — build on the platform; may request a variant, may not
  fork a platform component.
- [[System Architect]] — decides what is platform and what is product, and arbitrates
  variant requests; escalation to [[Marit Solberg]].

## Description

The power and metering module, control board, enclosure base, firmware base, bootloader,
OTA client and protocol stack are **platform**: one design, versioned, owned by the
platform teams. A product line needing something different files a variant request with
the platform team; the [[System Architect]] decides within one iteration whether it becomes
a platform variant, a product-side addition on top, or is declined. No product line
maintains a copy of a platform component.

> [!NOTE]
> **Modeling note.** This agreement is **organizational** — it is about domains, not about
> a board column. It is anchored on the two platform work systems themselves
> (`agreement-of` names them as entities, so it shows on their nodes and unit boxes), and
> its `for-domain` names the [[System Architect]] role as well — so it also lands on
> [[Elias Moreau]]'s box in the org chart, the person who has to hold the line.

## Evaluation Criteria

- No forked platform component in any product repository or BOM.
- Variant requests decided within one iteration.
- Platform share of each product's BOM rising, not falling.
