# Story-Teacher Skill — Detailed Workflow & Examples

## Full Internal Workflow

### Phase 1: Input Processing
1. Receive user request + content (text, summary, URL, etc.).
2. If content is long/raw/URL/video:
   - Strongly recommend or internally trigger `resource-summarizer` skill first.
   - Goal: Produce a clean 80/20 distillation with core concepts, Feynman-style explanations, and why each matters.
3. Extract 4–8 high-impact concepts that form the "spine" of the story. These will become the emotional/plot backbone.
4. Ask user for preferences if not already provided:
   - Genre(s) they enjoy (or offer 2–3 strong options)
   - Tone (gritty, hopeful, humorous, dark, epic)
   - Length preference (short story, novella 6–8 chapters, or longer 10–12 chapter short novel)
   - Any hard constraints (no violence, target audience age, must include X element, etc.)

### Phase 2: Story Design (Most Important Creative Step)
**Golden Rule**: The fictional world must make the concepts feel *necessary* for survival or victory. The reader should never feel the concepts were "added" — they should feel like the natural physics/magic/rules of this story's reality.

**Strong Premise Patterns** (use these as starting points):
- **Heist / Infiltration**: Characters must break into or fix a complex system. Bad architecture = traps, dead ends, cascading failures. Good architecture = elegant solutions under pressure.
- **Fantasy Magic System**: Spells = functions (must do one thing cleanly). Grimoires/modules have single responsibilities. Ancient artifacts = legacy code with hidden dependencies. "Drawing boundaries" = literal magical wards.
- **Cyberpunk / Dystopian Infrastructure**: The city or AI is a giant monolith. "Refactoring" it while it's running is the plot. Dependencies pointing outward = external actors can control or destroy core logic.
- **Mystery / Thriller**: The crime or conspiracy only makes sense once characters understand the hidden structure (layers, boundaries, what is detail vs policy).
- **Adventure / Quest**: The hero must "make the system scream its true purpose" or invert wrong dependencies to reach the goal.

**Mapping Concepts to Story Beats**:
For each core concept, design:
- A moment where *violating* it causes clear, painful, visible failure (ideally costs something the reader cares about).
- A later moment where *applying* it creates a reversal, clever win, or emotional catharsis.
- Weave them so they interact (e.g., bad naming + god-class causes a cascade that only a proper boundary + small focused components can fix).

### Phase 3: Writing Guidelines
- **Prose Quality**: Vivid, novelistic, character-driven. Use sensory details, internal conflict, dialogue that reveals character and advances plot simultaneously.
- **Pacing**: Alternate high-tension scenes with quieter character moments. Every chapter should end with a hook or revelation.
- **Invisible Teaching Test**: After writing a scene, ask: "Could a reader enjoy this without knowing the source concept?" If not, rewrite to make the idea emerge from consequences and character insight.
- **Chapter Count**: 6–8 chapters for tighter lessons. 9–12 for richer, multi-concept sources.
- **Length per Chapter**: Target 1,200–1,800 words for comfortable reading.
- **Avoid**: Any meta-commentary, "this is like SRP because...", lists, bullet points, or breaking immersion.

### Phase 4: Delivery & Iteration
- For short stories: Deliver full story in one response.
- For novellas/novels: 
  1. First response = Premise + 2–3 genre options + high-level chapter outline (no full prose yet).
  2. On user approval → Write Chapter 1 + offer to continue.
  3. Continue chapter-by-chapter, incorporating any feedback.
- At the very end (only on explicit request): Provide a clean, non-spoiler or spoiler-marked mapping of concepts to chapters.

## Example: How the Clean Code + Clean Architecture Summary Became "Clean Break"

**Source Input**: The `clean-books-summary.md` (80/20 distillation of both books).

**Core Concepts Selected as Story Spine** (the 80/20):
- Meaningful/intention-revealing names (and the danger of disinformation)
- Small functions / do one thing well + SRP (god classes and tangled responsibilities cause collapse)
- Dependency Rule + inward-pointing arrows (details must not control policy)
- Boundaries, layers, and treating frameworks/DBs as swappable plugins
- Screaming architecture (the structure should reveal its true purpose)
- Tests as the safety net that makes bold change possible
- Boy Scout Rule + cost of change (leave every system cleaner)

**Chosen Genre & Premise**:
Cyberpunk thriller/heist. The "System" is a literal city-wide monolithic codebase that runs everything. A team of rogue "refactors" must infiltrate and clean it from the inside while it's failing catastrophically. The concepts become literal survival mechanics during the job.

**How Concepts Were Made Invisible & Dramatic**:
- Bad naming → A critical "function" (security protocol) is misread because its name lied → people die in a chase.
- God class / doing too much → One central component tries to handle security + routing + power + citizen tracking → single point of failure that almost dooms the mission.
- Wrong-way dependencies → A low-level database detail controls high-level policy decisions → the elite can remotely shut down core logic.
- Proper boundaries + humble objects → They isolate a volatile external service behind a clean interface → it can be swapped without breaking everything else.
- Screaming architecture → When they finally draw the right lines, the city's true "use cases" (control vs freedom) become visible in the structure itself.
- Tests → The only reason they dare to refactor live is because they have fast, reliable tests that prove each change didn't break previous fixes.

**Result**: A tense heist story where every major principle saves (or dooms) characters in believable, high-stakes ways. A reader finishes the novel understanding the ideas viscerally without ever being "taught" them.

## Quick Premise Brainstorming Prompts (Use When Stuck)

For any new input, ask yourself:
- "What if this concept was a literal rule of magic/physics in this world?"
- "What job or mission would force characters to discover this principle or die?"
- "What kind of failure would make the cost of *not* following this idea painfully obvious?"
- "How can I make the 'aha' moment feel like a clever plot twist rather than a lesson?"

## Anti-Patterns to Avoid

- Making the protagonist a teacher or explainer who lectures other characters.
- Using chapter titles that reveal the principle (e.g., "The Single Responsibility Principle").
- Adding an "epilogue explanation" or appendix unless explicitly requested.
- Overloading the story with every minor point from the source (stick to 80/20 spine).
- Breaking immersion with modern tech jargon when the story is set in fantasy (translate concepts into the world's language).

This workflow produces stories that people actually want to read while making the underlying knowledge stick far better than direct instruction.