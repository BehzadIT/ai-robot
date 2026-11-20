# Component Curation Audit

Snapshot: 2026-11-20

This matrix separates review of currently registered sources from evidence that
identifies the physical product. `Curated` describes documentation coverage; it
does not promote physical identity.

| Component | Current vendor sources | Current-source action | Identity or exact-source gate |
| --- | ---: | --- | --- |
| Raspberry Pi Pico 2 W | 5 | Curated board and supporting RP2350 scope | Photograph installed board and headers; harness remains separate evidence |
| ESP32 development board | 2 | Curated classic-ESP32 family scope | Exact board, module, USB bridge, and regulator markings |
| Pololu 37D gearmotors | 1 | Curated 37D family scope | Both order numbers, gearbox, and encoder variants |
| Cytron MDD10A | 1 | Curated Rev 2.0 scope | Installed board revision |
| LiFePO4 battery pack | 1 | Curated candidate-cell scope | Construction/purchase record tied to installed cells; never unwrap solely for identity |
| DALY BMS | 1 | Curated family scope | Full label, series/current rating, connectors, and accessory identity |
| Panther iQLoad EVO charger | 1 | Curated EVO 5/7 family scope | Exact label first; displayed program requires separate no-battery procedure |
| Tracked chassis | 1 | Curated retained chassis scope | Installed chassis revision and modifications |
| Xbox-compatible controller | 0 | Keep stub | Exact label/model and official support source |
| HC-SR04 modules | 0 | Keep stub | Supplier/board markings and evidence that both modules are homogeneous |
| VL53L0X module | 2 | Curated bare-sensor/API scope | Carrier manufacturer, regulator, level shifting, pinout, and cover |
| DYP-A02 | 0 | Keep stub | Exact interface variant and manufacturer source |
| Legacy 520 motors | 1 shared | Curated only legacy data in chassis source | Physical availability and exact motor markings |
| Power protection/distribution | 0 | Keep assembly documentation partial | Visible fuse, disconnect, switch, regulator, connectors, conductor markings, and routing |
| Pololu shaft adapter | 0 | Keep stub | Physical/product identity and purchase record |
| Pololu motor brackets | 0 | Keep stub | Exact bracket product and availability |

## Reconciliation notes

- The former `docs/reference/manuals/` summaries for the DALY BMS, candidate
  Goldencell cell, and iQLoad charger were rechecked against their retained
  PDFs, merged into the owning component packs, and removed as a duplicate
  documentation layer.
- The retained VL53L0X API manual is UM2039 Rev 1 from June 2016, not Rev 2;
  its filename, source metadata, links, and reviewed hash now agree.
- The iQLoad family manual does not unambiguously establish a 14.6 V LiFePO4
  termination value. The previous registry claim was removed, and charging
  remains blocked pending exact charger, program, cell, pack, and BMS evidence.

## Split rule

When evidence identifies an independently rated, replaceable cell, fuse,
disconnect, switch, regulator, or other power product, create a product record
and documentation pack. Link it from the pack or power-path assembly using
`member_component_ids`. If supposedly homogeneous motor or sensor instances
prove different, create per-variant member records rather than normalizing the
difference.

## Completion rule

Every required pack is processed. A pack becomes `curated` only when all mapped
sources are reviewed at their registered hashes, applicable coverage is
complete, and retained facts have exact locators. Missing identity or an exact
authoritative source remains an explicit `partial`/`stub` future activation
condition, not a global development blocker.
