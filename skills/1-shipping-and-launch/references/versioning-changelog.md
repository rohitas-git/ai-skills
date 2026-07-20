# Versioning + human changelog (harvested)

Source: archive vendor `git-workflow-and-versioning` (Release & Versioning).  
Use with **`/1-shipping-and-launch`**. Day-to-day commits → `/1-git-commit-helper`.

## When versioning matters

Anything with **consumers** (other teams, packages, deployed clients) needs a version contract. “Latest on main” is not enough.

## Semantic versioning

`MAJOR.MINOR.PATCH`:

| Bump | Meaning |
|------|---------|
| **MAJOR** | Breaking — consumers must change |
| **MINOR** | Backward-compatible feature |
| **PATCH** | Backward-compatible fix |

If unsure whether a change is breaking, assume **major**. Behavior consumers relied on is a break even if the diff looks small (Hyrum). See `/1-api-and-interface-design`.

## Tags as source of truth

- Annotated tags: `git tag -a v1.4.0 -m "Release 1.4.0"`
- Derive published version from the tag; avoid hand-editing version in many files out of sync

## Changelog for humans

Not raw `git log`. Curated, newest first, by impact:

`Added` · `Changed` · `Fixed` · `Deprecated` · `Removed` · `Security`

Write the entry **with the change**, not reconstructed at release day. Breaking changes need migration notes and deprecation windows (`/1-deprecation-and-migration`). Deploy/go-no-go remains this skill’s pre-launch checklist.
