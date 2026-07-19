# Knowledge Placement Examples

## Example 1: New Authentication Middleware

**Changed code**: `src/middlewares/auth.js`, `src/middlewares/checkAdminAuth.js`

**Trigger rule matched**: "authentication" → docs: [`docs/guides/authentication.md`, `docs/adr/0004-layered-auth.md`]

**Decision**:
- Primary canonical owner: `docs/guides/authentication.md` (how it works now)
- ADR already exists and still accurate → no new ADR needed
- Update `docs/guides/authentication.md` with the new behavior and any limitations.
- If the layering decision was the key change, consider whether a new ADR superseding 0004 is warranted (only if it meets all three strict criteria).

## Example 2: New Prompt Engineering Pattern

**New concept** introduced in `src/prompts.js` / orchestration layer and used by planner and worker nodes.

**No existing trigger** yet, or existing "orchestration-and-prompts" rule points to `docs/guides/prompts-and-orchestration.md`

**Decision**:
- Canonical owner: `docs/guides/prompts.md`
- If this is a significant new durable pattern that is surprising and hard to reverse → propose ADR.
- Otherwise, document the pattern and usage in the prompts guide.
- Update `CONTEXT.md` only if new domain terminology is introduced.

## Example 3: Superseded Session Serialization Design

Old design document in `docs/archive/old-session-design.md` explains a previous approach.

**Current code** has moved to a new model in `src/models/Session.js` + `src/persistence/`.

**Decision**:
- Living docs (`docs/architecture/sessions-and-memory.md` or `docs/guides/sessions.md`) must already describe the current implementation.
- Keep the old document in archive with a clear header: "Historical — superseded by [current living doc] on [date]. Retained for understanding migration path."
- Do **not** update the archived file to match current behavior.

## Example 4: Glossary Term Clarification

User asks to define "AceStaging" precisely.

**Decision**:
- Update `CONTEXT.md` (the glossary).
- Do **not** create a new page unless the term requires substantial explanation beyond definition + relationships.
- If the term is central to agentic tools, ensure `docs/architecture/agentic-tools.md` links to the glossary entry.

## Bad Example (Avoid)

Creating `docs/guides/new-auth-flow.md` when `docs/guides/auth.md` already exists and is the canonical owner.

**Correct action**: Extend `docs/guides/auth.md` (or the relevant subsection) and update any trigger rules if the ownership granularity changed.