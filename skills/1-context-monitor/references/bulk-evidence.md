# Keep bulky evidence bounded

Choose the smallest slice needed for the current question, cap tool output and retain raw artifacts
at their owned location. Prefer targeted queries, pagination, compact tables and source locators to
repeated full-file or transcript dumps. Summaries must preserve failures, uncertainty, authority and
candidate identity rather than laundering claims into facts.

Large read-only slices can go to independent workers only with explicit delegation authority. Give
each the real scope and a bounded return contract; no automatic model override, global transcript
scan or mutable service sharing follows from context pressure. A supplied local index can often
answer a question without another model call.

Use host telemetry when it exists and say usage is unknown when it does not. A token budget, cost
limit or long elapsed run is not a measured context-window percentage. Recommend compact/handoff
only at a safe checkpoint; preserve in-flight state instead of interrupting an external write.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
