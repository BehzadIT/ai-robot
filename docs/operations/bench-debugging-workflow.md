# Bench Debugging Workflow

## Purpose
Define the preferred debugging workflow for this robot.

## Current status
- `Implemented`: live log relay path exists.
- `Design decision`: non-halting debugging is preferred for motor-control work.

## Workflow
- Use normal USB REPL and IDE tools for Pico interaction when needed.
- Use UART mirrored logs through the ESP32 bridge for runtime observation during live movement.
- Prefer live telemetry and logging over breakpoint debugging when motors or encoders are involved.
- Keep logging changes compatible with REPL tooling.

## Notes
Any logging change that breaks REPL tooling or IDE memory probes is a regression.
In particular, do not put the normal Pico USB REPL/stdout path behind a shared
logger lock; only the custom UART logging path should be serialized.

## Related Docs
- Logging and telemetry: `../firmware/logging-and-telemetry.md`
- ESP32 telemetry bridge: `../control-and-apps/esp32-telemetry-bridge.md`
- Pico logging implementation: `../../robot-pico-platform/docs/logging-and-telemetry.md`
