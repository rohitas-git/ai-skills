# Recommended Q&A Response Template

Use this structure for every project-knowledge question answer.

```
{Answer prose in the language of the user's query. Be concise but complete. Include inline citations like (source: docs/guides/authentication.md, section: Layered Auth) or (source: src/middlewares/auth.js).}

---
**Key Evidence** (include only when a short verbatim quote clarifies meaning or shows contradiction)
> "Exact original wording from source" (source: path/to/file.ext, section: X)

---
**Sources Consulted**
*Living documentation:*
- `docs/guides/authentication.md` — primary canonical owner for authentication behavior; provided current implementation details and limitations.
- `docs/CONTEXT.md` — confirmed glossary definitions for key domain terms.

*Code / configuration / OpenAPI directly read:*
- `src/middlewares/auth.js` — verified exact middleware logic and error paths.
- `config/swagger.js` — confirmed OpenAPI schema for auth-related endpoints.

*Trigger rules involved:*
- "authentication" rule — matched because `src/middlewares/auth.js` changed; confirmed that `docs/guides/authentication.md` was updated in the same change.

---
**Wiki Gap / Suggested Action** (include only when the answer was primarily from raw sources not yet folded into living docs)
📥 **Wiki Gap detected**
This answer was synthesized from current source code. 
**Suggested update**: Add a section on internal service account authentication to `docs/guides/authentication.md`.
**One-sentence summary**: Document the new internal auth path, its early rejection logic, and how it differs from standard user/admin flows.
Would you like me to draft the update?
```

**Rules for this template**:
- The Sources block is **mandatory**.
- List only items that directly contributed to the final answer.
- Living docs subsection first.
- Clearly separate code/config from docs.
- Mention trigger rules when they influenced which docs were consulted.
- Offer to persist important new synthesis back into the canonical owner.