# Component Documentation Catalog

This file is generated from the component and source registries plus documentation
front matter. Do not edit it directly; update those records and run
`python3 tools/docs/validate_us002_records.py --write-indexes`.

Read the component documentation first, then its registry state and unresolved
questions. Open cited source pages next and the complete vendor source only
when the documentation is insufficient.

## Coverage Summary

- Registered components: 24
- Documentation requirement: 16 required, 8 conditional, 0 not required
- Documentation: 10 curated, 1 partial, 5 stub, 0 missing required
- Conditional registry records without documentation: 8

Coverage reports documented decision areas, not physical qualification.

## Components

| ID | Component | Category | Identity | Requirement | Documentation | Coverage | Sources | Open questions |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| `component-raspberry-pi-pico-2w-01` | [Raspberry Pi Pico 2 W](controllers/raspberry-pi-pico-2w/README.md) | controller | owner-reported | required | curated | 8/8 | 5 | `Q-US002-003`, `Q-US002-016` |
| `component-esp32-dev-board-01` | [ESP32 development board](controllers/esp32-development-board/README.md) | controller | unknown | required | curated | 8/8 | 2 | `Q-US002-004` |
| `component-pololu-37d-motors-01` | [Pololu 37D 30:1 gearmotors with encoders](actuators/pololu-37d-gearmotors/README.md) | actuator | owner-reported | required | curated | 8/8 | 1 | `Q-US002-002`, `Q-US002-003`, `Q-US002-005` |
| `component-cytron-mdd10a-01` | [Cytron MDD10A dual-channel motor driver](interfaces/cytron-mdd10a-motor-driver/README.md) | interface | owner-reported | required | curated | 8/8 | 1 | `Q-US002-005`, `Q-US002-006`, `Q-US002-016` |
| `component-lifepo4-pack-01` | [4S2P LiFePO4 battery pack](power/lifepo4-battery-pack/README.md) | power | owner-reported | required | curated | 7/7 | 1 | `Q-US002-006`, `Q-US002-017`, `Q-US002-018`, `Q-US002-019` |
| `component-daly-bms-01` | [Installed DALY-family BMS](power/daly-bms/README.md) | power | conflicting | required | curated | 8/8 | 1 | `Q-US002-001`, `Q-US002-006`, `Q-US002-017` |
| `component-panther-iqload-evo-charger-01` | [Panther iQLoad EVO charger](power/panther-iqload-evo-charger/README.md) | power | owner-reported | required | curated | 7/7 | 1 | `Q-US002-007`, `Q-US002-014`, `Q-US002-017` |
| `component-tracked-chassis-01` | [Double-layer suspension crawler chassis](mechanical/tracked-chassis/README.md) | mechanical | documented-unverified | required | curated | 5/5 | 1 | `Q-US002-012`, `Q-US002-013` |
| `component-xbox-compatible-controller-01` | [Xbox-compatible game controller](interfaces/xbox-compatible-controller/README.md) | interface | unknown | required | stub | 0/8 | 0 | — |
| `component-hcsr04-sensors-01` | [HC-SR04 ultrasonic sensors](sensors/hc-sr04/README.md) | sensor | documented-unverified | required | stub | 0/8 | 0 | `Q-US002-020` |
| `component-vl53l0x-sensors-01` | [VL53L0X time-of-flight sensor modules](sensors/vl53l0x/README.md) | sensor | documented-unverified | required | curated | 8/8 | 2 | `Q-US002-020` |
| `component-dyp-a02-sensor-01` | [DYP-A02-V2.0 waterproof ultrasonic sensor](sensors/dyp-a02/README.md) | sensor | documented-unverified | required | stub | 0/8 | 0 | `Q-US002-020` |
| `component-legacy-520-motors-01` | [Legacy 520 encoder DC gearmotors](actuators/legacy-520-gearmotors/README.md) | actuator | documented-unverified | required | curated | 8/8 | 1 | — |
| `component-power-protection-01` | [Power fuse, disconnect, switch, connectors, and high-current wiring](power/power-protection-and-distribution/README.md) | power | suspected-missing | required | partial | 0/6 | 0 | `Q-US002-006`, `Q-US002-019` |
| `component-prototyping-stock-01` | Electronics prototyping stock | consumable | documented-unverified | conditional | conditional | — | 0 | `Q-US002-013` |
| `component-wire-cable-stock-01` | Low-voltage wire and cable stock | consumable | documented-unverified | conditional | conditional | — | 0 | `Q-US002-013` |
| `component-connector-stock-01` | Connector and test-clip stock | consumable | documented-unverified | conditional | conditional | — | 0 | `Q-US002-013` |
| `component-fastener-stock-01` | Fastener, spacer, and washer stock | mechanical | documented-unverified | conditional | conditional | — | 0 | `Q-US002-013` |
| `component-sheet-material-stock-01` | Sheet, plate, and foam material stock | mechanical | documented-unverified | conditional | conditional | — | 0 | `Q-US002-013`, `Q-US002-014` |
| `component-insulation-adhesive-stock-01` | Insulation, tape, and heat-shrink stock | consumable | documented-unverified | conditional | conditional | — | 0 | `Q-US002-013` |
| `component-solder-consumables-01` | Soldering consumables | consumable | documented-unverified | conditional | conditional | — | 0 | `Q-US002-010`, `Q-US002-013`, `Q-US002-014` |
| `component-battery-construction-stock-01` | Battery-construction material stock | consumable | documented-unverified | conditional | conditional | — | 0 | `Q-US002-013`, `Q-US002-014`, `Q-US002-015` |
| `component-pololu-shaft-adapter-01` | [Candidate Pololu 6 mm D-shaft to 12 mm hex adapter](mechanical/pololu-shaft-adapter/README.md) | mechanical | documented-unverified | required | stub | 0/5 | 0 | `Q-US002-012`, `Q-US002-013`, `Q-US002-014` |
| `component-pololu-motor-brackets-01` | [Pololu aluminum motor brackets](mechanical/pololu-motor-brackets/README.md) | mechanical | documented-unverified | required | stub | 0/5 | 0 | `Q-US002-013` |
