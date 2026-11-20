# Human-Agent Working Contract

## Purpose

Define the active collaboration baseline for this robot project. The lightweight
workflow and repository skills in `agentic-development-workflow.md` apply now.

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

## Consequential Decisions And Questions

Investigate before asking. Repository files, project documentation, registered
evidence, safe read-only diagnostics, and established precedent are agent-owned
discovery work. Routine, reversible implementation details are also agent-owned
when the approved outcome and boundaries determine them.

Ask the owner when an unresolved choice materially changes product intent,
scope, architecture, subsystem ownership, safety, acceptance or evidence,
irreversible or destructive action, or meaningful cost or elapsed time. A
missing physical fact, approval, or observation also requires owner input when
it cannot be gathered safely. Do not manufacture a question when no such
decision remains; say that no owner decision is required in the handoff.

Combine at most three decisions only when they share evidence and consequences,
or when answering one independently would mislead. Ask safety, physical
approval, destructive, and immediately blocking decisions separately. Pause
only the work that depends on the answer.

Before using a compact question interaction, explain the decision in friendly,
plain language. Include only the relevant parts of this template:

```text
🧭 Situation
What the agent is trying to decide and why it arose now.

🔎 What I investigated
The project facts, evidence, precedents, and remaining uncertainty.

⚖️ Options and consequences
Viable choices with their material advantages, disadvantages, risks, and
effects on readiness or dependent work.

💡 Recommendation
The evidence-backed preferred option and why it best fits this project.

❓ Owner input needed
One complete question per decision. The compact question UI may shorten the
options, but it must not introduce choices absent from this explanation.
```

After each accepted answer, update the artifact that owns the decision before
continuing: the story definition during refinement, `implementation-plan.md`
during planning, the plan/story/evidence record during execution, or the review
record and routed artifact during review.

## Meaningful Handoffs

Every phase-ending handoff uses the relevant parts of this template:

```text
✅ Outcome
The phase result and lifecycle/readiness state.

📦 Coverage
What the definition, plan, implementation, or review covers.

🧭 Boundary
The subsystem boundary preserved or intentionally changed.

🔑 Decisions
Material decisions made, including whether no owner decisions remain.

🧪 Verification and evidence
What was checked, at which evidence level, and the result.

⚠️ Remaining uncertainty
Unverified work, hardware facts, residual risks, blockers, or none.

➡️ Next dependent action
The next responsible phase, owner, approval, or concrete unblock action.
```

Use emoji as restrained navigation cues, not decoration. Optional domain cues
are `⚡` electrical/power, `⚙️` motors/control, `🔩` mechanical, `🤖`
AI/autonomy, and `💻` software. Durable artifacts remain professional Markdown
and need not repeat conversational emoji.

The evidence and adaptations behind this protocol are recorded in
[human-agent interaction practices](human-agent-interaction-practices.md).

## Task Treatment

Use the risk classes and Ready/Done rules in `../backlog/workflow.md`. Apply the
smallest useful artifact:

- `Tiny`: state intent, affected boundary, and focused check.
- `Normal`: record current/target behavior, ownership, non-goals, and expected
  static/runtime/documentation checks.
- `Safety/control`: additionally record failure modes, verified and unverified
  bench assumptions, approval gates, safe posture, stop conditions, and bench
  evidence.
- `Future autonomy`: additionally define confidence limits, stale or
  contradictory perception behavior, bounded admission, and manual override.

For every meaningful handoff, use the shared handoff contract above and state
what changed, what was verified, what was not run, remaining hardware
uncertainty, and the next dependent action.

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
When a physical or real-time concept affects a decision, explain it concisely
at the owner's software/AI level: concept, robot relevance, analogy and limit,
failure symptom, measurement or observation, tool limitation, and authoritative
source. Promote only reusable material to `../learning/`.

## Related Docs

- Backlog index: `../backlog/README.md`
- Backlog contract: `../backlog/workflow.md`
- System architecture: `../overview/system-architecture.md`
- Active agentic harness: `agentic-development-workflow.md`
