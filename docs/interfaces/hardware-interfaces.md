# Hardware Interfaces

## Purpose
Summarize the physical and electrical interfaces between the robot subsystems.

## Current status
- `Implemented / documented`: Cytron PWM/DIR, encoder quadrature inputs, Pico-to-ESP32 UART.
- `Available inventory`: several sensor interfaces exist in the project inventory but are not fully integrated into current control code.

## Current core interfaces
- Pico <-> Cytron MDD10A: PWM + DIR signals, shared ground
- Pico <-> encoders: quadrature A/B inputs
- Pico <-> ESP32: UART debug/telemetry link
- Driver <-> battery pack: motor power path

## Available but not central today
- HC-SR04
- VL53L0X
- DYP-A02-V2.0

## Sources
- Source file: [wiring-reference.txt](../assets/electrical/wiring-reference.txt)
- Manual/source file: [robot-project-complete-component-list.txt](../assets/reference/robot-project-complete-component-list.txt)
