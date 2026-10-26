---
name: extract-interactions
description: >-
  Turn the interactions written as prose in a DWSD meeting — notes, an agenda, a
  description of what happens — into the meeting's `## Interactions` table
  (`Name | Outcome | Interaction of`), so each one that touches a board position shows as
  a chip there. Proposes first, writes only on a yes. Use when asked to extract, tabulate
  or structure the interactions or agenda of a meeting.
argument-hint: "<meeting file>"
---

# extract-interactions

**Spec root** — the folder that holds `conventions.md`, `types/`, `templates/` and
`examples/`; paths below start there (`<spec-root>/…`). In Claude Code it is
`${CLAUDE_PLUGIN_ROOT}`; another host names its own.

Read `<spec-root>/types/meeting.md` › Body (the table form) and `<spec-root>/conventions.md`
› How do I refer to an interaction from a meeting table first. The file you are given
(**$ARGUMENTS** in Claude Code) is the meeting; the interactions you find are the ones it
bundles.

## Steps

1. **Read the meeting** — the four framing sections, any `## Interactions` already there,
   the frontmatter `interaction-of` — and the board(s) it works on.
2. **Find the interactions in the prose.** An interaction is a step people take together
   with a result: "we go through what is done", "blockers get an owner". Not one: the
   reason for the meeting, a rule, a decision taken once. Give each a short name, in the
   order the meeting runs them, and its **outcome** in the text's words. No outcome in the
   text → leave the cell empty and say so; do not invent one.
3. **Find the board position each one works on**, only when the text says so ("we walk the
   Blocked column"). Write it as a locator; take column and lane names from the board's
   fence. If the meeting's frontmatter `interaction-of` already names the board, a
   relative locator (`#col:Done::in`) is enough. Unsure → leave `Interaction of` empty.
4. **Interactions that already have a file** (an `interaction` or a `meeting` the prose
   links): one row with the `[[…]]` link alone, the other cells empty — the file is the
   source.
5. **Propose, do not write yet.** Show the table with the sentence each row came from, and
   what you left as prose and why.
6. **On a yes, write** the table under `## Interactions` — replacing a bullet list there
   only if the person agrees; keep the file's line endings. Prose elsewhere stays.
7. **Check what you wrote** as `org-validate` would: every locator resolves to a board
   position that exists, every `[[…]]` resolves.

## Do not

- Do not invent interactions, outcomes or board positions.
- Do not change other files. If an interaction has a life of its own (its own agreements,
  used by several meetings), **suggest** pulling it out into an `interaction` file; create
  it only when asked.
