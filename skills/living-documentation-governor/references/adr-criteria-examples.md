# ADR Criteria Examples

## Good ADR Candidate

**Decision**: Switch from in-memory session storage to MongoDB-backed checkpointer with specific serialization format for LangGraph turns.

**Why it meets criteria**:
1. Hard to reverse: Requires data migration, changes to all session-related code, potential downtime or dual-write period.
2. Surprising without context: The choice of serialized turns + dedicated MongoDB client is not obvious from the code alone.
3. Real trade-off: Between simplicity of in-memory (fast, easy) vs durability, scalability, and LangGraph compatibility.

**Result**: Create `docs/adr/0001-dedicated-langgraph-mongodb-client.md` explaining alternatives considered and rationale.

## Another Good Candidate

**Decision**: Implement layered authentication boundaries (internal vs user vs admin) with separate middleware and early rejection.

**Why**:
- Hard to reverse (security model change).
- Surprising (many apps use single auth layer).
- Trade-off between security isolation vs development ergonomics and maintenance cost.

## Bad ADR Candidate (Do Not Create)

**Decision**: "Use Express.js for the web framework."

**Why it fails**:
- Not hard to reverse in a meaningful way for most projects (common choice).
- Not surprising.
- No meaningful trade-off being resolved in the current context (it was the baseline).

**Correct place**: Mention in `docs/architecture.md` or `docs/guides/operations.md` as "we use Express with the following middleware stack..."

## Another Bad Example

**Decision**: "Add a new endpoint at /api/v1/ace/chat"

**Why it fails**:
- Purely additive and reversible.
- Not surprising.
- No architectural trade-off.

**Correct place**: Update `docs/api_reference.md` (or the OpenAPI spec) and `docs/guides/frontend.md` if relevant.

## When an Existing ADR Needs Superseding

The original auth ADR described a two-layer model. Later requirements force a three-layer model with internal service accounts.

**Action**:
- Create `docs/adr/0005-three-layer-auth-with-internal-accounts.md`
- In the new ADR, explicitly state it supersedes 0004.
- Update living docs (`docs/guides/auth.md`) to reflect current state.
- Do **not** edit the old ADR file.