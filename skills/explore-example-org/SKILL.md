---
name: explore-example-org
description: >-
  Copy a bundled DWSD example organization into the current working directory so the user
  can browse it, follow its guided tour, and see the boards render. Use whenever the user
  asks to see, explore, open, or try an example org (e.g. "show me the Goldcrust bakery",
  "give me an example organization to look at").
argument-hint: "[example-name]"
---

# explore-example-org

Copy a complete DWSD **example organization** out of the plugin and into the user's current
working directory, so they can open the files in the editor, follow the guided tour, and see
the visual board renders. Use this whenever the user wants to see or explore an example org —
the bundled examples otherwise live inside the plugin folder and are not visible in the
workspace.

1. **List the available examples.** Each subdirectory of `${CLAUDE_PLUGIN_ROOT}/examples/` is
   one example org. Right now there is exactly one: `goldcrust-bakery` (a small bakery — the
   DWSD tour org).

2. **Pick the example:**
   - If the user named one in **$ARGUMENTS**, use it.
   - Else if there is exactly one example, use that one.
   - Else list the names and ask which one they want.

3. **Copy the whole tree** into a subfolder of the current directory named after the example,
   preserving its structure:
   ```bash
   cp -r "${CLAUDE_PLUGIN_ROOT}/examples/<name>" "./<name>"
   ```
   If `./<name>` already exists, do **not** overwrite it — tell the user it is already there
   and point them to it.

4. **Confirm and orient.** State the folder you copied (e.g. `goldcrust-bakery/`) and tell the
   user to start with **`<name>/TOUR.md`** — a short guided tour. Mention that the DWSD files
   (`*.dwsd-board`, `*.dwsd-flightroute`, `*.dwsd-topology`, and `dwsd.board` fences inside
   `.md` files) render visually via **"Open DWSD Preview"** at the top of the editor.
