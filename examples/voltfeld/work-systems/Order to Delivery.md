---
type: unit
unit-type: work-system
flightlevel: 2
contributes-to: "[[Portfolio]]"
delegator: "[[Ingrid Halvorsen]]"
tags: [factory-studio]
version: "1.0"
decision_date: "2026-06-01"
review_date: "2027-05-31"
created_at: "2026-10-11"
---

## In context

```dwsd.topology
mode: infer
radius: 2
```

## Purpose

Take every customer order from entry to invoice — and take care of the few that do not go
through on their own. The order process itself is defined in the ERP and runs there:
order entry, scheduling, production order, invoice. About ninety-three in a hundred orders
pass without anyone touching them. That part is **factory mode**, and it should stay that
way.

The rest — an unpriceable configuration, a date the plant cannot make, a credit block —
falls out. This work system exists for those: a defined trigger (the
[[Order Andon]]), a place where people work the case together with an agent
([[Order Studio Board]]), a way back into the ERP, and a loop that learns *why* orders fall
out. That part is **studio mode**. Neither the ERP nor the line organization describes it;
here it is a work system of its own.

Its people come from three departments — [[Sales]], [[Manufacturing]] and
[[Supply Chain]] — and stay there. The work system is the flow they share, not a unit they
belong to.

## Key Responsibilities

- Own the [[Customer Order Route]]: the factory stages in the ERP and the studio around
  them.
- Answer every flagged order within four working hours and return it to the ERP within two
  working days (the [[Order Andon]]).
- Turn recurring reasons for studio cases into changes — an ERP rule, an agent, an
  agreement — at the monthly [[Order Exceptions Review]].

## Customers and Deliverables

- Fleet operators, depots and installers — confirmed dates, delivered chargers, correct
  invoices.
- [[Portfolio]] — order intake, on-time delivery, and the reasons orders fall out.

## Dependencies

On the ERP and the external partner who runs it (Voltfeld has no IT department of its own);
on [[Manufacturing]] for capacity and dates; on [[Supply Chain]] for parts availability; on
the [[Platform Variant Rule]] for which configurations exist at all.

## Key Challenges

- The ERP assumes every order goes through. The seven in a hundred that do not used to
  live in mail threads and a shared spreadsheet, with no owner and no clock.
- Fixes to the ERP went into the partner's ticket queue and rarely came back.

## Key Resources

- [[Paula Weiss]] (order coordination), [[Hanna Berglund]] (sales), [[Leyla Demir]]
  (production planning), [[Wen Zhao]] (supply), the [[Order Exception Agent]].

## Key Metrics and Monitoring

- Share of orders that need the studio (target: falling); age of open studio cases;
  on-time delivery; reasons for studio cases, by month.

## Evaluation Schedule

Reviewed yearly; next review 2027-05-31.

> [!NOTE]
> **Modeling note.** The work system has no `member-of`.
