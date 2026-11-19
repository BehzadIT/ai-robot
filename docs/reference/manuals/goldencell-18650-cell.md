# Goldencell JGCFR18650 Cell Specification

Source: `source-goldencell-18650-spec`, revision `R1.1`.

## Project-relevant facts

- Model scope: `18FC-7.04Wh` / `JGCFR18650-2200mAh-3.2V` (cover and section 2).
- Nominal capacity: 2,200 mAh; minimum 2,100 mAh (section 6, items 1-2).
- Nominal voltage: 3.2 V (section 6, item 3).
- Maximum charge current: 1.1 A at 25 °C (section 6, item 5).
- Documented fast continuous discharge current: 2.2 A, with pack-level use
  constrained by construction and a 60 °C temperature limit (section 6, item
  6).
- Standard charge: 0.5 C constant current to 3.65 V, then constant voltage to
  0.01 C cutoff (section 7.1).

## Applicability limit

These limits must not be applied to the robot pack until `Q-US002-018` proves
the installed cells match this model and revision. A 2P arrangement does not by
itself prove compatibility with the candidate charger's possible 5 A output.
