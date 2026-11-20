# Hardware And Workshop Record Maintenance

## Purpose

Keep component, tool, source, question, and evidence records consistent without
turning a project note or owner statement into stronger proof than it is.

## Adding or updating hardware

1. Search existing IDs and aliases before adding a record.
2. Reuse the stable ID when identity becomes more precise; update fields and
   retain aliases rather than replacing the ID.
3. Set identity, inventory, installation, connection, and functional state
   independently.
4. Add decision-relevant facts as claims with a source locator, evidence ID, or
   dated owner report.
5. Add or link a question when an unresolved fact affects safety,
   compatibility, procedure, or documentation.
6. Set `documentation_requirement`. Use `required` for distinct products that
   are installed, available, safety-relevant, or repeatedly decision-relevant;
   use `conditional` for mixed stock until an exact product affects a decision.
7. Put a required component's canonical documentation and vendor sources in its
   category/product pack under `docs/assets/components/`.
8. Regenerate the BOM/source/component views and validate all records.

Unknown exact identity is valid. A guessed manufacturer or variant is not.
An open question records where evidence would matter; it is dormant until a
story decision depends on it. Do not launch bulk inspection or measurement to
clear the registry. The dependent story requests the minimum useful owner input
just in time, retains the evidence, and updates these records.

When an assembly contains independently rated, replaceable products whose
limits affect a decision, give those products their own stable component
records and documentation packs. Link them from the assembly with
`member_component_ids`. Keep the assembly record for system topology and
as-built context; do not map a product-specific manual only to the assembly.

## Sources and owner reports

Register a durable source once with its path, SHA-256, applicability, and
limitations. Cite page, section, code symbol, photograph, or measurement point
on each claim. A family manual is not an exact product identity.

For material acquired from the web, record the exact retrieval URL, retrieval
date, and host type. Prefer the manufacturer host. A vendor-authored document
retained from a distributor mirror remains vendor-authored, but its retrieval
record and limitations must disclose the mirror. HTML-only vendor documentation
may be retained as a source-faithful Markdown snapshot; do not present format
conversion as project analysis.

PDFs stay binary and use `not-extracted` until a later review explicitly
creates page- or section-linked claims. Downloading or registering a manual does
not by itself qualify its applicability to installed hardware.

Vendor manuals, datasheets, and source-faithful HTML snapshots live in the
matching component pack's `vendor/` directory. Project wiring, configuration,
measurements, CAD, and as-built artifacts remain in their owning electrical,
mechanical, reference, or evidence areas and are linked from the documentation.

The component documentation contract is in
[`component-documentation-contract.md`](component-documentation-contract.md).
Use the repository `curate-component-documentation` skill for later source review.
Until that review occurs, keep the documentation `stub` or `partial`, leave reviewed
source hashes empty, and do not imply that a navigational source list is a
curated summary.

Owner input is useful and is recorded as `owner-reported`. Physical labels,
continuity, voltage, behavior, and condition require a new evidence bundle when
they materially affect a decision.

## Evidence and supersession

Copy the evidence templates into a new `EV-YYYY-NNN` directory. Retain original
artifacts, store annotations as derivatives, and record hashes. Never edit a
completed bundle to match a later build; create a new bundle and link what it
supersedes.

As-built revisions follow the same rule. A logical schematic may describe the
intended design but cannot qualify a physical connection.

## Validation

Install the pinned documentation dependencies, then run:

```text
python3 -m pip install -r requirements-docs.txt
python3 tools/docs/validate_us002_records.py --write-indexes
python3 tools/docs/validate_us002_records.py --base-ref HEAD
python3 -m unittest discover -s tools/docs/tests -v
```

Use the real integration base rather than `HEAD` for the append-only check in a
review or CI environment.
