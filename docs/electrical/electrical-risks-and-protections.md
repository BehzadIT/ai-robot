# Electrical Risks And Protections

## Purpose
Capture electrical hazards and protection assumptions that matter during development.

## Current status
- `From vendor/project files`: battery, charger, and BMS impose real safety constraints.
- `Needs verification`: final pack assembly details and protection settings of the installed BMS.

## Key risks
- Reversed BMS wiring can damage the BMS.
- Encoder supply assumptions may be invalid if the installed motor/encoder variant does not tolerate 3.3 V operation.
- Motor stall current can far exceed normal current draw and must be considered in wiring, protection, and thermal expectations.
- Charger behavior must be verified against the actual LiFePO4 mode and the current pack.

## Protections and rules
- Follow the BMS wiring order from the manual.
- Use common ground discipline between control and driver subsystems.
- Treat battery charging as a controlled procedure, not a background convenience action.
- Validate pack voltage and BMS identity before integrating any battery telemetry features.

## Sources
- Manual/source file: [DALY smart active-balance BMS manual](../assets/components/power/daly-bms/vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf)
- Manual/source file: [candidate JGCFR18650 cell specification](../assets/components/power/lifepo4-battery-pack/vendor/candidate-jgcfr18650-cell-specification-r1.1.pdf)
- Manual/source file: [iQLoad EVO 5 and 7 manual](../assets/components/power/panther-iqload-evo-charger/vendor/iqload-evo-5-and-7-manual-2021.pdf)
