# Current Architecture

## Purpose
Describe the current implemented architecture across the Pico, ESP32, Android app, motor driver, encoders, and power system.

## Current status
- `Implemented`: Pico runs the live control server and motor-control loop.
- `Implemented`: ESP32 runs a UART-to-WebSocket telemetry bridge.
- `Implemented`: ESP32 also forwards normalized joystick snapshots over a dedicated UART to the Pico.
- `Implemented`: Android app connects to the Pico WebSocket endpoint for control.
- `Implemented`: Pico enforces stale-command stop behavior for disconnected or silent control sessions.
- `Needs verification`: long-term target command routing if the architecture is later changed.
- `Project note`: the ESP32 firmware project is named `robot-esp32-platform` because it now owns both telemetry bridging and controller-input transport while still preserving Pico control authority.

## Architecture
### Control plane
- Android app sends signed throttle / turn drive intent plus stop / recover commands to the Pico over WebSocket.
- ESP32 can now receive Xbox controller input over Bluetooth and forward normalized joystick snapshots to the Pico over a dedicated UART.
- Pico receives commands, updates drive targets, and runs PID-based motor control.
- Pico treats transport disconnect or stale command freshness as a safety event and stops until a fresh command arrives.
- Pico also exposes legacy HTTP `/drive` and `/stop` endpoints.

### Telemetry plane
- Pico mirrors `print()` output and UART-only structured logs to UART0 on `GP0/GP1`.
- ESP32 receives those UART lines on `GPIO16/17`.
- ESP32 broadcasts received lines to WebSocket clients on `/ws`.

### Controller transport plane
- ESP32 transmits framed joystick snapshots on `GPIO25/26`.
- Pico receives those snapshots on `GP4/5`.
- Pico stores and validates the new transport input, but robot mapping from that input is still a later phase.

### Hardware ownership split
- Pico owns motors, encoders, drive targets, and stop behavior.
- ESP32 may own controller connectivity, normalization, and controller transport, but it must not own motor control, safety control, or timing-sensitive logic.
- Android acts as operator input only.

## Key data paths
- Control: `Android -> Pico WebSocket/HTTP -> Pico motor control`
- Telemetry: `Pico UART -> ESP32 -> WebSocket -> PC terminal`
- Controller transport: `Xbox controller -> ESP32 BLE/Bluepad32 -> dedicated UART -> Pico receiver`

## Related Docs
- Project summary: `project-summary.md`
- Design decisions: `design-decisions.md`
- Command protocol: `../interfaces/command-protocol.md`
- Telemetry protocol: `../interfaces/telemetry-protocol.md`
- Platform implementation docs:
  - `../../robot-android-app/docs/README.md`
  - `../../robot-esp32-platform/docs/README.md`
  - `../../robot-pico-platform/docs/README.md`
