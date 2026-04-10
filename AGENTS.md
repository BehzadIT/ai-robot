# AGENTS.md

## Purpose
This repository is the integration workspace for the AI robot system.

It provides shared project context for agents and humans working across the
Android operator app, ESP32 platform firmware, Pico control firmware, and
system documentation.

## Repository Layout
- `docs/`: canonical shared robot documentation.
- `robot-android-app/`: Android operator app submodule.
- `robot-esp32-platform/`: ESP32 platform firmware submodule.
- `robot-pico-platform/`: Pico firmware and real-time control submodule.

The platform directories are independent Git repositories with separate release
cycles. The parent repository records integrated system snapshots and shared
context; it does not replace the child repositories.

## Read First
For system-level or cross-project work, start with:
- `docs/README.md`
- `docs/overview/project-summary.md`
- `docs/overview/current-architecture.md`
- `docs/overview/design-decisions.md`
- `docs/interfaces/command-protocol.md`
- `docs/interfaces/telemetry-protocol.md`
- `docs/electrical/wiring-and-pinout.md`
- `docs/verification/known-issues-and-open-questions.md`

For platform-specific work, also read the nearest `AGENTS.md` inside the target
submodule.

## Ownership Boundaries
- Android owns operator UI, app state, and client transport lifecycle.
- Pico owns real-time control, safety behavior, motor authority, encoders, and
  timing-sensitive hardware interaction.
- ESP32 currently owns passive telemetry bridging and platform support only.
- Shared docs own architecture, protocol, hardware, verification, and known
  cross-project decisions.

Do not move control or safety ownership between subsystems unless the relevant
architecture docs are intentionally updated in the same change.

## Git and Submodule Rules
- Commit platform code changes inside the relevant submodule.
- Commit parent-level docs, context, and submodule pointer updates in this repo.
- Update the parent submodule pointer only when recording a new integrated
  system state.
- Do not assume all child repositories are released together.
- Preserve unrelated dirty work in child repositories.

## Agent Working Rules
- Treat `docs/` as the source of truth for project-wide context.
- Keep parent docs focused on system behavior, subsystem boundaries, protocols,
  hardware, operations, and verification.
- Put platform implementation details in the relevant child repo's `docs/`
  directory.
- Keep `AGENTS.md` files short and navigational; put durable technical detail in
  docs or code comments.
- When changing protocols, wiring, safety behavior, or subsystem boundaries,
  update the shared docs together with the platform change.
- Before non-trivial edits, state the subsystem boundary being preserved or
  changed, the implementation pattern being used, and the engineering reason.
