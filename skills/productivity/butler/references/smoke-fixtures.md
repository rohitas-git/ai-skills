# Smoke fixtures

Manual (and future scripted) checks after catalog changes.

## Query utterances → expected skill

| Utterance | Expected primary |
|-----------|------------------|
| which skill should I use? | butler (query) |
| grill me / stress-test this plan | grill-with-docs or grill-me |
| turn this into a spec | to-spec |
| this bug is weird | diagnosing-bugs |
| put this in my vault / query my notes | vault-ingest / wiki-query |
| implement these tickets | implement |

## Lint

```bash
./scripts/lint-skills
```

Expect **0 critical** on the promoted set. Known warns may remain (README blurb drift, optional progressive disclosure).

## Success metrics (spec)

| Metric | Expect |
|--------|--------|
| Steward | butler exists, user-invoked |
| Single tdd | only `engineering/tdd` in discovery |
| No ask-matt live router | ask-matt under deprecated only |
| No setup-matt name | setup-rohitas-skills only |
| Vendor dual-router offline | nestedSkillRoots empty; using-agent-skills only under vendor |
| Model-invoked budget | promoted model-invoked &lt; ~25 |

## Review closer

| Utterance / path | Expected |
|------------------|----------|
| implement finishes build | multi-axis `code-review` |
| review since main | `code-review` (not code-review-v2) |

