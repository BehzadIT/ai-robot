---
id: US-003
title: Agentic Toolchain, Devices, And Verification Loop
status: in-progress
priority: high
risk_class: normal
owner: parent-plus-platform-adapters
created: "2026-11-19"
updated: "2026-11-19"
dependencies: [{id: US-001, kind: blocks}, {id: US-002, kind: informs}]
references: [docs/operations/agentic-toolchain.md, docs/reference/scenario-registry.yaml]
diagrams: [{path: diagrams/verification-loop.mmd, kind: system-context}]
---
# US-003: Agentic Toolchain, Devices, And Verification Loop

## User Story
As an agent-assisted developer, I want repository-owned discovery, build, flash, monitor, test, and evidence interfaces so feedback loops are safe and reproducible.

## Acceptance Criteria
- **AC-001:** Host verification and platform adapters return structured results.
- **AC-002:** Device and physical operations fail closed at explicit approval gates.
- **AC-003:** Connected-device, HIL, bench, and motion claims require matching evidence depth.

## Current Status
Host contracts and adapters exist; connected-device scenarios remain. See [implementation-plan.md](implementation-plan.md) and [historical record](materials/legacy-story-record.md).
