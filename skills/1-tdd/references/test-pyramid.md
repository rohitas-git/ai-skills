# Test portfolio and resource size

Use this reference to choose the cheapest seam that still proves the behavior. A fixed
pyramid percentage is not a universal target; architecture, risk, feedback speed, and
failure cost determine the portfolio.

| Test shape | Good fit | Main limit |
|---|---|---|
| Pure/unit | deterministic business rules and transformations | may miss boundary wiring |
| Component/integration | API, database, filesystem, queue, or module contracts | requires isolated state/services |
| Browser/system | critical user journey or browser-only behavior | slower, broader failure surface |
| Evaluation/statistical | probabilistic model/RAG output | not strict TDD; route to `/1-agent-evaluation` |

Classify resource ownership separately from test level. A “unit” test that touches a
shared database is not isolated; an end-to-end local test may still be disposable. Record
processes, ports, databases, accounts, queues, files, clocks, network, and cleanup owner.

Prefer the lowest seam that retains the real causal behavior. Add a higher-level check
when lower seams cannot prove integration or user-visible outcome. Do not build a broad
portfolio during one red-green slice unless the caller explicitly includes that work.
