# Atomize Workflow Detail

Load only for the exact overlap cluster pinned by `/1-skill-atomize`.

## Evidence model

Content overlap exists when two live skills plausibly claim the same request and substantially repeat procedure or output. Shared domain words alone are not overlap.

Exclude:

- explicit hub, wrapper, pipeline, leaf, axis, satellite, or caller-return relationships;
- cousins with distinct positive boundaries;
- archived/vendor packages unless explicitly included;
- generated route projections as behavioral truth.

## Detection

1. Record each candidate's exact path, revision, hub parents, role, description, triggers, output, effects, and authority.
2. Compare trigger intersection, procedural duplication, and whether either skill silently owns the other's outcome.
3. Classify:
   - **same job** — one canonical owner is likely;
   - **trigger collision** — jobs differ but route wording overlaps;
   - **adjacent jobs** — explicit handoff is enough;
   - **shared theme** — no change.
4. Cite evidence for every classification and state coverage limits.

## Resolution

Use the smallest move that restores one-job ownership:

1. positive Boundary and redirects;
2. remove duplicated cousin procedure;
3. merge true duplicates only when identity/behavior loss is explicitly accepted;
4. split only when distinct invocation or sequence jobs remain after pruning.

For every applied cluster, update only directly affected descriptions, metadata, flows, hub workflow/HTML, and human indexes. Generated projections are regenerated from their sources. Re-read targets before writing and preserve unrelated dirty content.

## Authority

An explicit atomize/fix request selects **apply** for the named scope. A review/audit request selects **assess**. Ask only when scope is materially ambiguous, a merge/split would change public identity or discard behavior, or the operation would delete, overwrite, install, sync, publish, commit, push, or mutate external/global state.

## Completion

The cluster has one-job descriptions, valid caller/return handoffs, no stale route surface, focused route tests, and `/1-skill-linter` evidence. Report applied and deferred items. No automatic catalog-wide expansion.

