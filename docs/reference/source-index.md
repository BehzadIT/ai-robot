# Source Index

This file is generated from `source-registry.yaml`. Do not edit it directly;
update the registry and run
`python3 tools/docs/validate_us002_records.py --write-indexes`.

## Repositories

- [robot-pico-platform](../../robot-pico-platform)
- [robot-esp32-platform](../../robot-esp32-platform)
- [robot-android-app](../../robot-android-app)

## Registered Sources

| ID | Source | Kind | Authority | Extraction |
| --- | --- | --- | --- | --- |
| `source-pico-micropython-drivetrain-constants` | [Active MicroPython Drivetrain Constants](../../robot-pico-platform/src/control/drivetrain_constants.py) | code | code-backed | text-reviewed |
| `source-pico-cpp-drivetrain-constants` | [Migrated C++ Drivetrain Constants](../../robot-pico-platform/cpp/include/robot/control/constants.hpp) | code | code-backed | text-reviewed |
| `source-esp32-sdkconfig` | [ESP32 Platform SDK Configuration](../../robot-esp32-platform/sdkconfig) | code | code-backed | text-reviewed |
| `source-project-components-updated` | [Robot Project Components Reference](../../docs/assets/reference/robot-project-components-updated.pdf) | project-pdf | generated-project-note | render-reviewed |
| `source-complete-component-list` | [Exhaustively Complete Component List](../../docs/assets/reference/robot-project-complete-component-list.txt) | project-note | generated-project-note | text-reviewed |
| `source-pololu-37d-project-note` | [Pololu 37D Encoder Specification And RPM Test Note](../../docs/assets/reference/pololu-37d-encoder-spec-and-rpm-test-code.txt) | project-note | owner-project-note | text-reviewed |
| `source-battery-system-note` | [Robot Battery System Component Reference](../../docs/assets/electrical/robot-battery-system.txt) | project-note | owner-project-note | text-reviewed |
| `source-wiring-reference` | [Robot Wiring Reference](../../docs/assets/electrical/wiring-reference.txt) | project-note | owner-project-note | text-reviewed |
| `source-motor-wire-photo` | [Motor Wire Connector Diagram](../../docs/assets/electrical/motor-wire.jpg) | photo | unknown | render-reviewed |
| `source-goldencell-18650-spec` | [JGCFR18650 2200 mAh 3.2 V Cell Specification](../../docs/assets/electrical/jgcfr18650-2200mah-lifepo4-cell-specification.pdf) | vendor-manual | vendor | render-reviewed |
| `source-daly-active-balance-manual` | [DALY Smart Active Balance BMS User Manual](../../docs/assets/electrical/smart-active-balance-bms-manual.pdf) | vendor-manual | vendor | render-reviewed |
| `source-iqload-evo-manual` | [iQLoad EVO 5 And EVO 7 Charger Manual](../../docs/assets/electrical/iqload-evo-charger-manual-en-2021.pdf) | vendor-manual | vendor | render-reviewed |
| `source-suspended-chassis-manual` | [Suspension Crawler Vehicle Technical Parameters](../../docs/assets/mechanical/suspended-tracked-vehicle-technical-parameters.pdf) | vendor-manual | vendor | render-reviewed |
| `source-chassis-expansion-note` | [Robot Chassis Expansion Design](../../docs/assets/mechanical/robot-chassis-expansion-design.txt) | project-note | generated-project-note | text-reviewed |
| `source-shaft-adapter-note` | [Faulty Shaft Adapter And Proposed Solution](../../docs/assets/mechanical/faulty-shaft-and-solution.txt) | project-note | owner-project-note | text-reviewed |
| `source-37d-mounting-geometry` | [37D Mounting Geometry Data](../../docs/assets/mechanical/37d-mounting-geometry-data.json) | data | generated-project-note | text-reviewed |
| `source-37d-safe-mounting-image` | [37D Safe Mounting Detail](../../docs/assets/mechanical/37d-safe-mounting-detail.png) | data | generated-project-note | render-reviewed |
| `source-37d-unsafe-mounting-image` | [37D Unsafe Mounting Detail](../../docs/assets/mechanical/37d-unsafe-mounting-detail.png) | data | generated-project-note | render-reviewed |

A registered source is not automatically proof that its claims apply to the
installed robot. Applicability and limitations live in the source registry;
physical qualification lives in evidence bundles.
