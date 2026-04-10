# Command Protocol

## Purpose
Document the current control commands that future tooling must respect.

## Current status
- `Implemented`: Pico accepts WebSocket and HTTP drive/stop commands.
- `Implemented`: Android sends JSON WebSocket drive and stop commands.
- `Implemented`: WebSocket drive and stop commands use a compact JSON schema on the active control path.
- `Implemented`: drive commands include freshness metadata for recoverability.
- `Implemented`: malformed or invalid WebSocket commands return protocol errors without breaking the WebSocket session.

## Current drive command
WebSocket JSON object containing:
- `k = "d"`
- `t = signed throttle percent`
- `r = signed turn percent`
- `q = sequence`
- `w = sent-at ms`

HTTP JSON object remains legacy:
- `type = "drive"`
- `target_rpm`
- `target_direction`
- `target_angle`

## Current stop command
WebSocket JSON object containing:
- `k = "s"`
- `q`
- `w`

## Current recover command
WebSocket JSON object containing:
- `k = "r"`
- `q`
- `w`

## Server responses
- Ack: `k = "a"`, `c`, `q`
- Error: `k = "e"`, `c`, `q`, `m`

HTTP JSON object remains legacy:
- `type = "stop"`

## Endpoints
- WebSocket: `/ws`
- HTTP PUT: `/drive`
- HTTP PUT: `/stop`

## Notes
- The active WebSocket protocol is now operator-intent based, not RPM / direction / angle based.
- HTTP remains a legacy debug / compatibility path and is not the primary operator protocol.
- Pico-side timeout enforcement is authoritative for stale or disconnected control.
- Protocol errors such as `invalid_json`, `bad_drive_command`, and `unknown_command` are recoverable session-level events, not transport failures.
- WebSocket control is compact-schema only.
- The earlier WebSocket `r/d/a` payload shape is retired.

## Related Docs
- Current architecture: `../overview/current-architecture.md`
- Operator model: `../control-and-apps/operator-control-model.md`
- Android implementation: `../../robot-android-app/docs/operator-control-ui.md`
- Pico implementation: `../../robot-pico-platform/docs/firmware-architecture.md`
