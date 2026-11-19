---
story_id: US-003
plan_version: 1
updated: "2026-11-19"
tasks:
  - id: T001
    title: Implement structured host verification and adapters
    status: done
    depends_on: []
    parallel_safe: true
    repositories: [parent, android, esp32, pico]
    subsystems: [toolchain]
    acceptance: [AC-001, AC-002]
    test_mode: tdd
    evidence_levels: [static, host]
    test_support: [{kind: fake, seam: device discovery, purpose: exercise structured results without hardware, limitation: cannot establish device behavior}]
    red: {test: Adapter contract rejects malformed results, expected_failure: Contract check fails before adapter support, command: "python3 -m unittest discover"}
    green: {implementation: Repository adapters and schemas, command: "python3 -m unittest discover"}
    refactor_boundary: Keep platform commands behind their owning adapters.
  - id: T002
    title: Run connected-device and physical scenarios
    status: planned
    depends_on: [T001]
    parallel_safe: false
    repositories: [parent, android, esp32, pico]
    subsystems: [devices, verification]
    acceptance: [AC-002, AC-003]
    test_mode: physical-procedure
    evidence_levels: [device, bench, hil, motion]
    test_support: [{kind: simulator, seam: transport and control scenarios, purpose: rehearse failure paths before hardware, limitation: does not qualify timing or physical safety}]
    physical:
      approval_gate: Owner approves flashing, energization, and any motion stage.
      safe_setup: Scenario-specific safe setup from the registry.
      stop_conditions: [Unexpected motion, heat, current, communication loss, or stop-path failure]
      expected_result: Structured result plus evidence at the claimed level.
      evidence_destination: docs/verification/evidence/
---
# US-003 Implementation Plan
## Architecture And Boundaries
The parent defines contracts; each platform owns its adapter and authority.
## Pattern Analysis
Decision: extend platform adapters and scenario registry; do not centralize control logic.
## Change Map
Shared schemas, verification CLI, platform adapters, scenarios, and evidence.
## Diagram Index
[Verification loop](diagrams/verification-loop.svg).
## Test Strategy And Doubles
TDD at host seams; fakes/simulation expose contracts, followed by device-depth evidence.
## Task Graph
`T001 --> T002`
## Detailed Tasks
T001 is complete. T002 remains staged by device, bench, HIL, and motion risk.
## Physical Gates
Every energized, flash, and motion operation follows scenario approval and stop conditions.
## Traceability
T001 covers AC-001/2; T002 covers AC-002/3.
## Plan Change Log
- v1: migrated implemented and outstanding stages.
