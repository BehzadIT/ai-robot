# AGENTS.md

## Purpose
This directory is the canonical project documentation root for the AI robot
project.

## Instructions
- Read the relevant files in this docs tree before making changes in any related repo.
- Prefer these docs for project-wide context across mechanics, power, firmware, telemetry, Android control, and verification status.
- Treat this docs tree as the first stop for system understanding and current known conflicts.
- Keep this docs tree system-level. It may describe platform responsibilities,
  interactions, and boundaries, but implementation plans belong in child repo
  docs.
- Link to child implementation docs instead of duplicating low-level code plans
  here.
- When documenting significant changes, note the underlying best practice, design pattern, technology choice, and architectural rationale so future work has decision context.
- Document reliability, recovery, timeout, and logging behavior clearly when transport or control semantics change.
- Treat code documentation as an engineering requirement for this project: non-obvious behavior in code should be reflected either in code comments/docstrings, in this docs tree, or both.
- Prioritize documenting lifecycle, hardware ownership, fault handling, recovery behavior, timing assumptions, protocol semantics, and subsystem boundaries over obvious implementation detail.
- If information in code, manuals, or bench reality conflicts with these docs, update the docs and record unresolved issues in `verification/known-issues-and-open-questions.md`.
- Do not treat rough notes in other locations as canonical when the same topic is documented here.
- This directory lives inside the parent `ai-robot` repository. Platform code
  lives in sibling submodules at `../robot-android-app`,
  `../robot-esp32-platform`, and `../robot-pico-platform`.

## Structure Pattern Summary
- Apply one shared structural rule across robot repos: organize first by deployable project or capability boundary, then by the smallest set of technical folders that match the stack.
- For Android code, prefer `app/`, `feature/`, and `core/` as the main parent directories.
- For Pico firmware, prefer root `main.py` plus `lib/` for deployed runtime dependencies, and `src/` with `app/`, `control/`, `protocol/`, `transport/`, `platform/`, `hardware/`, and `support/` for project-owned runtime code.
- Keep cross-cutting folders narrow and intentional. Avoid generic dumping grounds such as `misc`, `utils`, `services`, or `common` unless the scope is explicit and controlled.
- Treat transport/protocol concerns as separate from control/hardware concerns.
- Preserve system ownership boundaries in both code and docs:
  - Android owns operator UI and transport lifecycle.
  - Pico owns real-time control, safety, and hardware authority.
- When documenting or reviewing structural changes, describe them in terms of:
  - project boundary
  - capability boundary
  - technical support boundary
  - ownership and safety boundary

## Key files
- `README.md`
- `overview/project-summary.md`
- `overview/system-architecture.md`
- `overview/capability-roadmap.md`
- `backlog/README.md`
- `backlog/workflow.md`
- `operations/human-agent-working-contract.md`
- `electrical/wiring-and-pinout.md`
- `verification/known-issues-and-open-questions.md`
- `reference/source-index.md`
- `reference/component-registry.yaml`
- `reference/tool-registry.yaml`
- `reference/hardware-records.md`
- `verification/questions/US-002.yaml`

For hardware, wiring, power, fabrication, or workshop procedures, use the
registries and live question queue rather than inferring availability or exact
identity from the generated BOM view. Link verified physical claims to an
append-only evidence bundle.

Use Mermaid diagrams with explicit `layout: elk` when they materially clarify
system structure, state, timing, dependencies, or wiring. Diagrams do not
replace schematics, harness drawings, measurements, or as-built evidence.
