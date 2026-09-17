# Teaching-workspace wiring audit

Reviewed skills:

- `1-teach`
- `1-teaching-workspace`
- `1-lesson-authoring`
- `1-learning-progress-record`
- `1-learning-glossary` (newly promoted atomic operation)

Operative shared schemas reviewed in full:

- `MISSION-FORMAT.md`
- `RESOURCES-FORMAT.md`
- `LEARNING-RECORD-FORMAT.md`
- `GLOSSARY-FORMAT.md`

## Result

The former course workflow is now five explicit atomic contracts. `1-teach` selects one
operation and performs no workspace work. Its leaves establish one confirmed mission,
author one non-overwriting lesson, append one evidence-labeled progress record, or govern
one glossary term. Every write leaf requires an exact workspace and, when applicable,
repository/worktree/branch/`HEAD`, dirty ownership, allowed paths, and current evidence.
No skill creates or switches a worktree, assumes the current directory, commits, pushes,
publishes, merges, researches, or silently chains another operation.

The shared schemas now preserve the distinctions needed for safe reuse:

- a mission records observable outcomes and its evidence basis without inferred learner
  traits or fixed quotas;
- a resource entry records provenance, checked state, limitations, and deprecation while
  treating external content as untrusted data;
- progress is append-only and distinguishes demonstrated, self-reported, corrected, and
  tutor-supplied evidence; supersession is declared by a new record;
- a glossary mutation changes one entry, preserves aliases and historical meaning, and
  cannot override mission, source, repository, safety, or user authority.

Learn metadata, workflow JSON, hub HTML, and Butler flows expose all five skills and
return one leaf result to the actual caller. The wiki index includes the new glossary
leaf. Non-Git teaching directories explicitly require no worktree; Git-backed course
artifacts use the caller's existing exact worktree and acknowledge that external sources,
accounts, and services remain shared.

## Verification

Sixteen focused Teach/Learn routing checks pass. The full routing suite passes all 241
tests; route-index generation reports 217 live skills; catalog lint passes with 0
critical findings, 0 warnings, 59 informational findings, and 0 hub-member orphans;
`git diff --check` passes. No commit, push, merge, host sync, publication, external
research, or workspace-course mutation was performed during this audit.
