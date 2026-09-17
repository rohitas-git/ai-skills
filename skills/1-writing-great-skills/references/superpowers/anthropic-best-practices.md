# Anthropic Skill-Authoring Guidance — House Adaptation

Source: Anthropic's public skill-authoring guidance, captured previously in this package.

Status: provenance note only; current house rules and the live host contract take precedence.

## Useful principles retained

- Assume the model already knows general concepts; spend tokens on non-obvious domain facts and failure boundaries.
- Match instruction specificity to task fragility.
- Put a precise name and discovery description in frontmatter.
- Keep `SKILL.md` lean and disclose conditional depth through directly reachable files.
- Use clear sequential workflows and validation loops where correctness benefits.
- Prefer one default over an undifferentiated menu.
- Make scripts bounded, non-interactive, verifiable, and explicit about read-versus-execute intent.
- Test real use and revise from observed navigation or failures.

## House qualifications

This catalog uses depth-prefixed names and `metadata.catalog` route fields, enforced by `/0-skill-manager`. Its lean target is stricter than the source's broad 500-line guidance.

Testing is proportional: no mandatory three evaluations, model matrix, agent pair, or baseline for every edit. Large references still impose maintenance and prompt-injection risk when opened; “not loaded yet” is not a reason to keep sediment.

Package installation, network retrieval, script execution, worktree creation, catalog placement, sync, commit, push, publication, and external mutation are distinct effects requiring compatible authority. Never instruct installation merely because a dependency is absent.

For current behavior use `/0-skill-creator`; for craft use `/1-writing-great-skills`.

