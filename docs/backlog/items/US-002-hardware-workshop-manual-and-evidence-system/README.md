---
id: US-002
title: Hardware, Workshop, Manuals, And Evidence
status: in-progress
priority: high
risk_class: safety-control
owner: parent-workspace
created: "2026-11-19"
updated: "2026-11-19"
dependencies: [{id: US-001, kind: blocks}]
references: [docs/reference/component-registry.yaml, docs/reference/tool-registry.yaml, docs/verification/questions/US-002.yaml]
diagrams: [{path: diagrams/information-flow.mmd, kind: data-flow}]
---
# US-002: Hardware, Workshop, Manuals, And Evidence

## User Story
As the robot builder, I want components, tools, manuals, and physical evidence catalogued so proposed work is feasible, safe, and traceable.

## Acceptance Criteria
- **AC-001:** Component and tool records distinguish identity, availability, condition, and confidence.
- **AC-002:** Physical claims use append-only evidence and unresolved facts remain explicit.
- **AC-003:** Relevant manuals and safe measurement procedures are discoverable.

## Current Status
Registry foundations exist; connected-hardware identification and qualification remain in progress. See [implementation-plan.md](implementation-plan.md) and the [historical record](materials/legacy-story-record.md).
