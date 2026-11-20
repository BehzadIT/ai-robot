# Wiring And Pinout

## Purpose
Provide the canonical wiring reference to support bench work and future firmware changes.

## Current status
- `Project note`: this file reflects the intended or documented wiring.
- `Needs verification`: second encoder pins conflict with one live code path.
- `Needs verification`: PWM/DIR roles in this note conflict with both current
  MicroPython and C++ drivetrain constants.

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

## Controller UART
- ESP32 `GPIO25 TX` -> Pico `GP5 RX`
- Pico `GP4 TX` -> ESP32 `GPIO26 RX`
- Common GND

## Verification note
The current PIO encoder implementation in code uses `GP10/11` for the right encoder and `GP20/21` for the left encoder. Bench verification is required before changing firmware around this area.

Current Pico implementations map right PWM/DIR to `GP7/GP6` and left PWM/DIR
to `GP9/GP8`, while this note assigns PWM/DIR as `GP8/GP9` and `GP6/GP7`.
Resolve `Q-US002-016` with power-isolated continuity to named Cytron inputs.
Do not choose one source as correct or energize motors merely to infer the map.

The open question registry is
[`US-002.yaml`](../verification/questions/US-002.yaml). Activate a question only
when a wiring or control story depends on it; retained evidence then populates
the relevant revision under `as-built/`.

## Sources
- Source file: [wiring-reference.txt](../assets/electrical/wiring-reference.txt)
