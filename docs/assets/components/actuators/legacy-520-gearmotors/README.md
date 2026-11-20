---
component_id: component-legacy-520-motors-01
documentation_status: curated
reviewed_on: "2026-11-20"
reviewed_sources:
  - id: source-suspended-chassis-manual
    sha256: 12b91c0f66c0476213c7613e0494e0f48264786a00e544f413fd3a3ab7b41f3c
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
# Legacy 520 Encoder Gearmotors

These motors are the stock drivetrain described with the suspension-crawler
package. They are historical references and must not supply voltage, current,
encoder, speed, torque, or calibration constants for the current Pololu 37D
drivetrain. The physical motors' manufacturer, exact identity, inventory,
condition, and location remain unverified.

## Decision Summary

- The source labels the stock unit “520 encoder DC gear motor” and gives 12 V
  rated voltage, 0.1 A rated current, a 7–13 V range, 0.15 N·m rated torque,
  permanent-magnet brushed construction, 45:1 reduction, and 1.5 A
  locked-rotor current
  [source-suspended-chassis-manual, PDF p. 3, 520 encoder DC gear motor table](../../mechanical/tracked-chassis/vendor/suspension-crawler-technical-parameters.pdf#page=3).
- The continuation gives 0.5 N·m “gridlock torque,” a 6 mm D-type eccentric
  output shaft, 6500 rpm before reduction, 150 ± 10 rpm reduced speed, and a
  Hall encoder
  [source-suspended-chassis-manual, PDF p. 4, motor table continuation](../../mechanical/tracked-chassis/vendor/suspension-crawler-technical-parameters.pdf#page=4).
- The source does not define the test voltage or conditions for speed and
  torque, nor whether “gridlock torque” is a stall value. Treat that wording as
  vendor terminology, not a qualified continuous limit.

## Safety, Power, and Encoder Gaps

Locked-rotor current is not a normal operating target. The source gives no
thermal limit, duty cycle, winding-temperature protection, safe continuous
load envelope, jam procedure, or environmental rating. Do not power an
unidentified legacy motor until its condition, restraint, wiring, and current
limiting are qualified.

The source says only “Hall encoder.” It provides no encoder supply range,
pinout, channel count, logic levels, counts per revolution, timing, connector,
or calibration procedure. Therefore it cannot support firmware scaling or
electrical connection, even for the legacy motor.

## Mechanical and Replacement Notes

The source includes a motor dimensional drawing on PDF page 5, but several
labels are low-resolution or ambiguous. Open that page for orientation and
measure the physical motor before selecting a bracket, shaft adapter, fastener,
or replacement
[source-suspended-chassis-manual, PDF p. 5, dimensional drawing 03](../../mechanical/tracked-chassis/vendor/suspension-crawler-technical-parameters.pdf#page=5).

These values describe the source's stock motor, not the current Pololu motors.
A stock-equivalent replacement would still require verified mechanical fit,
encoder interface, electrical limits, and drivetrain intent. Do not substitute
it into the present control system by matching only “520,” 12 V, or 45:1.

## Diagnostics and Applicability

The source provides no indicators, fault reporting, troubleshooting, or
maintenance instructions. Missing encoder feedback, excess current, abnormal
noise, heating, or shaft runout would require physical inspection and
measurement; none should be attributed to a specific cause from this source
alone.

The registry model alias `JGB3865-520R45-12` is documented-unverified. The PDF
itself does not print that full model designation, so source curation does not
promote the physical identity.

## Sources and Coverage

The registered suspension-crawler source was reviewed at the hash above for
legacy-motor scope, separately from its chassis scope. It supplies a small
stock specification table and drawing but omits the encoder interface,
operating conditions, and safe-use procedure. Those omissions are captured
here; curation does not verify inventory, identity, condition, or behavior.
Use the [component registry](../../../../reference/component-registry.yaml) for
the current project state.
