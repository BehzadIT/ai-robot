# System Architecture

## Purpose

Provide the canonical system model for the robot. This document separates
deployed behavior from approved target behavior while keeping both in one
component-oriented view.

Implementation detail belongs in the platform repositories. Capability
priorities belong in `capability-roadmap.md`, durable tradeoffs in
`design-decisions.md`, and unresolved facts in
`../verification/known-issues-and-open-questions.md`.

## System Outcome

The robot is a tracked teleoperation and experimentation platform. It combines
an Android operator client, an ESP32 connectivity platform, a Raspberry Pi Pico
2 W real-time controller, a motor/encoder drivetrain, and a battery/power
system.

The central safety boundary is stable across the current and target designs:
Pico admits commands and remains the only subsystem with final motor and safety
authority. Android and ESP32 may communicate operator intent, but neither may
decide actuator output.

## Architecture At A Glance

### Current deployed paths

```text
Android --WebSocket operator intent--> Pico --PWM/DIR--> motor driver --> motors
                                          ^                  |
                                          |                  v
                                      encoders <-------------+

Pico --UART logs--> ESP32 --WebSocket--> bench clients
Xbox controller --Bluetooth--> ESP32 --UART snapshots--> Pico
```

The active Pico firmware also exposes legacy HTTP control endpoints. The
MicroPython runtime and staged C++ paths coexist.

### Approved clean-start target

```text
Android / bench clients --Wi-Fi/WebSocket--> ESP32 --bounded UART DTOs--> Pico
Xbox controller --------Bluetooth----------> ESP32 --bounded UART DTOs--> Pico
Pico --logs/status UART--> ESP32 --best-effort WebSocket--> clients
Pico --admitted targets / PWM / DIR--> drivetrain
```

The target changes where wireless connections terminate. It does not transfer
command admission, freshness, stop/recover behavior, motor output, or safety
authority away from Pico.

## Component Model

### Android operator app

| Field | System contract |
| --- | --- |
| Identity | `robot-android-app`; deployable Android application |
| Purpose | Present robot state and convert operator actions into bounded operator intent |
| Current behavior | Connects directly to the Pico WebSocket endpoint and sends drive, stop, and recover messages |
| Target behavior | Connects to the ESP32 wireless gateway without changing operator-intent semantics |
| Ownership | Operator experience, app state, and client connection lifecycle |
| Non-responsibilities | Motor authority, safety policy, drivetrain mixing, and command admission |
| Interfaces | WebSocket command protocol and operator-facing diagnostics |
| Failure behavior | Connection loss or reconnect must not automatically resume motion; Pico independently stops stale input |
| Maturity | `Implemented` on the direct-to-Pico path; ESP32 routing is `Planned` |
| Evidence | Android platform docs and command-protocol implementation/tests |
| Evolution triggers | Richer diagnostics, additional operator workflows, or a qualified gateway endpoint |

### ESP32 platform

| Field | System contract |
| --- | --- |
| Identity | `robot-esp32-platform`; deployable ESP-IDF firmware |
| Purpose | Isolate wireless, controller, telemetry, and diagnostic concerns from real-time control |
| Current behavior | Bridges Pico UART logs to WebSocket clients and forwards normalized controller snapshots to Pico over a dedicated UART |
| Target behavior | Terminates robot Wi-Fi/WebSocket services and forwards bounded operator-intent DTOs to Pico |
| Ownership | Wi-Fi, WebSocket gateway, Bluetooth controller connectivity, normalization, diagnostics, and bounded transport |
| Non-responsibilities | Final command admission, motor control, safety policy, and timing-critical drivetrain behavior |
| Interfaces | Pico log UART, controller UART, WebSocket routes, Bluetooth controller link, and `/healthz` |
| Failure behavior | Disconnects and malformed traffic remain transport events; log/stat backpressure may drop best-effort data but must not delay control freshness |
| Maturity | Telemetry and controller transport are `Implemented`; the full wireless command gateway is `Planned` |
| Evidence | ESP32 platform docs, firmware builds, bridge behavior, and controller-transport observations |
| Evolution triggers | Qualified Pico UART command handoff, additional diagnostics, or new non-authoritative connectivity roles |

### Pico control platform

| Field | System contract |
| --- | --- |
| Identity | `robot-pico-platform`; Raspberry Pi Pico 2 W firmware and real-time control boundary |
| Purpose | Convert admitted intent and encoder feedback into safe, deterministic drivetrain output |
| Current behavior | Hosts the live control API, admits commands, runs control logic, handles encoders, drives motors, and emits logs |
| Target behavior | Runs as a no-network C++ controller with service/transport work isolated from the deterministic control task |
| Ownership | Command admission, freshness, stop/recover state, watchdog behavior, encoders, PID, motor output, and final safety authority |
| Non-responsibilities | Operator UI, public wireless services, Bluetooth connectivity, and gateway routing in the clean-start target |
| Interfaces | Current WebSocket/HTTP control, target bounded UART DTOs, log/status UART, encoders, and motor-driver PWM/DIR |
| Failure behavior | Missing, stale, malformed, or disconnected input leads to Pico-owned neutral/stop behavior; reconnect alone cannot resume motion |
| Maturity | The MicroPython control path is `Implemented`; the no-network C++ control path is partially implemented and otherwise `Planned` |
| Evidence | Pico platform docs, host tests, builds, serial boot observations, and future safe-bench control evidence |
| Evolution triggers | C++ parity, qualified gateway transport, or an intentionally reviewed change to the control/safety boundary |

### Parent integration workspace

| Field | System contract |
| --- | --- |
| Identity | `ai-robot`; shared documentation and integrated Git snapshot boundary |
| Purpose | Preserve cross-project truth, architecture, protocols, hardware context, verification expectations, and known-good combinations |
| Current behavior | Holds canonical system docs and selected child-repository revisions |
| Target behavior | Adds lightweight backlog traceability and reproducible integrated-state records without absorbing platform implementation |
| Ownership | Shared architecture, interfaces, hardware truth, verification expectations, and integrated snapshots |
| Non-responsibilities | Platform build logic, application state, gateway implementation, or motor control |
| Interfaces | Documentation links, shared protocol contracts, and Git submodule pointers |
| Failure behavior | Conflicts remain explicit and block only dependent decisions; uncertain claims are not silently promoted |
| Maturity | Documentation integration is `Implemented`; richer snapshot and evidence identity is `Planned` under US-002 and US-003 |
| Evidence | Parent Git history, documentation review, and child commit identities |
| Evolution triggers | Cross-project behavior changes, resolved hardware facts, or a qualified integrated release |

### Operator command transport

| Field | System contract |
| --- | --- |
| Identity | End-to-end transport for Android drive, stop, and recover intent |
| Purpose | Deliver fresh operator intent to Pico without transferring admission or safety authority |
| Current behavior | Android sends compact JSON over WebSocket directly to Pico; legacy Pico HTTP endpoints remain available |
| Target behavior | ESP32 terminates WebSocket and forwards validated, bounded transport DTOs over UART to Pico |
| Ownership | Android owns its client lifecycle, ESP32 owns the target gateway session/transport, and Pico owns admission and execution |
| Non-responsibilities | Transport success is not motion permission; ESP32 must not synthesize safe state or resume motion after reconnect |
| Interfaces | Shared command schema, sequence/freshness metadata, WebSocket, and target UART framing |
| Failure behavior | Malformed messages are recoverable protocol events; disconnect, silence, or stale intent produces Pico-owned stop behavior |
| Maturity | Direct Android-to-Pico transport is `Implemented`; ESP32-routed command transport is `Planned` |
| Evidence | Command-protocol docs, Android/Pico tests and runtime observations, and future gateway integration checks |
| Evolution triggers | Qualified gateway UART framing, additional operator clients, or an explicitly reviewed new intent source |

### Telemetry and diagnostics transport

| Field | System contract |
| --- | --- |
| Identity | Pico log/status production, ESP32 forwarding, and Android/bench consumption |
| Purpose | Make runtime and failure behavior observable without coupling observability to control timing |
| Current behavior | Pico emits line-oriented and structured telemetry over UART; ESP32 broadcasts it over `/ws` |
| Target behavior | ESP32 exposes compatible logs plus structured stats and diagnostics through one bounded gateway service |
| Ownership | Pico owns control truth, ESP32 owns gateway/bridge health and delivery, and clients own presentation |
| Non-responsibilities | Telemetry delivery is not a command heartbeat, safety acknowledgement, or prerequisite for stopping |
| Interfaces | UART lines, structured telemetry packets, `/ws`, planned log/stat routes, and `/healthz` |
| Failure behavior | Slow clients, backpressure, and disconnects may drop best-effort data but must not delay command freshness or the control loop |
| Maturity | UART log mirroring and `/ws` broadcast are `Implemented`; richer gateway stats/diagnostics are `Planned` |
| Evidence | Telemetry protocol, Pico/ESP32 platform docs, bridge logs, and future multi-client/backpressure checks |
| Evolution triggers | Structured status requirements, additional consumers, or observed diagnostic blind spots |

### Controller input transport

| Field | System contract |
| --- | --- |
| Identity | Xbox-compatible controller through ESP32/Bluepad32 and dedicated UART to Pico |
| Purpose | Provide a second operator-intent source while preserving one Pico-owned control boundary |
| Current behavior | ESP32 connects to the controller, normalizes snapshots, and sends framed snapshots to Pico; Pico maps them into drivetrain intent |
| Target behavior | Preserve the bounded transport and integrate it with explicit Pico source admission alongside gateway commands |
| Ownership | ESP32 owns connectivity and normalization; Pico owns source admission, freshness, mapping into control state, and motor output |
| Non-responsibilities | Controller connection state on ESP32 does not grant motion authority or replace Pico stale-input handling |
| Interfaces | Bluetooth/Bluepad32, normalized snapshot schema, and dedicated UART framing |
| Failure behavior | Disconnect, missing/stale snapshots, or invalid frames must become Pico-owned neutral/stop behavior without blocking other service work |
| Maturity | Controller connection and UART forwarding are `Implemented`; full clean-start source-admission parity remains `Planned` |
| Evidence | ESP32/Pico implementation docs, firmware behavior, and future stale/disconnect qualification |
| Evolution triggers | Additional controller types, command-source arbitration needs, or gateway/control transport consolidation |

### Drivetrain and encoder capability

| Field | System contract |
| --- | --- |
| Identity | Two Pololu 37D gearmotors, Cytron MDD10A, encoders, tracks, and Pico control software |
| Purpose | Produce and measure left/right track motion |
| Current behavior | Pico generates motor output and consumes quadrature feedback |
| Target behavior | Restore equivalent control, stop, encoder, PID, and watchdog behavior through the clean C++ control boundary |
| Ownership | Pico owns all software decisions affecting drivetrain output; the power and mechanical assemblies remain shared physical system concerns |
| Non-responsibilities | ESP32 and Android must not mix tracks or write actuator output |
| Interfaces | PWM/DIR, encoder quadrature, motor power, mechanical shafts, and track loading |
| Failure behavior | Invalid or stale intent must produce a safe stop; encoder or wiring uncertainty blocks dependent closed-loop qualification |
| Maturity | Current control is `Implemented`; exact left-encoder wiring is `Conflicting`; C++ parity is `Planned` |
| Evidence | Motor/encoder docs, firmware behavior, wiring sources, and future bench measurements |
| Evolution triggers | Verified as-built wiring, drivetrain changes, encoder replacement, or new motion capabilities |

### Power capability

| Field | System contract |
| --- | --- |
| Identity | 4S2P LiFePO4 pack, DALY-family BMS, charger, distribution, and grounding |
| Purpose | Supply protected energy to control electronics and the drivetrain |
| Current behavior | Powers the physical robot; exact BMS identity and some electrical facts remain unresolved |
| Target behavior | Maintain an as-built, measured power model with qualified protection and first-power procedures |
| Ownership | Shared hardware documentation owns system truth; firmware may observe power but must not invent electrical limits |
| Non-responsibilities | Software status is not proof of wiring, protection, chemistry configuration, or safe current capacity |
| Interfaces | Battery, BMS, charger, motor driver, logic rails, grounds, fusing, and disconnects |
| Failure behavior | Conflicting identity or unsafe measurements block dependent power work and require owner participation |
| Maturity | Installed operation is `Owner reported`; exact BMS identity is `Conflicting` and other details are `Documented / unverified` |
| Evidence | Electrical source assets, labels/manuals when confirmed, and future measurements under US-002 |
| Evolution triggers | Verified labels, as-built wiring evidence, protection changes, or additional powered capabilities |

## Cross-Cutting Invariants

- Operator and autonomy layers may propose intent; Pico admits or rejects it.
- Pico command freshness and stop behavior do not depend on Android, ESP32, log
  delivery, or client reconnection.
- Logs and statistics are best-effort and may be dropped under backpressure.
- Transport parsing and other unbounded service work do not run in the
  timing-critical control loop.
- Current behavior, approved target behavior, and exploratory capabilities are
  labeled separately using the shared glossary vocabulary.
- Every future deployable component, sensor, or autonomous capability must use
  the same system-contract fields before its backlog item can become `Ready`.
- Protocol, wiring, safety, or ownership changes update shared documentation in
  the same change.

## Related Docs

- Project summary: `project-summary.md`
- Capability roadmap: `capability-roadmap.md`
- Design decisions: `design-decisions.md`
- Command protocol: `../interfaces/command-protocol.md`
- Telemetry protocol: `../interfaces/telemetry-protocol.md`
- Clean-start implementation sequence:
  `../operations/esp32-gateway-pico-control-clean-start-plan.md`
- Known issues: `../verification/known-issues-and-open-questions.md`
