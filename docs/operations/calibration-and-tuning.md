# Calibration And Tuning

## Purpose
Capture the tuning areas that matter when the robot is adjusted in the future.

## Current status
- `Implemented`: PID gains and PWM thresholds exist in current firmware.
- `Needs verification`: tuned values versus current as-built robot mass, traction, and battery state.

## Current tuning surfaces
- PID gains for left and right tracks
- minimum PWM threshold
- PWM frequency
- RPM normalization assumptions
- steering mapping from angle to left/right track setpoints

## Mechanical interactions
Tuning is not purely firmware-side. Track tension, shaft adapter alignment, motor mounting geometry, and battery state all influence drive behavior.

## Sources
- Source file: [faulty shaft and solution.txt](../../robot-pico-platform/docs/faulty%20shaft%20and%20solution.txt)
