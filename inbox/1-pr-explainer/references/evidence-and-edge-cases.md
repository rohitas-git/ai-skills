# Evidence and edge cases

Load when the source is incomplete, intent conflicts with the code, or a change removes or reorganizes behavior.
These fictional cases illustrate the explanation contract. They are not results from actual PRs or model evaluations.

## Evidence rules

- Pin the intended base and head before comparing. A dirty checkout is not the PR.
- Build a private coverage list from the changed files. Map each material change to a feature group or a stated gap.
  Include operational changes even when they have no screen: a migration, permission change, dependency, or deployment flag can matter.
- Prefer links to the exact PR discussion, revision, file, and lines that support a claim.
  For pasted material, use supplied hunk names or short quoted identifiers. Say when no stable location was supplied.
- A description supports stated intent. Code supports expected behavior. Tests describe checked cases.
  A recorded run supports only its tested scope and revision; passing unit tests alone do not confirm the full user journey.
- Explain source conflicts directly: “The description promises X; the supplied code still does Y.”
  Leave unresolved intent unknown. Do not manufacture a requirement to reconcile the sources.
- If the diff is truncated or inaccessible, explain the visible scope and name the missing material.
  Ask for missing evidence only when it prevents a useful answer. Do not claim complete coverage.

## Case 1: reason missing

**Input:** A diff changes a retry limit from three attempts to five. No requirement, discussion, or run is supplied.

**Expected explanation:** Before, the system allowed three attempts; after, it allows five.
The author's reason is unknown. Allowing more retries is an inferred purpose, not proof of better reliability.
Undoing the change would restore the three-attempt limit. Whether five attempts are necessary remains unknown.

**Reject:** “This fixes network failures” or “Never remove this reliability improvement.”

## Case 2: removal with a replacement

**Input:** The PR removes an old export endpoint. A linked requirement retires it; a new endpoint supports active clients.
The deployment configuration also stops routing requests to the old endpoint.

**Expected explanation:** Explain the old path, the replacement, and which callers lose access.
The reason is the stated retirement requirement. Keeping the removal preserves that retirement.
Restoring one handler alone may not restore access because routing also changed.
Restoring the retired service is not automatically beneficial or safe.

**Reject:** Treating “Why keep it” as a reason to keep the deleted endpoint, or giving an unsupported rollback recipe.

## Case 3: internal refactor

**Input:** Two callers now use one shared parser. The PR description says this avoids maintaining duplicate parsing rules.
The available code shows no intended change in accepted inputs. No timing measurements are supplied.

**Expected explanation:** Classify the change as Internal. Explain the shared parsing path and the stated maintenance goal.
Undoing it would restore duplicate logic, with no demonstrated immediate user-visible failure.
Do not claim faster execution or fewer bugs without evidence.

**Reject:** Inventing a runtime benefit to justify keeping a refactor.

## Case 4: incomplete coverage and stale CI

**Input:** The file list includes a migration, but its diff is missing. A test was added at the current head.
The only passing CI run belongs to the previous head.

**Expected explanation:** Explain the visible changes and identify the migration as unexamined.
Say the test exists, but current-head results are unavailable. Attribute the passing run to the older revision.
Leave database behavior and full PR coverage unverified.

**Reject:** “All changes explained,” “The new test passed,” or “The migration is safe.”

## Final review

Check the output against the supplied evidence, not against how persuasive it sounds.
Every material group needs before/after conditions, a stated or inferred reason (or unknown), and a specific undo consequence (or unknown).
Keep dependencies, exceptions, coverage gaps, source conflicts, and validation limits visible.
