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
6. Add a dossier only for installed, safety-relevant, or repeatedly
   decision-relevant items.
7. Regenerate the BOM/source views and validate all records.

Unknown exact identity is valid. A guessed manufacturer or variant is not.

## Sources and owner reports

Register a durable source once with its path, SHA-256, applicability, and
limitations. Cite page, section, code symbol, photograph, or measurement point
on each claim. A family manual is not an exact product identity.

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
