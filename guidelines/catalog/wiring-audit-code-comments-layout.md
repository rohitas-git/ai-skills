# Code comments and file-layout wiring audit

Reviewed `1-code-comments`, `1-inline-comments`, `1-execution-flow-comments`, `1-stepdown-rule`, the
Inline Comments agent manifest, Ship parent surfaces, and adjacent Code Explainer, Coding Standards,
Codebase Design, Architecture Review, and Code Review boundaries.

## Result

The family now exposes four distinct one-candidate operations: language-native documentation for one
public/exported surface; one concise internal why/constraint comment; one explicitly requested numbered
execution-flow block for one function; and one behavior-independent declaration reorder in one source
file. Each chooses read-only assessment or authorized edit, pins repository/worktree/branch/`HEAD`, dirty
ownership, committed versus working-tree candidate, exact file/symbol/block/function/hash, repository and
language convention, allowed path, verification, and edit/Git authority. Assessment creates no worktree;
edits reuse the caller's matching checkout.

Public documentation is treated as a contract derived from code plus authoritative tests/contracts; it
cannot invent semantics or change behavior to resolve a contradiction. Generated output routes to its
source. Inline comments default to no change when code is already clear, preserve machine-significant
directives, and never invent business/history/owner/TODO claims. Execution-flow comments require an
explicit request or repository mandate, use the real ordered path with no fixed step or tree quota, and
do not expand across modified functions.

Stepdown is no longer a universal language template. It inspects hoisting, binding, initialization,
decorators, registration/import side effects, reflection, serialization/property order, preprocessors,
type/member ownership, and generated regions before proposing the smallest order-only permutation.
Repository and language conventions win; callers-before-callees does not authorize declaration-form
conversion, forward-reference scaffolding, module extraction, or behavior changes. Verification checks
the moved-text multiset plus fitting parser/type/build/tests and reports remaining runtime uncertainty.

All four skills now return to Ship. None automatically invokes Code Review, another comment mode, broad
refactoring, commit, push, or publication. Their bodies are below the lean target; three former lean
warnings are removed. Parent workflow, HTML, flows, README/wiki descriptions, and the Inline Comments
agent prompt distinguish the same atomic operations.

## Verification

- Focused comment/layout routing and contract tests: 8 passed.
- Ship parent routing tests: 6 passed.
- Package-local links and handoff identifiers resolve through inherited workspace checks.
- Targeted run: 14 tests passed.

No product source, comment, declaration order, formatter output, generated documentation, worktree, test,
Git history, remote system, or published documentation was read or changed.
