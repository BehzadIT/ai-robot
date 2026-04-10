# Telemetry Protocol

## Purpose
Document the observable telemetry and logging formats used between the Pico, ESP32, and bench tools.

## Current status
- `Implemented`: line-oriented UART log stream.
- `Implemented`: JSON telemetry packets from the Pico logger helper.

## UART line behavior
- Plain `print()` output is mirrored to UART with tick prefixing.
- Structured logs emit line-oriented text with level and tick data.
- ESP32 forwards UART lines as WebSocket text frames.
- ESP32 also emits a small set of bridge-owned text lines prefixed with `[bridge]` for important lifecycle and warning conditions.
- New WebSocket clients currently receive readiness text and readiness JSON before joining the live stream.

## Structured telemetry packet
Current `telemetry()` output contains:
- `t`
- `tag`
- `data`

## Notes
The telemetry path is optimized for observability during live robot motion without halting execution.

## Related Docs
- Current architecture: `../overview/current-architecture.md`
- Logging and telemetry: `../firmware/logging-and-telemetry.md`
- ESP32 telemetry bridge: `../control-and-apps/esp32-telemetry-bridge.md`
