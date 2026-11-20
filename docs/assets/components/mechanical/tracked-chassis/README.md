---
component_id: component-tracked-chassis-01
documentation_status: curated
reviewed_on: "2026-11-20"
reviewed_sources:
  - id: source-suspended-chassis-manual
    sha256: 12b91c0f66c0476213c7613e0494e0f48264786a00e544f413fd3a3ab7b41f3c
coverage:
  identity_and_applicability: covered
  safety_and_limits: covered
  power_and_electrical: not-applicable
  interfaces_and_timing: not-applicable
  configuration_and_calibration: not-applicable
  mechanical_and_environmental: covered
  diagnostics_and_failure_modes: covered
  replacement_and_compatibility: covered
---
# Tracked Chassis

The robot base is documented as a suspension crawler chassis modified for a
Pololu 37D/Cytron drivetrain. The retained source describes the **original
stock package**, including its 520 motors and STM32 controller. Its base
geometry is relevant to the chassis, but its motor and controller data are
legacy and must not be used for the upgraded drivetrain.

## Decision Summary

- The stock product table gives an overall envelope of 27.3 × 19.3 × 9.4 cm,
  1.4 kg weight, 3 m/s maximum speed, 35° climb rating, and 10 kg load rating
  [source-suspended-chassis-manual, PDF p. 1, Suspension crawler chassis table](vendor/suspension-crawler-technical-parameters.pdf#page=1).
- These are vendor nominal stock-package values, not verified properties or
  safe limits of the modified robot. Added decks, the expanded width, current
  drivetrain, payload placement, track condition, and center of mass can
  invalidate the stock speed, slope, and load claims.
- The high-level base-plate drawing gives 270 mm length and 143 mm width
  [source-suspended-chassis-manual, PDF p. 4, dimensional drawing 01](vendor/suspension-crawler-technical-parameters.pdf#page=4).
  It does not establish the current expanded width, hole locations, tolerances,
  or as-built clearances.

## Safety, Fit, and Inspection

Secure the tracks and chassis before powered motion, fitting, cutting, or
drilling. Cutting or drilling also requires compatible tooling, secure
workholding, debris control, deburring, PPE, and post-work inspection. The
vendor source does not specify chassis material, tolerances, fastener grades,
payload distribution, environmental limits, track tension, or safe modification
practice.

Before fabrication or replacement, photograph and measure the installed
revision, motor brackets, shaft adapters, track alignment, plate thickness,
hole pattern, and working clearances. Inspect for loose fasteners, track
misalignment, insufficient motor clearance, bracket movement, and shaft-adapter
runout. Those checks reflect project failure risks; the vendor source supplies
no diagnostic or maintenance procedure.

## Legacy-versus-current Boundary

The same PDF describes the stock STM32 controller and 520 encoder gearmotor on
pages 2–5. Those pages document the original package only. Current motor and
driver decisions belong in the
[Pololu 37D](../../actuators/pololu-37d-gearmotors/README.md) and
[Cytron MDD10A](../../interfaces/cytron-mdd10a-motor-driver/README.md)
component packs. The stock motor is curated separately in the
[legacy 520 motor pack](../../actuators/legacy-520-gearmotors/README.md).

Project-specific expansion dimensions, hole offsets, bracket placement, and
shaft-adapter changes remain under [`assets/mechanical`](../../../mechanical/).
They are project notes, not proof of the current as-built chassis.

## Open Questions

The source review does not resolve available fabrication/workholding equipment
or material and hardware stock. Those remain `Q-US002-012` and `Q-US002-013`
in the [US-002 question record](../../../../verification/questions/US-002.yaml).
Neither question substitutes for an as-built chassis survey.

## Sources and Coverage

The registered suspension-crawler source was reviewed at the hash above for
base-chassis scope. This README intentionally excludes its legacy motor and
controller values from current chassis decisions. Open PDF pages 4–5 for the
original drawings, then verify all decision-critical geometry on the physical
robot. Curation does not verify identity, modification state, condition, fit,
or load capability; use the
[component registry](../../../../reference/component-registry.yaml) for those
states and provenance.
