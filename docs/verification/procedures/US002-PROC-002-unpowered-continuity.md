# US002-PROC-002: Power-Isolated Harness Continuity Mapping

Version: 1

## Goal

Map Pico-to-encoder, Pico-to-Cytron, and Pico-to-ESP32 conductors without
energizing the robot.

## Why this is needed

Current code and wiring notes conflict. Firmware changes based on the wrong map
can corrupt feedback or motor output.

## Tools and protective equipment

- Qualified continuity meter and sound probes/clips.
- Eye protection.
- Connector/pin diagrams for the exact identified hardware.

## Safe setup

Battery and charger physically isolated, bench supply and USB disconnected,
stored energy discharged according to identified hardware instructions, and
the absence of voltage confirmed before selecting continuity mode. Do not probe
through an energized or unidentified module.

## Procedure

1. Record the meter ID, condition, leads, and zero/lead resistance behavior.
2. Name both endpoints before each measurement; never record only a wire color.
3. Map right and left encoder A, B, VCC, and GND to Pico pins.
4. Map each Cytron PWM and direction input to Pico pins and record the physical
   motor channel/track association.
5. Map debug and controller UART TX/RX and common grounds.
6. Record unexpected cross-connections separately; do not reinterpret them.

## Expected result and tolerance

The procedure must define the meter's continuity threshold from its exact
manual. Each expected conductor is continuous within that threshold and is not
shorted to adjacent power or ground nets. No generic resistance threshold is
invented here.

## Failure indications

Residual voltage, unstable readings, multiple unexpected endpoints, damaged
connectors, inaccessible labels, or a mapping inconsistent with safe voltage
domains.

## Stop conditions

Stop on any observed voltage, inability to isolate all supplies, evidence of a
short, or uncertainty about a battery/BMS connection.

## How the result changes the decision

Qualified continuity may resolve `Q-US002-003` and `Q-US002-016` and populate
the first as-built harness revision. It does not prove signal voltage,
direction convention, or powered function.

## Evidence to retain

Endpoint table, annotated connector photos, meter identity, isolation checks,
raw notes, discrepancies, and file hashes.
