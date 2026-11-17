# Suitability evidence

Use only dimensions that can change the decision. Do not average away a severe harm with a favorable score.

| Dimension | Evidence/question |
|---|---|
| User outcome | Which actual task improves, for whom, and how will they notice? |
| Baseline | What happens today; would rules, search or a better form solve it? |
| Error cost | Which false positives, omissions, incorrect claims or actions matter? |
| Data | Is relevant information authorized, representative, accessible and current? |
| Control | Draft, recommend, decide or execute; who owns correction and escalation? |
| Economics | Cost per accepted outcome, including retries and human correction |
| Operations | Latency, availability, maintenance, feedback and recovery owner |
| Experiment | Which observation could disprove the proposed advantage? |

## Fictional example

A support team wants AI to answer delivery questions. Historical response time and error data are unavailable.
The policy is searchable, but customers also need live order status.

Compare ordinary policy search/status lookup with a grounded draft assistant. Do not assume that answering
questions requires an autonomous agent. Keep refunds and message sending outside the proposed drafting scope.
Recommend a bounded comparison on permitted representative questions, including missing policy and ambiguous
orders. The outcome remains conditional; do not invent a time saving, accuracy target or approval rule.

A requirement for exact arithmetic or eligibility rules favors ordinary code for that decision, even if AI
helps interpret the user's words before validated inputs reach the rule engine.

Sources and limits: [research ledger](../../../guidelines/catalog/research-ai-app-engineering-2026-11-17.md), S1–S4.
