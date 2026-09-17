# Bug reproduction within TDD

Use this branch only after `/0-diagnosing-bugs` or a confirmed bug contract identifies a
stable behavior, correct seam, independent oracle, and edit authority.

1. Pin the before candidate and original reported scenario.
2. Add the smallest regression test at the seam that preserves the causal pattern.
3. Run the focused command and confirm the predicted behavioral failure.
4. Apply the minimum authorized implementation and rerun the same command.
5. Re-run the original scenario and proportionate adjacent checks.
6. Return red/green evidence and coverage limits to the caller.

If no faithful automated seam exists, do not add a shallow test for appearances. Preserve
the runtime/log/trace evidence, report the seam gap, and let the caller decide whether a
characterization test, architecture change, or post-fix regression is warranted.

A regression guard should remain only when it is stable, maintainable, and useful under
the repository's policy. Do not promise “forever,” duplicate stronger coverage, or retain
a brittle test solely to demonstrate process compliance.

Delegating test authorship is optional and requires explicit delegation plus isolated
ownership. It does not create an independent oracle if every agent receives the same
unverified assumption.
