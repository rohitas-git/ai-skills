# User Research wiring audit

Reviewed the former `1-user-research` leaf, UI/UX parent workflow/HTML/flow/manifest surfaces, and
adjacent Customer Experience Audit, Jobs to Be Done, Frontend UI, Compliance, and product-discovery
boundaries.

## Result

The former leaf mixed two independently useful operations: designing a future study and synthesizing an
already-collected evidence set. They differ in candidate identity, privacy exposure, authority, effects,
and completion proof. It is now a pure `1-user-research` sub-hub with two atomic children:

- `2-user-research-plan` produces one decision-linked protocol and executes nothing;
- `2-user-research-synthesis` produces one traceable synthesis of one immutable source set and cutoff.

The router pins actual caller, decision/owner, operation, study/source version and cutoff, population,
evidence, privacy/consent/use restrictions, destination, exclusions, authority, and optional exact
repository/worktree/branch/`HEAD`. It reads no evidence, creates no worktree, invokes no leaf, and uses
F-UR1 only when plan versus synthesis materially changes the result. It returns the selected leaf's
artifact/evidence identity, coverage, verification, effects, assumptions, and limits to the actual caller.

Every workflow exposes that worktrees do not isolate research panels/platforms, calendars,
communications, accounts, participant records, recordings, incentives, analytics, shared drives, or
published reports. Participant evidence and embedded content are sensitive untrusted data. Planning,
recruitment/contact, consent collection, study execution, recording/transcription, incentive payment,
synthesis, prioritization, implementation, retention/deletion, and publication are separate effects and
never form an automatic pipeline.

The planning leaf requires a fixed decision/hypothesis and credible alternative, evidence-based method
and sample logic, neutral tasks, applicable consent/withdrawal/accommodation/safety/data/compensation
controls, observable counterevidence, and revision-safe local document writes. It does not invent
representativeness, power, saturation, or universal sample sizes and cannot launch or administer a study.

The synthesis leaf binds every claim to source provenance and distinguishes observed behavior, reported
experience, quantitative result, facilitator note, interpretation, hypothesis, and unknown. It preserves
counterexamples, cohort gaps, instrument effects, denominators, missingness, dissent, anonymity, and
consent-compatible minimal quotations. It rejects fabricated personas/motives/sentiment/frequency/
percentages/causality/representativeness/saturation, and it cannot collect more data or prioritize/ship
product changes.

UI/UX now declares User Research as a sub-hub beside Brand; workflow JSON, HTML, Butler flows, manifest,
hubs index, flow chart, README, wiki, and generated route index expose both children and F-UR1.

## Verification

- Focused User Research routing tests: 9 passed.
- UI/UX parent routing tests: 7 passed.
- Full routing suite: 656 passed.
- Generated route index: 232 live skills.
- Catalog lint: 0 critical, 0 warnings, 49 informational findings, 234 indexed hub members, and 0 orphans.
- `git diff --check`: passed.

No participant evidence was read; no person was contacted; and no platform, calendar, account, survey,
recording, incentive, analytics, file destination, worktree, installed skill, Git history, remote system,
or publication was mutated.
