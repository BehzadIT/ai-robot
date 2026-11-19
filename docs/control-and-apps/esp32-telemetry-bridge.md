# ESP32 Wireless Gateway

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
- In the target clean-start architecture, ESP32 becomes the robot wireless
  gateway for logs, structured stats, diagnostics, and optionally Android
  command transport.
- If ESP32 receives Android operator commands, it forwards bounded intent DTOs
  to the Pico and does not make safety or actuator decisions.

## Boundary
- No motor control.
- No command-source arbitration or motion permission decisions.
- No safety-loop authority.
- No timing-sensitive drivetrain behavior.
- Logs and stats are best-effort. Command freshness and controller heartbeat
  traffic must not be blocked by log broadcast backpressure.

Any future ESP32 capability must preserve this boundary unless the parent
architecture docs are intentionally updated.

## Related Docs
- Parent architecture: `../overview/system-architecture.md`
- Parent telemetry protocol: `../interfaces/telemetry-protocol.md`
- ESP32 implementation: `../../robot-esp32-platform/docs/telemetry-bridge.md`
