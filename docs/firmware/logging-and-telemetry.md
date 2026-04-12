# Logging And Telemetry

## Purpose
Describe logging and telemetry as a cross-system behavior.

Detailed Pico logging implementation notes live in
`../../robot-pico-platform/docs/logging-and-telemetry.md`. ESP32 bridge details
live in `../../robot-esp32-platform/docs/telemetry-bridge.md`.

## System-Level Behavior
- Pico produces runtime logs and telemetry.
- ESP32 bridges Pico UART output to WebSocket clients for bench diagnostics.
- Logging must preserve the Pico REPL and avoid blocking safety-critical control
  behavior.
- The Pico's normal USB REPL/stdout path must stay direct. Only the custom UART
  logging path should be serialized; lock-coupling USB stdout to the logger was
  bench-verified to break `mpremote` raw-REPL access.
- Telemetry should help diagnose transport, control, hardware, and safety state
  without moving ownership away from the Pico.

## Related Docs
- Parent telemetry protocol: `../interfaces/telemetry-protocol.md`
- Parent ESP32 role: `../control-and-apps/esp32-telemetry-bridge.md`
- Pico implementation: `../../robot-pico-platform/docs/logging-and-telemetry.md`
- ESP32 implementation: `../../robot-esp32-platform/docs/telemetry-bridge.md`
