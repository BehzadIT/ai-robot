# Telemetry Protocol

## Purpose
Document the observable telemetry and logging formats used between the Pico, ESP32, and bench tools.

## Current status
- `Implemented`: line-oriented UART log stream.
- `Implemented`: JSON telemetry packets from the Pico logger helper.
- `Planned`: ESP32 wireless gateway exposes logs, structured stats, and
  diagnostics to Android and bench clients without making telemetry part of the
  safety/control path.

## UART line behavior
- Plain `print()` output is mirrored to UART with tick prefixing.
- Structured logs emit line-oriented text with level and tick data.
- ESP32 forwards UART lines as WebSocket text frames.
- ESP32 also emits a small set of bridge-owned text lines prefixed with `[bridge]` for important lifecycle and warning conditions.
- New WebSocket clients currently receive readiness text and readiness JSON before joining the live stream.

## Target clean-start behavior
- ESP32 is the target wireless endpoint for robot logs, stats, and diagnostics.
- Log and stats WebSocket traffic is best-effort and may be dropped or
  throttled under backpressure.
- Command/control freshness must not depend on log delivery.
- The ESP32 may expose separate WebSocket routes for logs, stats, and control,
  but those routes should be served by one HTTP/WebSocket server.
- The current `/ws` telemetry behavior should remain compatible until new
  routes are introduced and bench tools are migrated.

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
