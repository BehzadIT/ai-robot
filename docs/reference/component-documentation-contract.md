# Component Documentation Contract

## Purpose

Give humans and agents a small, decision-relevant entry point for each
documented product without replacing the registered vendor sources or claiming
that a manual qualifies installed hardware.

## Authority Layers

1. `component-registry.yaml` owns inventory, identity state, claims, and
   provenance.
2. The component pack `README.md` is the canonical human/agent documentation.
3. Files in the component pack's `vendor/` directory preserve original vendor
   material.
4. Project wiring, configuration, measurements, CAD, and as-built records stay
   in their owning documentation areas and are linked from the documentation.
5. Physical observations require append-only evidence; source review cannot
   promote a physical state.

## Documentation Requirement

- `required`: a distinct product or aggregate is installed, available,
  safety-relevant, or repeatedly decision-relevant and needs component
  documentation.
- `conditional`: a mixed-stock record needs no documentation until an exact product's
  material or rating affects a decision. Create a distinct component record at
  that point.
- `not-required`: documentation would not improve a foreseeable decision.

An assembly may link independently rated product records through
`member_component_ids`. Exact cell, fuse, disconnect, switch, regulator, or
other product manuals belong to the product record; the assembly documentation
owns topology and integration context.

## Documentation Status

- `stub`: routing, current uncertainty, and sources may be listed, but no source
  review is claimed.
- `partial`: useful project context or some source review exists, with visible
  coverage gaps.
- `curated`: every applicable coverage category is covered and every registered
  vendor source mapped to the component has been reviewed at its current hash.

Coverage means the documentation accurately reports what is known or unresolved. It
does not mean the physical identity, connection, condition, or behavior has
been verified.

## Progressive Qualification

Unresolved component questions are durable routing context, not a queue that
must be cleared before development continues. A `stub`, `partial` pack, unknown
physical identity, or open question blocks only a story decision that actually
depends on the missing fact.

When a story needs an exact physical property, activate the relevant question
inside that story, request only the smallest useful observation or measurement,
retain the result with story evidence, and update this component pack and the
registries. Do not run broad inventory or measurement campaigns merely to make
the catalog look complete. Safety gates still apply immediately before work
that depends on an unverified power, motion, fabrication, or protection fact.

## Citation Format

Use the registered source ID in every decision-relevant source citation:

```markdown
[source-example, PDF p. 17, §3.3](vendor/example-datasheet-r2.pdf#page=17)
[source-example-html, §Power Supply](vendor/example-guide.md#power-supply)
```

PDF page numbers are the one-based PDF-viewer page index used by `#page=`. If
the document's printed page differs, include both. HTML snapshots use a stable
heading anchor. A source list without reviewed locators is navigation, not
curation.

## Curation Boundary

Text extraction and OCR may locate candidate passages. Retained numerical,
safety, pinout, dimensional, configuration, or compatibility claims require
inspection of the rendered page or source section, including tables, diagrams,
conditions, and footnotes. Keep absolute maxima distinct from recommended
operation, retain units and test conditions, and label family or candidate
applicability.

Do not copy the complete manual into Markdown. Summarize only information that
answers a current or foreseeable robot decision, and direct agents to the
original when the documentation does not answer it.

## Agent Reading Order

1. Open the generated component catalog.
2. Open the component documentation.
3. Check registry identity state, claims, and unresolved questions.
4. Open cited source pages or sections.
5. Search or read the complete source only when the documentation is insufficient.

Use `.agents/skills/curate-component-documentation/` when creating or revising
curated component documentation.
