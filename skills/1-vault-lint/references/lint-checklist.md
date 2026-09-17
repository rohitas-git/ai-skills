# Vault lint check definitions

Select only checks within the requested scope and active schema:

| Check | Evidence needed before a finding |
|---|---|
| Link/anchor/embed resolution | exact source token plus target/alias/anchor resolution under current conventions |
| Path containment | canonical target escapes or violates the configured root/scope |
| Metadata/schema | exact field/value and the active schema rule it violates |
| Hub/concept placement | current folder/type convention plus actual candidate path/content role |
| Orphan/weak connectivity | defined inbound-link universe and exclusions; report as topology, not automatic defect |
| Duplicate/overlap | claim-level comparison showing redundant scope, not title similarity alone |
| Contradiction | both exact claims, provenance/locators, and why their conditions cannot coexist |
| Source provenance | missing/broken declared source under the active evidence policy |
| Index drift | exact index obligation and missing/stale entry |
| Inbox/archive state | explicit lifecycle rule and item state; age/backlog alone is not failure |
| Freshness | date/version evidence only; current factual invalidity requires separate research |
| Format/plugin behavior | static defect or authorized runtime evidence; never assume plugin availability |

Severity follows demonstrated impact, not category name. A missing link may be harmless; a
misresolved private embed may be serious. Separate `proven`, `likely`, and `needs decision`.

For a sampled audit, record selection method, files/checks inspected, excluded population,
and why the sample was chosen. Never report “0 issues” for the whole vault from a sample.
