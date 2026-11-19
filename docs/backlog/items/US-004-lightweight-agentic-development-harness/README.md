---
id: US-004
title: Lightweight Agentic Development Harness
status: done
priority: high
risk_class: normal
owner: parent-workspace
created: "2026-11-19"
updated: "2026-11-19"
completed: "2026-11-19"
dependencies: [{id: US-001, kind: blocks}, {id: US-002, kind: informs}, {id: US-003, kind: informs}]
references: [docs/backlog/workflow.md, docs/operations/human-agent-working-contract.md]
evidence: [tools/docs/validate_backlog.py, docs/verification/change-log.md]
diagrams: [{path: diagrams/original-harness.mmd, kind: state}]
---
# US-004: Lightweight Agentic Development Harness

## User Story
As the solo developer, I want a lightweight agentic harness so stories are refined, executed, reviewed, learned from, and completed with risk-appropriate evidence.

## Acceptance Criteria
- **AC-001:** A minimal Draft-to-Done lifecycle and durable story records exist.
- **AC-002:** Repository skills route refinement, execution, review, and mentoring.
- **AC-003:** Validation prevents status, dependency, and index drift.

## Outcome
Completed and subsequently evolved by US-005. See [implementation-plan.md](implementation-plan.md) and [historical record](materials/legacy-story-record.md).
