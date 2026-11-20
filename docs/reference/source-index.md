# Source Index

This file is generated from `source-registry.yaml`. Do not edit it directly;
update the registry and run
`python3 tools/docs/validate_us002_records.py --write-indexes`.

## Repositories

- [robot-pico-platform](../../robot-pico-platform)
- [robot-esp32-platform](../../robot-esp32-platform)
- [robot-android-app](../../robot-android-app)

## Registered Sources

| ID | Source | Kind | Authority | Extraction | Retrieval |
| --- | --- | --- | --- | --- | --- |
| `source-pico-micropython-drivetrain-constants` | [Active MicroPython Drivetrain Constants](../../robot-pico-platform/src/control/drivetrain_constants.py) | code | code-backed | text-reviewed | — |
| `source-pico-cpp-drivetrain-constants` | [Migrated C++ Drivetrain Constants](../../robot-pico-platform/cpp/include/robot/control/constants.hpp) | code | code-backed | text-reviewed | — |
| `source-esp32-sdkconfig` | [ESP32 Platform SDK Configuration](../../robot-esp32-platform/sdkconfig) | code | code-backed | text-reviewed | — |
| `source-pico-2w-datasheet` | [Raspberry Pi Pico 2 W Datasheet](../../docs/assets/components/controllers/raspberry-pi-pico-2w/vendor/pico-2-w-datasheet-release-2.pdf) | vendor-manual | vendor | not-extracted | [manufacturer](https://pip-assets.raspberrypi.com/categories/1088-raspberry-pi-pico-2-w/documents/RP-008304-DS-3-pico-2-w-datasheet.pdf) (2026-11-19) |
| `source-pico-2w-pinout` | [Raspberry Pi Pico 2 W Pinout](../../docs/assets/components/controllers/raspberry-pi-pico-2w/vendor/pico-2-w-pinout-rev-1.pdf) | vendor-manual | vendor | not-extracted | [manufacturer](https://pip-assets.raspberrypi.com/categories/1088-raspberry-pi-pico-2-w/documents/RP-008305-DS-1-pico-2-w-pinout.pdf) (2026-11-19) |
| `source-pico-2w-schematic` | [Raspberry Pi Pico 2 W Schematic](../../docs/assets/components/controllers/raspberry-pi-pico-2w/vendor/pico-2-w-schematic-rev-1.pdf) | vendor-manual | vendor | not-extracted | [manufacturer](https://pip-assets.raspberrypi.com/categories/1088-raspberry-pi-pico-2-w/documents/RP-008306-DS-1-pico-2-w-schematic.pdf) (2026-11-19) |
| `source-rp2350-datasheet` | [RP2350 Microcontroller Datasheet](../../docs/assets/components/controllers/raspberry-pi-pico-2w/vendor/rp2350-datasheet-release-3.pdf) | vendor-manual | vendor | not-extracted | [manufacturer](https://pip-assets.raspberrypi.com/categories/1214-rp2350/documents/RP-008373-DS-3-rp2350-datasheet.pdf) (2026-11-19) |
| `source-rp2350-hardware-design` | [Hardware Design With RP2350](../../docs/assets/components/controllers/raspberry-pi-pico-2w/vendor/rp2350-hardware-design-release-3.pdf) | vendor-manual | vendor | not-extracted | [manufacturer](https://pip-assets.raspberrypi.com/categories/1214-rp2350/documents/RP-008280-DS-2-hardware-design-with-rp2350.pdf) (2026-11-19) |
| `source-esp32-series-datasheet` | [ESP32 Series Datasheet](../../docs/assets/components/controllers/esp32-development-board/vendor/esp32-series-datasheet-v5.3.pdf) | vendor-manual | vendor | not-extracted | [manufacturer](https://documentation.espressif.com/esp32_datasheet_en.pdf) (2026-11-19) |
| `source-esp32-hardware-design-guidelines` | [ESP32 Hardware Design Guidelines HTML Snapshot](../../docs/assets/components/controllers/esp32-development-board/vendor/esp32-hardware-design-guidelines-v1.9.md) | vendor-web-page | vendor | not-extracted | [manufacturer](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/index.html) (2026-11-19) |
| `source-cytron-mdd10a-manual` | [Cytron MDD10A Dual Channel Motor Driver User Manual](../../docs/assets/components/interfaces/cytron-mdd10a-motor-driver/vendor/cytron-mdd10a-user-manual-v2.0.pdf) | vendor-manual | vendor | not-extracted | [manufacturer-controlled](https://docs.google.com/document/d/1ol8nICCTTw5dAHHE_hju08cCVH2GN5_Y3cGC6B4Gbas/export?format=pdf) (2026-11-19) |
| `source-pololu-37d-vendor-datasheet` | [Pololu 37D Metal Gearmotors Datasheet](../../docs/assets/components/actuators/pololu-37d-gearmotors/vendor/pololu-37d-metal-gearmotors-rev-1.2.pdf) | vendor-manual | vendor | not-extracted | [manufacturer](https://www.pololu.com/file/0J1736/pololu%E2%80%9037d%E2%80%90metal%E2%80%90gearmotors%E2%80%90rev%E2%80%901%E2%80%902.pdf) (2026-11-19) |
| `source-vl53l0x-datasheet` | [ST VL53L0X Time-of-Flight Sensor Datasheet](../../docs/assets/components/sensors/vl53l0x/vendor/st-vl53l0x-datasheet-rev-6.pdf) | vendor-manual | vendor | not-extracted | [distributor-mirror](https://www.hestore.hu/prod_getfile.php?id=18866) (2026-11-19) |
| `source-vl53l0x-api-manual` | [ST VL53L0X API User Manual](../../docs/assets/components/sensors/vl53l0x/vendor/st-vl53l0x-api-user-manual-rev-2.pdf) | vendor-manual | vendor | not-extracted | [distributor-mirror](https://www.pololu.com/file/0J1508/VL53L0X-UM2309.pdf) (2026-11-19) |
| `source-project-components-updated` | [Robot Project Components Reference](../../docs/assets/reference/robot-project-components-updated.pdf) | project-pdf | generated-project-note | render-reviewed | — |
| `source-complete-component-list` | [Exhaustively Complete Component List](../../docs/assets/reference/robot-project-complete-component-list.txt) | project-note | generated-project-note | text-reviewed | — |
| `source-pololu-37d-project-note` | [Pololu 37D Encoder Specification And RPM Test Note](../../docs/assets/reference/pololu-37d-encoder-spec-and-rpm-test-code.txt) | project-note | owner-project-note | text-reviewed | — |
| `source-battery-system-note` | [Robot Battery System Component Reference](../../docs/assets/electrical/robot-battery-system.txt) | project-note | owner-project-note | text-reviewed | — |
| `source-wiring-reference` | [Robot Wiring Reference](../../docs/assets/electrical/wiring-reference.txt) | project-note | owner-project-note | text-reviewed | — |
| `source-motor-wire-photo` | [Motor Wire Connector Diagram](../../docs/assets/electrical/motor-wire.jpg) | photo | unknown | render-reviewed | — |
| `source-goldencell-18650-spec` | [JGCFR18650 2200 mAh 3.2 V Cell Specification](../../docs/assets/components/power/lifepo4-battery-pack/vendor/candidate-jgcfr18650-cell-specification-r1.1.pdf) | vendor-manual | vendor | render-reviewed | — |
| `source-daly-active-balance-manual` | [DALY Smart Active Balance BMS User Manual](../../docs/assets/components/power/daly-bms/vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf) | vendor-manual | vendor | render-reviewed | — |
| `source-iqload-evo-manual` | [iQLoad EVO 5 And EVO 7 Charger Manual](../../docs/assets/components/power/panther-iqload-evo-charger/vendor/iqload-evo-5-and-7-manual-2021.pdf) | vendor-manual | vendor | render-reviewed | — |
| `source-suspended-chassis-manual` | [Suspension Crawler Vehicle Technical Parameters](../../docs/assets/components/mechanical/tracked-chassis/vendor/suspension-crawler-technical-parameters.pdf) | vendor-manual | vendor | render-reviewed | — |
| `source-chassis-expansion-note` | [Robot Chassis Expansion Design](../../docs/assets/mechanical/robot-chassis-expansion-design.txt) | project-note | generated-project-note | text-reviewed | — |
| `source-shaft-adapter-note` | [Faulty Shaft Adapter And Proposed Solution](../../docs/assets/mechanical/faulty-shaft-and-solution.txt) | project-note | owner-project-note | text-reviewed | — |
| `source-37d-mounting-geometry` | [37D Mounting Geometry Data](../../docs/assets/mechanical/37d-mounting-geometry-data.json) | data | generated-project-note | text-reviewed | — |
| `source-37d-safe-mounting-image` | [37D Safe Mounting Detail](../../docs/assets/mechanical/37d-safe-mounting-detail.png) | data | generated-project-note | render-reviewed | — |
| `source-37d-unsafe-mounting-image` | [37D Unsafe Mounting Detail](../../docs/assets/mechanical/37d-unsafe-mounting-detail.png) | data | generated-project-note | render-reviewed | — |

A registered source is not automatically proof that its claims apply to the
installed robot. Applicability and limitations live in the source registry;
physical qualification lives in evidence bundles.
