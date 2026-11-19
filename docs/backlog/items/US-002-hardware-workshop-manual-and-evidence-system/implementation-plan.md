---
story_id: US-002
plan_version: 1
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
---
# US-002 Implementation Plan
## Architecture And Boundaries
Shared facts stay in parent docs; firmware ownership is unchanged.
## Pattern Analysis
Decision: extend current registries and append-only evidence rather than invent another inventory system.
## Change Map
Registries, manuals, question queue, and evidence bundles.
## Diagram Index
[Information flow](diagrams/information-flow.svg).
## Test Strategy And Doubles
Schema checks precede controlled physical inspection; fixtures aid repeatability but never substitute for observations.
## Task Graph
`T001 --> T002`
## Detailed Tasks
T001 establishes contracts. T002 resolves identity and condition with approved procedures.
## Physical Gates
T002 is owner-gated and stops on unexpected energy, motion, heat, damage, or identity uncertainty.
## Traceability
T001 covers AC-001/2; T002 covers all criteria.
## Plan Change Log
- v1: migrated current progress from the historical story.
