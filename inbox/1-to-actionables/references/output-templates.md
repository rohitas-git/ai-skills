# Output templates

Write one file per ticket:

```text
.scratch/<feature-slug>/actionables/<NN>-<slug>--<mode>.md
```

`<mode>` is `actionables` or `pseudocode`. Fill every section; drop a subsection only if truly N/A (say so).

---

## Shared header (both modes)

```markdown
# <NN> — <Ticket title> — <mode>

**Source ticket:** <path or URL>
**Parent spec:** <path or URL or "none loaded">
**Generated:** <ISO date>
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** actionables | pseudocode
**Scope run:** ticket | set

## Goal

<1–3 sentences: user-facing behaviour this ticket delivers>

## Preconditions

- [ ] Blockers done: <list or "none">
- [ ] Other: <env, feature flags, data seeds, or "none">

## Acceptance criteria → verification

| AC | How the human proves it |
|----|-------------------------|
| <criterion 1> | <test command, manual path, or check> |
| <criterion 2> | … |

## Do not touch

- <files/areas out of scope for this ticket>

## Deviations

- <One line per divergence from a ticket AC. Format: "AC said X; live code shows Y; default taken: Z." Example: "AC said add PLANNER_TIMEOUT_MS; planner.js:267 already reads PLANNER_INVOCATION_MS; default taken: add PLANNER_TIMEOUT_MS literally and leave old key in place (deprecation is a follow-up).">
- <Or "None — every AC mapped cleanly to live code.">
```

---

## Mode: `actionables`

After the shared header:

````markdown
## Steps

### Step 1 — <short name>

- **File:** `path/to/file.ext` *(modify | create | delete)*
- **Find:** <symbol, function, route, component, or line region description>
- **Change:** <what to do in plain language>
- **Sketch:** *(optional, ≤15 lines)*

```<lang>
// only the shape of the change — not a full working module
```

- **Done when:** <observable local check>

### Step 2 — …

…

## Order notes

- Why this sequence (deps between steps).
- Safe stop points (after which AC partial progress is still coherent).

## Final verification

1. <command or manual flow for full ticket AC>
2. <typecheck / lint if project uses them>
3. <regression touchpoints if any>

## Open questions

- <only blockers; else "None — defaults taken: …">
````

### Actionables quality bar

- Every step has a real **File** path from this session’s exploration.
- Prefer **modify** existing symbols over **create** new files.
- Sketches show shape (types, branch structure, API), not a paste-and-ship PR.
- Steps are ordered so each leaves the tree closer to green, not “all types then all impl.”
- Map every AC to at least one step and one verification row.

---

## Mode: `pseudocode`

After the shared header:

````markdown
## Walkthrough

### Unit 1 — <behaviour name>

**Purpose:** <what this unit achieves for the user or system>

**Inputs / outputs:**
- In: …
- Out: …

**Pseudocode:**

```
function handleThing(input):
  // 1. …
  // 2. …
  return result
```

**Touch list (live paths):**
- `path/a.ts` — <why>
- `path/b.test.ts` — <why>

### Unit 2 — …

…

## End-to-end sequence

1. <user or system trigger>
2. <unit order>
3. <observable result>

## Final verification

1. …
2. …

## Open questions

- …
````

### Pseudocode quality bar

- Units follow the vertical slice (request → domain → persistence → response/UI), not layer dumps.
- Pseudocode uses project vocabulary (glossary/ADR terms).
- Every unit ends with a **Touch list** of real paths.
- Still no full implementation dump — if a unit needs a long algorithm, outline phases and point to an existing similar function in-repo as a pattern.

---

## Scope `set` index (chat + optional index file)

When `--scope set`, also print (and optionally write `.scratch/<feature>/actionables/README.md`):

```markdown
# Actionables index — <feature>

| Ticket | Mode | File | Blocked by | Ready? |
|--------|------|------|------------|--------|
| 01 — … | actionables | `01-…--actionables.md` | none | yes |
| 02 — … | actionables | `02-…--actionables.md` | 01 | no |
```

Work recommendation: start at the first **Ready?** row.

---

## Tracker-only tickets

If there is no local issues tree yet:

1. Create `.scratch/<feature-slug>/actionables/`.
2. Put `**Source ticket:** <URL>` in the header.
3. Do not invent a local issues file unless the user asks to mirror tickets locally.
