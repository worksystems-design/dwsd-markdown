---
name: org-read
description: >-
  Read and explain a DWSD organization folder — answer questions about who does what, who
  decides, how work flows, and why something changed, by finding the right entity files and
  following their links. Use when asked to explain, summarize, or answer questions about a
  DWSD org (e.g. "who decides about X?", "how does an order reach the bakehouse?", "where
  did this agreement come from?").
---

# org-read

**Spec root** — the folder that holds `conventions.md`, `types/`, `templates/` and
`examples/`; paths below start there (`<spec-root>/…`). In Claude Code it is
`${CLAUDE_PLUGIN_ROOT}`; another host names its own.

You answer from the files of the org you are given (default: the current folder). This is
**read-only**. Every type page has a `## Reading it` section
(`<spec-root>/types/<type>.md`) that says what that entity answers and where to go next —
open it for each type you land on. `<spec-root>/conventions.md` is authoritative for
relationships, locators and the views.

## Route the question to a starting point

| The question is about … | Start at | Then follow |
|---|---|---|
| a person — what they do, whom they report to | `individuals/` | `reports-to`, `member-of`, the roles naming them as `role-keeper` |
| who takes care of something, who may decide | `roles/` | the role's `for-domain`; the agreements, interactions and routes scoped `for-domain` to the role; its `## Accountabilities` anchors |
| a team, site, department, the shape of the org | `units/`, `work-systems/` | first `member-of` upward; `contributes-to` between work systems; the board via `visualization-of` |
| how work flows, where an item is | `visualizations/` (boards), `flight-routes/` | columns and lanes; route stages and `bound-to`; what anchors there (`interaction-of`, `agreement-of`, `bound-to`) |
| how people work together, a meeting | `interactions/` | `interaction-of`, `for-domain`; a meeting's `## Interactions` table, row by row |
| a rule, a working agreement | `agreements/` | `agreement-of`, `for-domain`; `derived-from` back to the decision |
| why something changed, what was decided | `decision-records/` | `derived-from` back to proposal, driver, insight, signal; forward to what names the record in `derived-from` |
| something someone noticed, an open issue | `signals/`, `insights/`, `drivers/`, `proposals/` | `observes`; up and down the ladder along `derived-from` |
| an AI agent and where it acts | `ai-agents/` | `bound-to`, `for-domain`, `delegator` |

The folder is a convenience; the `type:` field decides. A work system is a `unit` whose
`unit-type` includes `work-system`; a meeting is an `interaction` with
`interaction-type: meeting`.

## Read, then follow

1. **Find the files.** Search the org for the names in the question — the filename is the
   label and the `[[wikilink]]` target.
2. **Read the entity**, frontmatter first, then the body sections its type page names.
3. **Follow links both ways.** Outgoing wikilinks point up (`for-domain`), into the detail
   (a locator) or back (`derived-from`). Backlinks — files that name this one — usually
   finish the answer: search the org for `[[<Name>]]`.
4. **Use the pictures when they help.** A board or a flight route shows flow; the four
   inferred views (topology, org chart, units, change trail) are drawn from the files.
   A fence's `around:` says which entity the picture is drawn from (`focus:` is its earlier
   name). The view describes the files; when they disagree, the files win.
5. **Answer with sources.** Name the files you relied on, and say plainly when the org does
   not record something rather than filling the gap.

For writing or changing files, use the `dwsd-format` skill; for checking an org, the
`org-validate` skill.
