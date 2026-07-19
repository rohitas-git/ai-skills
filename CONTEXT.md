# Domain glossary — skills catalog

Catalog vocabulary for the Rohitas skills monorepo. Implementation detail lives in skills and ADRs, not here.

| Term | Meaning |
|------|---------|
| **Catalog skill** | Skill under a discoverable Matt bucket (`engineering` / `productivity` / `misc` / `personal` / `in-progress`). Not vendor-only packs. |
| **Tombstone** | Skill under `deprecated/` with a named successor; not promoted; not host-installed via symlink sync. |
| **Wrapper** | Thin entry skill whose body loads an SSOT skill. |
| **Implement closer** | Review skill `implement` runs after `tdd` and before commit: multi-axis **code-review**. |
| **Review axis** | One evaluation dimension inside `code-review`: Spec, Standards, or Maintainability. |
| **Applicable axis** | Axis the pre-review scan decides has enough inputs; otherwise soft-skipped and reported. |
| **Schema steward** | Sole owner of Rohitas’s Notes folder/frontmatter rules: **rohitas-vault-wiki**. |
| **Authoring SSOT** | Skill that owns create/improve/eval of skill bodies: **skill-creator** (`create-skill` is a wrapper). |
