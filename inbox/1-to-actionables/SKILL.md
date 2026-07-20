---
name: 1-to-actionables
description: >
  Turn a tracer-bullet ticket (or a set of them) into a human-executable coding
  plan: which files to open, where to change, and what to write — without the
  agent implementing. Use after /1-to-spec and /1-to-tickets when the user will
  code manually. Triggers: "to actionables", "break this ticket into coding
  steps", "manual implementation plan", "file-level plan", "what do I change
  where", "/1-to-actionables", flags --mode actionables|pseudocode and
  --scope ticket|set.
disable-model-invocation: true
---

# To Actionables

Turn tickets into **human coding plans**. You explore the **live** codebase and produce ordered steps a developer can execute by hand. You do **not** implement, open a PR, or run `/0-implement`.

**Pipeline position:** `/1-to-spec` → `/1-to-tickets` → **`/1-to-actionables`** → human codes (or later `/0-implement` if they change their mind).

**Why paths are allowed here:** `/1-to-tickets` forbids file paths because tickets go stale. This skill re-reads the live tree **now** so paths are current for immediate human use. Plans still rot — regenerate if the tree moved.

## Flags

Parse from the invocation / user message. Defaults if omitted: `--mode actionables --scope ticket`.

| Flag | Values | Meaning |
|------|--------|---------|
| `--mode` | `actionables` \| `pseudocode` | Output shape (see below) |
| `--scope` | `ticket` \| `set` | One ticket vs whole ticket set |

Full flag rules + examples: [references/flags-and-modes.md](./references/flags-and-modes.md).  
Output templates: [references/output-templates.md](./references/output-templates.md).

### Mode `actionables` (default)

Ordered, file-level checklist. Each step names **path → symbol/region → change → sketch** (short, not paste-ready apps). Human can work top-to-bottom.

### Mode `pseudocode`

Narrative walkthrough: call order, data flow, function-level pseudocode. Fewer rigid steps; better when the human wants to understand the design before typing.

### Scope `ticket` (default)

One ticket. Require a ticket path, issue URL/number, or the ticket body in context. If missing, ask once for the ticket id/path.

### Scope `set`

All tickets for the feature (local `.scratch/<feature>/issues/` or tracker parent). Produce one actionables file per ticket, dependency order (blockers first). Only expand the **frontier** in detail if the user says so; otherwise plan every ticket against current code, noting “blocked until N lands.”

## Process

### 1. Resolve inputs

1. Read flags (`mode`, `scope`).
2. Load ticket(s): local file(s) under `.scratch/<feature>/issues/`, or fetch tracker issue(s). Prefer full body + acceptance criteria + blocked-by.
3. Load parent **spec** if available (same feature folder, linked parent issue, or conversation). Use it for intent; tickets win on scope cuts.
4. If `--scope ticket` and multiple candidates exist, ask which ticket — do not invent.

### 2. Explore the live codebase (required)

Do not invent paths. Search/read until you can name real files and symbols:

- Prefer existing seams, modules, tests, and domain glossary / ADR language.
- Note patterns to match (naming, error handling, test style).
- List **create** vs **modify** vs **delete** honestly; prefer modify over new files when a home already exists.
- If a path is uncertain, mark `VERIFY:` and say what to search for — never fake a path.

### 3. Draft the plan (mode-specific)

**Both modes must include:**

- Goal restated from the ticket (user-facing behaviour)
- Preconditions (blockers done? migrations landed? env?)
- Ordered work units that cover acceptance criteria
- Verification commands or manual checks mapped to each AC
- Out of scope / do-not-touch list
- **Deviations** — every case where the plan diverges from a ticket AC because live code already covers it (e.g. AC says "add knob X" but X exists), or where a ticket-named path lives elsewhere on disk. State the divergence, the default you took (honor-literally vs reuse-existing), and move on. One line each.
- **Open questions** — only if both options genuinely block coding (max ~3). If one option is codebase-consistent and unblocks the human, it is a Deviation, not an Open Question.

**`actionables` extras:** numbered steps with `File`, `Find`, `Change`, optional `Sketch` (≤15 lines), `Done when`.

**`pseudocode` extras:** sequence of units with purpose, inputs/outputs, pseudocode body, and a short “touch list” of real files at the end of each unit.

Refuse to dump a full working implementation. Sketches teach *where* and *what shape*; the human writes the code.

### 4. Write beside the ticket

Write under the feature’s scratch tree (create dirs as needed):

```text
.scratch/<feature-slug>/actionables/<NN>-<slug>--<mode>.md
```

Examples:

- `.scratch/checkout-retry/actionables/03-retry-banner--actionables.md`
- `.scratch/checkout-retry/actionables/03-retry-banner--pseudocode.md`

If tickets live only on a remote tracker, still use `.scratch/<feature-slug>/actionables/` (derive slug from parent title) and link the issue URL at the top of the file.

For `--scope set`, one file per ticket, same numbering as issues (`01`, `02`, …).

Use the matching template in [references/output-templates.md](./references/output-templates.md).

### 5. Hand off to the human

In chat: short summary (ticket title, mode, path to the written file, step count or unit count, top risks). Do **not** start coding. Do **not** run `/0-implement` unless the user explicitly switches.

## Hard rules

1. **No implementation** — no app code edits, no “while we’re here” refactors.
2. **Live paths only** — every path from repo exploration this run.
3. **One ticket’s AC** — do not expand into neighbouring tickets; note cross-ticket deps instead.
4. **Vertical, not horizontal** — steps follow the slice’s end-to-end path, not “all models then all APIs.”
5. **Stale warning** — header note: regenerate if tree changed since this file’s date.
6. **Respect DoD language** — verification should make ticket AC + standing project DoD checkable by the human (`/0-implement` definition-of-done is the standing bar when present).

## Boundary

| Need | Skill |
|------|--------|
| Spec / PRD | `/1-to-spec` |
| Tracer-bullet tickets | `/1-to-tickets` |
| Human coding plan (this) | `/1-to-actionables` |
| Agent implements | `/0-implement` |
| Red-green tests while building | `/1-tdd` |

## Progressive disclosure

| Load when | File |
|-----------|------|
| Flags, defaults, invocation examples | [references/flags-and-modes.md](./references/flags-and-modes.md) |
| Markdown templates for both modes | [references/output-templates.md](./references/output-templates.md) |
