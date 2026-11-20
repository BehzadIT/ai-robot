---
component_id: component-raspberry-pi-pico-2w-01
documentation_status: partial
reviewed_on: null
reviewed_sources: []
coverage:
  identity_and_applicability: partial
  safety_and_limits: pending
  power_and_electrical: pending
  interfaces_and_timing: pending
  configuration_and_calibration: pending
  mechanical_and_environmental: pending
  diagnostics_and_failure_modes: pending
  replacement_and_compatibility: pending
---
# Raspberry Pi Pico 2 W

The Pico owns final command admission, freshness, encoders, drivetrain output,
and real-time safety. ESP32 and Android may deliver intent but do not replace
that authority.

The board identity is owner-reported. Its mounting and as-built harness remain
unqualified, and current code conflicts with the shared wiring note for some
left-encoder and motor-driver signals. Resolve `Q-US002-003` and
`Q-US002-016` with power-isolated continuity evidence before changing firmware
or canonical wiring.

The registered vendor documents in `vendor/` have not been curated into this
documentation. The RP2350 documents are supporting chip-level sources and cannot
override Pico 2 W board-level behavior.

## Registered vendor sources awaiting curation

- [Pico 2 W datasheet](vendor/pico-2-w-datasheet-release-2.pdf)
- [Pico 2 W pinout](vendor/pico-2-w-pinout-rev-1.pdf)
- [Pico 2 W schematic](vendor/pico-2-w-schematic-rev-1.pdf)
- [RP2350 datasheet](vendor/rp2350-datasheet-release-3.pdf)
- [RP2350 hardware-design guide](vendor/rp2350-hardware-design-release-3.pdf)

Use the [component registry](../../../../reference/component-registry.yaml) for
claim provenance and confidence.
