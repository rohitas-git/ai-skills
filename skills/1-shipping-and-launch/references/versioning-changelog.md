# Versioning and changelog boundary

Use only when the release has a repository- or ecosystem-defined version contract. An internal
deployment, mutable web application, data rollout, or infrastructure change does not automatically
need Semantic Versioning or a Git tag.

## Determine the contract

Inspect package manifests, release tooling, tags, changelog policy, compatibility promises, and
consumer update model. Record:

- version owner and source of truth;
- artifact(s) covered by the version;
- compatibility surface and supported consumers;
- whether tags, manifests, generated files, or release metadata must agree;
- changelog audience and canonical location.

If the project uses Semantic Versioning, classify against its documented public API:

| Change | Usual bump before 1.0 caveats/project policy |
|---|---|
| incompatible public contract | major |
| backward-compatible capability | minor |
| backward-compatible correction | patch |

Do not declare a major bump merely because compatibility is uncertain. Investigate consumers and
route contract/deprecation questions to `/1-api-and-interface-design` or
`/1-deprecation-and-migration`; unresolved compatibility blocks the version decision.

## Human changelog

Summarize user/operator impact rather than copying commit subjects. Include breaking changes,
migration or rollout requirements, security implications at an appropriate disclosure level, known
limitations, and recovery notes when relevant. Use the project's existing headings and format.

Editing version/changelog files requires repository-edit authority. Creating tags, GitHub/GitLab
releases, publishing packages, pushing, or notifying consumers are separate remote effects and are
never implied by preparing release metadata. Report the exact candidate and which artifacts remain
unpublished.
