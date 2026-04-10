# Motor Control And Encoders

## Purpose
Summarize the system-level motor and encoder responsibilities.

Detailed Pico motor-control and encoder implementation notes live in
`../../robot-pico-platform/docs/motor-control-and-encoders.md`.

## System-Level Ownership
- Pico owns drivetrain control and encoder interpretation.
- Android sends throttle and turn intent, not motor RPM or PWM authority.
- ESP32 must not own motor control or safety decisions.

## Current Integration Facts
- The robot uses a dual-track drivetrain with two motor outputs.
- Encoder polarity, exact as-built pinout, and supply assumptions must remain
  visible in parent electrical and verification docs.
- Control behavior should fail safe when encoder data or motor output state is
  untrustworthy.

## Related Docs
- Parent wiring: `../electrical/wiring-and-pinout.md`
- Parent hardware interfaces: `../interfaces/hardware-interfaces.md`
- Parent known issues: `../verification/known-issues-and-open-questions.md`
- Pico implementation: `../../robot-pico-platform/docs/motor-control-and-encoders.md`
