# Evidence Bundles

Create one new `EV-YYYY-NNN/` directory per run. Copy the templates from
`_template/`, record raw artifacts and their SHA-256 values, then run:

```text
python3 tools/docs/validate_us002_records.py
```

Never edit or delete a completed evidence bundle to describe a later build or
observation. Create a new ID and link the superseded run. The optional
`--base-ref` validation rejects modifications, deletion, or renames of existing
`EV-*` directories relative to an integration base.

An owner statement is recorded as a human observation, not an instrument
measurement. A build pass is not physical qualification.
