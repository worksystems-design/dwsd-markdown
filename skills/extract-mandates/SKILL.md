---
name: extract-mandates
description: >-
  Turn the mandates written as prose in a DWSD file — what a person, role, unit or work
  system must or may do — into mandate rows (`Name | Mandate of`) under
  `## Accountabilities`, `## Decision Rights`, `## Key Responsibilities` or `## Mandates`,
  so the ones that hang somewhere show as chips there. Proposes first, writes only on a yes.
  Use when asked to extract, tabulate or structure the mandates, responsibilities or
  decision rights in a file.
argument-hint: "<file> (an individual, role, unit or work system)"
---

# extract-mandates

**Spec root** — the folder that holds `conventions.md`, `types/`, `templates/` and
`examples/`; paths below start there (`<spec-root>/…`). In Claude Code it is
`${CLAUDE_PLUGIN_ROOT}`; another host names its own.

Read `<spec-root>/conventions.md` › Mandates first. The file you are given (**$ARGUMENTS**
in Claude Code) is the **holder**: every mandate you find in it is the holder's own.

## Steps

1. **Read the file** — body and frontmatter — and the files it links that could bound a
   mandate: its role's or unit's agreements, a mandate file, the board it works on.
2. **Find the mandates in the prose.** A mandate is something the holder **must** do (an
   accountability) or **may** decide or do (a decision right). Not a mandate: what someone
   else does, the purpose, history, a description of the flow. Write each as one short
   sentence and **keep how free the holder is in its words** — "with [[Deliveries]]",
   "up to $200 alone", "within the band [[Shop Manager Mandate]] sets". Never sharpen a
   vague sentence into a rule; quote it as vague.
3. **Find where each one hangs**, only when the files say so: a board column, a route
   stage, a meeting, a work system. Write it as an absolute locator
   (`[[Board]]#Board Name/col:Column::in`); take column and lane names from the board's
   fence, not from memory. Unsure → leave `Mandate of` empty. A row without a locator is
   still a mandate; it just shows no chip.
4. **Mandates that already have a file** (a `type: mandate` the prose links): one row with
   the `[[…]]` link alone, `Mandate of` empty — the file is the source.
5. **Propose, do not write yet.** Show, per heading (`## Accountabilities` for must,
   `## Decision Rights` for may; `## Key Responsibilities` on a work system; `## Mandates`
   if the file already uses the general form), the rows with the sentence each came from,
   and the sentences you left as prose and why. Name anything you could not place.
6. **On a yes, write.** Add the tables under their headings, or extend existing ones; keep
   the file's line endings. Leave the prose in place unless the person asks to remove
   sentences the rows now say fully — prose that says more (why, context) stays.
7. **Check what you wrote** as `org-validate` would: every locator resolves to a board
   position that exists, every `[[…]]` resolves.

## Do not

- Do not invent a mandate, a limit, a delegator or a locator the files do not contain.
- Do not change other files. If a mandate has a band, a delegator worth naming or a
  history, **suggest** pulling it out into a `type: mandate` file
  (`<spec-root>/types/mandate.md`); create it only when asked.
- Do not move a mandate from one holder to another — a mandate the text gives to a role
  belongs in the role's file, not the person's; say so instead.
