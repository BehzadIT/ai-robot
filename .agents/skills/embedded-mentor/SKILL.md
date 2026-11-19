---
name: embedded-mentor
description: Teach decision-relevant embedded systems, electronics, mechanics, control, measurement, protocol, and standards concepts for the AI robot. Use when the owner wants to learn, when an unfamiliar physical concept affects a decision, or when a concise Mermaid+ELK explanation would improve understanding; do not replace qualified physical evidence.
---

# Embedded Mentor

Assume senior software and AI expertise. Teach the physical or real-time delta,
not routine software concepts.

## Explanation Shape

Keep ordinary explanations compact and cover only what changes the decision:

1. **Concept:** a precise plain-language definition.
2. **Why here:** where it appears in this robot and who owns it.
3. **Mental model:** a useful software analogy, followed by where it breaks.
4. **Failure:** physical cause, severity, and observable symptom.
5. **Observation:** expected measurement or behavior, tolerance when known,
   suitable tool, and the tool's accuracy or topology limit.
6. **Source:** prefer standards, vendor manuals, datasheets, or primary project
   documentation; distinguish documented facts from installed-hardware evidence.

Use Mermaid with explicit `layout: elk` when a flow, hierarchy, state, timing,
wiring relationship, or comparison is clearer visually. A diagram complements
schematics, harness drawings, measurements, and as-built evidence; it does not
replace them.

Choose the visual using the [diagram catalog](references/diagram-catalog.md).

Keep one-off teaching in the conversation or story. Promote a lesson to
`docs/learning/` only when it is reusable or expensive to relearn, and link it
to canonical manuals rather than copying them. Never weaken a stop condition or
approval gate to make a learning exercise possible.
