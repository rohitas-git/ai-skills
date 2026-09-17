# Query procedure

Use this only after the main skill has pinned the root, question, snapshot, authority, privacy
boundary, and exclusions. The active vault layout and schemas override every example here.

## 1. Form a retrieval plan

- Extract the question's load-bearing entities, relations, time window, and requested output.
- Identify likely active registry, MOC, index, or canonical-note entries by name/metadata first.
- Search content only when metadata cannot narrow the candidate set enough.
- State any excluded private areas, archives, attachments, generated/plugin views, or unreadable
  files. Never silently substitute another vault or outside source.

## 2. Retrieve incrementally

For each candidate, record path, version, relevant heading/locator, and reason for reading it.
Read the minimum relevant selection. Expand to one named local neighbor only when a specific
unsupported claim requires it. Stop when the question is answered, the remaining uncertainty
is known, or further reading would exceed authority/scope.

Search results establish possible relevance, not claim truth. A backlink establishes a relation,
not agreement. A note title establishes neither content nor freshness. Archives/raw sources may
be useful evidence but do not silently override active canonical notes.

## 3. Reconcile evidence

Build claim rows containing:

- claim or question component;
- exact supporting/contradicting note and heading;
- observed wording/date/condition;
- status: note-backed, user-supplied, synthesis, conflict, unknown, or out of scope;
- limits caused by missing, stale, ambiguous, or unreadable evidence.

When notes disagree, preserve each position and its conditions. Do not manufacture consensus,
choose the newest file without a schema rule, or use general knowledge to patch a vault gap.

## 4. Return one answer

Lead with the direct answer. Cite note-backed claims near the claim using resolvable wikilinks,
then provide a compact evidence list and explicit gaps/coverage. Include snapshot identity when
it matters to reproducibility. Say `not found in the inspected scope` rather than `the vault has
nothing` unless the authorized complete population was actually checked.

If the question cannot be answered, return the searched scope and exact missing evidence. Offer
no automatic follow-on. The caller may separately choose research, ingest, Concept teaching, or
another bounded query.

## 5. Optional persistence packet

Only when the user separately wants the answer preserved, return a proposed packet to
`/1-vault-ingest`: fixed answer text, original question, source ledger, conflicts/gaps, snapshot,
candidate destination if grounded, and requested outcome. This procedure grants no write or
schema authority and does not create a page, update an index/MOC, or append a log.
