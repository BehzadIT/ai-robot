# Current Architecture

## Purpose
Describe the current implemented architecture across the Pico, ESP32, Android app, motor driver, encoders, and power system.

## Current status
- `Implemented`: Pico 2 W runs the live control server and motor-control loop
  as separate FreeRTOS tasks pinned to different cores.
- `Implemented`: ESP32 runs a UART-to-WebSocket telemetry bridge.
- `Implemented`: ESP32 also forwards normalized joystick snapshots over a dedicated UART to the Pico.
- `Implemented`: Android app connects to the Pico WebSocket endpoint for control.
- `Implemented`: Pico enforces stale-command stop behavior for disconnected or silent control sessions.
- `Planned`: next clean-start C++ architecture moves robot wireless gateway
  duties to the ESP32 so the Pico control firmware does not require Pico
  Wi-Fi/CYW43 bring-up.
- `Planned`: in that clean-start architecture the Raspberry Pi Pico 2 W remains
  the Pico hardware target, but it is treated as a no-network controller: no
  Pico Bluetooth role, no Pico HTTP server, and no Pico WebSocket server.
- `Needs verification`: ESP32-routed Android command transport over a bounded
  UART handoff to the Pico.
- `Project note`: the ESP32 firmware project is named `robot-esp32-platform` because it now owns both telemetry bridging and controller-input transport while still preserving Pico control authority.

## Architecture
### Control plane
- Android app sends signed throttle / turn drive intent plus stop / recover commands to the Pico over WebSocket.
- ESP32 can now receive Xbox controller input over Bluetooth and forward normalized joystick snapshots to the Pico over a dedicated UART.
- Pico receives commands, updates drive targets, and runs PID-based motor control
  on the core 1 control task.
- Pico treats transport disconnect or stale command freshness as a safety event and stops until a fresh command arrives.
- Pico also exposes legacy HTTP `/drive` and `/stop` endpoints.

### Target clean-start control plane
- Android remains a WebSocket client, but the target server is the ESP32
  wireless gateway instead of the Pico.
- ESP32 receives bounded operator-intent messages over WebSocket and forwards
  only transport DTOs to the Pico over UART.
- Pico admits or rejects received intent, owns stale-input stop behavior, and
  remains the only subsystem that may decide final motor output.
- Existing Pico WebSocket/HTTP control remains a current implementation path
  until the clean-start gateway path is built and bench-verified.
- The target Pico firmware should expose no network API. All Bluetooth,
  HTTP, WebSocket, Wi-Fi, and client-facing network behavior belongs on ESP32.

### Telemetry plane
- Pico mirrors `print()` output and UART-only structured logs to UART0 on `GP0/GP1`.
- ESP32 receives those UART lines on `GPIO16/17`.
- ESP32 broadcasts received lines to WebSocket clients on `/ws`.
- Target clean-start telemetry uses the ESP32 as the robot wireless gateway for
  logs, structured stats, diagnostics, and bench clients. Log and stats traffic
  is best-effort and must not block command freshness.

### Controller transport plane
- ESP32 transmits framed joystick snapshots on `GPIO25/26`.
- Pico receives those snapshots on `GP4/5`.
- Pico now maps the received controller snapshots into live drivetrain intent while keeping all motor authority and stop behavior on the Pico.

### Hardware ownership split
- Pico core 1 owns motors, encoders, controller-to-drive mapping, drive targets,
  and stop behavior.
- Pico core 0 currently owns Wi-Fi, HTTP/WebSocket transport, and logging drain
  in the active Pico-network firmware path.
- In the target clean-start C++ path, Pico core 0 should own UART transport,
  logging drain, diagnostics, and bounded handoff to the control domain without
  requiring CYW43/Wi-Fi startup.
- ESP32 may own robot wireless gateway duties, controller connectivity,
  normalization, diagnostics, telemetry transport, and bounded command
  transport, but it must not own motor control, safety control, or
  timing-sensitive logic.
- Android acts as operator input only.

## Key data paths
- Control: `Android -> Pico WebSocket/HTTP -> Pico motor control`
- Target control: `Android -> ESP32 WebSocket -> Pico UART -> Pico motor control`
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
