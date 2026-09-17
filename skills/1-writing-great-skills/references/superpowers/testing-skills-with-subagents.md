# Optional Skill Evaluation With Fresh Contexts

Source: the vendored Superpowers subagent-testing guide.

Status: provenance note only. It does not authorize delegation or prescribe TDD for every skill edit.

## When it helps

Use a fresh-context comparison when a consequential instruction is repeatedly ignored, a trigger has measurable false fires/misses, or output quality cannot be assessed from static review. Pure reference updates and low-risk wording changes often need only structural checks or one direct scenario.

## Minimal experiment

1. State the exact behavior and immutable skill revision being tested.
2. Define a realistic case and objective completion criterion.
3. Add a no-skill or prior-version baseline only if it answers a real comparison.
4. Use the smallest authorized fresh-context mechanism available.
5. Capture inputs, outputs, runtime/model, assertions, and uncertainty.
6. Revise the generalized cause, then re-run the affected case plus a near miss.

Delegation is optional and is used only when the user or controlling instructions authorize it. Never fake a real emergency, authority grant, filesystem, or irreversible choice. Scenarios may test reasoning, but they do not grant permission to act.

## Completion

Report observed behavior and limits. One passing sample is not “bulletproof,” and one failing sample is not proof of a universal pattern.

