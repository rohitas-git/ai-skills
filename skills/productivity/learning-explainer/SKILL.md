---
name: learning-explainer
description: >
  Unified skill for summarizing resources and explaining them across audience
  levels (child to frontier researcher) with mental models, diagrams, progressive
  deep-dive, user knowledge probe, compact mode, and verification. Default is no
  CLT. Use for any learning or explanation request.
---

# Learning Explainer

## Overview
This unified skill merges resource summarization with adaptive multi-level explanations. It is designed for high flexibility, token efficiency (via modular references), and pedagogical quality.

## Core Workflow
0. **Honor Brief Plain-English Overrides**  
   If the user asks for a brief/simple/plain-English explanation (for example "explain in simple terms briefly", "simple and short", "plain English", or "ELI5 but short"), answer directly in 1 short paragraph or 3-4 bullets. Skip the knowledge probe, mental model requirement, diagram descriptions, confidence score, and progressive follow-up structure unless the user explicitly asks for them. The user is asking for compression, not a lesson plan.

1. **Start with Knowledge Probe**  
   Assess the user's familiarity and goals (see `knowledge-probe.md`).

2. **Default Mode = No CLT**  
   Use Cognitive Load Theory principles **only** when the user explicitly requests it.

3. **Process the Resource**  
   If the input is long, first distill it (using resource-summarizer techniques or tools). Then generate explanations at the requested or appropriate level(s).

4. **Always Include**:
   - One or more mental models + diagram descriptions
   - Clear structure adapted to the audience level
   - Confidence score with justification
   - Offer to go deeper or change direction

5. **Support Progressive Deep-Dive**  
   Enable iterative expansion when the user requests "go deeper", "continue", or uses `--progressive`.

## Key References (Load as Needed)
- **Audience Levels & Triggers** → `level-*.md` (child through frontier)
- **Flags & Modes** → `flags.md`
- **Mental Models & Diagrams** → `mental-models.md`
- **Knowledge Probe** → `knowledge-probe.md`
- **CLT Clarification** → `clt-clarification.md` (explicit request only)
- **Progressive Deep-Dive** → `progressive-deep-dive.md`
- **Examples** → `examples.md`
- **Templates** → `templates.md`

## Design Principles
- **Modular & Token-Efficient**: Keep the main SKILL.md lean. Load detailed guidance from references only when needed.
- **User-Centered**: Always begin with the knowledge probe and adapt accordingly.
- **Flexible**: Support single-level, multi-level, compact, and progressive modes.
- **High Quality**: Ground explanations in evidence, use strong mental models, and maintain appropriate tone per level.

## Best Practices
- Respect explicit user requests (especially for CLT or specific levels).
- Treat explicit simple/brief wording as a stronger instruction than the default rich explanation template.
- Offer branching choices after each response.
- Maintain coherence across progressive deep-dives.
- End responses with a clear next-step invitation.

This skill is ready for use in learning, teaching, research support, and explanation tasks across a wide range of topics and audience types.
