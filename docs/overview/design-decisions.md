# Design Decisions

## Purpose
Capture durable design intent that should survive code churn.

## Current status
- `Implemented`: ESP32 telemetry bridge plus controller-input transport.
- `Implemented`: Pico-side UART mirroring designed to preserve REPL compatibility.
- `Project note`: robot should own its own timeout and stale-command behavior.
- `Needs verification`: some intended behaviors are not fully implemented yet.
- `Project note`: the ESP32 firmware repo is now named `robot-esp32-platform` because the codebase now includes both telemetry bridging and controller transport without moving control authority away from the Pico.

## Decisions
### Pico is the source of truth
The Pico is the real-time controller and should remain the owner of motor control, encoder handling, and time-sensitive logic.

### ESP32 is transport-only, not control-authoritative
The ESP32 may own log transport, network bridging, controller connectivity, and controller-state forwarding. It should not take control responsibilities or safety responsibilities.

### Non-halting debug is preferred
Breakpoint-style debugging is avoided for control-loop work because halting execution distorts PWM, encoder timing, and robot behavior.

### USB REPL output must remain normal
The print-mirroring design preserves IDE and REPL compatibility by keeping USB output unchanged and decorating only the UART copy.

### Canonical docs must preserve uncertainty
Conflicts and unresolved facts should be documented explicitly instead of normalized away.

## Related Docs
- Current architecture: `current-architecture.md`
- Known issues and open questions: `../verification/known-issues-and-open-questions.md`
- Pico drivetrain review: `../../robot-pico-platform/docs/drivetrain-pid-pio-reliability-review.md`
