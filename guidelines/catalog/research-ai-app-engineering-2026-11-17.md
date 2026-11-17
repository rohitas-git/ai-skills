# AI application engineering research and catalog integration

Research cutoff: 2026-11-17. Source snapshot: the AI Engineer research answer in this conversation,
materialized here in a condensed form with its primary-source references. This is an authored synthesis,
not an imported vendor package, a new source crawl, or an assessment of a deployed application.

## Scope and confidence

Practical engineering for AI features, integrations, agents, and upgrades to existing applications.
The core covers software/product design, data and context, evaluation, integration, security, economics,
and operations. Training methods, GPU serving and modality-specific pipelines are conditional specialties.
Confidence is high in the shared engineering principles; the proposed skill boundaries are design judgments.
Provider features, pricing, retention, regional availability, and legal obligations need current verification
when an actual application decision depends on them. No model, application, compliance or performance test ran here.

## Materialized findings

1. Define the user outcome, current non-AI baseline, success evidence, failure costs and ownership before
   selecting a model. Separate drafting/recommending from consequential decisions and actions.
2. Ordinary code, one model call, retrieval, tools, fixed workflows and agents solve different problems.
   Prefer the smallest adequate design. Autonomy and multiple agents need evidence of added value.
3. Engineers need software fundamentals plus working knowledge of tokens, embeddings, context limits,
   output variability, datasets, leakage, sampling, precision/recall, uncertainty and meaningful comparisons.
4. Architecture preserves deterministic business rules and authorization outside model text. Bound the
   probabilistic seam, data flows, state, retries, cancellation, external effects and recovery.
5. Context engineering manages relevant information, provenance, freshness, memory scope, retention and
   deletion. More tokens do not guarantee better outcomes. Retrieval and generation need distinct checks.
6. Retrieval requires ingestion/parsing, chunking, metadata, ranking, source references, permission filters
   and update/deletion behavior. A grounded answer may still use irrelevant or outdated evidence.
7. Structured output constrains shape, not truth, business validity or authority. Handle refusals,
   incomplete output and API errors. Untrusted content cannot grant access or authorize a tool action.
8. Evaluate deterministic contracts, model components, end-to-end outcomes and production behavior separately.
   Use representative and difficult cases, held-out data, qualified checkers, known defects/clean controls,
   uncertainty and failure slices. Averages must not hide consequential failures.
9. AI UX distinguishes a suggestion, draft, pending action and completed action; supports appropriate edit,
   rejection, cancellation, fallback and recovery; and communicates limitations without invented confidence.
10. Production requires quality, privacy/security, reliability, latency, cost per accepted outcome,
    observability, ownership and recovery. Shadow traffic must not duplicate writes or other side effects.
11. An AI candidate includes code, provider/model/version, parameters, prompts, tools/policy, retrieval corpus/
    index/embedding/ranker, memory/cache and runtime. Any relevant change may invalidate prior evidence.
12. Existing-app integration starts from current contracts and adds a bounded seam and fallback. Upgrades
    inspect semantic behavior, persisted outputs, conversation state, embeddings/indexes, caches and consumers.
    API compatibility alone does not establish behavioral compatibility or rollback safety.

## Evidence ledger

The links were consulted during the preceding research on 2026-11-17. The claims below summarize what each
source supports; vendor examples are not universal requirements or default numeric gates.

| ID | Source | Supported claim |
|---|---|---|
| S1 | [Google People + AI: user needs](https://pair.withgoogle.com/guidebook-v2/chapter/user-needs/) | Problem fit, non-AI alternatives, automation versus augmentation |
| S2 | [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) | Simple compositions, workflows versus agents, feedback and stopping conditions |
| S3 | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) | Data/generalization, evaluation metrics, embeddings, LLM and production foundations |
| S4 | [OpenAI: accuracy optimization](https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy) | Distinguish context failures from behavior failures; methods are not a mandatory ladder |
| S5 | [Anthropic: context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Curated context, finite attention, retrieval and memory/compaction trade-offs |
| S6 | [Microsoft: RAG evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators?view=foundry) | Retrieval relevance, groundedness, completeness and end-to-end quality are distinct |
| S7 | [Microsoft: document-level access](https://learn.microsoft.com/azure/search/search-document-level-access-overview) | Permission-aware ingestion/query boundaries; support varies by service configuration |
| S8 | [OpenAI: structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | Schema conformance, refusals/incomplete results, separate business validation |
| S9 | [OWASP: prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | Direct/indirect content attacks, least privilege and defense in depth |
| S10 | [OpenAI: evaluation practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Task-specific, representative, continuous evaluations and human-calibrated scoring |
| S11 | [Google People + AI: feedback/control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/) | User control, meaningful feedback and data-collection transparency |
| S12 | [OpenAI: API compatibility](https://developers.openai.com/api/reference/overview) | Model behavior can change between snapshots despite API compatibility |
| S13 | [AWS: production operations](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-advanced-operations.html) | Shadow/A-B/canary exposure, quality/cost/health monitoring and promotion gates |
| S14 | [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Voluntary lifecycle risk-management context; not a compliance certification |

## Integration decisions

| Research need | Disposition | Owner |
|---|---|---|
| Decide whether an AI intervention is suitable | New bounded assessment | `1-ai-suitability` |
| Define context/retrieval behavior and permission-aware evidence | New design/assessment contract | `1-context-retrieval-design` |
| Choose architecture and model/workflow alternatives | Extend existing decision owner | `2-software-architect` |
| Integrate AI at an application contract | Extend existing interface owner | `1-api-and-interface-design` |
| Evaluate one-call features as well as agents | Extend existing evaluation scope | `1-agent-evaluation` |
| Assess model/prompt/data/tool upgrades | Extend existing impact owner | `1-change-impact` |
| AI readiness and controlled exposure | Extend existing release owner | `1-shipping-and-launch` |
| AI interaction states and user control | Extend existing UI owner | `1-frontend-ui-engineering` |
| Implementation lifecycle | Optional composition reference; no new execution hub | `0-implement` |
| Vault knowledge | One new concept and two scoped discovery updates | Separate `1-vault-ingest` change set |

Prompt optimization, tool schemas, human oversight, spending, platform operations, security and observability
retain their existing owners. No model-training framework, runtime tool, scheduler or background agent is installed.
The two new leaves are authored procedures, not proof that any real project has passed their checks.

## Behavioral review cases

These are specification examples, not recorded model evaluations.

| Case | Required handling |
|---|---|
| Exact tax/eligibility rule with no language ambiguity | Compare deterministic baseline; do not force an LLM |
| Useful draft answer but unsafe auto-send | Separate draft benefit from action authority and human control |
| Missing current facts with a good format | Investigate context; do not assume model training is the remedy |
| Relevant private document from the wrong tenant | Exclude before generation; a citation cannot cure access leakage |
| Permission revoked after embedding/caching | Propagate access/deletion changes and prevent stale disclosure |
| Valid JSON with an unsupported amount | Reject through business validation outside the model |
| Same API but a changed model/prompt/index | Re-evaluate affected behavior and persisted-state compatibility |
| Shadow agent proposes a real external write | Suppress/simulate effects; do not duplicate actions |
| Proposed measurements with no execution authority | Return an unrun protocol and explicit unknowns |

## Completion boundaries

Catalog checks establish structure and routing, not model quality or application safety. Vault ingestion
preserves the distinction between source claims and this synthesis. Runtime sync, commits, provider calls,
publication, deployment, production mutation and paid evaluation are outside this change set.
