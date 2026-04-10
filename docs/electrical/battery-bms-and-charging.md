# Battery BMS And Charging

## Purpose
Document the battery pack, BMS family, and charging constraints that future work must respect.

## Current status
- `From project files`: battery pack is documented as `4S2P LiFePO4`, `12.8 V nominal`, `4.4 Ah`.
- `Conflict`: two different BMS descriptions appear in the source material.
- `From manual / project files`: charger is Panther iQLoad EVO 5 and is intended for LiFePO4 charging.

## Battery pack
- Chemistry: LiFePO4
- Cell count: `8 x 18650`
- Configuration: `4S2P`
- Nominal pack voltage: `12.8 V`
- Pack capacity: `4.4 Ah`

## BMS
Two BMS identities appear in project material:
- DALY Smart BMS `4S 12V 30A`
- DALY Smart Active Balance `R24TK1A-17S100A`, `4-8S`

Do not write software against the BMS UART protocol until the actual installed BMS is bench-confirmed.

## Charging
- Charger family: Panther iQLoad EVO 5
- Intended use: LiFePO4 charge mode for the 4S pack
- Verify actual charge termination voltage on the bench before unattended charging

## Sources
- Source file: [Robot battery system.txt](../../robot-pico-platform/docs/Robot%20battery%20system.txt)
- Manual/source file: [JGCFR18650-2200mAh-3.2V_18FC-7.04Wh_specification_.pdf](../../robot-pico-platform/docs/JGCFR18650-2200mAh-3.2V_18FC-7.04Wh_specification_.pdf)
- Manual/source file: [Smart Active Balance BMS manual.pdf](../../robot-pico-platform/docs/Smart%20Active%20Balance%20BMS%20manual.pdf)
- Manual/source file: [Anleitung_iQLoadEVO_EN_2021.pdf](../../robot-pico-platform/docs/Anleitung_iQLoadEVO_EN_2021.pdf)
