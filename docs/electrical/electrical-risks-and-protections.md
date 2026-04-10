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
- Manual/source file: [Smart Active Balance BMS manual.pdf](../../robot-pico-platform/docs/Smart%20Active%20Balance%20BMS%20manual.pdf)
- Manual/source file: [JGCFR18650-2200mAh-3.2V_18FC-7.04Wh_specification_.pdf](../../robot-pico-platform/docs/JGCFR18650-2200mAh-3.2V_18FC-7.04Wh_specification_.pdf)
- Manual/source file: [Anleitung_iQLoadEVO_EN_2021.pdf](../../robot-pico-platform/docs/Anleitung_iQLoadEVO_EN_2021.pdf)
