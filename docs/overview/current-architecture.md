# Current Architecture

## Purpose
Describe the current implemented architecture across the Pico, ESP32, Android app, motor driver, encoders, and power system.

## Current status
- `Implemented`: Pico runs the live control server and motor-control loop.
- `Implemented`: ESP32 runs a UART-to-WebSocket telemetry bridge.
- `Implemented`: Android app connects to the Pico WebSocket endpoint for control.
- `Implemented`: Pico enforces stale-command stop behavior for disconnected or silent control sessions.
- `Needs verification`: long-term target command routing if the architecture is later changed.
- `Project note`: the ESP32 firmware project is named `robot-esp32-platform`, but telemetry bridging remains the only implemented ESP32 runtime capability.

## Architecture
### Control plane
- Android app sends signed throttle / turn drive intent plus stop / recover commands to the Pico over WebSocket.
- Pico receives commands, updates navigation targets, and runs PID-based motor control.
- Pico treats transport disconnect or stale command freshness as a safety event and stops until a fresh command arrives.
- Pico also exposes legacy HTTP `/drive` and `/stop` endpoints.

### Telemetry plane
- Pico mirrors `print()` output and UART-only structured logs to UART0 on `GP0/GP1`.
- ESP32 receives those UART lines on `GPIO16/17`.
- ESP32 broadcasts received lines to WebSocket clients on `/ws`.

### Hardware ownership split
- Pico owns motors, encoders, navigation targets, and stop behavior.
- ESP32 must not own motor control, safety control, or timing-sensitive logic.
- Android acts as operator input only.

## Key data paths
- Control: `Android -> Pico WebSocket/HTTP -> Pico motor control`
- Telemetry: `Pico UART -> ESP32 -> WebSocket -> PC terminal`

## Sources
- Code: [Pico route registration](../../robot-pico-platform/server/routes/navigation.py)
- Code: [Pico control entrypoint](../../robot-pico-platform/main.py)
- Code: [ESP32 bridge](../../robot-esp32-platform/components/telemetry_bridge/telemetry_bridge.c)
- Code: [Android WebSocket client](../../robot-android-app/app/src/main/java/com/bizi/roboapp/core/transport/NavigationWebSocketApi.kt)
