# Operator Control Model

## Purpose
Capture the intended operator model and distinguish it from the current live implementation.

## Current status
- `Project note`: intended model is stateful on the robot and stateless on the UI.
- `Implemented`: current app sends signed throttle / turn intent over WebSocket plus stop / recover.
- `Implemented`: Pico also maps Xbox controller transport snapshots into the same robot-level throttle / turn intent model.
- `Needs verification / future work`: richer throttle / turn input and stale-command handling are not fully represented in the current code.

## Intended model
- UI sends operator intent, not raw PWM spam.
- Android expresses operator intent as `throttle` and `turn`.
- On the Android side, both are naturally represented as percentages of available control authority.
- `throttle` represents signed drive demand from reverse through neutral to forward.
- `turn` represents signed turning demand from full left through straight to full right.
- Robot continues its last valid state until updated or timed out.
- Timeout or disconnect should lead to a safe stop.

## Ownership boundary
- Android owns the operator-facing abstraction and touch mapping.
- Pico owns the translation from operator intent into controller variables.
- Pico also owns the translation from normalized controller transport snapshots into the same robot-level intent.
- That means Android should send `throttle` / `turn` intent, while Pico may internally convert that into RPM targets, PWM output, direction bits, startup thresholds, or other drivetrain-specific control values.
- The UI and protocol should not leak PID internals or motor-control implementation details unless there is a real operator need.

## Current implementation gap
The current app already speaks operator intent over WebSocket, but the visible control widgets are still temporary slider adapters rather than the intended split touch-lane UI.

## Preferred future vocabulary
- User-facing labels:
  - `Throttle`
  - `Turn`
- Android-side input values:
  - `throttle_percent`
  - `turn_percent`
- Pico-side implementation:
  - may continue to use internal RPM, PWM, angle, or left/right track target variables as needed
  - should treat Android percentages as operator intent, not as direct hardware commands

## Related Docs
- Android system role: `android-control-app.md`
- Command protocol: `../interfaces/command-protocol.md`
- Pico control role: `../firmware/pico-firmware-architecture.md`
