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
