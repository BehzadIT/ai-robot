---
id: US-002
title: Hardware, Workshop, Manuals, And Evidence
status: done
priority: high
risk_class: safety-control
owner: parent-workspace
created: "2026-11-19"
updated: "2026-11-20"
completed: "2026-11-20"
dependencies: [{id: US-001, kind: blocks}]
references: [docs/reference/component-registry.yaml, docs/reference/tool-registry.yaml, docs/verification/questions/US-002.yaml]
evidence: [docs/assets/components/README.md, docs/reference/source-index.md, tools/docs/validate_us002_records.py, tools/docs/tests/test_validate_us002_records.py]
diagrams: [{path: diagrams/information-flow.mmd, kind: data-flow}]
---
# US-002: Hardware, Workshop, Manuals, And Evidence

## User Story
As the robot builder, I want components, tools, manuals, and physical evidence catalogued so proposed work is feasible, safe, and traceable.

## Acceptance Criteria
- **AC-001:** Component and tool records distinguish identity, availability, condition, and confidence.
- **AC-002:** Physical claims use append-only evidence and unresolved facts remain explicit.
- **AC-003:** Relevant manuals and safe measurement procedures are discoverable.
- **AC-004:** Decision-relevant products use category/product documentation
  packs with registered vendor sources and machine-countable coverage.
- **AC-005:** Component documentation preserves uncertainty and uses exact source
  locators when later curated.
- **AC-006:** Agents follow the component catalog and documentation before opening a
  complete manual.

## Current Status
Registry foundations and the component-documentation curation system are
complete, and all currently registered vendor sources have been curated. Six
packs remain `stub` or `partial` because no exact source is registered yet.
Those and other physical unknowns are dormant context, not standing blockers;
future stories activate only the facts their decisions need and reconcile the
result here. See
[implementation-plan.md](implementation-plan.md) and the
[historical record](materials/legacy-story-record.md).

No bulk owner inspection is required. When a future story needs physical
identity evidence, it may activate the reusable
[non-energizing capture procedure](../../../verification/procedures/US002-PROC-001-unpowered-identity.md).
Charger display inspection remains an operation-specific gate under
[`US002-PROC-004`](../../../verification/procedures/US002-PROC-004-charger-display-identity.md),
not a blocker for unrelated development.
