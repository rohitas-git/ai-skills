---
name: 1-to-questionnaire
description: >
  Create a discovery questionnaire for one recipient who holds missing knowledge.
  Use when a decision needs someone else's facts or expertise, gathered asynchronously
  or in a meeting. Not for interviewing the current user, research surveys, or sending messages.
  Hub: /0-grilling.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-grilling
    role: leaf
    when: [draft a questionnaire for an external knowledge holder]
    not_when: ["interview the current user → 0-grilling", "research study → 1-user-research"]
    prev: [0-grilling]
    next: [0-grilling]
    triggers: [discovery questionnaire, questions for a stakeholder, turn this into a questionnaire]
    requires_setup: false
  vendor:
    source: mattpocock/skills
    upstream_id: to-questionnaire
    commit: 5863806dd4e15c63174bee4e7515a4256792ecfa
---

# To Questionnaire

Create one Markdown questionnaire that extracts the knowledge needed for a named decision.

## Boundary

| Need | Owner |
|---|---|
| Questions for someone other than the current user | This skill |
| Resolve the current user's requirements interactively | `/0-grilling` |
| Design a participant research study | `/1-user-research` |

## Process

1. Identify the recipient's role, expertise, relationship to the user, and relevant context.
   Reuse supplied facts. Ask about missing recipient details, not subject matter the user lacks.
2. Identify the decisions or facts the user needs back. Ask only about remaining material gaps.
   Done when every requested answer has a purpose and an intended use.
3. Draft a discovery questionnaire, most important questions first. Include purpose, sender/recipient
   when known, how answers will be used, and enough context for someone outside this conversation.
4. Give brief answer instructions. Include a deadline or effort estimate only when supplied or agreed.
   Invite partial answers and explicit uncertainty. Ask one idea per question with an answer stub.
   Group longer questionnaires by theme. Add a short reason only where it clarifies a question.
   End with an optional question about missing context.
5. Write `to-questionnaire-<topic>.md` in the caller's agreed directory, or honor a specified path.
   Check for collisions and preserve unrelated work. Never invent identities, deadlines, or answers.
6. Check that every needed decision/fact is covered and the recipient can understand the document alone.
   Report the file path and any unresolved assumptions. Return to the caller without sending it.

No email, posting, recipient contact, commit, or publication is implied.
Source and adaptation evidence: [ingest report](../../guidelines/catalog/ingest-mattpocock-2026-11-12.md).
