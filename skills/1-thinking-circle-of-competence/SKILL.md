---
name: 1-thinking-circle-of-competence
description: >
  Use when a specific claim may lack grounding. Check evidence boundary, size wrongness cost, then answer, fetch, or abstain — never confabulate.
  Use when: Use when a specific claim may lack grounding. Check evidence boundary, size wrongness cost, then answer, fetch, or abstain — never confabulate.
  Not for: Claim is grounded in something you read, ran, or can cite this session, or is stable un…; Error cost is trivial and reversible and you will flag the claim as unverified.
  Hub: /0-thinking. Triggers: thinking circle of competence, circle-of-competence.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "Use when a specific claim may lack grounding. Check evidence boundary, size wrongness cost, then answer, fetch, or ab…"
    not_when:
      - "Claim is grounded in something you read, ran, or can cite this session, or is stable un…"
      - "Error cost is trivial and reversible and you will flag the claim as unverified"
      - "Grounding is one cheap fetch away"
      - "User explicitly wants labeled brainstorming or hypotheticals"
    cousins:
      - "0-thinking"
    triggers:
      - "1-thinking-circle-of-competence"
      - "thinking circle of competence"
      - "circle of competence"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-circle-of-competence
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Circle of Competence

Treat competence as an evidence boundary, not self-image. Answer only when grounded; otherwise fetch, mark uncertainty, or abstain. The failure mode is a fluent fabrication treated as fact.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Circle of Competence (this) | **1-thinking-circle-of-competence** (this) |
| House routing (which domain) | `/0-butler` |

## When to Use

- About to assert a specific fact (API, path, number, config, version behavior) without a citable source from this session.
- The claim is about this codebase or system and you have not read or run the relevant artifact.
- Pattern reconstruction would sound complete but is unconfirmed.
- Cost of a wrong confident answer is material (security, data, irreversible action, trust).

## When NOT to Use

- Claim is grounded in something you read, ran, or can cite this session, or is stable universal knowledge — answer without false humility.
- Error cost is trivial and reversible and you will flag the claim as unverified.
- Grounding is one cheap fetch away — fetch first; abstention is not an excuse to skip a check.
- User explicitly wants labeled brainstorming or hypotheticals.

## Process

1. **Name the claim.** Isolate the assertion that would be treated as fact.
2. **Classify the zone.**
   - *Grounded:* citeable session source (read/run) or stable non-version-specific knowledge.
   - *Partial:* general shape known; version/repo/config detail unconfirmed.
   - *Ungrounded:* would invent a concrete value with no source.
3. **Size wrongness cost.** If high-stakes (security, data loss, irreversible ops), treat Partial as Ungrounded until verified.
4. **Act by zone.**
   - Grounded → answer; cite when useful; do not hedge verified facts.
   - Partial → cheap fetch then answer; else answer only with explicit uncertainty and a check path.
   - Ungrounded → fetch if possible; else ask or abstain with what would enable an answer. Never invent.
5. **Refuse competence creep.** Adjacent code, prior versions, or general capability do not ground the unread target.
6. **Stop.** Emit answer, fetch request, or abstention. Do not round "probably" to a flat assertion.

**Stop condition:** Claim answered with grounding, marked partial with a check path, or refused with missing-evidence note.

## Output

```text
Claim: <assertion>
Zone: grounded | partial | ungrounded
Evidence: <source or none>
Wrongness cost: low | medium | high
Action: answer | fetch-then-answer | answer-with-uncertainty | abstain/ask
Response: <wording or missing artifact>
```

## Verification

- Falsify if a specific value was asserted with no session source and no uncertainty marker.
- Falsify if Partial/high-stakes was treated as Grounded, or a cheap fetch was skipped for abstention theater.
- Over-application guard: do not hedge or refuse claims verified this session.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-circle-of-competence/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
