---
component_id: component-raspberry-pi-pico-2w-01
documentation_status: curated
reviewed_on: "2026-11-20"
reviewed_sources:
  - id: source-pico-2w-datasheet
    sha256: 8f519b945e9f7078ffd3fee464992fca376d8037ebcd1f83bd2a021241717eb2
  - id: source-pico-2w-pinout
    sha256: 42d3092e901ef10846ae5eea5f4b3f73e1b577985ad6baa1b145d05559cc9f89
  - id: source-pico-2w-schematic
    sha256: f6791f8a818bc73b6963bd4cdb66afaa3e2479db9edd9ef76bb4aaaacc9bf7d1
  - id: source-rp2350-datasheet
    sha256: a638d6780da919162660691bfa02c6dcf7c2a0b6e9f18e2d7519c80b664a2e39
  - id: source-rp2350-hardware-design
    sha256: cef88bc7d87e67b4262ee15f2b94b03566667143f4e8daf6931828bef6408059
coverage:
  identity_and_applicability: covered
  safety_and_limits: covered
  power_and_electrical: covered
  interfaces_and_timing: covered
  configuration_and_calibration: covered
  mechanical_and_environmental: covered
  diagnostics_and_failure_modes: covered
  replacement_and_compatibility: covered
---
# Raspberry Pi Pico 2 W

This pack covers the documented Raspberry Pi **Pico 2 W board** and its RP2350
chip-level supporting material. The installed board identity is still only
owner-reported; source review does not verify the board, its mounting, its
harness, or its condition. The RP2350 sources apply to the chip or to custom
bare-chip designs and cannot override Pico 2 W board-level behavior. The
hardware-design guide specifically presents separate RP2350A/RP2350B Minimal
reference boards, not the Pico 2 W
[source-rp2350-hardware-design, PDF p. 4, §1](vendor/rp2350-hardware-design-release-3.pdf#page=4).

In this robot, the Pico owns final command admission, freshness, encoders,
drivetrain output, and real-time safety. ESP32 and Android may deliver intent
but do not replace that authority.

## Decision Summary

- Treat every exposed robot signal as **3.3 V logic** unless a separately
  qualified interface says otherwise. The board's GPIO rail is fixed at 3.3 V;
  GPIO26–29 have an internal reverse diode and input must not exceed IOVDD by
  about 300 mV. Applying voltage to those pins while the RP2350 is unpowered can
  back-power IOVDD. GPIO0–25 and the debug pins may have up to 3.3 V applied
  while the chip is unpowered
  [source-pico-2w-datasheet, PDF p. 14, §3.2](vendor/pico-2-w-datasheet-release-2.pdf#page=14).
- Power the board through an identified path. `VBUS` is the nominal 5 V USB
  input; `VSYS` has an allowed 1.8–5.5 V range. The generated `3V3` rail may
  power external circuits, but Raspberry Pi recommends keeping that external
  load under 300 mA, with the actual capability dependent on VSYS and RP2350
  load
  [source-pico-2w-datasheet, PDF p. 9, §2.1](vendor/pico-2-w-datasheet-release-2.pdf#page=9).
- Do not change encoder or motor-driver pins from a diagram alone. The official
  pinout identifies board header positions and alternate functions, but it does
  not establish the robot's harness
  [source-pico-2w-pinout, PDF p. 1, pinout diagram](vendor/pico-2-w-pinout-rev-1.pdf#page=1).
- Preserve the antenna keep-out. The surface-mount recommendation uses a
  14 mm x 9 mm antenna cutout, places the antenna at the carrier-board edge,
  and warns against nearby material or a metal enclosure
  [source-pico-2w-datasheet, PDF p. 11, §2.2.1](vendor/pico-2-w-datasheet-release-2.pdf#page=11).

## Safety and Limits

The board's recommended conditions are `VSYS` 1.8–5.5 V, `VBUS` 5 V ±10%,
and -20 °C to 70 °C operation including self-heating
[source-pico-2w-datasheet, PDF p. 12, §2.3](vendor/pico-2-w-datasheet-release-2.pdf#page=12)
[source-pico-2w-datasheet, PDF p. 13, §2.3](vendor/pico-2-w-datasheet-release-2.pdf#page=13).
These are board recommendations, not measured robot conditions.

The RP2350's chip-level absolute maxima are stress ratings, not operating
targets. They include -0.5 V to 3.63 V for IOVDD and -0.5 V to `IOVDD + 0.5 V`
for a standard I/O, while fault-tolerant I/O has separate conditional ratings
[source-rp2350-datasheet, PDF p. 1336, §14.9.1](vendor/rp2350-datasheet-release-3.pdf#page=1336).
Do not infer that a Pico header pin is 5 V tolerant from the chip table: the
board documentation and project safety rule remain the integration authority.

`3V3_EN` is pulled to VSYS through 100 kΩ and disables the 3.3 V rail when
shorted low; `RUN` resets the RP2350 when shorted low. Do not drive these pins
until the attached circuit and common reference are known
[source-pico-2w-datasheet, PDF p. 9, §2.1](vendor/pico-2-w-datasheet-release-2.pdf#page=9).

## Power, Interfaces, and Configuration

The board schematic is the authority for board nets: it shows USB `VBUS`
feeding `VSYS` through the board power path, the generated `3V3` rail, the
40-pin header, BOOTSEL, debug connector, flash, ADC filtering, and the RP2350
connections. It does not document the robot-side wiring
[source-pico-2w-schematic, PDF p. 1, sheet 1](vendor/pico-2-w-schematic-rev-1.pdf#page=1).

For board recovery, power down, hold BOOTSEL during power-up, and use the USB
mass-storage programming mode; the ROM boot code cannot be overwritten. SWD is
the alternate programming/debug path
[source-pico-2w-datasheet, PDF p. 14, §3.1](vendor/pico-2-w-datasheet-release-2.pdf#page=14).
This is a vendor recovery capability, not evidence that the installed USB or
SWD path works.

The canonical project wiring remains
[wiring-and-pinout.md](../../../../electrical/wiring-and-pinout.md). It currently
conflicts with active firmware constants for parts of the left encoder and
motor-driver control harness. The official pinout is suitable for locating a
named board pin after the signal assignment is known; it cannot resolve that
conflict.

## Mechanical and Environmental

The bare board is documented as 51 mm x 21 mm x 1 mm, with 2.54 mm header
pitch and four 2.1 mm (±0.05 mm) mounting holes
[source-pico-2w-datasheet, PDF p. 7, §2](vendor/pico-2-w-datasheet-release-2.pdf#page=7).
Those dimensions support fit checks only. The installed fasteners, clearances,
strain relief, antenna clearance, and enclosure effects remain unverified.

## Diagnostics and Failure Modes

- A BOOTSEL or SWD recovery attempt can distinguish a recoverable firmware
  image from some runtime failures, but cannot by itself qualify power integrity
  or the robot harness.
- Wrong encoder or motor-control mapping can invalidate feedback or produce an
  unsafe output. Do not energize the drivetrain to infer the mapping.
- Voltage on GPIO26–29 while the board is unpowered can back-power the IOVDD
  rail; isolate external signals before unpowered continuity work.
- The Pico 2 W wireless subsystem is not part of the target reliable
  motor-control dependency path; a wireless failure must not transfer safety
  authority away from the Pico.

## Replacement and Compatibility

Use the exact Pico 2 W board documentation for a replacement decision. An
RP2350 chip, an RP2350 Minimal board, Pico 2 without wireless, or an older Pico
is not established here as a drop-in replacement. Before substitution, compare
the exact board model, header mapping, power path, antenna clearance, firmware
target, and robot harness.

## Open Questions

- [`Q-US002-003`](../../../../verification/questions/US-002.yaml): identify by
  power-isolated continuity which Pico pins reach left encoder A and B.
- [`Q-US002-016`](../../../../verification/questions/US-002.yaml): identify by
  power-isolated continuity each Pico-to-Cytron PWM/direction signal and track
  channel.

Neither question can be closed from a datasheet, schematic, or pinout image.

## Sources and Coverage

All registered sources were reviewed at the hashes recorded above. The Pico 2 W
datasheet, pinout, and schematic provide board-level coverage. The RP2350
datasheet supplies supporting silicon limits, and the RP2350 hardware-design
guide was reviewed only to establish its custom-board scope. Open the original
pages for complete pin multiplexing, schematic detail, dimensional drawings,
or limits not summarized here. Coverage is `curated` for the registered source
set; installed identity, wiring, condition, and behavior remain physical
evidence questions.
