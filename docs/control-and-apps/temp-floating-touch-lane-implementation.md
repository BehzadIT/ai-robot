# Floating Touch Lane Implementation Note

## Purpose
Preserve the parent-level pointer to the Android touch-lane implementation
research and rollout plan.

The detailed implementation note belongs to the Android app repository because
it is about Compose gesture handling, Android haptics, UI state, and local app
file structure.

## System-Level Decision
The robot operator UI should move toward a landscape, two-thumb, axis-locked
control surface:
- left lane: signed throttle intent
- right lane: signed turn intent
- release returns the affected lane to neutral
- all motion commands remain operator intent, not motor authority

The Pico remains responsible for translating intent into safe drivetrain
behavior. ESP32 may transport operator intent in the target clean-start
architecture, but it is not control-authoritative.

## Implementation Owner
Android implementation details live in:
- `../../robot-android-app/docs/floating-touch-lanes.md`

Parent-level behavior and protocol expectations live in:
- `android-control-app.md`
- `operator-control-model.md`
- `../interfaces/command-protocol.md`
