---
story_id: US-002
plan_version: 4
updated: "2026-11-20"
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
    status: skipped
    skip_reason: Superseded by progressive qualification; future stories activate only the physical facts their decisions need.
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
  - id: T008
    title: Curate currently registered component sources
    status: done
    depends_on: [T005]
    parallel_safe: true
    repositories: [parent]
    subsystems: [hardware-documentation]
    acceptance: [AC-003, AC-005, AC-006]
    test_mode: static-only
    evidence_levels: [static]
    test_support: [{kind: fixture, seam: registered source hashes and component documentation front matter, purpose: prevent stale or incomplete curated claims, limitation: static validation cannot prove semantic source accuracy}]
    static_check: {method: Source, citation, and documentation validation, command: "python3 tools/docs/validate_us002_records.py"}
  - id: T009
    title: Prepare all-component non-energizing visual identity capture
    status: done
    depends_on: [T001]
    parallel_safe: true
    repositories: [parent]
    subsystems: [hardware-documentation, workshop]
    acceptance: [AC-001, AC-002, AC-003]
    test_mode: static-only
    evidence_levels: [static]
    test_support: []
    static_check: {method: Procedure structure and documentation validation, command: "python3 tools/docs/validate_us002_records.py"}
  - id: T010
    title: Execute non-energizing visual identity capture
    status: skipped
    skip_reason: No bulk capture campaign; a future dependent story may activate this reusable procedure just in time.
    depends_on: [T009]
    parallel_safe: false
    repositories: [parent]
    subsystems: [workshop, shared-hardware]
    acceptance: [AC-001, AC-002]
    test_mode: physical-procedure
    evidence_levels: [bench]
    test_support: [{kind: fixture, seam: camera and identity checklist, purpose: capture labels and layout reproducibly, limitation: photographs cannot prove hidden wiring or powered behavior}]
    physical:
      approval_gate: Owner performs and approves the visual inspection; no agent inference substitutes for photographs or records.
      safe_setup: Known external sources disconnected without manipulating unidentified wiring; tracks stationary; no pack opening or connector removal; any region with unknown battery or high-current isolation is treated as energized and inaccessible.
      stop_conditions: [Heat, odor, swelling, damaged insulation, exposed conductors, unexpected indicators, unknown isolation requiring close access, strained wiring, or required disassembly]
      expected_result: EV-2026-001 identifies visible products or records explicit unresolved identities for all required component packs.
      evidence_destination: docs/verification/evidence/EV-2026-001/
  - id: T011
    title: Reconcile identity and split independently rated products
    status: skipped
    skip_reason: Perform within the future story that obtains decision-relevant identity evidence.
    depends_on: [T010]
    parallel_safe: false
    repositories: [parent]
    subsystems: [hardware-documentation, shared-hardware]
    acceptance: [AC-001, AC-002, AC-004]
    test_mode: static-only
    evidence_levels: [static]
    test_support: []
    static_check: {method: Registry, assembly-reference, evidence, and question validation, command: "python3 tools/docs/validate_us002_records.py --base-ref HEAD"}
  - id: T012
    title: Acquire exact identified product sources
    status: skipped
    skip_reason: Acquire an exact source only when a future story identifies the product and needs the source.
    depends_on: [T011]
    parallel_safe: false
    repositories: [parent]
    subsystems: [hardware-documentation]
    acceptance: [AC-003, AC-004]
    test_mode: static-only
    evidence_levels: [static]
    test_support: []
    static_check: {method: Source authority, retrieval, hash, and component-map validation, command: "python3 tools/docs/validate_us002_records.py"}
  - id: T013
    title: Curate post-identity component documentation
    status: skipped
    skip_reason: Curate incrementally in the future story that changes component knowledge.
    depends_on: [T008, T012]
    parallel_safe: true
    repositories: [parent]
    subsystems: [hardware-documentation]
    acceptance: [AC-003, AC-004, AC-005, AC-006]
    test_mode: static-only
    evidence_levels: [static]
    test_support: [{kind: fixture, seam: component documentation coverage and reviewed hashes, purpose: require complete source review before curated status, limitation: physical applicability still depends on evidence}]
    static_check: {method: Full component documentation validation, command: "python3 tools/docs/validate_us002_records.py"}
  - id: T014
    title: Inspect charger configuration without a battery
    status: skipped
    skip_reason: Retained as a reusable operation-specific procedure; activate only in a charging or power-electronics story.
    depends_on: [T013]
    parallel_safe: false
    repositories: [parent]
    subsystems: [workshop, shared-hardware]
    acceptance: [AC-001, AC-002, AC-003]
    test_mode: physical-procedure
    evidence_levels: [bench]
    test_support: [{kind: fixture, seam: exact charger manual and display checklist, purpose: observe configuration without charging, limitation: displayed configuration does not prove charge-current enforcement}]
    physical:
      approval_gate: Separate explicit owner approval after exact-manual review confirms safe no-battery menu access.
      safe_setup: Charger disconnected from robot pack; output leads isolated; settings unchanged; no charging initiated.
      stop_conditions: [Heat, odor, unexpected output behavior, error indication, damaged leads, or uncertain standalone operation]
      expected_result: EV-2026-002 records the displayed model, program, and settings or an honest blocked result.
      evidence_destination: docs/verification/evidence/EV-2026-002/
  - id: T015
    title: Reconcile, regenerate, and independently review curation
    status: done
    depends_on: [T013, T014]
    parallel_safe: false
    repositories: [parent]
    subsystems: [hardware-documentation]
    acceptance: [AC-001, AC-002, AC-003, AC-004, AC-005, AC-006]
    test_mode: static-only
    evidence_levels: [static]
    test_support: []
    static_check: {method: Full registry, documentation, backlog, and diagram validation, command: "python3 -m unittest discover -s tools/docs/tests -v"}
---
# US-002 Implementation Plan
## Architecture And Boundaries
Shared facts stay in parent docs; firmware ownership is unchanged.
## Pattern Analysis
Decision: extend current registries and append-only evidence rather than invent another inventory system.
Current-source and identity gates are recorded in
[the component curation audit](materials/component-curation-audit.md).
## Change Map
Registries, component packs, manuals, curation skill, generated indexes,
question queue, and evidence bundles.
## Diagram Index
[Information flow](diagrams/information-flow.svg).
## Test Strategy And Doubles
Schema checks precede controlled physical inspection; fixtures aid repeatability but never substitute for observations.
## Task Graph
`T001 --> T002`; `T001 --> T003`; `T003 --> T004`; `T003 --> T005`;
`T004 + T005 --> T006 --> T007`; `T005 --> T008`; `T001 --> T009 --> T010 --> T011 --> T012`;
`T008 + T012 --> T013 --> T014`; `T013 + T014 --> T015`.
## Detailed Tasks
T001 establishes registry and evidence contracts. T002 resolves identity and
condition through approved physical procedures. T003-T007 establish the
agent-first component-documentation system without extracting manual content.
T008-T009 curate existing sources and prepare reusable evidence procedures.
T010-T014 are deliberately skipped as a bulk campaign: future stories activate
only the identity, source, measurement, or charger evidence their decisions
need and update the shared records. T015 reconciles and reviews this delivery.
## Physical Gates
No physical task is a standing prerequisite. If a future story activates T010's
procedure, it permits non-energizing visual capture only. If a charging story
activates T014's procedure, it remains a separate owner gate and never connects
the charger to the robot pack. Hazardous work keeps its operation-specific
approval, safe-state, and stop conditions.
## Traceability
T001 covers AC-001/2; T002 covers AC-001/2/3; T003-T007 cover AC-003/4/5/6;
T008 covers AC-003/5/6; T009-T010 cover AC-001/2/3; T011 covers
AC-001/2/4; T012 covers AC-003/4; T013 covers AC-003/4/5/6; T014 covers
AC-001/2/3; and T015 covers AC-001 through AC-006.
## Plan Change Log
- v1: migrated current progress from the historical story.
- v2: added component packs, documentation coverage contracts, deterministic source
  locators, a repository curation skill, and generated agent-first navigation;
  actual manual extraction remains a later task.
- v3: added current-source curation, all-component non-energizing visual identity evidence,
  exact-source acquisition, independently rated product splitting, and a
  separately gated charger-display inspection.
- v4: replaced bulk physical qualification with progressive, story-scoped
  activation. Open hardware questions remain dormant until a concrete decision
  needs them; reusable procedures and documentation are updated by that story.
