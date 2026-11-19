# Human-Agent Working Contract

## Purpose

Define the active collaboration baseline for this robot project. This contract
applies now; the broader workflow experiments in
`agentic-development-workflow.md` remain deferred.

## Owner Context

The owner is a senior software and AI engineer. Agents may assume expert-level
fluency in software architecture, APIs, distributed systems, AI/ML,
automation, testing, and complex application code.

The owner is actively developing deeper experience with MCU and real-time
constraints, electronics and power, schematics and measurement, and mechanical
fabrication. This is a communication preference, not a limit on participation.

Agents should:

- communicate software and AI decisions at a senior-engineer level;
- define embedded, electrical, and mechanical terminology when it first
  affects a decision;
- explain the physical reason, likely failure mode, severity, and observable
  symptom;
- distinguish facts, assumptions, hypotheses, recommendations, and unknowns;
- give expected measurements, tolerances, and stop conditions for bench work;
- explain why a tool is suitable and where its accuracy or capability ends;
- avoid re-teaching routine software concepts.

## Agent-By-Default Behavior

Within the authority granted by a task, agents should independently:

- inspect relevant parent and child docs, code, configuration, assets, and Git
  state before proposing changes or asking discoverable questions;
- preserve Android, ESP32, Pico, and parent-workspace ownership boundaries;
- use available safe tools for builds, tests, static checks, and read-only
  diagnostics;
- capture exact commands, versions, logs, and outcomes when they form useful
  evidence;
- ask the owner only for intent, unavailable physical facts, approvals, or
  observations that cannot be gathered safely;
- hand off explicit unverified items instead of implying completion.

Unknowns block only their dependent decisions. Unrelated work should continue
when it remains safe and within scope.

## Task Treatment

Use the risk classes and Ready/Done rules in `../backlog/README.md`. Apply the
smallest useful artifact:

- `Tiny`: state intent, affected boundary, and focused check.
- `Normal`: record current/target behavior, ownership, non-goals, and expected
  static/runtime/documentation checks.
- `Safety/control`: additionally record failure modes, verified and unverified
  bench assumptions, approval gates, safe posture, stop conditions, and bench
  evidence.
- `Future autonomy`: additionally define confidence limits, stale or
  contradictory perception behavior, bounded admission, and manual override.

For every meaningful handoff, state what changed, the boundary preserved or
changed, what was verified, what was not run, remaining hardware uncertainty,
and the next dependent action.

## Human Participation And Approval Boundaries

Owner participation or explicit approval is required before:

- first power-on after wiring or power-path changes;
- flashing firmware that changes motion, watchdog, stop, encoder, actuator, or
  command-admission behavior;
- enabling motor output or running tracks;
- changing BMS, charger, or battery configuration;
- operating fabrication equipment when setup, workholding, or safe use is not
  established.

Read-only inspection, host builds/tests, and non-mutating device discovery do
not replace physical approval where the next action can energize or move the
robot.

## Physical Procedure Template

Physical instructions must use this minimum structure:

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

Absence of required protective equipment, workholding, measurement capability,
hardware identity, or a reliable stop path is a blocking precondition. It is
not a reason to weaken the procedure.

## Durable Learning

Preserve only lessons that are likely to recur or expensive to relearn:

| Lesson | Durable form |
| --- | --- |
| Exact bug | Regression test |
| Repeated implementation pattern | Platform doc or focused solution note |
| Broad project convention | Agent instruction or operations doc |
| Repeated review concern | Checklist |
| Safety-critical issue | Guardrail, test, or bench checklist |
| Architectural tradeoff | `../overview/design-decisions.md` |
| Hardware uncertainty | `../verification/known-issues-and-open-questions.md` |
| Integrated system state | Parent submodule pointers and change log |

Prefer executable checks over prose when both express the lesson accurately.

## Related Docs

- Backlog contract: `../backlog/README.md`
- System architecture: `../overview/system-architecture.md`
- Deferred agentic workflow: `agentic-development-workflow.md`
