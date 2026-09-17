# API and interface design wiring audit

Date: 2026-09-11  
Skill: `1-api-and-interface-design`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the full live package: `SKILL.md`, the 375-line operative guide, and the
vendor/source map. Reviewed the relevant Architecture and Ship skill, workflow JSON,
HTML, and flows surfaces. This establishes the route and design contract; it does not
prove any particular API implementation or consumer is compatible.

## Decisions and changes

- Narrowed the atomic job to one consumer-visible API or cross-module contract and its
  evolution rules. Internal module design, detailed failure mechanics, model-facing tool
  schemas, MCP server implementation, deprecation execution, and database migrations keep
  their specialist owners.
- Kept Architecture as primary owner and added Ship as a formal soft caller. Both parent
  route metadata, bodies, workflow JSON, HTML, and flows now agree; a contract returns to
  Ship only when implementation was requested.
- Added explicit design/advice, read-only assessment, and authorized-implementation modes.
  Advice/review create no worktree; implementation confirms repo, branch, worktree path,
  dirty ownership, and scope, reusing the caller workspace or conditionally using
  `1-git-worktrees` before returning.
- Added a contract matrix covering consumers, authorization, schemas, effects, failure
  outcomes, limits, pagination/streaming, retry/idempotency, and compatibility evidence.
- Corrected the operative guide's universal claims: internal data is not inherently trusted;
  additive/optional changes are not automatically compatible; pagination, PATCH/PUT, and
  deletion semantics depend on the contract; broker guarantees do not automatically cover
  external effects.
- Marked the idempotency code as an incomplete state-transition sketch, distinguished its
  uniqueness claim from the whole design, and based retention on supported replay paths.
- Clarified that the full guide is adapted reference material, while the live main file owns
  routing and authority. Upstream installation/plugin behavior remains inactive.
- Added regression coverage for dual membership, both parent `next` and HTML surfaces,
  F-ARCH1, workspace modes, source disclosure, and corrected compatibility guidance.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **39 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 62 informational findings,
  and 0 hub-member orphans.
- `git diff --check`: passed.
- Main skill remains below the 120-line lean target; all three package files were reviewed.

## Remaining limits

- No concrete OpenAPI, GraphQL, protobuf, client, or runtime was supplied, so protocol-specific
  compatibility and behavior remain caller verification responsibilities.
- The Architecture and Ship hubs received scoped route changes only; their complete semantic
  audits remain separate pending tracker items.
