# US002-PROC-004: Charger Display And Configuration Identity

Version: 1

Status: Blocked until `EV-2026-001` identifies the exact charger, its exact
manual is reviewed, the manual confirms safe no-battery menu access, and the
owner separately approves mains-powered inspection.

## Goal

Observe the charger's displayed model, firmware when exposed, selected battery
chemistry program, voltage, and current settings without connecting a battery,
changing settings, or initiating charging.

## Why this is needed

A model label and family manual do not prove the selected program. Charge
voltage and available current must later be compared with exact pack, cell, and
BMS limits before any charging procedure can be considered.

## Tools and protective equipment

- Exact reviewed charger manual.
- Camera with adequate focus and lighting.
- Eye protection and a dry, nonconductive, heat-resistant work surface.
- Intact mains lead and charger output leads with individually insulated ends.

## Safe setup

Robot and battery pack physically absent from the charger connection area.
Charger output leads disconnected, separated, and insulated against contact.
Charger and mains lead visually inspected. No setting change, battery
connection, adapter improvisation, or charging load is permitted.

## Procedure

1. Record explicit owner approval and confirm all preconditions from the exact
   manual.
2. Photograph the label, lead condition, isolated output, and safe work area
   before connecting mains.
3. Connect only mains power using the manufacturer's documented sequence.
4. Navigate only read-only/default display states that the exact manual permits
   without a battery. Do not confirm, save, reset, or alter a setting.
5. Capture the displayed model or firmware, selected chemistry/program,
   voltage, current, and any status/error indication that is safely observable.
6. Disconnect mains using the documented sequence and confirm the charger is
   de-energized before handling output leads.
7. Hash originals and populate `EV-2026-002`. If any required value cannot be
   observed without changing a setting, record it as inconclusive.

## Expected result and tolerance

The display state is transcribed exactly and linked to photographs. No generic
tolerance is invented. Displayed configuration is evidence of a user setting,
not proof of output accuracy or current enforcement.

## Failure indications

Damaged leads, heat, odor, unexpected output behavior, error indication,
uncommanded setting change, inaccessible read-only display, or manual
instructions requiring a battery/load.

## Stop conditions

Disconnect mains immediately for heat, odor, smoke, noise, damaged insulation,
unexpected output behavior, an error state not covered by the exact manual, or
any uncertainty about standalone operation. Do not continue by connecting the
battery.

## How the result changes the decision

Qualified display evidence may answer the configuration portion of
`Q-US002-007` and inform `Q-US002-017`. It does not authorize charging or prove
pack compatibility.

## Evidence to retain

Approval, exact manual/source ID, safe-state photographs, label and display
photographs, verbatim transcription, operator, timestamps, outcome, stop or
failure observations, affected component/question IDs, and artifact hashes.
