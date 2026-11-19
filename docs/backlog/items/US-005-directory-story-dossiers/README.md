---
id: US-005
title: Directory-Based Story Dossiers And Deterministic Engineering Plans
status: done
priority: high
risk_class: normal
owner: parent-workspace
created: "2026-11-19"
updated: "2026-11-19"
completed: "2026-11-19"
dependencies: [{id: US-004, kind: blocks}]
references: [docs/backlog/workflow.md, .agents/README.md]
evidence: [tools/docs/validate_backlog.py, tools/docs/tests/test_validate_backlog.py, tools/docs/render_story_diagrams.py, package-lock.json]
diagrams: [{path: diagrams/dossier-workflow.mmd, kind: data-flow}]
---
# US-005: Directory-Based Story Dossiers And Deterministic Engineering Plans

## User Story
As the solo robot developer, I want each story to be a self-contained dossier with a separately reviewed definition and implementation plan so agents execute explicit tasks, tests, diagrams, and physical gates without adding ceremony.

## Acceptance Criteria
- **AC-001:** Every story is a stable directory containing definition, plan when Ready+, and optional diagrams/materials.
- **AC-002:** Planning produces a validated dependency DAG with acceptance traceability, test mode, doubles, evidence depth, and physical gates.
- **AC-003:** Mermaid sources and deterministic SVGs are repository-owned and checked for freshness.
- **AC-004:** Skills separate refinement, planning, execution, review, and embedded mentoring with deterministic checklists.
- **AC-005:** The backlog front door remains concise and only its marked index is generated.

## Scope
Parent workflow, skills, schemas, tooling, CI, and migration only. Platform ownership and runtime behavior do not change.

## Outcome
Implemented. Historical story content is retained under each dossier's
`materials/`; definitions, plans, diagrams, generated index, skills, schemas,
tests, rendering, and CI now follow the directory workflow.
