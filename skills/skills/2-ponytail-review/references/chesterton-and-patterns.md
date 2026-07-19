# Chesterton's Fence + simplification patterns (merged from vendor)

Source: archive vendor `code-simplification`. Complements one-line delete findings.

## Chesterton's Fence

Before deleting "useless" code: state **why it might exist** (or find the git blame/ADR). If you cannot, investigate once — then delete only with evidence.

## Pattern → simplify

| Smell | Prefer |
|-------|--------|
| One-implementation interface | Inline until second impl |
| Config nobody sets | Hardcode or delete |
| Wrapper with no policy | Call through |
| Hand-rolled util vs stdlib | stdlib / platform |
| Premature generality | YAGNI; extract on second use |

Still output **one line per finding** in the main skill format. Net metric remains `net: -N lines possible`.
