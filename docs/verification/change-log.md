# Change Log

## Purpose
Track documentation-level changes and major shifts in the understood state of the robot.

## Initial entry
- Established a shared canonical docs tree for the whole robot project.
- Consolidated implementation-backed facts from the three repos.
- Captured hardware, wiring, power, and app conflicts into the verification section.

## Agentic workflow plan introduced
- Added a deferred post-C++-migration operations plan for the robot-specific
  agentic development workflow.
- Captured the current sweet spot for context engineering, spec-driven work,
  harness and verification depth, compound learning, and lightweight evaluation.
- Linked the workflow plan into the parent docs and root agent instructions so
  future agents can revisit it after the Pico C++ migration and ESP32 gateway
  clean-start path are stable.

## Integrated VS Code workspace introduced
- Added a portable multi-root workspace for the parent integration repository
  and the Android, ESP32, and Pico platform repositories.
- Kept platform Git histories, build workflows, SDK configuration, and hardware
  deployment settings independently owned.
- Documented how to use the integrated workspace without changing subsystem
  ownership boundaries.

## US-001 system model and working contract adopted

- Replaced the mixed current/target architecture page with one canonical,
  component-oriented system model while retaining the old path as a child-repo
  compatibility link.
- Added capability horizons and moved unresolved product-direction questions
  into the durable roadmap.
- Activated lightweight backlog, risk, Ready/Done, traceability,
  communication, approval, and evidence guardrails.
- Kept detailed post-migration workflow enhancements deferred and preserved
  US-002 hardware/evidence and US-003 toolchain/device responsibilities as
  separate stories.
- Preserved Pico command-admission, motor, and safety authority; no runtime,
  protocol, wiring, or submodule revision changed.

## US-002 registry and evidence foundation implemented

- Added versioned component, workshop-tool, source, question, and evidence
  contracts with claim-level provenance and separate identity, inventory,
  installation, connection, and functional state.
- Seeded provisional records from retained project sources without promoting
  owner reports or project notes to physical verification.
- Added priority component/tool dossiers, curated manual summaries, reusable
  unpowered and powered procedures, append-only evidence templates, and a
  validator with schema, reference, source-hash, generated-index, local-link,
  and evidence-mutation checks.
- Exposed additional motor PWM/DIR and charger-current conflicts. Powered
  charging, encoder measurement, firmware changes, motion, the first as-built
  revision, and the KiCad schematic remain blocked on their documented owner
  input, equipment, and approval gates.
- Preserved Pico control/safety authority and made no platform-code or submodule
  revision change.

## Related Docs
- Project summary: `../overview/project-summary.md`
- System architecture: `../overview/system-architecture.md`
- Capability roadmap: `../overview/capability-roadmap.md`
- Source index: `../reference/source-index.md`
