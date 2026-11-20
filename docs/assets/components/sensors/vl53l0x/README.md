---
component_id: component-vl53l0x-sensors-01
documentation_status: curated
reviewed_on: "2026-11-20"
reviewed_sources:
  - id: source-vl53l0x-datasheet
    sha256: c8789c79235e9544bc355313f8ae51f96042026e8a7dbec3118c316def96f668
  - id: source-vl53l0x-api-manual
    sha256: b0eb07701b90ac2a7251e2988fe446131ac11e5cd2abed502e11a7637c90adce
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
# VL53L0X Sensor Module

The available product is an unidentified carrier board containing a candidate
VL53L0X sensor. The retained ST datasheet and API manual describe the **bare
sensor**, not the carrier regulator, level shifting, header pinout, mounting,
or optical cover. Do not apply bare-sensor voltage or pin numbers at the carrier
header until `Q-US002-020` identifies the board.

## Decision Summary

- Bare-sensor recommended AVDD is 2.6–3.5 V (2.8 V typical), with a -20 to
  70 °C operating range. The -0.5 to 3.6 V table is an absolute stress rating,
  not an operating range.
  [source-vl53l0x-datasheet, PDF p. 20, §§5.1–5.2](vendor/st-vl53l0x-datasheet-rev-6.pdf#page=20)
- The default API uses 1.8 V I/O mode; 2.8 V mode is programmable. This is a
  bare-device fact and cannot establish whether the carrier accepts 3.3 V or
  5 V supply/logic.
  [source-vl53l0x-datasheet, PDF p. 20, Table 8 notes](vendor/st-vl53l0x-datasheet-rev-6.pdf#page=20)
- The bare sensor uses I²C at up to 400 kbit/s and an address byte of `0x52`
  (`0x53` for read in the datasheet's 8-bit convention). The API can change the
  device address. Multiple devices therefore require controlled startup/address
  assignment, subject to the carrier exposing usable XSHUT pins.
  [source-vl53l0x-datasheet, PDF p. 16, §4](vendor/st-vl53l0x-datasheet-rev-6.pdf#page=16)
  [source-vl53l0x-api-manual, PDF p. 20, §6.6](vendor/st-vl53l0x-api-user-manual-rev-1.pdf#page=20)
- Bare-module range depends strongly on reflectance, ambient infrared, profile,
  calibration, full-target coverage, and cover glass. At 33 ms, no cover glass,
  2.8 V, 23 °C, and full 25° field of view, the table gives very different
  indoor/outdoor and white/gray target ranges; do not reduce it to a single
  project range.
  [source-vl53l0x-datasheet, PDF p. 24, §6.2](vendor/st-vl53l0x-datasheet-rev-6.pdf#page=24)

## Power and Interfaces

The bare LGA device's XSHUT is active low, GPIO1 is an open-drain interrupt,
and DNC must float. These package pins are not the carrier-header pinout.
[source-vl53l0x-datasheet, PDF p. 5, §2.3](vendor/st-vl53l0x-datasheet-rev-6.pdf#page=5)

For the bare-device reference circuit, ST calls for local 100 nF and 4.7 µF
decoupling, one set of I²C pull-ups per bus, a driven or pulled-up XSHUT, and a
10 kΩ recommended pull-up for XSHUT and GPIO1. A carrier may already contain
some or all of these parts.
[source-vl53l0x-datasheet, PDF p. 6, §2.4](vendor/st-vl53l0x-datasheet-rev-6.pdf#page=6)

Typical bare-device active-ranging current is 19 mA using the default 33 ms
settings; peak current can reach 40 mA. The same table gives 3–7 µA hardware
standby and 4–9 µA software standby in 2.8 V I/O mode under its stated nominal
conditions. Carrier quiescent current is additional and unknown.
[source-vl53l0x-datasheet, PDF p. 21, §5.4](vendor/st-vl53l0x-datasheet-rev-6.pdf#page=21)

XSHUT must be raised only after AVDD is present; maximum firmware boot time is
1.2 ms. The carrier may constrain how this sequence can be controlled.
[source-vl53l0x-datasheet, PDF p. 14, §3.9](vendor/st-vl53l0x-datasheet-rev-6.pdf#page=14)

## Configuration and Calibration

ST specifies an initial customer calibration flow that accounts for cover
glass, temperature, and voltage. A cover window can require renewed reference
SPAD, offset, and crosstalk calibration; offset calibration uses a white 88%
target at 100 mm in a dark environment in the documented procedure.
[source-vl53l0x-api-manual, PDF p. 5, §2 (continues through p. 7)](vendor/st-vl53l0x-api-user-manual-rev-1.pdf#page=5)

The host must retain calibration results and reload offset and crosstalk data at
startup. Do not assume an unknown carrier or library has suitable calibration
for the robot's cover and mounting.
[source-vl53l0x-api-manual, PDF p. 13, §4.3](vendor/st-vl53l0x-api-user-manual-rev-1.pdf#page=13)

The API timing budget defaults to 33 ms and has a documented 20 ms minimum;
increasing it improves precision, while relaxing limit checks can extend range
at the cost of more deviation and outliers.
[source-vl53l0x-api-manual, PDF p. 17, §§6.1–6.2](vendor/st-vl53l0x-api-user-manual-rev-1.pdf#page=17)

## Mechanical, Diagnostics, and Replacement

The bare optical LGA12 package is 4.4 × 2.4 × 1 mm and uses a 940 nm emitter.
Those dimensions do not describe the carrier, mounting holes, connector, or
required optical clearance.
[source-vl53l0x-datasheet, PDF p. 4, §2.1](vendor/st-vl53l0x-datasheet-rev-6.pdf#page=4)

Weak/no target can produce an invalid measurement rather than a distance.
Software should preserve range status, API status, timeout, and I²C errors;
the API table identifies `-20` as an I²C communication error and `-50` as a
reference-SPAD initialization failure with several possible causes.
[source-vl53l0x-api-manual, PDF p. 20, Table 4](vendor/st-vl53l0x-api-user-manual-rev-1.pdf#page=20)

Replacement requires the same sensor generation plus verified carrier supply,
logic translation, XSHUT/GPIO exposure, pull-ups, regulator, pinout, dimensions,
optical window, and software/API compatibility. Similar-looking VL53L0X boards
are not automatically interchangeable.

## Open Questions

- `Q-US002-020`: identify the carrier manufacturer, board markings, purchase
  link, header labels, regulator/level shifting, and optical cover.
- Installation, wiring, functional state, and calibration remain unverified;
  source review does not resolve them.

Use the [component registry](../../../../reference/component-registry.yaml) for
physical state and claim provenance.

## Sources and Coverage

- Reviewed the complete DS11555 Rev 6 datasheet and UM2039 DocID029105 Rev 1
  (June 2016) API manual at their recorded hashes.
- Open the originals for complete electrical timing, ranging profiles, error
  tables, calibration procedures, package drawings, and reflow/storage data.
- Source coverage is complete. Carrier-level applicability remains unresolved.
