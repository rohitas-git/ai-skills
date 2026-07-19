# Interactive Clarification Mode

This reference contains the full detailed instructions, questions, handling guidance, and confirmation format for the mandatory Interactive Clarification Mode.

When the skill is loaded for a new 0-review session, the agent must follow this mode **before** any measurement or code exploration.

## Purpose (explain to the user)
> "To give you the best possible 0-review while being smart about tokens and effort, I will ask a short series of multiple-choice questions. These help me understand exactly what you need — Goal, Scope, Depth, priorities, and constraints — without requiring you to know technical terms. I will not explore the codebase until we have clear agreement."

## Recommended Flow
1. Greet the user warmly and explain the purpose.
2. Ask the questions below. Present them **one at a time** or in **small batches of 2–3**. Wait for replies.
3. Be flexible. If the user says “I don’t know” or “surprise me”, offer helpful defaults and confirm.
4. After all questions, present a clean **Confirmed Review Parameters** summary and ask for explicit approval.
5. Only after confirmation, proceed to Phase 0 and apply the chosen parameters.

## Refined Clarification Questions (ask in this order)

**Q1. What is the main goal of this review?**  
(You can select more than one letter)

A. Quick health check or high-level overview (fast, surface-level insights)  
B. Detailed code quality, maintainability, and best practices assessment  
C. Security, vulnerability, compliance, or threat modeling focus  
D. Performance, scalability, resource usage, or bottleneck analysis  
E. Refactoring, modernization, technical debt reduction, or code cleanup  
F. Onboarding, knowledge transfer, documentation improvement, or contributor experience  
G. Comprehensive 0-review (balanced combination of several of the above)  
H. Other — please describe in your own words

**Q2. What 0-review scope would you like?**  
(This choice has the biggest impact on token usage and speed)

A. **Surface / High-level only** — Architecture map, top-level structure, obvious issues via grep and directory analysis. Minimal deep file reads. Ideal for quick 0-triage or strict token budgets.  
B. **Specific module(s) or path** — e.g. `src/auth/`, `packages/core/`, `lib/utils.py`. Deep analysis focused only inside the declared scope (still includes lightweight systemic checks).  
C. **Full codebase** — Smart prioritization and sampling across the entire repository.

**Q3. How deep or thorough do you want the analysis to be?**  
(This directly controls thinking effort and token consumption)

A. **Light / Surface** — High-level observations, quick wins, and key recommendations. Lowest token usage.  
B. **Moderate / Balanced** — Solid depth on important areas, good evidence, and actionable recommendations. Good balance of quality and efficiency.  
C. **Deep / Thorough** — Detailed reasoning, multiple reasoning passes, root-cause analysis, edge cases, and comprehensive recommendations. Highest effort.

**Q4. Are there any specific areas, modules, files, or concerns you want me to prioritize?**  
(Examples: authentication & authorization, database layer, API endpoints, recent changes, legacy code, error handling, testing strategy, etc.)

- If none: reply “None” or “Surprise me with the most important areas”
- You can list multiple items

**Q5. Any important constraints or special preferences?** (Select all that apply)

A. Tight on tokens, cost, or context window — strongly prefer aggressive token-saving techniques  
B. Need very fast turnaround / quick results  
C. This is critical production or security-sensitive code  
D. I want extra emphasis on systemic risks, cross-module interactions, and global patterns (even if scope is narrow)  
E. Maximize quality — I’m happy to spend more tokens for deeper insight  
F. No strong constraints — use your best judgment for an efficient, high-quality 0-review  
G. Other — please describe

**Q6. What style of output would you prefer?** (Optional but helpful)

A. Concise executive summary + prioritized recommendations table  
B. Detailed report with code examples, evidence quotes, and explanations  
C. Structured tables, checklists, and clear action items  
D. Mix of the above — adapt to what makes sense  
E. As you think best for this 0-review

## Handling User Answers
- Accept flexible input: letters (e.g. “A and C”, “Q2: B”), numbers, or natural language.
- If answers are vague or conflicting (“I don’t know”, “whatever you think is best”), politely propose reasonable defaults based on the other answers and ask for confirmation.
- Dynamically adapt: If the user chooses Scope = B (Specific module), ask for the exact path in the next message if not already provided.
- If the user wants to change an earlier answer later, simply accept the update and revise the parameters.
- Always stay helpful and non-judgmental.

## Confirmation Step (Mandatory)
After collecting answers, output a clear, professional summary in this format (or similar):

**✅ Confirmed Review Parameters**

- **Goal**: B + E (Detailed quality + Refactoring readiness)
- **Scope**: B — Specific module (`src/auth/`)
- **Depth / Effort**: C (Deep / Thorough)
- **Priorities**: Authentication flows, recent changes, error handling
- **Constraints**: Token-conscious + extra systemic checks enabled
- **Output Style**: Detailed report with code examples
- **Risk Mitigations**: Full (Systemic Awareness in Phase 1 + dedicated Scope Limitations section)

**Does this accurately reflect what you want?**  
Reply “Yes”, “Looks good”, or suggest any changes (e.g., “Make it more surface-level” or “Add performance focus”).

Only proceed to codebase measurement and analysis **after** receiving confirmation.

This mode ensures the review is perfectly tailored, token-efficient, and applies all risk mitigations intelligently.