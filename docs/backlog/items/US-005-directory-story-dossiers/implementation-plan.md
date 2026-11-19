---
story_id: US-005
plan_version: 2
updated: "2026-11-19"
tasks:
  - id: T001
    title: Migrate stories into directory dossiers
    status: done
    depends_on: []
    parallel_safe: true
    repositories: [parent]
    subsystems: [backlog]
    acceptance: [AC-001, AC-005]
    test_mode: tdd
    evidence_levels: [static, host]
    test_support: [{kind: fixture, seam: temporary dossier tree, purpose: exercise discovery and index generation, limitation: does not verify prose quality}]
    red: {test: Flat discovery and full-file generation fail new expectations, expected_failure: Directory cases fail old validator, command: "python3 -m unittest tools.docs.tests.test_validate_backlog"}
    green: {implementation: Directory discovery and marker-bounded generator, command: "python3 -m unittest tools.docs.tests.test_validate_backlog"}
    refactor_boundary: Preserve historical records under materials.
  - id: T002
    title: Validate deterministic engineering plans
    status: done
    depends_on: [T001]
    parallel_safe: true
    repositories: [parent]
    subsystems: [planning, verification]
    acceptance: [AC-002]
    test_mode: tdd
    evidence_levels: [static, host]
    test_support: [{kind: fixture, seam: plan front matter, purpose: cover DAG and conditional modes, limitation: semantic engineering judgment still needs review}]
    red: {test: Cycles, uncovered criteria, and incomplete modes are rejected, expected_failure: Invalid plans pass before schema and graph checks, command: "python3 -m unittest tools.docs.tests.test_validate_backlog"}
    green: {implementation: Plan schema and semantic validator, command: "python3 -m unittest tools.docs.tests.test_validate_backlog"}
    refactor_boundary: Keep definition and plan schemas separate.
  - id: T003
    title: Add deterministic Mermaid source and SVG pipeline
    status: done
    depends_on: [T001]
    parallel_safe: true
    repositories: [parent]
    subsystems: [documentation-tooling]
    acceptance: [AC-003]
    test_mode: tdd
    evidence_levels: [static, host]
    test_support: [{kind: fixture, seam: diagram file pairs, purpose: detect missing orphaned and stale output, limitation: rendering can vary when tool versions change}]
    red: {test: Missing and stale SVGs fail checks, expected_failure: No renderer freshness check exists, command: "npm run diagrams:check"}
    green: {implementation: Pinned Mermaid CLI and repository wrapper, command: "npm run diagrams:check"}
    refactor_boundary: Canonical source remains .mmd; SVG is generated.
  - id: T004
    title: Expand and separate lifecycle skills
    status: done
    depends_on: [T002]
    parallel_safe: true
    repositories: [parent]
    subsystems: [agent-skills]
    acceptance: [AC-004]
    test_mode: static-only
    evidence_levels: [static]
    test_support: []
    static_check: {method: Skill structure and quick validation, command: "python3 /home/behzad/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/plan-story"}
  - id: T005
    title: Integrate documentation CI and close the story
    status: done
    depends_on: [T002, T003, T004]
    parallel_safe: false
    repositories: [parent]
    subsystems: [ci, documentation]
    acceptance: [AC-001, AC-002, AC-003, AC-004, AC-005]
    test_mode: static-only
    evidence_levels: [static, host]
    test_support: []
    static_check: {method: Run complete documentation verification, command: "python3 -m unittest discover -s tools/docs/tests && python3 tools/docs/validate_backlog.py && npm run diagrams:check"}
---
# US-005 Implementation Plan
## Architecture And Boundaries
Parent workflow and tooling only. Android, ESP32, and Pico continue owning their existing runtime domains.
## Pattern Analysis
Decision: adapt the existing story harness. Directory dossiers solve artifact locality; a separate planning skill creates a deterministic execution contract. No precedent justifies a new tracker or mocking framework. Detailed analysis is retained in [materials/pattern-analysis.md](materials/pattern-analysis.md).
## Change Map
Backlog records and templates; story/plan schemas; validator/tests; Mermaid pipeline; repository skills; CI and operating docs.
## Diagram Index
[Dossier workflow](diagrams/dossier-workflow.svg) and the global [lifecycle](../../diagrams/story-lifecycle.svg).
## Test Strategy And Doubles
TDD is the default for behavior. Filesystem fixtures test invalid dossiers and plans. Static-only applies to instruction review. Physical procedures are not part of this tooling story.
## Task Graph
`T001 --> T002 --> T004 --> T005`; `T001 --> T003 --> T005`.
## Detailed Tasks
Tasks are intentionally small enough to verify independently. T001 preserves old records. T002 makes plan semantics executable. T003 pins rendering. T004 uses progressive skill references. T005 runs the integrated checks and records completion.
## Physical Gates
None. This story defines gates but performs no device or workshop operation.
## Traceability
Task front matter is the machine-checkable mapping; T005 rechecks every acceptance criterion.
## Plan Change Log
- v1: initial approved implementation plan.
- v2: recorded the unavailable Mermaid CLI 12.0.1 pin, selected published
  12.0.0, completed integration, and captured fresh validation evidence.
