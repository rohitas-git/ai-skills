# Specification format

Use only sections that materially define the accepted contract. A small change may need a few lines;
a cross-surface feature may need every section.

```markdown
# <Outcome-oriented title>

## Context and outcome
Who has what problem, what observable outcome is accepted, and why it matters.

## Scope
- In: accepted behavior or capability
- Out: explicit non-goal

## Requirements and acceptance evidence
| ID | Observable requirement | Source/decision | How acceptance is demonstrated |
|---|---|---|---|
| R1 | ... | ... | ... |

## Applicable constraints
Compatibility, security/privacy, accessibility, operational, data/migration, and rollback constraints
that are actually supported by the source or verified repository evidence.

## Assumptions and open decisions
Label assumptions explicitly. An open decision that changes behavior or acceptance blocks a settled spec.

## Evidence and provenance
Pinned source candidate, evidence cutoff, repository/worktree/HEAD when applicable, and known coverage gaps.
```

Do not pad the artifact with generic architecture, commands, file paths, test counts, user stories, or
metrics. Include such details only when they are accepted constraints and likely to remain stable. A
spec states the observable contract; implementation planning and ticket slicing remain separate jobs.

## Technical design and independent review

For an accepted software design, include the agreed component boundaries, observable interfaces,
data flow, code/source links, and viable alternatives with their recorded rejection reasons.
Keep feature intent separate from any detailed implementation plan; `/1-write-plan` owns the latter.
A spec may exist without a plan. Re-read the pinned concept brief before finalizing: report changed
decisions and material additions (architecture, external interfaces, dependencies) to the owner.
Never invent alternatives or approval to fill a template. A fresh reader should understand the
contract without the earlier conversation; missing links and unexplained project terms stay gaps.

If requested, [design review](../../1-design-review/SKILL.md) checks feature comprehension/design
first and readiness only when a detailed plan exists. Its [workflow map](../../1-design-review/references/workflow-and-connections.md)
preserves the EGM brief → design → review → resolution → approved implementation → drift chain.
This is a modified adaptation of Google EGM (Apache-2.0); [source and license](../../1-design-review/references/source-review.md).

## Version scope and follow-up changes

Use the project's established specification format and storage conventions; do not create a second
spec beside an existing canonical system. Name the version or immutable baseline when that matters
to acceptance. Keep deferred ideas separate from accepted requirements, with a short reason for
deferral. An idea captured in the same document is not automatically in scope.

For a settled change to shipped behavior, prefer a small delta that links the original contract:

- current behavior and its source revision;
- proposed behavior and the reason for the change;
- acceptance evidence, compatibility invariants, and changed constraints;
- explicitly deferred work and unresolved decisions.

Inherit unchanged requirements by reference instead of copying them. A proposed delta does not
redefine what is deployed or authorize implementation. Preserve historical decisions; reconcile the
canonical current-state spec and mark the delta implemented only when the caller authorizes that
documentation update and release evidence supports it. Do not silently expand accepted scope during
implementation or impose a new versioning system on a small change.

Adapted from Addy Osmani et al., MIT: [source and ingestion record](../../../guidelines/catalog/ingest-addyosmani-2026-11-15.md).
