# ESP32 Gateway + Pico Control Clean-Start Plan

## Purpose
Create a parallel clean-start application path that moves robot wireless
gateway duties to the ESP32 while keeping the Pico as the real-time motor,
encoder, command-admission, stale-input, and safety authority.

This plan exists because the Pico 2 W C++ CYW43/FreeRTOS bring-up path has
shown fragile startup behavior. The next control firmware should be able to
boot, enumerate over USB, and run the control loop without requiring Pico
Wi-Fi/CYW43 initialization.

## Architecture target
- Android and Linux clients connect to ESP32 WebSocket endpoints.
- ESP32 owns Wi-Fi, WebSocket routing, logs, stats, diagnostics, BLE controller
  connectivity, and bounded transport to the Pico.
- Pico owns command admission, command freshness, stale-input stop behavior,
  recover semantics, encoder truth, motor output, and all safety decisions.
- Pico does not require Wi-Fi or WebSocket service in the clean-start C++
  control firmware.
- Pico remains a Raspberry Pi Pico 2 W board, but the clean-start firmware
  treats it as a no-network controller: no Bluetooth role, no HTTP server, and
  no WebSocket server on Pico.
- Logs and stats are best-effort; command/control heartbeat traffic is bounded
  and prioritized separately.

## Pico dual-core / RTOS model
- Use pinned FreeRTOS tasks rather than unconstrained SMP scheduling.
- Treat core 0 as the service/transport core.
- Treat core 1 as the deterministic control engine.
- Keep inter-core communication narrow and explicit through bounded mailboxes or
  fixed-size DTO handoff.
- Do not share raw mutable state between service and control tasks.
- Do not hold locks while sleeping, logging, parsing large input, or waiting on
  I/O.
- Protect shared resources such as USB logging, UART peripherals, queues, and
  shared status snapshots with short critical sections only.
- Prefer dropping best-effort logs/status over delaying command freshness or
  the control loop.

## Step 1 (Done): C++ bench loop tooling
Add a clean Pico SDK app and host-side flash/reboot helper before rebuilding
the control stages.

Status:
- `Done`: clean Pico app target, local build/flash helper, `picotool` install
  notes, BOOTSEL/app reboot commands, and `minicom` observation notes exist.
- `Verified`: clean app builds, flashes, emits heartbeat logs, and can be
  inspected through `picotool info -a`.

Implementation requirements:
- Add the clean Pico app in a new directory, separate from the existing migrated
  C++ runtime sources.
- Use the initial target name `robot_pico_control_no_wifi`.
- Keep the initial clean app minimal: USB stdio, picotool USB reset support,
  startup banner, and heartbeat only.
- Do not initialize CYW43, Wi-Fi, Bluetooth, HTTP, WebSocket, UART command
  transport, motors, encoders, or watchdog-controlled motion in this step.
- Add a repo-owned helper for build, UF2 flashing, reboot to BOOTSEL, reboot to
  normal app mode, and serial monitoring.
- Use host `picotool`; do not vendor Raspberry Pi host tools into the repo.

Completed checks:
- The clean app builds and produces `robot_pico_control_no_wifi.uf2`.
- The helper fails clearly when `picotool` is unavailable or lacks USB support.
- `picotool` v2.3.0 is installed locally with USB support.
- `picotool info -a` reports the clean app on RP2350 / Pico 2 W.
- `picotool reboot -f` can request app-mode reboot.
- `picotool reboot -f -u` can request BOOTSEL / UF2 mode.
- `minicom` can observe the clean app startup and heartbeat logs.

## Step 2 (Done): Baseline and naming
Add parallel targets and names without deleting or rewriting the current
firmware paths.

Status:
- `Done`: the current Pico firmware path remains separate from the clean Pico
  no-Wi-Fi app target.
- `Done`: the ESP32 platform keeps its existing build identity while its docs
  describe the target gateway capability.
- `Done`: the clean-start split is visible in build configuration and
  documentation without changing motor behavior.

Implementation requirements:
- Keep the current Pico firmware and current ESP32 bridge buildable.
- Add new clean-start targets beside existing targets where the build system
  naturally supports parallel targets.
- Use names that make the split obvious:
  - Current ESP32 platform app: `robot_esp32_platform`
  - Target ESP32 gateway role: documented as `robot_esp32_gateway` until the
    ESP-IDF project is intentionally renamed or split.
  - Current migrated Pico firmware: `robot_pico_firmware`
  - Pico no-Wi-Fi control app: `robot_pico_control_no_wifi`
- Do not change motor behavior in this step.

Completed checks:
- Existing builds still build.
- New targets are visible in build configuration or documentation.
- No current bench workflow is broken.

## Step 3: ESP32 WebSocket gateway skeleton
Extend the ESP32 bridge toward a gateway while preserving current log viewing.

Implementation requirements:
- Keep current `/ws` telemetry behavior working for existing bench tools.
- Confirm or preserve multiple connected WebSocket clients.
- Prefer one ESP32 HTTP/WebSocket server with multiple routes rather than
  multiple independent servers.
- Introduce planned routes in this order:
  - `/ws/logs` for line-oriented logs
  - `/ws/stats` for structured status
  - `/ws/control` later for Android operator-intent transport
- Keep `/healthz` available.

Success checks:
- Two clients can connect at the same time.
- Logs remain visible.
- `/healthz` reports bridge readiness.
- Disconnecting one client does not break the other client.

## Step 4: Pico no-Wi-Fi C++ heartbeat/control skeleton
Create a Pico C++ target that proves reliable boot without CYW43.

Implementation requirements:
- Do not call `cyw43_arch_init()` or start Pico Wi-Fi.
- Do not add Pico Bluetooth, HTTP, or WebSocket service in this clean-start
  target.
- Bring up USB serial logging.
- Bring up pinned FreeRTOS tasks with a service task on core 0 and a control
  heartbeat/control task on core 1.
- Print a deterministic heartbeat over USB.
- Do not enable live motor output in this step.

Success checks:
- UF2 flashes normally.
- Pico enumerates as `/dev/ttyACM*` after reboot.
- `minicom` shows heartbeat logs.
- Repeated reboot/flash cycles do not lose USB enumeration.

## Step 5: ESP32-to-Pico UART status/control pipe
Create the first bounded gateway-to-control transport.

Implementation requirements:
- Define a tiny UART frame for gateway heartbeat and operator-intent DTOs.
- Include enough metadata for Pico-side freshness checks.
- Core 0 receives ESP32 UART bytes, parses frames, validates CRC/schema/ranges,
  and publishes fixed-size DTOs into a bounded mailbox.
- Core 1 consumes mailbox DTOs during its control tick but initially only logs
  or adopts neutral state.
- Bad frames must be rejected without disrupting the receive loop.
- UART ingress/parsing must not run inside the core 1 control loop.

Success checks:
- ESP32 sends test heartbeat frames to Pico.
- Pico logs valid receive, invalid receive, and stale/missing input states.
- No motor output is enabled.
- Log flooding does not block UART heartbeat processing or core 1 ticks.

## Step 6: Pico command admission and safety
Connect the UART intent DTO to Pico control ownership.

Implementation requirements:
- Core 1 admits ESP32-routed operator intent into the existing
  command-admission boundary.
- Pico owns stale-command stop behavior.
- Pico owns recover semantics.
- Pico owns final motor permission and actuator output.
- ESP32 never decides whether motion is safe.
- The fixed-period control task owns encoder sampling, drivetrain state, PID,
  watchdog feed, and motor writes.

Success checks:
- Fresh UART intent can update Pico drive targets on a safe bench setup.
- Missing or stale ESP32 input causes Pico-side stop.
- ESP32 reconnect does not resume motion without a fresh operator command.
- Stop behavior is verified before live driving.

## Step 7: Android through ESP32
Move Android wireless connection to the ESP32 gateway.

Implementation requirements:
- Android remains a WebSocket client.
- Android sends the same operator-intent semantics as the current protocol.
- ESP32 forwards only bounded command DTOs to Pico, not UI internals.
- Keep Android reconnect behavior: reconnect must not auto-resume robot motion.

Success checks:
- Android can connect to ESP32 gateway.
- Android can send drive, stop, and recover intent through ESP32 to Pico.
- Pico remains the system that admits, rejects, times out, and executes motion.
- Current direct-Pico path remains available until the new path is bench-proven.

## Step 8: Stats and diagnostics
Add structured robot observability without coupling it to control freshness.

Implementation requirements:
- Add structured `/ws/stats` output for Android and Linux clients.
- Include gateway health and Pico-reported control status when available.
- Keep log and stats delivery best-effort and droppable under backpressure.
- Keep command heartbeat and controller transport independent from log broadcast
  work.

Success checks:
- Android or a Linux client can view stats while logs are active.
- Log flooding does not block command heartbeat.
- Stats continue across client reconnects.
- Gateway health remains visible through `/healthz`.

## Verification rules
- Documentation review: docs must distinguish current Pico WebSocket control
  from the target ESP32 gateway path.
- Ownership review: every step must preserve Pico motor and safety authority.
- ESP32 verification: build, multi-client WebSocket test, `/healthz`, client
  disconnect cleanup.
- Pico verification: UF2 flash, `/dev/ttyACM*` enumeration, `minicom`
  heartbeat logs, no-CYW43 startup.
- Integration verification: ESP32 heartbeat to Pico, Pico valid/stale/missing
  input handling, log backpressure check.
- Robot safety verification: motors disabled or lifted for first motion tests;
  stale-command stop verified before live driving.

## Defaults
- Keep current `/ws` telemetry compatibility until bench tools move to new
  routes.
- Use one ESP32 HTTP/WebSocket server with multiple routes.
- Do not make Pico Wi-Fi/CYW43 part of the clean-start control firmware boot
  path.
- Do not put Bluetooth, HTTP, or WebSocket network responsibilities on Pico in
  the clean-start architecture.
- Treat logs and stats as best-effort.
- Treat command freshness and safety as Pico-owned.
