# Progressive Deep-Dive & Progressive Learning

## Purpose
Support **iterative, user-driven deepening** of explanations until the user stops. This enables true progressive learning paths, allowing learners to control the depth and focus of their understanding.

## How It Works
1. **After initial explanation**, always offer next steps:
   - "Which part would you like to deep-dive into?"
   - "Would you like to continue to the next level of depth?"
   - "Go deeper on any specific aspect?"

2. **On user request**, expand the chosen section with:
   - More technical depth and precision
   - Supporting evidence, data, or citations
   - Counter-arguments and limitations
   - Historical context and development of ideas
   - Mathematical formalization, equations, or models (if applicable)
   - Interdisciplinary connections
   - Latest research or developments (via `web_search` when appropriate)
   - Critical analysis and open questions

3. **Conversation Flow**:
   - Maintain coherence by referencing previous explanations.
   - Gradually increase complexity only when requested or when moving to higher audience levels.
   - Track which parts have been explored.

## Levels of Depth
- **Level 1 (Basic Expansion)**: Clarify key terms, add simple examples, restate in different words.
- **Level 2 (Detailed Mechanisms)**: Explain how things work, add processes, workflows, or step-by-step breakdowns, include more examples and edge cases.
- **Level 3+ (Advanced / Frontier)**: Rigorous analysis, primary sources, debates in the field, mathematical formalizations, cutting-edge research, philosophical implications, future directions, and open problems (especially powerful in Frontier mode).

## Best Practices
- **Maintain audience alignment**: Stay consistent with the chosen level (Child, Beginner, Layperson, etc.) or gradually increase complexity only when the user demonstrates readiness.
- **CLT Integration**: Apply Cognitive Load Theory principles **only if explicitly requested** by the user.
- **Track State**: Keep mental track of what has already been explained to avoid repetition and build on prior knowledge.
- **Offer Branching Choices**: "Would you like to go deeper on X, or explore how this connects to Y?"
- **Active Learning**: Include self-assessment or reflection prompts such as:
  - "Can you explain this in your own words?"
  - "What questions does this raise for you?"
  - "How might this apply to [real-world scenario]?"
- **Stop Condition**: Continue only while the user keeps requesting more depth. Offer a natural exit point when appropriate.

## Flags & Trigger Phrases
- `--progressive`
- "deep dive", "go deeper", "continue", "next level", "expand on X", "tell me more about Y"

## Additional Guidelines
- When moving to higher depth levels, optionally suggest moving up one audience level (e.g., from Layperson to Specialist).
- For technical topics, introduce formal notation gradually.
- Always end deep-dive responses with a clear offer for further exploration or a summary of what was covered.