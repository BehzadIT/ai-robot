# BOM And Parts Status

This file is generated from `component-registry.yaml` and `tool-registry.yaml`.
Do not edit it directly; update the registries and run
`python3 tools/docs/validate_us002_records.py --write-indexes`.

States describe evidence strength, not desired target architecture. Follow each
record's questions and claim provenance before relying on a hardware fact.

## Components

| ID | Name | Category | Identity | Installation | Functional |
| --- | --- | --- | --- | --- | --- |
| `component-raspberry-pi-pico-2w-01` | Raspberry Pi Pico 2 W | controller | owner-reported | owner-reported | implemented |
| `component-esp32-dev-board-01` | ESP32 development board | controller | unknown | owner-reported | implemented |
| `component-pololu-37d-motors-01` | Pololu 37D 30:1 gearmotors with encoders | actuator | owner-reported | owner-reported | owner-reported |
| `component-cytron-mdd10a-01` | Cytron MDD10A dual-channel motor driver | interface | owner-reported | owner-reported | owner-reported |
| `component-lifepo4-pack-01` | 4S2P LiFePO4 battery pack | power | owner-reported | owner-reported | owner-reported |
| `component-daly-bms-01` | Installed DALY-family BMS | power | conflicting | owner-reported | owner-reported |
| `component-panther-iqload-evo-charger-01` | Panther iQLoad EVO charger | power | owner-reported | not-applicable | owner-reported |
| `component-tracked-chassis-01` | Double-layer suspension crawler chassis | mechanical | documented-unverified | owner-reported | owner-reported |
| `component-xbox-compatible-controller-01` | Xbox-compatible game controller | interface | unknown | not-applicable | owner-reported |
| `component-hcsr04-sensors-01` | HC-SR04 ultrasonic sensors | sensor | documented-unverified | unknown | not-tested |
| `component-vl53l0x-sensors-01` | VL53L0X time-of-flight sensor modules | sensor | documented-unverified | unknown | not-tested |
| `component-dyp-a02-sensor-01` | DYP-A02-V2.0 waterproof ultrasonic sensor | sensor | documented-unverified | unknown | not-tested |
| `component-legacy-520-motors-01` | Legacy 520 encoder DC gearmotors | actuator | documented-unverified | legacy | unknown |
| `component-power-protection-01` | Power fuse, disconnect, switch, connectors, and high-current wiring | power | suspected-missing | unknown | unknown |
| `component-prototyping-stock-01` | Electronics prototyping stock | consumable | documented-unverified | not-applicable | not-tested |
| `component-wire-cable-stock-01` | Low-voltage wire and cable stock | consumable | documented-unverified | not-applicable | not-tested |
| `component-connector-stock-01` | Connector and test-clip stock | consumable | documented-unverified | not-applicable | not-tested |
| `component-fastener-stock-01` | Fastener, spacer, and washer stock | mechanical | documented-unverified | not-applicable | not-tested |
| `component-sheet-material-stock-01` | Sheet, plate, and foam material stock | mechanical | documented-unverified | not-applicable | not-tested |
| `component-insulation-adhesive-stock-01` | Insulation, tape, and heat-shrink stock | consumable | documented-unverified | not-applicable | not-tested |
| `component-solder-consumables-01` | Soldering consumables | consumable | documented-unverified | not-applicable | not-tested |
| `component-battery-construction-stock-01` | Battery-construction material stock | consumable | documented-unverified | not-applicable | not-tested |
| `component-pololu-shaft-adapter-01` | Candidate Pololu 6 mm D-shaft to 12 mm hex adapter | mechanical | documented-unverified | unknown | not-tested |
| `component-pololu-motor-brackets-01` | Pololu aluminum motor brackets | mechanical | documented-unverified | unknown | not-tested |

## Workshop Tools

| ID | Name | Category | Availability | Condition |
| --- | --- | --- | --- | --- |
| `tool-peaktech-3350-01` | PeakTech 3350 digital multimeter | measurement | unknown | needs-check |
| `tool-ruzizao-bench-supply-01` | RUZIZAO adjustable bench power supply | measurement | unknown | needs-check |
| `tool-yihua-898bd-01` | Yihua 898BD soldering and hot-air station | electronics-assembly | unknown | needs-check |
| `tool-icrimp-micro-connector-01` | iCRIMP micro-connector crimping tool | electronics-assembly | unknown | needs-check |
| `tool-wiha-side-cutters-01` | Wiha electronic side cutters | hand-tool | unknown | needs-check |
| `tool-bosch-pliers-set-01` | Bosch professional pliers set | hand-tool | unknown | needs-check |
| `tool-yurinwoo-cutting-disc-set-01` | YURINWOO cutting-disc set | fabrication | unknown | needs-check |
| `tool-baer-tap-drill-set-01` | Baer tap and drill set | fabrication | unknown | needs-check |
| `tool-professional-file-set-01` | Professional file set | fabrication | unknown | needs-check |
| `tool-newaner-protractor-01` | Newaner 360-degree digital protractor | measurement | unknown | needs-check |
| `tool-oregon-face-shield-01` | Oregon polycarbonate face shield | safety | unknown | needs-check |
| `tool-workholding-unknown-01` | Workshop vise, clamps, and sacrificial backing | workholding | unknown | unknown |
| `tool-waveform-instrument-unknown-01` | Oscilloscope or logic analyzer | measurement | unknown | unknown |
| `tool-enventor-wrench-set-01` | Enventor ratcheting wrench set | hand-tool | unknown | needs-check |
