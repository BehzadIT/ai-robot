---
id: US-001
title: System Roadmap And Human-Agent Workflow
status: done
priority: high
risk_class: normal
owner: parent-workspace
created: "2026-11-19"
updated: "2026-11-19"
completed: "2026-11-19"
dependencies: []
references:
  - docs/overview/system-architecture.md
  - docs/operations/human-agent-working-contract.md
evidence:
  - docs/verification/change-log.md
diagram: not-needed
---
# US-001: System Roadmap And Human-Agent Workflow

## Implementation Outcome

Completed on 2026-11-19 as a parent-documentation change. The implemented
artifacts are:

- component-oriented system model:
  `../../overview/system-architecture.md`;
- capability horizons and durable roadmap questions:
  `../../overview/capability-roadmap.md`;
- active backlog lifecycle, risk, Ready/Done, decision, and traceability rules:
  `../workflow.md`;
- active owner profile, collaboration rules, physical approval boundaries, and
  minimum evidence expectations:
  `../../operations/human-agent-working-contract.md`;
- shared claim vocabulary: `../../reference/glossary.md`.

The previous architecture path remains as a compatibility link for
independently released child repositories. The detailed agentic workflow stays
deferred as an enhancement plan; its baseline rules are active through the
artifacts above.

US-002 remains responsible for component/tool registries and structured
evidence. US-003 remains responsible for toolchain, device-discovery, and
automated verification interfaces. Neither is hidden inside this story's
completion.

## User Story

As the robot's owner and future collaborator, I want a structured system model,
capability roadmap, and human-agent working contract so that humans and agents
understand what the robot is, why each subsystem exists, what is implemented,
and how future decisions should be made and verified.

## Why This Story Existed

At refinement time, the workspace already contained unusually strong subsystem
boundaries and a useful deferred agentic workflow. It did not yet provide one
active backlog model that connected:

- project purpose;
- present implementation;
- target architecture;
- long-range capabilities;
- engineering decisions;
- implementation work;
- verification evidence;
- known-good integrated states.

This matters because a robot can evolve over years. A locally attractive
software, firmware, or hardware decision can make later autonomy, sensing,
diagnostics, serviceability, or safety work unnecessarily difficult. Future
direction must influence decisions without allowing speculative plans to be
described as current behavior.

## Current Project Context

### Current system

- Android is the operator client and currently sends operator intent to the
  Pico network endpoint.
- ESP32 currently bridges Pico telemetry and forwards normalized controller
  snapshots.
- Pico owns command admission, motor output, encoders, stale-input behavior,
  recovery, timing-sensitive control, and final safety authority.
- The active MicroPython path and staged C++ paths coexist.
- The clean-start target moves wireless gateway duties to ESP32 and treats the
  Pico 2 W as a no-network control computer.

### Durable ownership boundary

| Subsystem | Owns | Must not silently acquire |
| --- | --- | --- |
| Android | Operator experience, app state, client connection lifecycle | Motor authority, safety policy, drivetrain mixing |
| ESP32 | Wi-Fi, WebSocket gateway, controller connectivity, normalization, diagnostics, bounded transport | Final command admission, motor control, timing-critical safety |
| Pico | Command admission, freshness, control state, encoders, PID, watchdog, motors, stop/recover authority | Operator UI or public wireless service in the clean-start target |
| Parent workspace | Architecture, shared protocols, hardware truth, verification expectations, integrated snapshots | Platform implementation detail that belongs in a child repository |

Moving one of these boundaries requires an explicit architecture decision,
updated shared documentation, migration and compatibility analysis, and
verification appropriate to the resulting risk.

## Fact And Planning Vocabulary

Every meaningful claim in this backlog and related documentation should use one
of these states.

| State | Meaning |
| --- | --- |
| `Bench verified` | Confirmed on the physical system with retained evidence |
| `Software verified` | Confirmed by an automated or repeatable software check, but not necessarily on hardware |
| `Owner reported` | Supplied by the owner and useful, but not independently verified |
| `Documented / unverified` | Present in a project source but not reconciled with code or hardware |
| `Implemented` | Exists in code; runtime or physical qualification may still be outstanding |
| `Planned` | Approved target direction, not current behavior |
| `Explore` | A possibility worth retaining without architectural commitment |
| `Conflicting` | Two or more credible sources disagree |
| `Suspected missing` | Evidence suggests a fact or component exists, but it is absent from canonical context |
| `Unknown` | Required information has not been established |

An agent must not promote a claim between these states without recording the
reason and supporting source or evidence ID.

## Human-Agent Working Model

### Owner capability profile

The owner is a senior software and AI engineer. Agents may assume expert-level
fluency in:

- software architecture and engineering;
- AI/ML and agentic systems;
- APIs, distributed systems, automation, tests, and delivery workflows;
- reading and modifying complex application code.

The owner has useful general engineering knowledge but is actively developing
depth in:

- MCU and embedded-runtime constraints;
- real-time firmware and hardware interfaces;
- electronics, power, grounding, and signal integrity;
- schematics, datasheets, and electrical measurement;
- mechanical fabrication, loading, tolerance, and material selection.

This is a communication preference and planning input, not a limit on what the
owner may do.

### Communication contract

Agents should:

- communicate software and AI decisions at a senior-engineer level;
- define unfamiliar embedded, electrical, and mechanical terminology in plain
  language when it first affects a decision;
- explain the physical reason for a decision, not only the convention;
- state likely failure modes, severity, and observable symptoms;
- distinguish facts, assumptions, hypotheses, and recommendations;
- relate unfamiliar concepts to software concepts when helpful, while noting
  where the analogy stops being accurate;
- give expected measurements, tolerances, and stop conditions for bench work;
- explain why a selected tool is suitable and where its accuracy or capability
  is insufficient;
- avoid condescension and avoid re-teaching routine software concepts.

For physical procedures, use this minimum structure:

```text
Goal
Why this is needed
Tools and protective equipment
Safe setup
Procedure
Expected result and tolerance
Failure indications
Stop conditions
How the result changes the decision
Evidence to retain
```

### Agent-by-default behavior

Within the authority granted by a task, agents should independently:

- inspect relevant parent and child documentation before proposing changes;
- inspect code, configuration, build targets, and connected-device state;
- use available safe tools instead of delegating routine observations;
- run builds, host tests, static checks, and read-only device diagnostics;
- capture exact commands, logs, versions, and outcomes;
- ask the owner only for facts or physical actions that cannot be discovered
  safely from the workspace;
- hand off explicit unverified items rather than implying completion.

Agents require owner participation or explicit approval before:

- first power-on after wiring or power-path changes;
- flashing firmware that changes motion, watchdog, stop, encoder, or actuator
  behavior;
- enabling motor output;
- running tracks on the ground;
- changing BMS, charger, or battery configuration;
- operating a fabrication tool when setup, workholding, or safe use is not
  established.

The durable owner profile and detailed working contract now live in
`../../operations/human-agent-working-contract.md`. Agent entry points should stay
short and link to it while retaining concise ownership and physical-safety
boundaries.

## Semantic System Model

Every deployable component or major capability should be described with the
following fields:

| Field | Required meaning |
| --- | --- |
| Identity | Stable name and repository or hardware boundary |
| Purpose | User or system outcome it exists to provide |
| Current behavior | Implementation fact, including limitations |
| Target behavior | Approved direction, clearly separated from current behavior |
| Ownership | Decisions and state this component authoritatively owns |
| Non-responsibilities | Behavior that must remain elsewhere |
| Interfaces | Inputs, outputs, timing, protocol, electrical, and mechanical dependencies |
| Failure behavior | Safe state, timeout, recovery, and observability |
| Maturity | Planned, implemented, software verified, or bench verified |
| Evidence | Tests, logs, photos, measurements, and evidence IDs |
| Evolution triggers | Conditions that justify replacement or architectural change |

This model should be applied to Android, ESP32, Pico control, power, drivetrain,
encoders, operator transport, telemetry, controller transport, and every future
sensor or autonomous capability.

## Capability Roadmap

The roadmap uses capability horizons rather than unreliable calendar promises.

### Now: reliable control foundation

- Complete a reliable Pico C++ no-network runtime baseline.
- Stabilize the ESP32 gateway shape without transferring safety authority.
- Resolve control-critical hardware identity and wiring conflicts.
- Activate minimum risk classification and evidence requirements during the
  migration rather than waiting until after it.
- Establish the component, tool, evidence, and integrated-snapshot contracts in
  `US-002` and `US-003`.

### Next: integrated and observable teleoperation

- Add bounded, validated ESP32-to-Pico command transport.
- Restore drivetrain, encoder, watchdog, stop, and recover parity in safe
  slices.
- Route Android operator intent through ESP32.
- Add structured gateway and Pico control diagnostics.
- Qualify disconnect, stale input, malformed command, reconnect, and log
  backpressure behavior.

### Later: reproducible sensing and platform capabilities

- Admit sensors only after exact variants, electrical interfaces, mounting,
  calibration, and failure behavior are documented.
- Add reproducible integrated releases containing software, hardware,
  calibration, and evidence identities.
- Add richer replay, simulation, hardware-in-the-loop, and maintenance
  diagnostics.
- Establish data capture and perception foundations without coupling them
  directly to actuator authority.

### Explore: autonomy and physical AI

- Obstacle avoidance, mapping, localization, and autonomous navigation.
- Edge inference and perception-assisted operator control.
- Dataset capture, simulation-to-real workflows, and learned policies.
- Additional mechanical capabilities or manipulation.

Exploratory autonomy may propose bounded operator-like intent. Pico must retain
freshness, admission, manual override, fault handling, and final motion
authority unless a future safety review intentionally changes that design.

## Engineering Decision Framework

For significant low-level, high-level, or hardware decisions, record:

1. Desired capability and current constraint.
2. Owning subsystem and affected safety boundary.
3. Options considered, including retaining the current design.
4. Available tools, skills, parts, and verification paths.
5. Tradeoffs across:
   - safety and fault containment;
   - determinism, latency, and bandwidth;
   - power, memory, CPU, and physical constraints;
   - observability and recovery;
   - toolchain and ecosystem maturity;
   - reversibility and migration cost;
   - solo-maintainer complexity;
   - future capability compatibility.
6. Selected option and explicit non-goals.
7. Evidence required to keep or overturn the decision.

Do not choose an architecture solely because an agent can generate its code
quickly. Prefer designs that make failures observable and verification
repeatable.

## Canonical Backlog Lifecycle

US-004 later simplified the original lifecycle while preserving its risk,
evidence, and traceability intent. The active contract is `../workflow.md`:

```text
Draft -> Ready -> In Progress -> Done
          \-> Blocked
Any active state -> Deferred
```

| State | Exit requirement |
| --- | --- |
| `Draft` | Stable ID, user story, and initial outcome exist |
| `Ready` | Interactive refinement is complete and the Definition of Ready is satisfied |
| `In Progress` | Implementation, testing, review, device work, and evidence collection own the work |
| `Blocked` | Blocking fact, owner, and unblock condition are explicit |
| `Done` | Definition of Done and acceptance criteria are satisfied |
| `Deferred` | Reason and reactivation trigger are recorded |

Refinement and verification remain required activities; they are not separate
status columns for this solo project.

### Definition of Ready

- The user or system outcome is clear.
- Current and desired behavior are separated.
- The owning subsystem and affected boundaries are identified.
- Risk is classified as tiny, normal, safety/control, or future autonomy.
- Known conflicts and owner questions are recorded.
- Dependencies and non-goals are explicit.
- Available components and tools have been considered.
- Acceptance criteria and evidence depth are defined.
- Required human approvals and physical interventions are known.

### Definition of Done

- Implementation matches the approved ownership boundary.
- Relevant builds, tests, lint, and static checks pass.
- Required runtime, device, and bench evidence is retained.
- Failure, stop, recovery, and degraded behavior are verified when relevant.
- Shared docs and platform docs agree with implementation.
- Remaining uncertainty is recorded rather than hidden.
- Reusable lessons become tests, checklists, instructions, or decisions.
- A known-good integrated snapshot is recorded when system behavior changed.

## Interactive Discovery And Owner Questions

Before asking the owner, an agent must inspect the relevant docs, code,
configuration, assets, Git history, and connected-device information available
within the task. Remaining questions should be grouped and prioritized.

Each question should contain:

```yaml
id: Q-<story>-<number>
topic: short stable topic
known_context: what the workspace already establishes
question: the smallest answerable missing decision or fact
reason: why the answer changes planning or verification
impact: safety | compatibility | architecture | documentation
preferred_evidence: text | photo | label | manual | measurement | observation
status: open | answered-owner-reported | verified | no-longer-needed
```

Typical roadmap questions include:

- Is a mentioned capability installed, owned as inventory, or only desired?
- Is a future sensor a committed platform capability or an experiment?
- Which long-range behaviors matter most: teleoperation, diagnostics,
  obstacle avoidance, mapping, autonomous navigation, or manipulation?
- Is a constraint intentional, or only a temporary consequence of current
  hardware or migration state?

Unknowns should block only the dependent decision. They should not stop
unrelated documentation, tests, or software work.

### Owner Input Transferred To The Capability Roadmap

These questions remain intentionally unanswered, but no longer keep this
foundational story open. Their canonical location is
`../../overview/capability-roadmap.md`; the table below is retained as historical
story context.

| ID | Question | Why it matters | Preferred answer | Status |
| --- | --- | --- | --- | --- |
| `Q-US001-001` | After reliable teleoperation, which outcomes matter most: obstacle avoidance, mapping/localization, autonomous navigation, perception/edge AI, manipulation, or another capability? | Establishes capability priority without treating every owned sensor as planned integration | Ranked goals plus any important use case | `Transferred` |
| `Q-US001-002` | Is the robot primarily a long-running personal learning platform, a future product/research platform, or both? | Changes acceptable process weight, modularity, reproducibility, and hardware investment | Owner description | `Transferred` |
| `Q-US001-003` | Which physical environments should the future robot operate in: indoor bench/floor, outdoor terrain, remote operation, or others? | Affects chassis, sensing, ingress protection, communications, and safety decisions | Environments and expected constraints | `Transferred` |
| `Q-US001-004` | Which present constraints are known temporary compromises that should not shape the long-term architecture? | Prevents migration artifacts and available spare parts from becoming accidental strategy | List of temporary compromises | `Transferred` |

## Traceability Contract

Every implementation slice should be traceable through:

```text
capability/backlog ID
  -> implementation issue or task
  -> architecture decision when required
  -> child-repository commits
  -> automated checks
  -> evidence IDs
  -> parent integrated snapshot
```

GitHub issues may track execution, but this Markdown story retains product
intent, architectural rationale, lifecycle definitions, and completion rules.

## Completed Implementation Stages

1. Adopted the claim vocabulary and backlog lifecycle for meaningful new work.
2. Mapped existing plans into capability horizons without rewriting their
   platform implementation content.
3. Reconciled the canonical current/target architecture model while preserving
   a compatibility link for independently released child docs.
4. Created and linked the focused human-agent working contract.
5. Left integrated evidence/snapshot schema to US-002 and US-003.
6. Retained workflow pilots and regression-task-bank work as deferred
   enhancements rather than prerequisites for this foundation.

## Acceptance Criteria

- A new collaborator can state the purpose, owner, current state, target state,
  and safety boundary of Android, ESP32, and Pico without reading source code.
- Future capabilities are visible without being confused with implemented
  behavior.
- Hardware and tooling availability influence architecture decisions.
- Owner questions contain context and do not repeat discoverable facts.
- Agent explanations match the owner's software expertise while making
  embedded, electrical, and mechanical reasoning accessible.
- No motion, power, wiring, protocol, or ownership change can reach `Ready`
  without an evidence plan.
- `Done` cannot mean only "code was written" or "firmware compiled."

## External Evidence And Practices

Only sources active or published inside the six-month research window were used
for the initial comparison.

| Source | Recent evidence | Practice adopted | Applicability limit |
| --- | --- | --- | --- |
| [PX4-Autopilot](https://github.com/PX4/PX4-Autopilot) | Pushed 2026-11-17; approximately 13.1k stars when reviewed | Thin agent entry point, path-scoped guidance, tracked build/review skills, simulation-to-hardware test ladder | Much larger contributor base and flight-safety scope |
| [ArduPilot](https://github.com/ArduPilot/ardupilot) | Pushed 2026-11-15; approximately 16.4k stars | Evidence-bearing PRs, SITL/autotest, board builds, subsystem-focused changes | Project governance is heavier than this solo workspace needs |
| [Zephyr contributor expectations](https://docs.zephyrproject.org/latest/contribute/contributor_expectations.html) | Current documentation reviewed 2026-11-19 | Small logical changes, RFCs for large work, explicit tested/not-tested statements, regression tests | RTOS platform practices must be scaled down for one robot |
| [LeRobot](https://github.com/huggingface/lerobot) | Active September 2026; approximately 29k stars | Explicit AI policy, human accountability, hardware-aware guidance, tiered CI | Primarily high-level robotics/ML rather than control-critical firmware |
| [Microsoft Physical AI Toolchain](https://github.com/microsoft/physical-ai-toolchain) | Current in November 2026 | Capability tiers and acceptance-gated simulate/train/evaluate/deploy workflows | Enterprise/cloud stack is not a baseline requirement here |
| [RoboParty RP1](https://github.com/Roboparty/RP1) | Current in November 2026; approximately 1.2k stars | Clear repositories for hardware, firmware, test, deployment, and learning | Young project; useful structure, not yet a mature process authority |

## Remaining Risks

- Formal agent evaluation remains deferred until repeated failures justify a
  regression bank; the lightweight workflow and skills are active.
- Long-range goals have not yet been prioritized by the owner.
- Integrated software versions are represented by submodule pointers, but
  hardware, calibration, and evidence identity are not yet part of the same
  snapshot.
- A large documentation system could become overhead; implementation should
  preserve lightweight handling for tiny, low-risk changes.
