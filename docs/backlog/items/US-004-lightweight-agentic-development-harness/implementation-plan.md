---
story_id: US-004
plan_version: 1
updated: "2026-11-19"
tasks:
  - id: T001
    title: Implement the lightweight harness
    status: done
    depends_on: []
    parallel_safe: false
    repositories: [parent]
    subsystems: [workflow, agent-skills]
    acceptance: [AC-001, AC-002, AC-003]
    test_mode: tdd
    evidence_levels: [static, host]
    test_support: [{kind: fixture, seam: temporary backlog tree, purpose: test invalid lifecycle records, limitation: does not assess instruction quality}]
    red: {test: Invalid stories and stale indexes fail validation, expected_failure: New validation tests initially fail, command: "python3 -m unittest tools.docs.tests.test_validate_backlog"}
    green: {implementation: Workflow, skills, schema, validator, and CI, command: "python3 -m unittest tools.docs.tests.test_validate_backlog"}
    refactor_boundary: Keep lifecycle policy separate from platform implementation.
---
# US-004 Implementation Plan
## Architecture And Boundaries
Parent process/tooling only.
## Pattern Analysis
Decision: adapt software agent harness practices to solo embedded risk.
## Change Map
Workflow, skills, schema, validator, tests, and CI.
## Diagram Index
[Original harness](diagrams/original-harness.svg).
## Test Strategy And Doubles
TDD with filesystem fixtures.
## Task Graph
`T001`
## Detailed Tasks
T001 completed the original harness.
## Physical Gates
None; rules describe but do not perform physical work.
## Traceability
T001 covers AC-001 through AC-003.
## Plan Change Log
- v1: retrospective plan for completed work.
