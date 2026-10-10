# Examples

Complete, self-consistent DWSD organizations — worked examples that show the
[entity types](../README.md) wired together into a whole, not in isolation. They are
**reference instances**, not part of the spec.

| Example | What it shows |
|---|---|
| [`goldcrust-bakery/`](goldcrust-bakery/) | A small bakery — production + two shops + a coordination and a strategy layer. Exercises every entity type once. The gentler start. |
| [`voltfeld/`](voltfeld/) | A hardware product company — EV chargers — with one Agile Release Train (partially SAFe-inspired), a plant and a supply base outside it. The line (`reports-to`) and the work (`member-of`) are two different trees; platform work systems contribute to several teams; agents are bound to column groups. Every entity type at least once. |

Each example is laid out like a real organization: one folder per entity type
(`individuals/`, `roles/`, `work-systems/`, …), one Markdown file per entity.
