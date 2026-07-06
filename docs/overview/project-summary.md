# Project Summary

## Purpose
This documentation set is the canonical working reference for the DIY tracked robot project spanning mechanics, power, firmware, telemetry, and operator control.

## Current status
- `Implemented`: Raspberry Pi Pico 2 W firmware in MicroPython drives the robot, exposes control endpoints, and emits logs.
- `Implemented`: ESP32 firmware relays Pico UART logs over Wi-Fi via WebSocket.
- `Implemented`: Android app sends drive and stop commands over WebSocket.
- `Planned`: next clean-start C++ architecture moves robot wireless gateway
  duties to the ESP32 and keeps Pico Wi-Fi/CYW43 out of the reliable control
  firmware dependency path.
- `Bench-verified / project note`: current robot uses Pololu 37D motors, Cytron MDD10A, 4S2P LiFePO4 battery pack, and tracked chassis.
- `Needs verification`: exact BMS model, exact encoder supply voltage, and exact live pinout for the second encoder.

## What this file is the source of truth for
- Overall identity and current project scope.
- Which subsystems are active today.
- Which unknowns still block deeper engineering work.

## Project snapshot
The robot is a tracked crawler platform with the Pico as the real-time controller. The Pico owns motors, encoder feedback, drive behavior, command admission, stale-input stop behavior, and safety authority. The current Pico firmware still exposes the live control API, but the target clean-start architecture moves robot wireless endpoints to the ESP32 gateway. The Android app is an operator client, not an autonomy layer.

The ESP32 firmware code now lives in the broader `robot-esp32-platform` repo. That repo identity is intentionally wider than the original telemetry bridge because ESP32 is the target owner for Wi-Fi/WebSocket gateway duties, controller transport, diagnostics, and best-effort logs/stats while preserving Pico control authority.

The project is not purely software. Future work depends on consistent documentation of the mechanical stack, battery system, charger and BMS constraints, wiring, firmware behavior, and the distinction between intended design and current implementation.

## Current primary stack
- Chassis: suspension crawler platform, double-layer aluminum structure.
- Motor stack: 2x Pololu 37D 30:1 metal gearmotors with integrated encoders.
- Motor driver: Cytron MDD10A.
- Main controller: Raspberry Pi Pico 2 W.
- Telemetry bridge: ESP32-DevKitC-class board.
- Operator app: Android Compose app.
- Power: 4S2P LiFePO4 pack with DALY-family BMS.

## Sources
- Manual/source file: [robot-project-components-updated.pdf](../assets/reference/robot-project-components-updated.pdf)
- Manual/source file: [robot-project-complete-component-list.txt](../assets/reference/robot-project-complete-component-list.txt)
