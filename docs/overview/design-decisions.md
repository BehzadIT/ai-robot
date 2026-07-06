# Design Decisions

## Purpose
Capture durable design intent that should survive code churn.

## Current status
- `Implemented`: ESP32 telemetry bridge plus controller-input transport.
- `Implemented`: Pico-side UART mirroring designed to preserve REPL compatibility.
- `Project note`: robot should own its own timeout and stale-command behavior.
- `Planned`: ESP32 becomes the robot wireless gateway for the next clean-start
  C++ architecture while Pico remains the real-time control and safety owner.
- `Needs verification`: some intended behaviors are not fully implemented yet.
- `Project note`: the ESP32 firmware repo is now named `robot-esp32-platform` because the codebase now includes both telemetry bridging and controller transport without moving control authority away from the Pico.

## Decisions
### Pico is the source of truth
The Pico is the real-time controller and should remain the owner of motor control, encoder handling, and time-sensitive logic.

### ESP32 is transport-only, not control-authoritative
The ESP32 may own log transport, network bridging, controller connectivity, and controller-state forwarding. It should not take control responsibilities or safety responsibilities.

### ESP32 owns the target wireless gateway
The next clean-start application should place robot wireless endpoints on the
ESP32. That includes WebSocket transport for logs, structured stats,
diagnostics, and optionally Android operator-intent messages.

The ESP32 may forward bounded command DTOs to the Pico, but command freshness,
recover behavior, source admission, safety state, and final actuator output
remain Pico responsibilities.

### Pico Wi-Fi is not required for the next reliable C++ control firmware
Pico 2 W CYW43 plus FreeRTOS bring-up has shown fragile behavior during the C++
migration. The next reliable Pico control firmware should be able to boot,
enumerate over USB, run control tasks, and exchange UART messages without
initializing CYW43 or hosting WebSocket endpoints.

Although the board remains a Raspberry Pi Pico 2 W, the clean-start Pico
firmware should be treated as a no-network controller. It should not own
Bluetooth, Wi-Fi, HTTP, or WebSocket responsibilities. Those network-facing
roles belong to the ESP32 wireless gateway.

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
