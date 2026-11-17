# Context contract and example

Use the existing project format; these are required questions, not a new mandatory configuration schema.

| Boundary | Contract |
|---|---|
| Purpose | Supported questions, expected evidence and explicit no-answer cases |
| Sources | Owner, version, provenance, authorized scope, source locator, authoritative versus supplemental |
| Preparation | Formats, parsing, semantic chunking, metadata and deletion/update lineage |
| Retrieval | Trusted identity filters, query construction, retrieval/ranking and relevance decisions |
| Context | Budget, redundancy, conflicts, instruction/data separation and source attribution |
| Memory/cache | User/session/tenant namespace, permissible writes, retention and invalidation |
| Freshness | Update trigger, index age, stale-data behavior and permission-revocation propagation |
| Quality | Retrieval labels, answer support/completeness, useful end-to-end result and checker qualification |
| Isolation | Other-user/tenant, revoked, poisoned and absent-evidence cases |
| Operations | Proposed owner, rebuild/re-embedding implications, unrun evidence and recovery dependencies |

## Fictional example

An internal policy assistant can answer only from documents the current employee may read.
The source gives an effective date and a stable policy identifier. Order status is live structured data,
so a separate authorized lookup fits that need better than indexing yesterday's status into documents.

For each question, trusted application identity restricts retrieval before content reaches the model.
The answer cites the permitted policy and signals missing or conflicting evidence. A deleted or revoked
policy must disappear from derived chunks, reusable context and caches according to the stated contract.
Describe temporary unavailability honestly; do not substitute another employee's cached answer.

Test retrieval relevance independently of the generated answer. A fluent answer using a superseded policy
can fail freshness even when its citation is real. A correct answer containing an inaccessible document
still fails the access contract. Source read-through alone does not demonstrate runtime isolation.

Sources and limits: [research ledger](../../../guidelines/catalog/research-ai-app-engineering-2026-11-17.md), S4–S10.
