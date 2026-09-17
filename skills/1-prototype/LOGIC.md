# Logic experiment

Use to answer a specific state-transition, data-shape or algorithm question.
The parent [skill](./SKILL.md) controls scope, workspace, data and return authority.

## Procedure

1. Write the question and a small set of input/action sequences that distinguish
   candidate designs. Include the edge case that motivated the experiment.
2. Use the project's existing runtime. Keep the logic separable from a thin driver
   where that aids inspection, but do not introduce a reusable framework.
3. Choose the smallest useful driver: a replay script or a simple interactive
   terminal loop when the user needs to explore actions. A full TUI is optional.
4. Keep state in memory with synthetic examples. Print relevant transitions and
   invariants, not credentials or customer records. Include a safe quit path.
5. Document one runnable command. Prefer an existing runner or direct command;
   a package-script edit is optional and belongs within the requested paths.
6. Run the chosen sequences and record observed versus expected results. Small
   assertions are useful when they establish the answer; a broad test framework
   or production-level suite is not required for every experiment.
7. Return the conclusion and limitations to the design caller. A promising reducer
   or function is still prototype code; production reuse requires a separately
   requested implementation, review and appropriate regression coverage.

Do not wire the experiment to a real database by default, add speculative states,
or call a manually pleasing outcome proof of general correctness. If persistence
is the question, use only explicitly authorized disposable/local state and the
repository's DB safety rules; do not reset an existing stack as preparation.
