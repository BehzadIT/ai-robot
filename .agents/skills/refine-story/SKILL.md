---
name: refine-story
description: Capture or interactively refine an AI robot story into a decision-complete definition. Use for ideas, boundaries, dependencies, acceptance criteria, risks, or definition review; do not create the implementation plan or mark Ready.
---
# Refine Story

Use the [workflow](../../../docs/backlog/workflow.md), definition
[template](../../../docs/backlog/templates/story/README.md), and
[checklist](references/refinement-checklist.md). Also read the consequential
decision and meaningful handoff sections of the
[human-agent contract](../../../docs/operations/human-agent-working-contract.md).

Inspect relevant context before asking. Play back the owner's intent and current
versus target behavior. Ask only for unresolved owner decisions identified by
the contract; do not turn discoverable facts or delegated implementation detail
into questions. Treat registry and hardware unknowns as dormant unless an
acceptance outcome or boundary decision depends on them. Activate only the
smallest decision-changing unknown; leave the rest open without reducing story
readiness. Before a compact question interaction, explain the situation,
investigation, options and consequences, recommendation, and readiness effect.
Use at most three tightly related decisions; isolate safety, destructive, and
blocking decisions. Persist each answer in the definition before continuing.

Number outcomes `AC-NNN`; identify evidence, physical gates, learning, and
diagrams. Record activated physical questions with the story decision they
serve; do not create an up-front inventory-clearance phase. Finish with the
meaningful-handoff template specialized to summarize definition coverage,
boundaries, decisions, remaining unknowns, and planning readiness. Leave the
story Draft and hand a complete definition to `plan-story`, or explicitly
remain Draft, split, Block, or Defer it.
