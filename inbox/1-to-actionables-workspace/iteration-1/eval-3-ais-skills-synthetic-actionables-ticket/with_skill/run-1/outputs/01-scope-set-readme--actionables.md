# 01 — Scope-set README index generator — actionables

**Source ticket:** `.scratch/actionables-index-file/issues/01-scope-set-readme.md`
**Parent spec:** none loaded
**Generated:** 2026-07-19
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** actionables
**Scope run:** ticket

## Goal

When `/1-to-actionables` runs with `--scope set`, the skill writes a `README.md` index file beside the per-ticket actionables files by default (one row per ticket: mode, file, blocked-by, ready, plus a recommended start row). A new `--no-index` flag opts out. Today this is described as optional; the ticket promotes it to default behavior.

## Preconditions

- [ ] Blockers done: none (ticket states "can start immediately").
- [ ] Other: none. This is a docs/skill-text change — no app runtime, no migrations, no env flags.

## Acceptance criteria → verification

| AC (from ticket checklist) | How the human proves it |
|----|-------------------------|
| Add `--no-index` flag to flag parser in `SKILL.md` + parsing rules in `references/flags-and-modes.md` | Grep `--no-index` in both files; it appears in the Flags table and in the Parsing block of `flags-and-modes.md`. |
| When `--scope set` and `--no-index` not present, write `.scratch/<feature>/actionables/README.md` using the existing template | `SKILL.md` Process step 4 + Scope `set` section say README is written by default; `output-templates.md` "Scope `set` index" section is reframed from optional to default. |
| Update defaults table in `references/flags-and-modes.md` to document `--no-index` | Defaults table has a `--no-index` row describing default-on and when to override. |
| Update `Scope set` section of `SKILL.md` so README write is described as default, not optional | The `### Scope \`set\`` subsection reads as default-on with opt-out. |
| Verification from ticket: invoke `--mode actionables --scope set` against an existing feature issues dir and confirm `README.md` appears with one row per ticket | Run the skill against any existing `.scratch/<feature>/issues/` dir; `ls .scratch/<feature>/actionables/README.md` exists and its table has one row per ticket. |

## Do not touch

- `inbox/1-to-actionables/agents/` — unrelated to flag parsing/output.
- `mode: pseudocode` template body, `Scope ticket` subsection, and shared header template in `output-templates.md` — out of scope (only the `set` index section changes).
- Any other skill under `skills/` outside `inbox/1-to-actionables/`.
- Do not change the `.scratch/<feature>/actionables/<NN>-<slug>--<mode>.md` per-ticket filename convention.

## Steps

### Step 1 — Add `--no-index` parsing rule

- **File:** `skills/inbox/1-to-actionables/references/flags-and-modes.md` *(modify)*
- **Find:** the `## Parsing` section's example blocks (lines ~5–17) and the "Natural language maps" table (lines ~19–27).
- **Change:** add a short example showing the `--no-index` flag shape (`--no-index`, a boolean — no value token), and a natural-language mapping row (`"no index"`, "skip README"` → `--no-index`). Keep it boolean; do not invent a `--index` positive twin.
- **Sketch:**

```text
--no-index
no-index: true
```

| User says | Parse as |
|-----------|----------|
| "no index", "skip README index" | `--no-index` |

- **Done when:** `rg -n "no-index" skills/inbox/1-to-actionables/references/flags-and-modes.md` shows the new parsing examples and table row.

### Step 2 — Document `--no-index` in the Defaults table

- **File:** `skills/inbox/1-to-actionables/references/flags-and-modes.md` *(modify)*
- **Find:** the `## Defaults` table (lines ~31–36).
- **Change:** add one row for `--no-index`: default value `false` (i.e., README **is** written on `--scope set`), override when the human wants a quieter run or the feature has a single ticket. Note the flag only takes effect under `--scope set`.
- **Sketch:**

```text
| `--no-index` | false (README written) | `--scope set` run where the human wants no index file (single ticket, custom README already present) |
```

- **Done when:** Defaults table has a `--no-index` row and the default-on behavior is unambiguous to a reader.

### Step 3 — Add `--no-index` row to the Flags table in `SKILL.md`

- **File:** `skills/inbox/1-to-actionables/SKILL.md` *(modify)*
- **Find:** the `## Flags` table (lines ~26–29, columns `Flag | Values | Meaning`).
- **Change:** add a row: `--no-index` | *(none — boolean)* | "Skip writing the `actions/README.md` index on `--scope set`." Keep the existing `--mode` / `--scope` rows untouched.
- **Sketch:**

```text
| `--no-index` | *(boolean, no value)* | When set with `--scope set`, do not write `actions/README.md`. Default off. |
```

- **Done when:** `rg -n "no-index" skills/inbox/1-to-actionables/SKILL.md` returns the Flags-table row.

### Step 4 — Rewrite `Scope set` subsection to default-on

- **File:** `skills/inbox/1-to-actionables/SKILL.md` *(modify)*
- **Find:** `### Scope \`set\`` subsection (line ~46), currently ending with "otherwise plan every ticket against current code, noting 'blocked until N lands.'"
- **Change:** append a sentence stating that on `--scope set` the skill writes `actions/README.md` (index table: ticket → mode → file → blocked-by → ready) **by default**, and that `--no-index` suppresses it. Reference the index template in `references/output-templates.md`.
- **Sketch:**

```text
On `--scope set`, also write `.scratch/<feature>/actionables/README.md` — an index
table (ticket → mode → file → blocked-by → ready) plus a recommended start row.
Default behavior; pass `--no-index` to suppress. See references/output-templates.md.
```

- **Done when:** the `### Scope \`set\`` subsection reads as default-on with an opt-out; no remaining wording calls the README "optional."

### Step 5 — Update Process step 4 to make README a default output

- **File:** `skills/inbox/1-to-actionables/SKILL.md` *(modify)*
- **Find:** `### 4. Write beside the ticket` (lines ~86–102), specifically the `For --scope set, one file per ticket, same numbering as issues` line (~100).
- **Change:** add a clause right after that line: "and write `actionables/README.md` (index table from the template) unless `--no-index` is set."
- **Sketch:**

```text
For `--scope set`, one file per ticket, same numbering as issues (`01`, `02`, …),
and write `actionables/README.md` (index table per references/output-templates.md)
unless `--no-index` is set.
```

- **Done when:** Process step 4 names the README as a default `--scope set` artifact gated by `--no-index`.

### Step 6 — Reframe the index section in output-templates.md as default

- **File:** `skills/inbox/1-to-actionables/references/output-templates.md` *(modify)*
- **Find:** the `## Scope \`set\` index (chat + optional index file)` heading and its lead sentence (lines ~156–158), which currently say "also print (and optionally write `.scratch/<feature>/actions/README.md`)."
- **Change:** rename heading to `## Scope \`set\` index (default README file)`; rewrite the lead to: "On `--scope set`, the skill writes `.scratch/<feature>/actionables/README.md` by default. Pass `--no-index` to skip the file (the index is still printed in chat)." Keep the existing table block (lines ~160–169) and "Work recommendation" line as-is — they are already correct.
- **Sketch:**

```markdown
## Scope `set` index (default README file)

On `--scope set`, the skill writes `.scratch/<feature>/actionables/README.md` by
default using the table below. Pass `--no-index` to skip the file (the index is
still printed in chat).
```

- **Done when:** the section heading and lead no longer say "optional"; the table template body is unchanged; `rg -n "optionally" skills/inbox/1-to-actionables/references/output-templates.md` returns nothing in this section.

## Order notes

- Steps 1–2 are the same file (`flags-and-modes.md`); do them in one sitting — parsing rule first so the Defaults row can reference it.
- Steps 3–5 are the same file (`SKILL.md`); do them top-to-bottom (Flags table → Scope set subsection → Process step 4) so each pass leaves the file self-consistent.
- Step 6 is the template reframe and is independent — safe to do anytime after Step 1.
- Safe stop points: after Step 3 the flag is documented but not yet wired into behavior text; after Step 5 the skill body is fully consistent; after Step 6 docs are fully consistent. Each AC maps to a step (AC1 → 1+3, AC2 → 4+5+6, AC3 → 2, AC4 → 4).

## Final verification

1. Text consistency: `rg -n "no-index" skills/inbox/1-to-actionables/` — expect matches in `SKILL.md` (Flags table, Scope set, Process step 4) and `references/flags-and-modes.md` (Parsing, Defaults).
2. No stale "optional" wording: `rg -n "optional index|optionally write" skills/inbox/1-to-actionables/` — expect zero hits after Step 6.
3. Behavior check (ticket's stated verification): invoke `/1-to-actionables --mode actionables --scope set` against any existing feature issues dir (e.g., a throwaway `.scratch/_index-smoke/issues/` with two tiny tickets) and confirm `actions/README.md` is written with one row per ticket. Re-run with `--no-index` and confirm the README is **not** written.

## Open questions

- None — defaults taken: `--no-index` is a boolean (no `--index` positive twin), it only affects `--scope set`, and the README is still printed in chat even when the file is suppressed. The existing index table body in `output-templates.md` is reused verbatim.
