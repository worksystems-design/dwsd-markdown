---
type: agreement
agreement-type: work
for-domain: "[[Order to Delivery]]"
agreement-of:
  - "[[Order Studio Board]]#Order Studio/col:Flagged::in"
  - "[[Customer Order Route]]/stage:case @ Studio::before"
tags: [factory-studio]
version: "1.0"
decision_date: "2026-06-01"
review_date: "2026-12-01"
created_at: "2026-10-11"
---

## Driver and Requirement

The ERP assumes every order goes through. About seven in a hundred do not, and until June
2026 those lived in mail threads and a shared spreadsheet: no owner, no clock, and the
customer learned about the problem when the delivery date passed. The factory needs an
andon cord — a defined way to stop *one* order, get the right people to it quickly, and
send it back.

## Who is responsible for what?

- The [[Order Exception Agent]] — flags an order the moment it will not go through, and
  prepares the case: what is missing, which options exist.
- [[Paula Weiss]] — picks up every flagged case and pulls in whoever it needs.
- [[Leyla Demir]] for dates, [[Wen Zhao]] for parts, [[Hanna Berglund]] for anything that
  needs the customer.

## Description

An order is flagged when it cannot be priced, scheduled or released without a person. A
flagged case is answered within **four working hours** and is back in the ERP within **two
working days**, or it moves to `Waiting on Customer` with the customer told. At most four
cases are worked at once. Every case leaves the studio with a **reason code** — that code is
what makes the next improvement possible.

## Evaluation Criteria

- No flagged case unanswered after four working hours.
- Fewer than five in a hundred orders need the studio by the end of 2026.
