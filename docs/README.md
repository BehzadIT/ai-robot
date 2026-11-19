# Robot System Documentation

This directory is the parent-level documentation set for the AI robot system.

Use these docs for cross-project context: architecture, subsystem boundaries,
protocols, hardware, operations, verification, and known integration risks.
Platform implementation details live in the child repositories.

## Start Here
- `overview/project-summary.md`: current system identity and stack.
- `overview/system-architecture.md`: component-oriented current and target
  behavior, interfaces, failure behavior, and ownership boundaries.
- `overview/capability-roadmap.md`: Now/Next/Later/Explore capability horizons
  and open product-direction questions.
- `overview/design-decisions.md`: durable cross-project design decisions.
- `backlog/README.md`: generated concise backlog grouped by story status.
- `backlog/workflow.md`: active lifecycle, risk classes, Ready/Done
  definitions, dependency semantics, and traceability contract.
- `reference/source-index.md`: where source material and platform repos live.

## Interfaces
- `interfaces/command-protocol.md`: operator-intent command semantics and
  current/target transport routing.
- `interfaces/telemetry-protocol.md`: Pico-to-ESP32 logs plus target ESP32
  gateway stats/diagnostics semantics.
- `interfaces/hardware-interfaces.md`: hardware-facing integration points.

## Hardware And Inventory
- `electrical/`: power, wiring, BMS, charging, and electrical risks.
- `mechanical/`: chassis, drivetrain, mounting fitment, and physical build notes.
- `reference/component-registry.yaml`: canonical component identity, state,
  claims, provenance, and blocking questions.
- `reference/tool-registry.yaml`: workshop capability, condition, limits,
  accessories, familiarity, and safe-use constraints.
- `reference/source-registry.yaml`: local source identity, hashes,
  applicability, and extraction status.
- `reference/hardware-records.md`: record update, provenance, evidence, and
  validation workflow.
- `reference/bom-and-parts-status.md`: generated human-readable registry view.
- `assets/electrical/`: battery, wiring, charger, BMS, and cell source files.
- `assets/mechanical/`: chassis, drivetrain, shaft adapter, and mounting source
  files.
- `assets/reference/`: component lists and general project source material.

## Operations And Verification
- `operations/`: bring-up, troubleshooting, calibration, maintenance, and bench
  debugging workflows.
- `operations/development-workspace.md`: canonical integrated VS Code workspace,
  repository boundaries, and platform tooling ownership.
- `operations/agentic-toolchain.md`: US-003 discovery, verification, safety
  gates, result contracts, and staged evidence workflow.
- `operations/esp32-gateway-pico-control-clean-start-plan.md`: staged plan for
  moving wireless gateway duties to ESP32 while keeping Pico as the control and
  safety authority.
- `operations/human-agent-working-contract.md`: active collaboration,
  communication, approval, and minimum evidence guardrails.
- `operations/agentic-development-workflow.md`: active lightweight harness,
  repository skills, evidence ladder, learning, and diagram conventions.
- `learning/`: concise reusable embedded, electrical, control, measurement, and
  mechanical learning notes.
- `verification/`: known issues, checklists, and project change notes.
- `verification/questions/US-002.yaml`: live hardware/workshop discovery queue.
- `verification/procedures/` and `verification/evidence/`: reusable physical
  procedures and append-only qualified observations.

## Platform Implementation Docs
- Android app details: `../robot-android-app/docs/README.md`
- ESP32 platform details: `../robot-esp32-platform/docs/README.md`
- Pico firmware details: `../robot-pico-platform/docs/README.md`

Parent docs may summarize platform behavior, but they should not duplicate
low-level implementation plans that belong in a child repo.
