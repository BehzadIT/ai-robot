# Source Review Method

## Build the Information Need

Start with the component's role, current identity state, safety constraints,
known failure modes, software links, and open questions. Mark each standard
coverage category as applicable or not applicable before searching sources.

Add the relevant category overlay:

- Power: chemistry, topology, charge/discharge limits, temperature, protection,
  balancing, connection order, and fault behavior.
- Controllers: supply rails, GPIO constraints, boot behavior, USB/UART, RF,
  flash, clocks, and board-versus-chip limits.
- Actuators: voltage, no-load and stall current, torque-speed data, encoder,
  thermal limits, duty cycle, and mounting.
- Sensors: supply and logic levels, range, field of view, accuracy conditions,
  timing, calibration, address behavior, and carrier differences.
- Interfaces and drivers: control modes, truth tables, thresholds, current,
  switching, protection, and fault indication.
- Mechanical products: dimensions, materials, load paths, fastening,
  tolerances, clearances, and environment.
- Consumables: chemistry, substrates, cure, temperature, dielectric behavior,
  shelf life, PPE, preparation, and removal.

## Review Sources

1. Use the table of contents, PDF text, or HTML search to locate candidate
   sections. OCR is navigation only.
2. Keep a temporary fact ledger with claim, source ID, locator, variant scope,
   conditions, and robot relevance.
3. Visually inspect every retained PDF page. Check table headings, diagrams,
   notes, footnotes, units, and nearby conditions.
4. Compare revisions and sources. Record conflicts rather than selecting the
   convenient value.
5. Include a fact only when it changes a safety, compatibility, configuration,
   diagnostic, mechanical, replacement, or open-question decision.

Do not reproduce large tables. Retain the subset needed for the robot and link
the original page for the rest.

## Quality Gate

Before setting `curated`, confirm:

- every applicable coverage field is `covered`;
- no registered vendor source mapped to the component is unreviewed;
- reviewed hashes equal the source registry;
- every important number has a locator, units, conditions, and value class;
- absolute limits are not operating targets;
- family, chip, board, carrier, and installed-product scope are distinct;
- open questions remain open unless their required evidence exists;
- project-specific wiring and measurements link to their owning records;
- the component documentation says when the original source must be opened.

If any condition fails, use `partial` and name the gap.
