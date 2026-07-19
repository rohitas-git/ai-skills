---
name: create-skill
description: >
  Thin entry for authoring skills. Loads skill-creator (create/improve/eval SSOT),
  then butler ingest for catalog citizenship. Use when scaffolding or improving a skill,
  or /create-skill.
disable-model-invocation: true
---

# Create Skill

This skill is a **thin wrapper**. The authoring body SSOT is **`/skill-creator`** (draft → eval → improve).

## Process

1. Load and follow **`skill-creator`** end-to-end for create/edit/optimize/eval work.
2. When the skill folder is ready for this catalog, hand off to **`/butler` ingest** (integration test → confirm → indexes/flows/lock).
3. Craft theory (predictability, progressive disclosure) remains **`/writing-great-skills`** — not replaced here.

## Don't use when

- Installing skills from the public ecosystem → `/find-skills`
- Catalog routing only ("which skill?") → `/butler` query
- Editing catalog layout / deprecations without a new skill body → `/butler` organize
