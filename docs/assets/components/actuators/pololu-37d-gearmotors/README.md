---
component_id: component-pololu-37d-motors-01
documentation_status: partial
reviewed_on: null
reviewed_sources: []
coverage:
  identity_and_applicability: partial
  safety_and_limits: pending
  power_and_electrical: partial
  interfaces_and_timing: partial
  configuration_and_calibration: pending
  mechanical_and_environmental: partial
  diagnostics_and_failure_modes: pending
  replacement_and_compatibility: pending
---
# Pololu 37D Gearmotors

Two owner-reported 37D 30:1 motors drive the tracks and provide quadrature
feedback. Exact order numbers and encoder variants remain unknown.

Project records disagree about encoder supply and left-channel pin mapping.
Do not normalize those conflicts. Use power-isolated continuity for mapping and
approval-gated measurement for powered supply and signal-level evidence.

The family datasheet has not been curated. Family data cannot select the
installed order number, gearbox, or encoder variant.

## Registered vendor source awaiting curation

- [Pololu 37D gearmotor family datasheet](vendor/pololu-37d-metal-gearmotors-rev-1.2.pdf)

Project-specific geometry remains under
[`assets/mechanical`](../../../mechanical/). Use the
[component registry](../../../../reference/component-registry.yaml) for claim
provenance and confidence.
