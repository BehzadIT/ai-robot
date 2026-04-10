# Power Architecture

## Purpose
Describe the robot power tree and electrical ownership boundaries.

## Current status
- `Project note`: motor power is supplied from a 4S LiFePO4 pack into the Cytron driver.
- `Implemented / code-backed`: Pico logic and motor-control pins use 3.3 V logic conventions.
- `Needs verification`: exact regulation path for every peripheral and sensor in the current build.

## Current power tree
- Battery pack: 4S2P LiFePO4.
- Motor power path: battery pack -> Cytron MDD10A VIN/GND -> motors.
- Logic side: Pico and ESP32 use 3.3 V logic signaling.
- Common ground between Pico, driver, and ESP32 is required for proper control and telemetry.

## Notes
- Separate power-domain documentation matters because the control, telemetry, and battery subsystems operate with different electrical constraints.
- Encoder supply voltage must be bench-checked against the exact installed motor variant.

## Sources
- Source file: [Robot battery system.txt](../../robot-pico-platform/docs/Robot%20battery%20system.txt)
- Source file: [wiring reference.txt](../../robot-pico-platform/docs/wiring%20reference.txt)
- Manual/source file: [JGCFR18650-2200mAh-3.2V_18FC-7.04Wh_specification_.pdf](../../robot-pico-platform/docs/JGCFR18650-2200mAh-3.2V_18FC-7.04Wh_specification_.pdf)
