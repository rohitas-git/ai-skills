# Engineering diagrams and non-UI examples

Use these within the walkthrough page. Keep the diagram optional, but give every material non-UI behavior change
a concrete example. A passing test name or “backend only” is not a demonstration of the effect.

## Choose the smallest useful diagram

| Change to explain | Diagram | Show |
|---|---|---|
| Request, worker, service or event exchanges | Sequence | Actors, ordered messages, result and changed interaction |
| Validation, retries, permissions or branching | Flowchart | Trigger, relevant decisions, success and failure paths |
| Lifecycle or allowed transitions | State | Previous/new transitions, guards and terminal states |
| Responsibility or dependency boundaries | Component | Relevant caller, owner and changed dependency |
| Storage or schema relationships | Data/ER | Relevant fields, keys, relations and change in their meaning |

- Omit diagrams for simple copy or value changes when an example explains the effect more clearly.
- Use matching actors and conditions for before/after views. Label removed paths and newly added edges in words.
  A single diagram with a clear change legend is enough when two would repeat the same information.
- Cite source paths/symbols and base/head revisions near the diagram. Label inferred relationships and missing context.
  Do not invent a service, database table, event, trust boundary, or runtime call from a suggestive name.
- Use an existing local Mermaid renderer if available, otherwise inline SVG/HTML in the page.
  Do not add a dependency, remote renderer or CDN just for a diagram. A raw Mermaid fence alone is not a rendered diagram.
- Keep diagrams readable on narrow screens, with text labels, directional arrows and a text explanation.
  Do not communicate additions/removals only through color. Inspect for clipping and overlapping labels.

## Example contract

For each change show:

1. **Situation and input:** synthetic payload, starting state, actor/role, flags and relevant limits.
2. **Before:** result under those conditions in the base version, including errors or side effects.
3. **After:** result under the same conditions in the PR version; identify the meaningful difference.
4. **Effect and why:** practical consequence, stated requirement or inferred purpose, and what undoing it would restore.
5. **Evidence:** exact source anchors and whether this is source-derived, illustrative, or exercised by a recorded check.

Use actual field names, enum values, status codes and semantics from the candidate. Show a meaningful failure,
boundary or permission case when changed. If an input is no longer accepted, keep it the same to expose that difference.
Never fabricate a successful response, timing measurement, deployment result or safe migration/rollback claim.

## Worked teaching case: validation with no screen change

This is fictional. Replace every field, limit and result with evidence from the actual PR.
Assume the supplied before/after handler shows that negative quantities were accepted before, but rejected after.
A linked requirement says quantities must be positive. No handler run or deployed result was supplied.

**Situation:** The same permitted caller submits `{"quantity": -1}` under the same configuration.

| | Base | PR head |
|---|---|---|
| Decision | Negative quantity accepted | Negative quantity rejected before the write |
| Expected effect | Invalid quantity can reach storage | This invalid input cannot reach the write through this handler |

**Why:** The linked requirement prohibits non-positive quantities.
**Why keep it:** Undoing the guard would allow the same invalid input again unless equivalent validation replaces it.
**Evidence label:** Source-derived example, not executed. This does not establish that other write paths validate quantities.
Also show a valid positive quantity if its continued acceptance is supported by the code.

A flowchart is useful if several guards changed. For this single guard, the input/output example may be sufficient.

## Other cases to cover

- **Background work:** show event/input, initial state, worker action and final state. Use a sequence or state diagram
  when delivery, retries or idempotency matter. Do not enqueue a real job to populate the page.
- **Migration/schema:** show synthetic records and relevant relationships before/after, with null/default/constraint
  behavior from the migration. Mark the example unrun; do not apply migrations or imply existing production data changed.
- **Permissions:** use the same synthetic actor and request to show allowed/denied differences; include the affected role.
  Do not sign in as a real person or change permissions merely to produce a screenshot.
- **Internal refactor:** show the same input and unchanged output, then the old/new responsibility or call structure.
  Explain the stated maintenance goal. Do not manufacture a speed or correctness improvement.
- **Removal:** show the old supported input and what now happens, including an evidenced replacement if one exists.
  Explain the value of keeping the removal, rather than arguing to retain the deleted feature.

## Evidence and limits

If execution would need a database, credentials, a remote service or side effects, keep the example illustrative.
An already supplied or separately permitted isolated check can support an observed result; record its exact command,
fixtures, revision and outcome. Rendering a response object in a browser proves only that the page displayed that object.
When before/after evidence is missing, mark the gap instead of inventing the missing half.
