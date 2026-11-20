---
name: plan-story
description: Turn a decision-complete AI robot story into a deterministic implementation plan and Ready story. Use for architecture analysis, task breakdown, tests, doubles, evidence, diagrams, physical gates, and readiness; do not implement tasks.
---
# Plan Story

Read the story, [workflow](../../../docs/backlog/workflow.md), nearest `AGENTS.md`,
the consequential decision and meaningful handoff sections of the
[human-agent contract](../../../docs/operations/human-agent-working-contract.md),
and [planning checklist](references/planning-checklist.md). Inspect docs,
code/tests, Git, and analogues. Record `reuse`, `extend`, `adapt`, `replace`, or
`no precedent`; retain non-trivial analysis under `materials/`.

Resolve repository and precedent facts independently. When investigation
reveals an unresolved owner decision that materially affects architecture,
ownership, scope, evidence, safety, or cost, record it and pause only dependent
planning. Explain the situation, evidence, viable consequences,
recommendation, uncertainty, and readiness effect before a compact question
interaction. Use at most three tightly related decisions and persist every
answer and rationale in the plan before continuing.

Create `implementation-plan.md` and observable `TNNN` tasks with an acyclic DAG,
parallel safety, AC coverage, test mode, doubles, evidence, and physical gates.
Do not add bulk hardware qualification as a prerequisite. Leave registry
unknowns dormant unless a planned task depends on them; attach each activated
unknown to the first dependent task and define the smallest just-in-time owner
observation or measurement that resolves it. Use applicable manufacturer
ratings for planning when their scope and conditions are preserved; require
physical evidence only for the as-built fact the decision needs.
Prefer named red/green/refactor TDD. Use a bounded retained spike only for a
genuine unknown; never silently promote prototype code. Render diagrams,
validate, review, then mark Ready. Later material changes increment
`plan_version` and append the change log.

Finish with the meaningful-handoff template specialized to summarize the
selected approach, task graph, acceptance coverage, test strategy, evidence
levels, gates, residual uncertainty, and Ready decision. If no owner decision
was needed or remains, say so without asking for acknowledgment.
