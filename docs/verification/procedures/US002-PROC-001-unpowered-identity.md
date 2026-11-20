# US002-PROC-001: Non-Energizing Identity And Overview Capture

Version: 3

## Goal

Identify all required component packs and externally visible control, power,
sensor, interface, and mechanical hardware without applying energy or
interacting with an unverified energized region. Do not disconnect sampling
leads, open the battery pack, or move unsafe wiring.

## Why this is needed

Exact labels determine which manuals, ratings, connectors, and procedures may
apply. Visual similarity is insufficient.

## Tools and protective equipment

- Camera with adequate focus and lighting.
- Eye protection when working around the assembled chassis.
- Nonconductive pointer or labels; do not place metal tools across terminals.

## Safe setup

This is a visual-only, non-energizing inspection. Disconnect every known
external source without manipulating unidentified wiring: charger from mains
and pack, USB cables, and bench supplies. Keep tracks stationary and protect
already accessible exposed terminals.

If safe battery isolation was established before this procedure, record how it
was established and preserve that state. Opening a switch or disconnect does
not by itself prove de-energization. If isolation of the installed pack or
high-current path is unknown, treat that region as energized and inaccessible:
do not touch it, move wiring, remove covers, position the camera inside it, or
approach exposed conductors. Capture only a safe-distance overview and record
the detailed views as blocked. Do not alter an unknown BMS sampling harness.

## Procedure

1. Capture a full robot overview and the power/control layout before touching
   anything.
2. Capture front, rear, connector, module, and label views of the Pico, ESP32,
   Cytron driver, Xbox-compatible controller, BMS, and charger where safely
   visible.
3. Capture separate label, gearbox, encoder, connector, and installed views of
   both current Pololu motors and any available legacy 520 motors.
4. Capture front, rear, connector, interface-label, and packaging views of each
   HC-SR04, VL53L0X, and DYP-A02 module. Keep distinct variants separate.
5. If verified safe isolation permits close visual access, capture the battery
   exterior, visible markings, insulation, accessible interconnect context, and
   temperature-sensor leads without opening or unwrapping the pack. Otherwise
   retain only a safe-distance overview and mark the close views blocked. Add
   purchase, construction, or pre-wrap records if they already exist.
6. Capture chassis labels and overview, the candidate shaft adapter, and motor
   brackets with packaging or purchase identifiers where available. Do not
   remove installed parts solely for photography.
7. Capture fuse, switch, disconnect, regulators, connectors, conductor
   markings, and visible cable routing only where the safe setup permits it,
   without moving a connection. Unknown isolation, exposed conductors, or a
   need to approach the high-current path blocks the close view. A photograph
   does not prove continuity, de-energization, or disconnect function.
8. Retain purchase records or order-history screenshots as separate original
   artifacts and state whether they are tied to the photographed item.
9. Transcribe only text that is legible in a retained photograph or record.
10. Hash originals, create annotated derivatives separately, and populate
    `EV-2026-001` with all affected component and question IDs.

## Expected result and tolerance

Each of the sixteen required component packs has legible identity evidence, a
clearly labelled documentary fallback, or an explicit unresolved result. No
electrical tolerance applies.

## Failure indications

Unclear labels, unknown isolation, inaccessible hardware, damaged insulation,
swollen or hot battery components, exposed conductors, or a need to dismantle
the pack.

## Stop conditions

Stop immediately for heat, odor, swelling, damaged high-current wiring,
unexpected power indication, inability to maintain safe distance, or any need
to disturb an unidentified battery or BMS connection. Unknown isolation blocks
close inspection; it is not permission to test a switch or move a lead.

## How the result changes the decision

Legible exact identity permits selecting exact manuals, splitting independently
rated products, and designing later unpowered checks. It does not prove hidden
wiring or authorize powered work.

## Evidence to retain

Original and annotated photos, purchase/construction records supplied for the
run, transcription, operator, time, safe-state confirmation, affected
component/question IDs, and file hashes. Suggested artifact groups are
`overview`, `controllers`, `drivetrain`, `power`, `sensors`, `mechanical`, and
`purchase-records`; filenames identify the component and view.

## Change log

- Version 2 expands the capture from primary control/power hardware to all
  required component packs and fixes the evidence destination as
  `EV-2026-001`.
- Version 3 reclassifies the work as non-energizing visual inspection and makes
  unknown battery/high-current isolation a blocking condition for close views.
