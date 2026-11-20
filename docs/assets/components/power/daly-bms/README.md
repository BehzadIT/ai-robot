---
component_id: component-daly-bms-01
documentation_status: curated
reviewed_on: "2026-11-20"
reviewed_sources:
  - id: source-daly-active-balance-manual
    sha256: 79c8c43d03d5a62b72802096019ee0910ab3299ad27c2171add4169e560d5265
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
# Installed DALY-Family BMS

Project records contain incompatible candidate identities for this BMS. The
retained manual covers DALY smart active-balance products spanning 4–24 series
cells and nominal 40–500 A variants; it cannot select the installed model,
current rating, supported cell-count band, connectors, firmware, balancing, or
communications options.
[source-daly-active-balance-manual, PDF p. 1, cover](vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf#page=1)

Photograph or transcribe the complete label and connectors before applying a
wiring diagram, cable, application setting, or protocol. Do not disconnect
sampling leads merely to identify the unit, and do not assume that the BMS
regulates charger current.

## Decision Summary

- Sampling-wire installation begins with the thin black wire at pack B-, then
  proceeds through each successive series-group positive, ending at total B+.
  The manual requires checking every sampling voltage and sequence before the
  harness is inserted into the BMS. This procedure is family guidance only and
  must not be applied until the installed model and harness are qualified.
  [source-daly-active-balance-manual, PDF p. 1, §II.1](vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf#page=1)
- The manual says sampling cables from different manufacturers are not
  interchangeable. Connector fit is therefore not evidence of compatibility.
  [source-daly-active-balance-manual, PDF p. 2, §II.4(1)](vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf#page=2)
- First-time configuration requires battery type and actual pack capacity in
  the app or PC. Although the family manual says its factory default is LFP,
  that default must not be trusted on the installed unit. Its described 100%
  state-of-charge calibration must not be attempted while charging is blocked.
  [source-daly-active-balance-manual, PDF p. 1, §II.3](vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf#page=1)

## Safety, Wiring, and Environment

The family wiring page assigns B- to battery negative and P- to load/charger
negative. It requires this power-on order: install B-, insert the collection
line, connect B+, then install P-. Power-off is B+, collection line, P-, then
B-. Reversing the wiring sequence can damage the BMS. Do not use this sequence
for physical work until the exact unit, harness, and approved procedure are
established.
[source-daly-active-balance-manual, PDF p. 3, wiring precautions](vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf#page=3)

The manual requires firm restraint of the collection, B+, B-, and P- harnesses,
plus waterproofing, moisture protection, and insulation. It gives a family
working-temperature range of -40 to 85 °C and calls for at least 10 MΩ between
pack total positive or negative and the enclosure. These values have not been
verified on the installed model.
[source-daly-active-balance-manual, PDF p. 3, BMS application environment](vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf#page=3)

Do not place the BMS heat-dissipation surface directly against a cell. The
manual warns that its enclosure can be electrically conductive and shares
ground with the motherboard; keep it away from cells and nickel strip and use
insulation appropriate to the installation.
[source-daly-active-balance-manual, PDF p. 2, §II.4(3–5)](vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf#page=2)

## Interfaces, Diagnostics, and Replacement

The family source depicts optional or variant-dependent Bluetooth/Wi-Fi, UART,
CAN/RS485, display, GPS, DIO, key, and NTC interfaces. Do not infer that any is
present or use its pin table until connector identity and board revision are
matched. Its status indication is green for normal operation and red for alarm
or protection, but a light alone does not diagnose the cause.
[source-daly-active-balance-manual, PDF p. 2, §§III–IV](vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf#page=2)

Replacement requires matching chemistry, supported series count, continuous
charge and discharge ratings, protection thresholds, balance behavior,
connector/harness family, communications, thermistors, mechanical mounting,
and firmware/application support. The manual's broad model table cannot make
that selection without the installed label.

## Open Questions

- `Q-US002-001`: record the complete installed BMS label and connectors.
- `Q-US002-017`: establish actual BMS and charger current enforcement after
  the cell and charger identities are known.
- `Q-US002-006`: map the unpowered high-current path, protection, conductors,
  and disconnects.

Use the [component registry](../../../../reference/component-registry.yaml) for
physical state and claim provenance.

## Sources and Coverage

- Reviewed all four pages of the 2024-11-15 family manual at the recorded hash.
  Open the original for model-specific current tables, connector-pin tables,
  balancing defaults, and series-count diagrams.
- Source coverage is complete. Installed-product applicability remains
  unresolved and no wiring, setting, condition, or function has been verified.
