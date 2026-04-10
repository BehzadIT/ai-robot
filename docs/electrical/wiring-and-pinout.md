# Wiring And Pinout

## Purpose
Provide the canonical wiring reference to support bench work and future firmware changes.

## Current status
- `Project note`: this file reflects the intended or documented wiring.
- `Needs verification`: second encoder pins conflict with one live code path.

## Encoder wiring
### Right motor
- A -> `GP10`
- B -> `GP11`
- VCC -> Pico `3.3 V`
- GND -> Pico `GND`

### Left motor
- A -> `GP12`
- B -> `GP13`
- VCC -> Pico `3.3 V`
- GND -> Pico `GND`

## Motor driver control
- M1 PWM -> `GP8`
- M1 DIR -> `GP9`
- M2 PWM -> `GP6`
- M2 DIR -> `GP7`
- Driver GND -> Pico GND

## Debug UART
- Pico `GP0 TX` -> ESP32 `GPIO16 RX`
- Pico `GP1 RX` -> ESP32 `GPIO17 TX`
- Common GND

## Verification note
The current PIO encoder implementation in code uses `GP10/11` for the right encoder and `GP20/21` for the left encoder. Bench verification is required before changing firmware around this area.

## Sources
- Source file: [wiring-reference.txt](../assets/electrical/wiring-reference.txt)
