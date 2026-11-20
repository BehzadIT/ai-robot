---
component_id: component-esp32-dev-board-01
documentation_status: curated
reviewed_on: "2026-11-20"
reviewed_sources:
  - id: source-esp32-series-datasheet
    sha256: a7917e6b47528c9dcab06837a49d452e582751335797db879f1cf2d17cd29adf
  - id: source-esp32-hardware-design-guidelines
    sha256: 139e58bf41cb03211d8860d5bba8da0825643272dd438615cb6f92512992bade
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
# ESP32 Development Board

This pack covers what the registered **classic ESP32 chip-family** sources can
say about the unidentified installed development board. It is source-complete,
but it is not a board manual. The exact development board, module, ESP32 chip
variant, USB/UART bridge, regulator, connector pinout, and exposed pins remain
unknown. Espressif's hardware guide explicitly uses "ESP32" for the series of
chips unless otherwise stated
[source-esp32-hardware-design-guidelines, §Product Overview](vendor/esp32-hardware-design-guidelines-v1.9.md#product-overview),
and lists multiple distinct development boards rather than one generic pinout
[source-esp32-hardware-design-guidelines, §ESP32 Development Boards](vendor/esp32-hardware-design-guidelines-v1.9.md#esp32-development-boards).

In this robot, the ESP32 owns wireless gateway, telemetry, controller
connectivity, normalization, diagnostics, and bounded transport. It does not
own motor control or safety decisions.

## Decision Summary

- Do not apply chip supply ratings to an unidentified board's USB, `VIN`, `5V`,
  or `3V3` connector. The chip design target is 3.3 V with a recommended source
  capability of at least 500 mA, but the installed board's regulator and input
  topology are unknown
  [source-esp32-series-datasheet, PDF p. 19, §2.5.3](vendor/esp32-series-datasheet-v5.3.pdf#page=19).
- Do not choose GPIOs from a generic online DevKit diagram. Classic ESP32 pins
  include input-only pins, flash/PSRAM-reserved pins, and startup/debug pins
  with restrictions
  [source-esp32-series-datasheet, PDF p. 17, §2.3.1](vendor/esp32-series-datasheet-v5.3.pdf#page=17).
- Loads on GPIO0, GPIO2, GPIO5, MTDI, or MTDO can alter boot-time strapping.
  The chip samples and latches these levels at reset, then releases the pins for
  normal I/O
  [source-esp32-series-datasheet, PDF p. 22, §3](vendor/esp32-series-datasheet-v5.3.pdf#page=22).
- Keep ESP32 transport bounded and fail-safe. No source in this pack grants the
  ESP32 final motor, stop, or fault authority.

## Safety and Limits

At **chip level**, the absolute maximum supply-pin range is -0.3 V to 3.6 V;
this is a stress limit and not a normal operating target. Recommended supply is
typically 3.3 V, with a 3.6 V maximum and a variant-dependent 2.3 V or 3.0 V
minimum for the listed domains. The same table calls for an external supply
capable of at least 0.5 A and gives variant-dependent operating-temperature
limits
[source-esp32-series-datasheet, PDF p. 51, §5.1–5.2](vendor/esp32-series-datasheet-v5.3.pdf#page=51).
These values do not establish allowable voltage at any development-board power
header, USB connector, or GPIO carrier circuit.

The hardware guide recommends a 3.3 V supply of at least 500 mA, an ESD diode,
and at least 10 µF at the main power entrance for a custom ESP32 design
[source-esp32-hardware-design-guidelines, §Power Supply](vendor/esp32-hardware-design-guidelines-v1.9.md#power-supply).
That guidance is useful when assessing a board schematic; it is not evidence
that these parts exist on the installed board.

## Power, Interfaces, and Configuration

The chip requires its rails to stabilize before `CHIP_PU` is asserted. The
datasheet specifies at least 50 µs for rail stabilization and at least 50 µs
with `CHIP_PU` low for reset. It also warns that rapid power cycling with a
large rail capacitor may need an added discharge path, and recommends a voltage
supervisor for battery use to avoid low-voltage boot failure
[source-esp32-series-datasheet, PDF p. 19, §2.5.3](vendor/esp32-series-datasheet-v5.3.pdf#page=19).
An unidentified development board may already implement different enable,
auto-reset, and USB/UART circuitry.

GPIO0 and GPIO2 control normal SPI boot versus joint download boot after reset;
the documented joint-download combination is GPIO0 low and GPIO2 low. The
strapping hold time is at least 1 ms after `CHIP_PU` rises
[source-esp32-series-datasheet, PDF p. 23, §3.1](vendor/esp32-series-datasheet-v5.3.pdf#page=23).
Espressif's design guide additionally warns to avoid flash/PSRAM pins and notes
that GPIO34 and above are input-only and lack internal pulls
[source-esp32-hardware-design-guidelines, §GPIO](vendor/esp32-hardware-design-guidelines-v1.9.md#gpio).

The project currently targets classic `esp32`, but that software target does
not identify the board. The intended robot UART assignments in
[wiring-and-pinout.md](../../../../electrical/wiring-and-pinout.md) remain
documented-unverified until the board/module and harness are physically
identified.

## Mechanical and Environmental

No registered source provides the installed board's dimensions, mounting-hole
pattern, connector locations, module antenna type, temperature grade, or
enclosure clearance. The hardware guide's antenna-layout recommendations apply
to a module-on-base-board design, not automatically to this unknown development
board. Do not use them as a mechanical drawing or proof of installed clearance.

Record board photos, module markings, USB-interface markings, mounting,
clearance, and antenna orientation before enclosure or replacement decisions.

## Diagnostics and Failure Modes

- Failure to boot can result from supply droop, reset timing, or an externally
  forced strapping pin; it does not by itself identify which cause occurred.
- A board may appear to accept firmware over USB/UART while robot UART pins or
  voltage domains remain incompatible.
- Wrong board targeting or use of unavailable/reserved GPIO can produce
  startup, flash, or transport failures.
- Wireless or transport loss must remain a bounded input failure; the Pico
  retains final command admission and safety authority.

## Replacement and Compatibility

No generic "ESP32 development board" replacement is qualified by these
sources. Compatibility requires the exact board and module identity, classic
ESP32 target compatibility, regulator/input path, USB/UART bridge and reset
circuit, exposed GPIO map, logic levels, antenna arrangement, dimensions, and
connector placement. A chip-family match alone is insufficient.

## Open Question

[`Q-US002-004`](../../../../verification/questions/US-002.yaml) requires board
front/rear photos plus exact board, module, and USB-interface markings (or an
exact owner transcription). That physical evidence is required before treating
any board-specific pinout, input rating, flashing sequence, or mechanical
drawing as applicable.

## Sources and Coverage

Both registered sources were reviewed at the hashes recorded above. The PDF is
the ESP32 series chip datasheet; the retained HTML-to-Markdown source is a
custom hardware-design guide. Together they cover chip constraints and expose
the exact board-level gaps, but neither identifies the installed development
board. Open the originals for variant tables, complete pin multiplexing,
electrical characteristics, RF design, or PCB-layout work. Coverage is
`curated` for this registered source set while physical identity, connection,
condition, and behavior remain unverified.
