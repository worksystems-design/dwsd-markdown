---
name: org-new
description: >-
  Scaffold a new DWSD entity from its template into the right folder. User-invoked only.
argument-hint: "[entity-type] [name]"
disable-model-invocation: true
---

# org-new

Create a new DWSD entity of type **$ARGUMENTS**. If the type or the name is missing, ask.

1. Resolve the type to its template `${CLAUDE_PLUGIN_ROOT}/templates/<type>.md` and its
   contract `${CLAUDE_PLUGIN_ROOT}/types/<type>.md`, and read both. Mind the subtypes: a
   **work system** is the `unit` template **plus** `work-system` in `unit-type` (and a
   `flightlevel`); a **meeting** is the `meeting` template (a `type: interaction` with
   `interaction-type: meeting`).
2. Determine the target folder by the *conceptual* type:
   - `individual` → `individuals/`, `role` → `roles/`, plain `unit` → `units/`,
     **work system (`unit` with `work-system` in `unit-type`) → `work-systems/`**,
     `interaction` and
     **`meeting` → `interactions/`**, `agreement` → `agreements/`, `signal` → `signals/`,
     `insight` → `insights/`, `driver` → `drivers/`, `proposal` → `proposals/`,
     `organizational-decision-record` → `decision-records/`, `visualization` → `visualizations/`,
     `flight-item-type` → `flight-item-types/`, `flight-route` → `flight-routes/`,
     `ai-agent` → `ai-agents/`.
3. Write `<folder>/<Name>.md` — the filename is the entity's human label (Title Case,
   spaces allowed; it is the wikilink target). Fill the frontmatter from the template
   (required fields + discriminator) and leave body sections as prompts to complete.
4. Wire any relationships the user provides as `[[wikilinks]]`. For a `meeting`, also offer
   to create the `.mw` Markwhen sibling.

Confirm the path you created and suggest running `/dwsd-md:org-validate` afterwards.
