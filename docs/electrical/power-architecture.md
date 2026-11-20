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
- Source file: [robot-battery-system.txt](../assets/electrical/robot-battery-system.txt)
- Source file: [wiring-reference.txt](../assets/electrical/wiring-reference.txt)
- Manual/source file: [candidate JGCFR18650 cell specification](../assets/components/power/lifepo4-battery-pack/vendor/candidate-jgcfr18650-cell-specification-r1.1.pdf)
