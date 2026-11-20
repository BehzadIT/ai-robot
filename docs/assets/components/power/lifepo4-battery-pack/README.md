---
component_id: component-lifepo4-pack-01
documentation_status: curated
reviewed_on: "2026-11-20"
reviewed_sources:
  - id: source-goldencell-18650-spec
    sha256: f2b9a83af80b89f7da974eea0cbb8920d1d9148a2903863cd5ad363a30223096
coverage:
  identity_and_applicability: covered
  safety_and_limits: covered
  power_and_electrical: covered
  interfaces_and_timing: not-applicable
  configuration_and_calibration: covered
  mechanical_and_environmental: covered
  diagnostics_and_failure_modes: covered
  replacement_and_compatibility: covered
---
# 4S2P LiFePO4 Battery Pack

This pack is owner-reported as eight 18650 LiFePO4 cells in 4S2P. The retained
Goldencell specification is for one candidate cell, `JGCFR18650-2200mAh-3.2V`
(`18FC-7.04Wh`, document `SDJG/C-LI-PS109`, revision R1.1); it does not identify
the installed cells or qualify the assembled pack.

Do not unwrap or dismantle the pack solely to identify it. Charging remains
blocked until the exact cells, pack construction, BMS, charger label and
program, protection, fire readiness, and enforced charge current are known.

## Decision Summary

- The candidate cell is nominally 3.2 V and 2200 mAh, with 2100 mAh minimum
  capacity at the stated 0.2C condition. Its maximum charging current is 1.1 A
  at 25 °C. These are **cell values**, not verified pack values.
  [source-goldencell-18650-spec, PDF p. 5, §6](vendor/candidate-jgcfr18650-cell-specification-r1.1.pdf#page=5)
- A hypothetical 2P group made from these exact matched cells would have 2.2 A
  of summed candidate-cell charge-current allowance only if current shares as
  intended. That arithmetic is a project inference, not a pack qualification;
  it does not make a 5 A charger setting acceptable.
- The source's standard-charge test is 0.5C constant current to 3.65 V followed
  by constant voltage to a 0.01C cutoff. Treat this as a candidate-cell test
  condition, not evidence of the installed pack's charger program.
  [source-goldencell-18650-spec, PDF p. 6, §7.1](vendor/candidate-jgcfr18650-cell-specification-r1.1.pdf#page=6)
- Candidate-cell working temperature, including temperature rise, is 0 to
  60 °C while charging and -20 to 65 °C while discharging; the source says to
  stop charge or discharge outside those ranges.
  [source-goldencell-18650-spec, PDF p. 6, §6 item 10](vendor/candidate-jgcfr18650-cell-specification-r1.1.pdf#page=6)

## Safety and Limits

For packs built from this candidate cell, the source calls for charge to stop
at 3.65 V per cell and discharge to stop at 2.5 V per cell. Its 3.85 V
overcharge-protection and 2.3/2.0 V overdischarge entries are emergency warning
thresholds beyond normal use, not operating targets; it prohibits charging a
cell below 2.0 V. It also requires short-circuit, overcurrent, overtemperature,
and low-temperature protection.
[source-goldencell-18650-spec, PDF p. 8, §7.9](vendor/candidate-jgcfr18650-cell-specification-r1.1.pdf#page=8)

The candidate charge-rate table is temperature-dependent: 0.1C at 0 or 5 °C,
0.2C at 10 °C, 0.5C from 15 through 50 °C, 0.2C at 55 °C, and zero at 60 °C.
Do not turn these into pack settings until cell identity and temperature sensing
are established.
[source-goldencell-18650-spec, PDF p. 8, §7.8](vendor/candidate-jgcfr18650-cell-specification-r1.1.pdf#page=8)

The source prohibits short circuit, mechanical shock or piercing, direct
welding to the steel can, disassembly, and charging below 2.0 V. It says to
stop use or charging and isolate a cell that develops odor, heat, discoloration,
deformation, leakage, or other abnormal behavior.
[source-goldencell-18650-spec, PDF p. 12, §11](vendor/candidate-jgcfr18650-cell-specification-r1.1.pdf#page=12)

## Mechanical and Replacement Notes

The candidate sleeved cell is 65.20 ± 0.30 mm high, no more than 18.60 mm in
diameter, and approximately 43 g. Those dimensions do not establish the pack's
interconnect, insulation, enclosure, fuse, disconnect, sensor placement, or
serviceability.
[source-goldencell-18650-spec, PDF p. 5, §§5–6 (continues on p. 6)](vendor/candidate-jgcfr18650-cell-specification-r1.1.pdf#page=5)

Do not select replacement cells from size and chemistry alone. Confirm the
exact model, revision, capacity, charge/discharge limits, matching requirements,
and pack-builder process. Any cell replacement or pack rework requires a
separate approved procedure.

## Open Questions

- `Q-US002-018`: identify the installed cells and retain construction evidence
  without dismantling solely for documentation.
- `Q-US002-017`: establish the charge-current limit actually configured or
  enforced after cell, BMS, and charger identity are resolved.
- `Q-US002-006` and `Q-US002-019`: establish the high-current protection path
  and a reachable emergency motor-power disconnect.

Project-specific battery records remain under
[`assets/electrical`](../../../electrical/). The
[component registry](../../../../reference/component-registry.yaml) owns the
pack's physical state and claim provenance.

## Sources and Coverage

- Reviewed the complete candidate specification at the recorded hash. Open the
  original for complete discharge-rate, cycle-life, environmental-test, and
  manufacturing requirements not reproduced here.
- Source coverage is complete, but applicability is unresolved: curation does
  not verify the installed cell identity or assembled-pack behavior.
