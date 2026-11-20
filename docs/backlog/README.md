# Product Backlog

This is the human and agent front door. Add an idea by copying the
[story definition template](templates/story/README.md) into a new
`items/US-NNN-slug/` directory. Then use `refine-story`, `plan-story`,
`execute-story`, and `review-story` in that order as needed. The precise gates,
examples, and file ownership rules are in [workflow.md](workflow.md).

![Draft to Done lifecycle](diagrams/story-lifecycle.svg)

Common requests: `Refine US-NNN interactively`; `Plan US-NNN`; `Execute
US-NNN`; `Review US-NNN for readiness`.

Only the section between the markers below is generated. Edit the rest normally.

<!-- BEGIN GENERATED STORY INDEX -->
### Ready

| ID | Title | Priority | Dependencies |
| --- | --- | --- | --- |
| `US-006` | [Migrate ESP32 Platform To ESP-IDF 6.1.1](items/US-006-migrate-esp32-platform-to-esp-idf-6-1-1/README.md) | high | US-002 (informs), US-003 (informs) |

### In Progress

| ID | Title | Priority | Dependencies |
| --- | --- | --- | --- |
| `US-003` | [Agentic Toolchain, Devices, And Verification Loop](items/US-003-agentic-toolchain-device-and-verification-loop/README.md) | high | US-001 (blocks), US-002 (informs) |

### Done

| ID | Title | Priority | Dependencies |
| --- | --- | --- | --- |
| `US-001` | [System Roadmap And Human-Agent Workflow](items/US-001-system-roadmap-and-human-agent-workflow/README.md) | high | — |
| `US-002` | [Hardware, Workshop, Manuals, And Evidence](items/US-002-hardware-workshop-manual-and-evidence-system/README.md) | high | US-001 (blocks) |
| `US-004` | [Lightweight Agentic Development Harness](items/US-004-lightweight-agentic-development-harness/README.md) | high | US-001 (blocks), US-002 (informs), US-003 (informs) |
| `US-005` | [Directory-Based Story Dossiers And Deterministic Engineering Plans](items/US-005-directory-story-dossiers/README.md) | high | US-004 (blocks) |
<!-- END GENERATED STORY INDEX -->
