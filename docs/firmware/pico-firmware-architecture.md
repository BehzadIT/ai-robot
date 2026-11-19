# Pico Firmware Architecture

## Purpose
Describe the Pico firmware's role in the overall robot system.

Detailed Pico module layout and runtime implementation notes live in
`../../robot-pico-platform/docs/firmware-architecture.md`.

## System Role
- Pico is the robot's real-time control authority.
- Pico owns motor control, encoder interpretation, safety stop behavior,
  drivetrain timing, and command freshness handling.
- Pico currently also hosts the live command server used by the Android app.
- Pico emits logs and telemetry that the ESP32 can bridge for bench visibility.

## Boundary With Other Subsystems
- Android sends operator intent and owns app transport lifecycle.
- ESP32 bridges telemetry and must not own drivetrain safety or motor output.
- Parent protocol docs define shared command and telemetry semantics.

## Related Docs
- Parent architecture: `../overview/system-architecture.md`
- Parent command protocol: `../interfaces/command-protocol.md`
- Parent telemetry protocol: `../interfaces/telemetry-protocol.md`
- Pico implementation: `../../robot-pico-platform/docs/firmware-architecture.md`
