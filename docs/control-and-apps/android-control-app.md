# Android Control App

## Purpose
Describe the Android app's role in the overall robot system.

Detailed Android UI and implementation notes live in
`../../robot-android-app/docs/operator-control-ui.md` and
`../../robot-android-app/docs/floating-touch-lanes.md`.

## System Role
- Android is the operator client.
- Android owns operator interaction, screen state, connection state, reconnect
  behavior, and transport diagnostics.
- Android currently sends operator intent to the Pico. In the target
  clean-start architecture, Android sends the same operator intent to the ESP32
  wireless gateway, which forwards a bounded DTO to the Pico.
- Android does not own motor control, safety decisions, or drivetrain timing.
- Android must not resume motion automatically after reconnect. A fresh operator
  command is required.

## Current System Behavior
- The app sends signed `throttle_percent` and `turn_percent` intent over the
  command protocol.
- The app can send `stop` and `recover` commands.
- Direction changes across forward/reverse require a stop handoff before motion
  resumes in the opposite direction.
- Loss of active drive input should result in neutral or stop behavior according
  to the current command protocol.

## Boundary With Other Subsystems
- Pico translates operator intent into closed-loop drivetrain behavior and owns
  safety-critical stop behavior.
- ESP32 is not control-authoritative. In the current implementation it is not
  in the Android drive-command path; in the target clean-start architecture it
  may be the wireless transport endpoint for Android commands.
- Parent protocol docs own shared command semantics; Android docs own UI and app
  implementation details.

## Related Docs
- Parent operator model: `operator-control-model.md`
- Parent command protocol: `../interfaces/command-protocol.md`
- Android implementation: `../../robot-android-app/docs/operator-control-ui.md`
- Android touch-lane plan: `../../robot-android-app/docs/floating-touch-lanes.md`
