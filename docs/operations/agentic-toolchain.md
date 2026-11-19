# Agentic Toolchain And Verification CLI

## Purpose

`tools/robot.py` is the parent entry point for US-003 discovery, verification,
and evidence capture. It orchestrates platform-owned adapters; it does not
replace Gradle, ESP-IDF, Pico SDK, or the existing Pico deploy helpers.

## Read-Only Discovery

```bash
python3 tools/robot.py doctor
python3 tools/robot.py doctor --platform pico --json
python3 tools/robot.py inventory --json
```

These commands do not open serial ports, install software, flash or reboot a
board, terminate port holders, or change device configuration. Dynamic
observations never update the canonical hardware registries automatically.

Copy `.robot/local.example.yaml` to the ignored `.robot/local.yaml` only when
stable SDK paths or device identities need local aliases. Do not put
credentials in this file.

## Verification

```bash
python3 tools/robot.py verify android
python3 tools/robot.py verify esp32
python3 tools/robot.py verify pico-host
python3 tools/robot.py verify pico-firmware
```

Defaults are host/build checks. Named device or physical scenarios require a
configured device alias and an interactive confirmation. Safe-bench scenarios
also require the scenario-specific physical checklist.

The parent and child adapters exchange result schema version 1. Outcomes are
`pass`, `fail`, `blocked`, `skipped`, or `inconclusive`; every result states the
highest verification level actually reached. Build success is never promoted
to device or physical qualification.

## Evidence

```bash
python3 tools/robot.py evidence run UART-FRAME-001
python3 tools/robot.py evidence promote RUN-YYYYMMDDTHHMMSSZ-uart-frame-001
```

Runs are first written to ignored `temp/us003/runs/`. Promotion is explicit and
creates a new append-only `docs/verification/evidence/EV-YYYY-NNN/` bundle after
schema and secret-marker checks. Pass, fail, blocked, and inconclusive runs may
all be retained when they are useful evidence.

## Safety Boundary

- Gate 0: read-only discovery and host builds/tests.
- Gate 1: app install, flash, reboot, bootloader transition, or active identity
  probe after exact-device confirmation.
- Gate 2: energized hardware after wiring, protection, and disconnect checks.
- Gate 3: constrained actuator output with restrained tracks and verified stop.
- Gate 4: ground motion after prior qualification and clear-area confirmation.

The CLI records human confirmations as human observations. It never treats
them as instrument measurements. Android and ESP32 remain intent/transport
systems; Pico retains final control and safety authority.
