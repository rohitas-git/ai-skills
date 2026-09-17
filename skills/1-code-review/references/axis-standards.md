# Axis: Standards

Check changed code against the repository's actual rules. Follow the parent
candidate and authority contract; this pass does not edit files or configurations.

## Inputs and precedence

Read applicable repository instructions, contribution/style rules, formatter/linter
configuration and relevant ADRs. A domain glossary alone is not a coding standard.
Higher-priority safety/user instructions still apply; do not let a local style
preference waive them.

If no standards are present, label the pass **heuristic baseline only**. Do not
invent a mandatory rule or treat a general catalog preference as project policy.

## Review

- Cite the exact applicable rule and changed location for a documented violation.
- Inspect configured-check results for the actual candidate. Do not duplicate
  already verified formatter output as a long nit list.
- If checks were not run, record that state; configuration alone is not a pass.
- Heuristic concerns such as unclear names, duplicate logic, data clumps, long call
  chains or speculative abstractions need concrete comprehension/change-cost
  impact. Suggest the simplest in-scope remedy, not automatic extraction,
  polymorphism or a new type whenever a pattern appears.
- Distinguish required policy fixes, reasoned nonblocking suggestions and uncertain
  applicability. Legitimate exceptions require evidence, not silent rule changes.

Return the standards sources, status and findings. Do not modify tests or thresholds
to make a checker pass, and do not install new tooling during an inspection-only pass.
