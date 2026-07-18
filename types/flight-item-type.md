# `flight-item-type`

> A *class* of work item that flows through the organization — e.g. a standard order, a
> custom order, an innovation increment. It defines what a kind of work *is*, not an
> individual item.

**Serialized `type`:** `flight-item-type`

## Frontmatter

| Field | Required | Format | Meaning |
|---|---|---|---|
| `type` | yes | `flight-item-type` | Entity type |

Plus the shared optionals from [conventions](../conventions.md).

## Body

Free Markdown. Answer four standard questions as `##` headings:

1. **Where do Flight Items of this type come from?**
2. **Why are you working on these? What is the customer value?**
3. **To whom is the finished Flight Item delivered?**
4. **How long does it take?**

## Example

```markdown
---
type: flight-item-type
---
## Where do Flight Items of this type come from?

Customer places an order for a standard configuration (3P / 4P / 5P) via the Sales channel.

## Why are you working on these? What is the customer value?

Core revenue stream — standard drones are the predictable, repeatable business that
funds custom and innovation work.

## To whom is the finished Flight Item delivered?

Customer receives an assembled, tested drone with documentation.

## How long does it take?

Year-1 baseline: 2–4 weeks. Year-5 reality: 4–6 weeks.
```

## Notes

- The four-question structure is a convention, not enforced.
- A [flight route](flight-route.md) names its primary flight-item-type in its `for:` key
  as a wikilink (e.g. `for: "[[Standard Order]]"`). The short stage tokens inside a
  route's `path:` (`order`, `contract`, …) are local to that route, not entity references.
