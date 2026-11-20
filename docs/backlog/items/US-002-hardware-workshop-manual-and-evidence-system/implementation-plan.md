---
story_id: US-002
plan_version: 2
updated: "2026-11-19"
tasks:
  - id: T001
    title: Establish registries and evidence contracts
    status: done
    depends_on: []
    parallel_safe: true
    repositories: [parent]
    subsystems: [hardware-documentation]
    acceptance: [AC-001, AC-002]
    test_mode: static-only
    evidence_levels: [static]
    test_support: []
    static_check: {method: Registry schema validation, command: "python3 tools/docs/validate_us002_registry.py"}
  - id: T002
    title: Qualify physical inventory and manuals
    status: in-progress
    depends_on: [T001]
    parallel_safe: false
    repositories: [parent]
    subsystems: [workshop, hardware]
    acceptance: [AC-001, AC-002, AC-003]
    test_mode: physical-procedure
    evidence_levels: [device, bench]
    test_support: [{kind: fixture, seam: physical inventory, purpose: identify and measure items reproducibly, limitation: cannot prove unobserved condition}]
    physical:
      approval_gate: Owner approves energized or invasive inspection.
      safe_setup: De-energized inspection first; use registered tools and PPE.
      stop_conditions: [Unexpected voltage, heat, motion, damage, or uncertain identity]
      expected_result: Qualified records linked to append-only evidence.
      evidence_destination: docs/verification/evidence/
  - id: T003
    title: Define component documentation contracts and validation
    status: done
    depends_on: [T001]
    parallel_safe: true
    repositories: [parent]
    subsystems: [hardware-documentation]
    acceptance: [AC-004, AC-005]
    test_mode: static-only
    evidence_levels: [static]
    test_support: [{kind: fixture, seam: synthetic documentation metadata and citations, purpose: reject stale or overstated curation state, limitation: does not assess source-summary quality}]
    static_check: {method: Schema and validator tests, command: "python3 -m unittest tools.docs.tests.test_validate_us002_records -v"}
  - id: T004
    title: Organize component packs and migrate registered vendor sources
    status: done
    depends_on: [T003]
    parallel_safe: false
    repositories: [parent]
    subsystems: [hardware-documentation]
    acceptance: [AC-003, AC-004]
    test_mode: static-only
    evidence_levels: [static]
    test_support: []
    static_check: {method: Path, hash, source-map, and link validation, command: "python3 tools/docs/validate_us002_records.py"}
  - id: T005
    title: Create reusable component documentation curation skill
    status: done
    depends_on: [T003]
    parallel_safe: true
    repositories: [parent]
    subsystems: [agentic-workflow, hardware-documentation]
    acceptance: [AC-005, AC-006]
    test_mode: static-only
    evidence_levels: [static]
    test_support: [{kind: fixture, seam: future documentation template, purpose: standardize coverage and citation structure, limitation: the skill is not applied to real manuals in this task}]
    static_check: {method: Skill package validation, command: "python3 /home/behzad/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/curate-component-documentation"}
  - id: T006
    title: Generate component catalog and update agent routing
    status: done
    depends_on: [T004, T005]
    parallel_safe: false
    repositories: [parent]
    subsystems: [hardware-documentation, agentic-workflow]
    acceptance: [AC-004, AC-006]
    test_mode: static-only
    evidence_levels: [static]
    test_support: []
    static_check: {method: Generated index and diagram checks, command: "python3 tools/docs/validate_us002_records.py && npm run diagrams:check"}
  - id: T007
    title: Review static documentation-system delivery
    status: done
    depends_on: [T006]
    parallel_safe: false
    repositories: [parent]
    subsystems: [hardware-documentation]
    acceptance: [AC-003, AC-004, AC-005, AC-006]
    test_mode: static-only
    evidence_levels: [static]
    test_support: []
    static_check: {method: Full documentation validation, command: "python3 -m unittest discover -s tools/docs/tests -v"}
---
# US-002 Implementation Plan
## Architecture And Boundaries
Shared facts stay in parent docs; firmware ownership is unchanged.
## Pattern Analysis
Decision: extend current registries and append-only evidence rather than invent another inventory system.
## Change Map
Registries, component packs, manuals, curation skill, generated indexes,
question queue, and evidence bundles.
## Diagram Index
[Information flow](diagrams/information-flow.svg).
## Test Strategy And Doubles
Schema checks precede controlled physical inspection; fixtures aid repeatability but never substitute for observations.
## Task Graph
`T001 --> T002`; `T001 --> T003`; `T003 --> T004`; `T003 --> T005`;
`T004 + T005 --> T006 --> T007`.
## Detailed Tasks
T001 establishes registry and evidence contracts. T002 resolves identity and
condition through approved physical procedures. T003-T007 establish the
agent-first component-documentation system without extracting manual content.
## Physical Gates
T002 is owner-gated and stops on unexpected energy, motion, heat, damage, or identity uncertainty.
## Traceability
T001 covers AC-001/2; T002 covers AC-001/2/3; T003-T007 cover AC-003/4/5/6.
## Plan Change Log
- v1: migrated current progress from the historical story.
- v2: added component packs, documentation coverage contracts, deterministic source
  locators, a repository curation skill, and generated agent-first navigation;
  actual manual extraction remains a later task.
