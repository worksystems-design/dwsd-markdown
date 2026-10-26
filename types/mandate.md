# `mandate`

> Something a holder must or may do, pulled out into its own file — because it has a band
> to stay in, a delegator worth naming, a history, or something wants to link to it. Most
> mandates never need one: they are rows on the holder's own file (see
> [conventions](../conventions.md#mandates--what-a-holder-must-or-may-do)).

**Serialized `type`:** `mandate`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `mandate` | Entity type |
| `for-domain` / `for_domain` | no | wikilink or list | The **holder** when it is a role, a unit or a work system — points *up*. Naming a role lands the mandate on every keeper of that role. A person holding a mandate directly is not named here; the row in the person's file that names this mandate says so |
| `delegator` | no | wikilink | Who **handed the mandate over** — a domain or a person — and can widen, narrow or withdraw it alone (metadata, not a typed edge) |
| `mandate-of` | no | locator or list (or a bare `[[entity]]`) | **Where it hangs** — a board position, a route stage, a meeting, a work system — points *into the detail*. This is where the mandate chip shows |
| `derived-from` | no | wikilink | The decision or proposal it came from — the [shared emergence key](../conventions.md#derived-from--the-shared-emergence-key) (metadata) |
| `version` | no | string | Version of the mandate |
| `decision_date` | no | date | When this version was decided |
| `review_date` | no | date | When it is due for review |

Plus the shared optionals from [conventions](../conventions.md).

## Relationships

- **`for-domain`** — the holder, when it is a domain. Points *up*.
- **`mandate-of`** — where the mandate hangs. Points *into the detail*; value-polymorphic
  like every locator ([conventions](../conventions.md)).
- **`delegator`** — who gave it. A mandate differs from an [agreement](agreement.md) in who
  can change it: the delegator alone, not the parties together.
- The holder's file names the mandate in a mandate row (`| [[Mandate]] | |`); that row,
  like a meeting's row for an interaction, leaves its other cell empty — the file is the
  source.

## Body

| Section | Content |
|---|---|
| `## Description` | What the holder must or may do, and **how free** it is — within which band, with whom, up to what |
| `## Evaluation` | Optional — how one sees the mandate is used well |

Free Markdown beyond that. The body structure is a recommendation.

## Example

```markdown
---
type: mandate
for-domain: "[[Market Street Site Lead]]"
delegator: "[[Market Street Shop Manager]]"
mandate-of: "[[Market Street Shop Board]]#Market Street Shop::in"
created_at: "2026-10-22"
---

## Description

Set the opening hours posted on the door of [[Market Street]] and keep them current —
holidays, a late delivery, a closed street. The hours stay within the band the
[[Market Street Shop Manager]] decides under the [[Shop Manager Mandate]]. Within that
band the site lead decides alone.

## Evaluation

- The posted hours match the hours the shop actually opens.
```

## Reading it

- **The question:** who may or must do this, how freely, and who can change that?
- **Look first:** `## Description` for the mandate and its freedom; `delegator` for who
  can change it.
- **Go next:** up via `for-domain` to the holder (a role there reaches each keeper); into
  the detail via `mandate-of`; to the delegator, whose own mandate may set the band this
  one stays in.
- **Backlinks:** the holder's file, whose mandate row names this file; a signal or insight
  that `observes` it.
- **Pictured in:** wherever `mandate-of` points, as a mandate chip; on the box of the
  holder role's keepers.

## Notes

- A row on the holder's file is enough for most mandates. Pull one out only when it needs
  an identity of its own.
- Whether a person holds a mandate directly or through a role: through a role is usual;
  a direct one is a row in the person's file.
- Hosts that draw an icon per type show a mandate with the Lucide icon `key-round`: a
  mandate unlocks what the holder could not do without it. It pairs with the agreement's
  handshake, which stands for what parties settle together.
