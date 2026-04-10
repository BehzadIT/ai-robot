# Verification Checklist

## Purpose
Track which core claims about the robot are verified and which still require confirmation.

## Checklist
- Confirm actual installed BMS model.
- Confirm actual left encoder pins on the current build.
- Confirm actual encoder supply voltage in the live robot.
- Confirm current battery charger LiFePO4 termination behavior.
- Confirm current WebSocket command path used during normal operation.
- Confirm stop behavior on command release, disconnect, and stale command conditions.
- Confirm current drivetrain hardware matches Pololu 37D and Cytron assumptions.

## Evidence sources
Use bench photos, continuity checks, running firmware behavior, and vendor manuals.

## Sources
- Source file: [wiring reference.txt](../../robot-pico-platform/docs/wiring%20reference.txt)
- Manual/source file: [Smart Active Balance BMS manual.pdf](../../robot-pico-platform/docs/Smart%20Active%20Balance%20BMS%20manual.pdf)
