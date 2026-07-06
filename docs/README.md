# Robot System Documentation

This directory is the parent-level documentation set for the AI robot system.

Use these docs for cross-project context: architecture, subsystem boundaries,
protocols, hardware, operations, verification, and known integration risks.
Platform implementation details live in the child repositories.

## Start Here
- `overview/project-summary.md`: current system identity and stack.
- `overview/current-architecture.md`: control plane, telemetry plane, and
  ownership boundaries.
- `overview/design-decisions.md`: durable cross-project design decisions.
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
- `reference/bom-and-parts-status.md`: current parts, available inventory, and
  legacy component-list status.
- `assets/electrical/`: battery, wiring, charger, BMS, and cell source files.
- `assets/mechanical/`: chassis, drivetrain, shaft adapter, and mounting source
  files.
- `assets/reference/`: component lists and general project source material.

## Operations And Verification
- `operations/`: bring-up, troubleshooting, calibration, maintenance, and bench
  debugging workflows.
- `operations/esp32-gateway-pico-control-clean-start-plan.md`: staged plan for
  moving wireless gateway duties to ESP32 while keeping Pico as the control and
  safety authority.
- `operations/agentic-development-workflow.md`: deferred post-C++-migration
  plan for right-sized agentic development, evidence depth, task sizing,
  handoff, and durable learning.
- `verification/`: known issues, checklists, and project change notes.

## Platform Implementation Docs
- Android app details: `../robot-android-app/docs/README.md`
- ESP32 platform details: `../robot-esp32-platform/docs/README.md`
- Pico firmware details: `../robot-pico-platform/docs/README.md`

Parent docs may summarize platform behavior, but they should not duplicate
low-level implementation plans that belong in a child repo.
