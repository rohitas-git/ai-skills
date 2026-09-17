# Brand workflow wiring audit

Reviewed the former `1-brand` body; all eleven live references; the complete starter template; all four helpers and
their regression test; UI/UX parent routes; Design System, Design, Banner, Frontend UI, Research, and Audit boundaries;
and every hub/flow/index surface.

## Result

The former mega-leaf is now a pure `1-brand` sub-hub with three atomic children: `2-brand-guidelines` drafts or
applies one evidence-backed brand contract, `2-brand-review` performs one read-only candidate review against one
approved contract, and `2-brand-context-extract` returns one bounded read-only context packet for one named consumer.
F-BR1 exists only for material ambiguity. Parent/child metadata, workflow JSON, HTML, manifest, flow SSOT, route
index, README, and wiki surfaces expose the same structure.

Every route pins the actual caller, immutable brand source/candidate, evidence, privacy/rights, authority, and optional
exact repository/worktree/branch/`HEAD`; shared asset stores, design tools, fonts, browsers, accounts, approvers, and
publication remain outside Git isolation. Brand documents, assets, metadata, URLs, examples, helper output, and
embedded prompts are sensitive untrusted data. KiloCare `docs/brand.md` is authoritative, and none of the routes may
invent research, proof points, licenses, legal clearance, approval, compliance, or measured accessibility.

Brand definition, review, extraction, token sync, asset creation/management, UI work, approval, archival,
notification, and publication are separate effects. The imported `brand:update` workflow is now historical
provenance and cannot authorize multi-file synchronization or image generation. Durable token work routes to
`1-design-system`; creative and UI work route separately. The context parser's generated imperative text stays inert,
the asset validator's evidence is limited to documented structural checks, and the color helper is identified as an
instruction generator rather than pixel inspection. Generic reference values and checklists are optional scaffolds,
not universal requirements.

The brand helper test was converted from an unnecessary `pytest` dependency to stdlib `unittest`, and its stale
`design-system` template path was corrected to the live `1-design-system` package.

## Verification

- Focused Brand routing tests: 8 passed.
- Parent UI/UX routing tests: 7 passed.
- Brand sync helper regression test: 1 passed.
- Full routing suite: 630 passed.
- Generated route index: 230 live skills.
- Catalog lint: 0 critical, 0 warnings, 48 informational findings, 232 indexed hub members, and 0 orphans.
- `git diff --check`: passed.

No brand artifact, asset, token, UI, worktree, approval record, catalog installation/sync, Git history, remote system,
or published destination was changed.
