---
component_id: component-cytron-mdd10a-01
documentation_status: curated
reviewed_on: "2026-11-20"
reviewed_sources:
  - id: source-cytron-mdd10a-manual
    sha256: dc1120016644500f63e2815006bb1b9cd5119b2e9d2c95a9307152338619f9fa
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
# Cytron MDD10A Motor Driver

The owner-reported MDD10A converts Pico PWM and direction outputs into power
for the two track motors. The retained manual is specifically for MDD10A
Rev 2.0. The installed board revision has not been photographed, so its
Rev 2.0 voltage limit must not be applied until `Q-US002-005` is resolved.

## Decision Summary

- The manual says boards shipped after January 2017 are Rev 2.0 and support a
  30 V maximum motor supply. It describes two brushed-DC channels, each rated
  up to 10 A continuous and 30 A peak for 10 seconds, and supports both
  sign-magnitude and locked-antiphase control
  [source-cytron-mdd10a-manual, PDF p. 3, §1 Introduction/Overview](vendor/cytron-mdd10a-user-manual-v2.0.pdf#page=3).
- Those electrical values appear under **Absolute Maximum Rating**. For Rev 2.0
  the table gives 5–30 V power input, 10 A maximum continuous current per
  channel tested at 25 °C, 30 A peak for no more than 10 seconds, logic-high
  input 3–5.5 V, logic-low input 0–0.5 V, and 20 kHz maximum PWM. Absolute
  maxima are not recommended operating targets
  [source-cytron-mdd10a-manual, PDF p. 5, §3 Product Specification and Limitations](vendor/cytron-mdd10a-user-manual-v2.0.pdf#page=5).
- The board accepts microcontroller TTL PWM, not hobby-RC receiver PWM
  [source-cytron-mdd10a-manual, PDF p. 3, feature list](vendor/cytron-mdd10a-user-manual-v2.0.pdf#page=3).

## Safety and Power

The manual warns that regenerative current from an inductive motor can cause a
switching supply to shut down. It recommends a battery; if a switching supply
is required, it says a battery of the same rated voltage must be placed in
parallel to absorb regenerative current
[source-cytron-mdd10a-manual, PDF p. 9, regenerative-current note](vendor/cytron-mdd10a-user-manual-v2.0.pdf#page=9).

That vendor example does not qualify the robot's battery, BMS, fuse,
disconnect, wiring, or bench-supply arrangement. Keep motor power independently
disconnectable during control bring-up, secure the tracks, and resolve the
as-built high-current path under `Q-US002-006`. Do not use 30 V, 10 A, or 30 A
as design targets, and do not assume an older MDD10A has the Rev 2.0 range.

## Inputs, Outputs, and Control Modes

The five-pin logic header order is GND, PWM2, DIR2, PWM1, DIR1. In the manual's
truth table PWM low drives both outputs low; with PWM high, DIR selects which
of outputs A and B is high. The six power terminals are Motor 1 B, Motor 1 A,
POWER+, POWER−, Motor 2 A, and Motor 2 B
[source-cytron-mdd10a-manual, PDF p. 8, §6 Input and terminal-block table](vendor/cytron-mdd10a-user-manual-v2.0.pdf#page=8).

In sign-magnitude mode, PWM controls speed and DIR controls direction. In
locked-antiphase mode, PWM is held high and a PWM waveform is applied to DIR;
50% duty stops and either side of 50% commands opposite directions, with the
physical direction depending on motor wiring
[source-cytron-mdd10a-manual, PDF p. 10, §6 Getting Started](vendor/cytron-mdd10a-user-manual-v2.0.pdf#page=10).

The shared wiring note and both current Pico implementations disagree about
which Pico signals reach PWM and DIR and which channel drives each track.
Resolve `Q-US002-016` using power-isolated continuity from named Pico pins to
named Cytron inputs. Do not alter constants or energize motors merely to infer
the map.

## Mechanical, Indicators, and Failure Clues

The manual gives an 84.5 mm × 62 mm board outline, approximately 78.74 mm ×
55.88 mm mounting-hole spacing, and approximately 3 mm mounting holes
[source-cytron-mdd10a-manual, PDF p. 6, §4 Dimension](vendor/cytron-mdd10a-user-manual-v2.0.pdf#page=6).
Verify the installed board and mounting before fabrication.

The green LED indicates board power. Four red LEDs indicate which A/B output
polarity is active; they are direction/output indicators, not documented fault
codes. The four test buttons directly command the corresponding output
direction
[source-cytron-mdd10a-manual, PDF p. 7, §5 Board Layout; continued on p. 8](vendor/cytron-mdd10a-user-manual-v2.0.pdf#page=7).
Do not press test buttons until motor power, isolation, polarity, and mechanical
restraint are qualified. The manual does not document a fault output or a
diagnostic distinction among overload, thermal behavior, wiring error, and
loss of logic input.

## Open Questions

`Q-US002-005` covers the installed board revision, `Q-US002-006` the
high-current path, and `Q-US002-016` the Pico-to-driver harness. They remain
open in the [US-002 question record](../../../../verification/questions/US-002.yaml).

## Sources and Coverage

The registered v2.0 manual was reviewed at the hash above. This README covers
the decision-relevant limits, terminals, truth table, control modes,
regeneration warning, dimensions, and indicators. Open the original for the
complete board diagrams and vendor examples. Curation does not verify the
installed revision, wiring, condition, configuration, or behavior; use the
[component registry](../../../../reference/component-registry.yaml) for those
states and provenance.
