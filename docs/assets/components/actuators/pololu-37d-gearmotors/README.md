---
component_id: component-pololu-37d-motors-01
documentation_status: curated
reviewed_on: "2026-11-20"
reviewed_sources:
  - id: source-pololu-37d-vendor-datasheet
    sha256: 71172f074ecd6752d59863f04616bcd341d7bdca5588734de31d328a10735ba1
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
# Pololu 37D Gearmotors

Two owner-reported 12 V, 30:1 Pololu 37D gearmotors drive the tracks and are
reported to have quadrature encoders. The retained datasheet covers the whole
37D family, including candidate 12 V 30:1 items, but it does **not** establish
the installed order numbers, encoder variants, or gearbox identity. Do not use
family resemblance to close `Q-US002-005`.

## Decision Summary

- The 12 V 30:1 family row covers items 4742 and 4752. It gives 330 rpm and
  0.2 A at no load; at maximum efficiency it gives 280 rpm, 18 kg·mm,
  0.78 A, and 5.1 W. Its 140 kg·mm and 5.5 A stall values are explicitly
  theoretical extrapolations, not operating targets
  [source-pololu-37d-vendor-datasheet, PDF p. 1, performance summary and notes](vendor/pololu-37d-metal-gearmotors-rev-1.2.pdf#page=1).
- Encoder-equipped family members provide 64 fully decoded counts per motor
  shaft revolution; output-shaft counts are the actual gear ratio multiplied
  by 64. This formula does not prove that the installed motors have the
  reported ratio or encoder
  [source-pololu-37d-vendor-datasheet, PDF p. 3, Using the encoder](vendor/pololu-37d-metal-gearmotors-rev-1.2.pdf#page=3).
- The datasheet distinguishes encoder and non-encoder products and multiple
  voltages and ratios. The August 2019 helical-pinion change is described as
  functionally identical to the earlier spur-pinion version, with lower noise
  and vibration and improved efficiency; it is not an installed-revision
  identifier
  [source-pololu-37d-vendor-datasheet, PDF p. 1, family description and note](vendor/pololu-37d-metal-gearmotors-rev-1.2.pdf#page=1).

## Safety and Limits

- Pololu warns that stalls can damage the motor in seconds. It recommends
  general brushed-DC operation at 25% or less of stall current. The gearbox
  recommendation is at most 100 kg·mm for continuous load and 250 kg·mm for
  instantaneous load; neither number qualifies the chassis, adapters, tracks,
  or installed motors
  [source-pololu-37d-vendor-datasheet, PDF p. 1, notes 2 and 3](vendor/pololu-37d-metal-gearmotors-rev-1.2.pdf#page=1).
- Secure both tracks before powered tests. The source gives performance data,
  not a safe project current limit, thermal cutoff, duty cycle, or jam
  recovery strategy. Those require the exact motors and system-level evidence.
- Motor mounting uses six M3 holes with a 3 mm thread-depth limit; exceeding
  that depth can damage the gearbox
  [source-pololu-37d-vendor-datasheet, PDF p. 2, dimension drawing note 1](vendor/pololu-37d-metal-gearmotors-rev-1.2.pdf#page=2).

## Power, Encoder, and Calibration

The six-lead encoder version uses red and black for motor power, green for
encoder ground, blue for encoder Vcc, yellow for A, and white for B. Encoder
Vcc is specified as 3.5–20 V and the Hall sensors draw at most 10 mA. A and B
are square waves from 0 V to Vcc, approximately 90° out of phase
[source-pololu-37d-vendor-datasheet, PDF p. 4, lead table and encoder electrical description](vendor/pololu-37d-metal-gearmotors-rev-1.2.pdf#page=4).

The shared wiring note says the encoders use Pico 3.3 V, below the datasheet's
3.5 V minimum, and project records conflict about the left A/B Pico pins. Do
not normalize either conflict. Resolve supply and signal levels under
[`Q-US002-002`](../../../../verification/questions/US-002.yaml), and resolve
the left harness with power-isolated continuity under `Q-US002-003` before
changing control constants. Supplying a higher Vcc would also raise A/B high
levels, so Pico input compatibility must be established rather than inferred.

Counting both edges of both channels gives 64 counts per motor revolution;
counting one edge of one channel gives 16. Direction comes from A/B phase
order, and speed from edge frequency
[source-pololu-37d-vendor-datasheet, PDF p. 4, quadrature description](vendor/pololu-37d-metal-gearmotors-rev-1.2.pdf#page=4).

## Mechanical and Replacement Notes

The family drawing gives a 6 mm D shaft, 37D gearbox envelope, ratio-dependent
gearbox length, and separate encoder/non-encoder rear geometry. Encoder models
weigh 190–210 g. Open the drawing before any bracket, adapter, fastener, or
clearance decision; do not reconstruct fit from this summary
[source-pololu-37d-vendor-datasheet, PDF p. 2, dimension drawings](vendor/pololu-37d-metal-gearmotors-rev-1.2.pdf#page=2).

Project-specific brackets, shaft adapters, and chassis expansion remain under
[`assets/mechanical`](../../../mechanical/). A replacement must match the
verified voltage, ratio, encoder, shaft, mounting, current, and performance
requirements; a generic 37D listing is insufficient.

## Diagnostics and Open Questions

With a qualified encoder supply, A and B should be 0-to-Vcc quadrature signals.
Missing transitions can indicate supply, ground, connector, mapping, or sensor
problems; reversed phase order can reflect swapped channels or reversed motor
motion. These are diagnostic interpretations, not evidence about the current
harness.

Open questions remain `Q-US002-002`, `Q-US002-003`, and `Q-US002-005` in the
[US-002 question record](../../../../verification/questions/US-002.yaml).

## Sources and Coverage

The registered Rev 1.2 family datasheet was reviewed at the hash above. This
README covers its decision-relevant performance, encoder, safety, and mounting
information. Open the original for the complete family table, performance
graphs, or dimensional drawing. Source curation does not verify installed
identity, wiring, condition, or behavior; use the
[component registry](../../../../reference/component-registry.yaml) for those
states and provenance.
