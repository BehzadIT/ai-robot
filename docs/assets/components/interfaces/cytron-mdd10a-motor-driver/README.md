---
component_id: component-cytron-mdd10a-01
documentation_status: partial
reviewed_on: null
reviewed_sources: []
coverage:
  identity_and_applicability: partial
  safety_and_limits: pending
  power_and_electrical: partial
  interfaces_and_timing: partial
  configuration_and_calibration: pending
  mechanical_and_environmental: pending
  diagnostics_and_failure_modes: pending
  replacement_and_compatibility: pending
---
# Cytron MDD10A Motor Driver

The driver converts Pico PWM and direction outputs into left and right motor
power. The exact installed board revision has not been photographed.

The shared wiring note and current Pico implementations disagree about signal
mapping. Resolve `Q-US002-016` by continuity from named Pico pins to named
Cytron inputs. Do not energize motors merely to infer the map.

The retained manual is for MDD10A Rev 2.0 and has not been curated. Do not apply
its revision-specific limits to an older board until `Q-US002-005` is resolved.

## Registered vendor source awaiting curation

- [Cytron MDD10A Rev 2.0 manual](vendor/cytron-mdd10a-user-manual-v2.0.pdf)

Use the [component registry](../../../../reference/component-registry.yaml) for
claim provenance and confidence.
