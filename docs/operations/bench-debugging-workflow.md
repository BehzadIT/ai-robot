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

## Sources
- Code: [logger.py](../../robot-pico-platform/src/support/logger.py)
- Code: [telemetry_bridge.c](../../robot-esp32-platform/components/telemetry_bridge/telemetry_bridge.c)
