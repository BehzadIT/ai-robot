# Agentic Development Workflow

## Current status
- `Status`: Deferred until the Pico C++ migration and ESP32 gateway clean-start
  path are complete enough to validate the workflow against real tasks.
- `Priority`: Planned / post-migration.
- `Owner`: Parent `ai-robot` workspace.
- `Scope`: Agentic development workflow, verification depth, context usage, and durable learning.
- `Current task`: Preserve a proposed operating model to revisit after the C++
  migration stabilizes.

## Purpose
This document is a deferred workflow-improvement plan for how AI agents and
humans should work inside the AI robot project after the current Pico C++
migration and ESP32 gateway clean-start work have stabilized.

The goal is not to add heavy process. The goal is to make future robot work
safer, clearer, and faster by using the right amount of specification, context,
verification, and durable learning for the project's actual scale.

This document is self-contained. A future agent should be able to use it without
reading the separate `agentic-workspace` research repository.

Until the C++ migration is complete, treat this document as guidance, not as a
required operating model. The immediate project priority is reliable firmware
architecture: ESP32 as wireless gateway and Pico as no-network real-time
control authority.

## Project scale classification
The AI robot project is currently:
- solo-developed;
- multi-repository;
- multi-platform;
- physical-system work;
- safety-sensitive around motion, power, wiring, and control authority;
- likely to grow later with edge AI, perception, and autonomy.

That combination needs a different balance than either a small toy app or a
large engineering organization.

The sweet spot is:

```text
lightweight process for normal code
+ strict evidence for hardware, control, protocol, safety, and integration work
+ selective durable learning
+ no formal evaluation platform until repeated agent workflow failures justify it
```

## Goal
Future robot work should be easy to start, hard to mis-scope, and clear to hand
off.

A future agent or human should be able to:
- classify the task risk before editing;
- load the right project context without wandering through unrelated files;
- choose the right specification depth;
- preserve Pico, ESP32, Android, and parent-doc ownership boundaries;
- know what verification evidence is expected;
- record unresolved hardware or implementation uncertainty;
- promote only valuable lessons into durable project memory.

## Success criteria
This workflow task is successful when:
- future agents start from the parent docs and nearest repo `AGENTS.md`;
- normal tasks use small task notes instead of long generated plans;
- cross-repo, protocol, hardware, and control changes use stronger specs;
- safety and control changes include explicit failure modes and bench evidence;
- handoffs say what changed, what was verified, what was not run, and what still
  needs hardware confirmation;
- repeated mistakes become tests, checklists, docs, or instructions instead of
  repeated chat history;
- the project does not adopt heavy context packaging or formal eval tooling
  before the scale justifies it.

## Core ownership rule
Preserve the current system boundary unless the architecture docs are
intentionally updated in the same change.

- Android owns operator UI, app state, and client transport lifecycle.
- ESP32 owns telemetry bridging, controller connectivity, controller
  normalization, diagnostics, and transport support.
- Pico owns real-time control, safety behavior, motor authority, encoders,
  command admission, stale-input stop behavior, and timing-sensitive hardware
  interaction.
- Parent docs own shared architecture, protocols, hardware facts, operations,
  verification expectations, and known cross-project decisions.

Do not move control or safety authority from the Pico to Android or ESP32 unless
that is the explicit purpose of the task and the shared architecture docs are
updated with the tradeoff.

## Five recommendations

### 1. Context engineering: keep context layered and navigational
Use the parent repository as the shared system context and child repositories as
platform implementation context.

Start with:
- `../../README.md`
- `../../AGENTS.md`
- `../README.md`
- `../overview/project-summary.md`
- `../overview/current-architecture.md`
- `../overview/design-decisions.md`
- `../verification/known-issues-and-open-questions.md`

Then read the nearest child repo `AGENTS.md` and relevant child repo docs for
platform-specific implementation work.

Keep `AGENTS.md` files short and navigational. Put durable detail in docs,
tests, code comments, or checklists.

Avoid wasting context on:
- build directories;
- vendored third-party source unless the task explicitly touches it;
- generated files;
- type stubs;
- old experiments unless the task is explicitly exploratory.

### 2. Spec-driven work: use the smallest useful spec
Small changes need small specs. Risky changes need stronger specs.

Use a tiny task note when:
- the change is local;
- behavior is already clear;
- no hardware, protocol, or ownership boundary changes.

Use a normal change spec when:
- the change crosses repos or modules;
- command or telemetry behavior changes;
- Android, ESP32, and Pico expectations need to stay aligned;
- docs and implementation must move together.

Use a safety/control spec when:
- Pico control behavior changes;
- stale-command, disconnect, recovery, watchdog, PID, encoder, motor, or
  actuator behavior changes;
- wiring, power, battery, BMS, charger, or pinout assumptions change;
- future autonomy or perception output can influence robot motion.

### 3. Harness engineering: invest most in evidence
For this project, the highest-leverage agentic development work is verification
and handoff, not a larger prompt system.

Expected evidence should match risk:
- static checks: build, unit tests, lint, typecheck, compile checks;
- runtime checks: local execution, protocol tests, transport tests, serial logs,
  emulator/device checks;
- bench checks: observed robot behavior, continuity checks, voltage
  measurements, photos, boot logs, stop behavior, hardware labels;
- system checks: parent docs updated, submodule state understood, unresolved
  questions recorded.

Done means the required evidence exists or the missing evidence is explicitly
called out.

### 4. Compound engineering: preserve only valuable lessons
Do not preserve every observation. Preserve lessons that are likely to recur or
expensive to relearn.

Use this rule of thumb:

| Lesson shape | Preserve as |
| --- | --- |
| Exact bug | Regression test |
| Repeated implementation pattern | Platform doc or solution note |
| Broad project convention | `AGENTS.md` or parent operations doc |
| Repeated review concern | Checklist |
| Safety-critical issue | Test, guardrail, bench checklist, or approval note |
| Architectural tradeoff | `docs/overview/design-decisions.md` |
| Hardware uncertainty | `docs/verification/known-issues-and-open-questions.md` |
| Integrated system state | Parent submodule pointer and change log |

Prefer executable memory where practical. A test or checklist that catches a
future mistake is stronger than prose alone.

### 5. Evaluation-driven development: stay lightweight for now
Do not introduce a formal evaluation platform yet.

For the current solo project, evaluation should start as a small task bank only
after repeated agent workflow failures appear. Good candidates are tasks where
agents repeatedly:
- miss the Pico control authority boundary;
- confuse intended architecture with current implementation;
- ignore known hardware uncertainty;
- update platform code without updating shared docs;
- fail to produce useful verification evidence.

Formal evals become more useful when:
- multiple people or agents work on the project;
- autonomy or perception enters the control path;
- agent behavior becomes inconsistent enough to measure;
- prompt, model, context, or harness changes need comparison across repeated
  tasks.

## Task sizing rules

### Tiny task
Use for local documentation edits, obvious code cleanup, or small tests.

Expected artifact:
- short task note or final handoff only.

Expected evidence:
- relevant focused check if code changed;
- documentation review if docs changed.

### Normal task
Use for non-trivial platform changes that do not alter safety authority.

Expected artifact:
- concise spec with intent, boundary, files, evidence, and non-goals.

Expected evidence:
- platform build or tests;
- relevant protocol or docs review;
- handoff with unverified items.

### Safety/control task
Use for Pico control, hardware, power, wiring, or robot motion behavior.

Expected artifact:
- safety/control spec.

Expected evidence:
- static and runtime checks where possible;
- bench evidence when hardware behavior is involved;
- explicit stop/fault/recovery behavior;
- unresolved assumptions recorded in verification docs.

### Future autonomy task
Use when perception, edge AI, or autonomy can influence motion.

Expected artifact:
- safety/control spec plus autonomy-specific risk review.

Expected evidence:
- clear separation between perception confidence and motion authority;
- bounded command admission into Pico-owned control;
- failure modes for stale, low-confidence, or contradictory perception;
- manual override and stop behavior.

## Evidence matrix

| Task type | Required evidence |
| --- | --- |
| Parent docs only | Link check by inspection, consistency with architecture and known issues |
| Android UI or operator model | Gradle tests when relevant, command protocol check, operator docs update |
| Android transport | Transport/protocol test or manual connection evidence, command protocol check |
| ESP32 telemetry bridge | ESP-IDF build, telemetry protocol check, bridge diagnostics evidence |
| ESP32 controller transport | ESP-IDF build, controller snapshot/transport evidence, Pico authority preserved |
| Pico protocol parsing | Unit/host tests where available, command protocol update, malformed-input behavior |
| Pico control behavior | Unit/host tests, bench stop/recovery evidence, safety behavior documented |
| Pico C++ migration | Host CTest, firmware build when relevant, migration parity docs update |
| Wiring, pinout, battery, BMS, charger | Bench measurement, photo/manual/source evidence, known issues update |
| Integrated robot state | Child repo commits complete, parent submodule pointer update only when known-good |

## Agent working flow
For meaningful work, follow this flow:

1. Orient from parent docs and nearest repo `AGENTS.md`.
2. Classify the task as tiny, normal, safety/control, or future autonomy.
3. State the subsystem boundary being preserved or changed.
4. Write the smallest useful spec for the task class.
5. Edit only the owning repo or docs layer.
6. Run the evidence path that matches the task risk.
7. Update shared docs when protocol, wiring, safety behavior, or subsystem
   boundaries change.
8. Record unresolved facts in known issues instead of smoothing them over.
9. Leave a handoff with changed scope, verification, skipped checks, and
   remaining risk.
10. Run a short compound learning pass if the task exposed a reusable lesson.

## Task templates

### Tiny task note
```md
## Intent

## Boundary
- Affects:
- Does not affect:

## Evidence
- Required:
- Not required because:
```

### Normal cross-repo change spec
```md
## Intent

## Current behavior

## Desired behavior

## Ownership boundary
- Android:
- ESP32:
- Pico:
- Parent docs:

## Non-goals

## Expected evidence
- Static:
- Runtime:
- Docs:
- Handoff:
```

### Safety/control change spec
```md
## Intent

## Safety boundary
- Pico authority preserved or intentionally changed:
- Motion, motor, encoder, watchdog, or stop behavior affected:

## Failure modes
- Disconnect:
- Stale input:
- Malformed command:
- Hardware mismatch:
- Recovery:

## Bench assumptions
- Verified:
- Needs verification:

## Expected evidence
- Static:
- Runtime:
- Bench:
- Docs:
- Remaining risk:
```

### Agent handoff note
```md
## Changed

## Boundary

## Verified

## Not run

## Hardware or bench evidence

## Remaining risks

## Follow-up
```

### Compound learning pass
```md
## What surprised us?

## What did the agent or workflow miss?

## Is this likely to recur?

## Is recurrence costly?

## Where should this learning live?

## Can it become executable?
```

## Activation criteria
This workflow plan should become active after:
- the clean-start Pico C++ control firmware boots without Pico Wi-Fi/CYW43;
- ESP32 gateway routing is implemented far enough to carry logs/stats and the
  intended bounded Pico UART handoff;
- Pico/ESP32/Android ownership boundaries are stable in code and docs;
- at least one real post-migration robot task can exercise the templates and
  evidence matrix.

## Completion criteria for this task
After activation, this workflow task can move out of `Deferred` when:
- this document is linked from `docs/README.md`;
- the root `AGENTS.md` points future agents here for task sizing, evidence
  depth, and handoff expectations;
- future work can use this document without reading `agentic-workspace`;
- at least one real future robot task has used the templates or evidence matrix
  and the workflow has been adjusted based on that experience.

Until activation, keep this as a parked plan and do not let it distract from the
Pico C++ migration and ESP32 gateway bring-up.
