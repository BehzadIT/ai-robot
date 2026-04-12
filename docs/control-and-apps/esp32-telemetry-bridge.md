# ESP32 Telemetry Bridge

## Purpose
Describe the ESP32 subsystem's role in the overall robot system.

Detailed ESP32 bridge implementation notes live in
`../../robot-esp32-platform/docs/telemetry-bridge.md`.

## System Role
- ESP32 currently acts as a telemetry bridge plus controller-input transport adapter.
- Pico emits logs and telemetry over UART.
- ESP32 receives UART lines and exposes them to clients over WebSocket.
- ESP32 may own platform support for Wi-Fi, diagnostics, telemetry transport,
  Bluetooth controller connectivity, and dedicated controller UART transport,
  but it does not own robot motion control.

## Boundary
- No motor control.
- No command arbitration.
- No safety-loop authority.
- No timing-sensitive drivetrain behavior.

Any future ESP32 capability must preserve this boundary unless the parent
architecture docs are intentionally updated.

## Related Docs
- Parent architecture: `../overview/current-architecture.md`
- Parent telemetry protocol: `../interfaces/telemetry-protocol.md`
- ESP32 implementation: `../../robot-esp32-platform/docs/telemetry-bridge.md`
