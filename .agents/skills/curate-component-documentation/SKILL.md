---
name: curate-component-documentation
description: Create or revise an AI-robot component README from registered PDF or HTML vendor sources, with project-relevant coverage, precise locators, and uncertainty preserved. Use for component-source curation; do not use merely to download sources or qualify physical hardware.
---

# Curate Component Documentation

Produce the smallest component README that answers likely robot decisions while
remaining traceable to original sources.

## Before Curation

Read the component record, mapped source records, open US-002 questions, the
existing component documentation, and the
[component documentation contract](../../../docs/reference/component-documentation-contract.md).
Verify every source path and SHA-256. Stop if a source is missing or changed;
registration and acquisition are separate work.

Read [the source-review method](references/source-review-method.md) before
reviewing a PDF or retained HTML source. Start from
[the component README template](assets/component-readme-template.md) when creating a
new pack.

## Required Outcome

- Keep vendor statements, project configuration, physical evidence, open
  questions, and inference visibly separate.
- Retain only decision-relevant facts and cite their exact registered source
  page or section.
- Preserve variant, revision, operating conditions, units, tolerances, and
  whether a value is absolute, recommended, nominal, or measured.
- State when a family or chip source cannot establish board, carrier, or
  installed-product behavior.
- Update reviewed source hashes and coverage honestly; use `curated` only when
  the repository contract permits it.
- Run the US-002 validator and documentation tests after editing.

Source review never verifies physical identity, wiring, condition, settings, or
behavior. Do not close evidence questions without the required evidence bundle.
