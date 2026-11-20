---
component_id: component-panther-iqload-evo-charger-01
documentation_status: curated
reviewed_on: "2026-11-20"
reviewed_sources:
  - id: source-iqload-evo-manual
    sha256: 81b8bc98ff297c2fc18f394e44e26a3c5d30e1f64d24ead1f0ed4095aab839ba
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
# Panther iQLoad EVO Charger

The project reports an iQLoad EVO 5, but its physical label and selected program
have not been verified. The retained 2021 manual covers both EVO 5 and EVO 7;
record the exact charger label and display before use.

**Charging remains blocked.** Qualification requires the exact cells, 2P
charge-current capability, BMS settings and current behavior, power-path
protection, selected charger mode, charger condition, and fire readiness.

## Decision Summary

- The EVO 5 table lists LiFePO4 among supported battery types, 2–110 Ah battery
  capacity, and a maximum 12 V charging current of 5 A. Those charger ratings
  do not prove compatibility with this pack.
  [source-iqload-evo-manual, PDF p. 9, Technical data](vendor/iqload-evo-5-and-7-manual-2021.pdf#page=9)
- The EVO 5 offers distinct 12 V vehicle and motorcycle LiFePO4 modes. The last
  selected mode is saved and restored when the charger is displayed, so a
  remembered mode must never substitute for a visible pre-charge check.
  [source-iqload-evo-manual, PDF p. 14, EVO 5 display description](vendor/iqload-evo-5-and-7-manual-2021.pdf#page=14)
- The manual requires selected voltage and battery technology to match the
  battery instructions and label. The EVO 5's 12 V mode accepts a connected
  battery from 3 V upward, but that detection window is not a safe pack-voltage
  qualification.
  [source-iqload-evo-manual, PDF p. 17, Start charging (continues on p. 18)](vendor/iqload-evo-5-and-7-manual-2021.pdf#page=17)
- The charging-stage section quotes 14.6 V values after explicitly warning that
  the listed stage values refer to a 12 V lead-acid battery and differ for other
  battery types. Therefore this source does **not** provide a sufficiently
  unambiguous LiFePO4 termination value for the project; verify the exact program
  from the physical charger/manual before charging.

## Safety and Operation

Inspect cables before use. Do not charge a damaged, frozen, or
non-rechargeable battery; do not use the charger around flammable materials;
keep it uncovered with adequate ventilation; and stop immediately for smoke or
unusual odor.
[source-iqload-evo-manual, PDF p. 5, Explosion and fire hazard](vendor/iqload-evo-5-and-7-manual-2021.pdf#page=5)

Connect or disconnect battery leads only with the charger unplugged from the
mains. Keep connections dry, prevent terminals from touching each other or
conductive tools, and do not open or repair the charger.
[source-iqload-evo-manual, PDF p. 6, Electric shock / short circuit](vendor/iqload-evo-5-and-7-manual-2021.pdf#page=6)

The rated ambient range is -20 to 40 °C; output power is automatically reduced
at high temperature. The housing is listed as IP65, but the manual still says
to use it in a safe, dry location and not expose it to rain or wet conditions.
[source-iqload-evo-manual, PDF p. 9, Technical data](vendor/iqload-evo-5-and-7-manual-2021.pdf#page=9)

To end charging, unplug the 230 V mains first, then remove the black negative
connection, then the red positive connection. This is vendor guidance, not an
authorization to charge the unresolved pack.
[source-iqload-evo-manual, PDF p. 19, End the charging process](vendor/iqload-evo-5-and-7-manual-2021.pdf#page=19)

## Diagnostics and Replacement

The manual associates `Er1`/`Er2` with causes including battery voltage below
3 V, selected voltage mismatch, an aborted process, failed recovery, excessive
main-charge duration, voltage collapse during monitoring, or charger
overtemperature. Disconnect mains before investigating; an error code does not
prove which cause occurred.
[source-iqload-evo-manual, PDF p. 19, Error messages (continues on p. 20)](vendor/iqload-evo-5-and-7-manual-2021.pdf#page=19)

Replacement or substitution must match supported chemistry, voltage, current,
capacity range, mains supply, environmental rating, leads, and charge-program
behavior. Do not substitute EVO 7 values for an EVO 5.

## Open Questions

- `Q-US002-007`: record the charger label, exact model, selected LiFePO4 mode,
  and displayed settings.
- `Q-US002-017`: establish the charge current actually configured or enforced
  against the verified cell and pack limits.
- `Q-US002-014`: establish battery-safe charging surface, ventilation, PPE,
  fire readiness, and emergency isolation.

Use the [component registry](../../../../reference/component-registry.yaml) for
physical state and claim provenance.

## Sources and Coverage

- Reviewed the complete 24-page EVO 5/EVO 7 manual at the recorded hash. Open
  it for accessory connection details, complete charge-stage descriptions,
  maintenance, and disposal.
- Source coverage is complete. The physical charger identity, condition,
  selected program, and compatibility with the robot pack remain unverified.
