# Electrical As-Built Revisions

An as-built revision records physical observations; it is separate from the
logical design schematic. Create `HW-YYYY-NNN/` only after an evidence bundle
supports the first connection or identity claim.

Each revision contains:

- `metadata.yaml` with revision status and applicable component/harness IDs;
- `connections.yaml` with connector, pin, net, voltage-domain, color/gauge,
  termination, and evidence references;
- `README.md` summarizing deviations from the design;
- links to evidence photographs rather than duplicated uncontrolled images.

Revisions are superseded, not silently rewritten. Unknown wire gauge, color,
or connector identity remains `unknown`.
