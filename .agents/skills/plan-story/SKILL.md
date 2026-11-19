---
name: plan-story
description: Turn a decision-complete AI robot story into a deterministic implementation plan and Ready story. Use for architecture analysis, task breakdown, tests, doubles, evidence, diagrams, physical gates, and readiness; do not implement tasks.
---
# Plan Story

Read the story, [workflow](../../../docs/backlog/workflow.md), nearest `AGENTS.md`,
and [planning checklist](references/planning-checklist.md). Inspect docs,
code/tests, Git, and analogues. Record `reuse`, `extend`, `adapt`, `replace`, or
`no precedent`; retain non-trivial analysis under `materials/`.

Create `implementation-plan.md` and observable `TNNN` tasks with an acyclic DAG,
parallel safety, AC coverage, test mode, doubles, evidence, and physical gates.
Prefer named red/green/refactor TDD. Use a bounded retained spike only for a
genuine unknown; never silently promote prototype code. Render diagrams,
validate, review, then mark Ready. Later material changes increment
`plan_version` and append the change log.
