# Product Backlog Contract

## Purpose

Connect system intent, architecture decisions, implementation work,
verification evidence, and known-good integrated states without imposing the
same process on every change.

## Lifecycle

```text
Discovered -> Draft -> Refined -> Ready -> In Progress -> Verification -> Done
                                      \-> Blocked
Any pre-Done state -> Deferred
```

| State | Exit requirement |
| --- | --- |
| `Discovered` | The problem or opportunity is recorded without claiming it is understood |
| `Draft` | Initial outcome, scope, and owner are described |
| `Refined` | Current state, target state, dependencies, risks, and unknowns are explicit |
| `Ready` | Definition of Ready is satisfied |
| `In Progress` | An implementation task owns the work and reports evidence status |
| `Blocked` | The blocking fact, owner, and unblock condition are explicit |
| `Verification` | Implementation is complete enough to execute its evidence plan |
| `Done` | Definition of Done and acceptance criteria are satisfied |
| `Deferred` | The reason and reactivation trigger are recorded |

## Risk Classes

| Class | Typical work | Minimum treatment |
| --- | --- | --- |
| `Tiny` | Local docs, obvious cleanup, or an isolated test | Intent, boundary, and focused check |
| `Normal` | Non-trivial platform work without safety-authority changes | Current/target behavior, ownership, non-goals, and platform checks |
| `Safety/control` | Motion, watchdog, stop/recover, encoder, wiring, battery, power, or control authority | Failure modes, safe setup, explicit approval gates, and bench evidence plan |
| `Future autonomy` | Perception or autonomy that can influence motion | Safety/control treatment plus confidence, stale-input, contradiction, and manual-override behavior |

## Definition Of Ready

- The desired user or system outcome is clear.
- Current and desired behavior are separated.
- The owning subsystem and affected boundaries are identified.
- Risk is classified.
- Known conflicts and owner questions are recorded.
- Dependencies and non-goals are explicit.
- Acceptance criteria and evidence depth are defined.
- Required human approvals and physical interventions are known.

## Definition Of Done

- Implementation matches the approved ownership boundary.
- Relevant builds, tests, lint, and static checks pass.
- Required runtime, device, or bench evidence is retained or explicitly handed
  off as unverified.
- Failure, stop, recovery, and degraded behavior are verified when relevant.
- Shared docs and platform docs agree with implementation.
- Remaining uncertainty is recorded rather than hidden.
- Reusable lessons become tests, checklists, instructions, or decisions.
- A known-good integrated snapshot is recorded when system behavior changes.

## Decision Framework

For significant software, firmware, or hardware decisions, record:

1. Desired capability and current constraint.
2. Owning subsystem and affected safety boundary.
3. Options considered, including retaining the current design.
4. Available tools, parts, skills, and verification paths.
5. Tradeoffs in safety, determinism, resources, observability, recovery,
   reversibility, maintenance cost, and future compatibility.
6. Selected option and explicit non-goals.
7. Evidence required to keep or overturn the decision.

Prefer designs whose failures are observable and whose verification is
repeatable. Ease of code generation is not an architectural criterion.

## Traceability

Meaningful implementation slices should retain this chain at a depth
appropriate to their risk:

```text
capability/backlog ID
  -> implementation issue or task
  -> architecture decision when required
  -> child-repository commits
  -> checks and observations
  -> evidence references
  -> parent integrated snapshot when system behavior changed
```

US-002 owns future component, tool, and evidence registries. US-003 owns future
toolchain, device-discovery, and automated verification interfaces. Their
absence does not weaken the ownership, risk, or honest-handoff rules here.

## Stories

- `US-001-system-roadmap-and-human-agent-workflow.md`: system model, roadmap,
  backlog rules, and human-agent contract (`Done`).
- `US-002-hardware-workshop-manual-and-evidence-system.md`: hardware,
  workshop, manuals, and structured evidence (`Refined`).
- `US-003-agentic-toolchain-device-and-verification-loop.md`: toolchain,
  connected-device, and automated verification loop (`Refined`).

## Related Docs

- System architecture: `../overview/system-architecture.md`
- Capability roadmap: `../overview/capability-roadmap.md`
- Human-agent working contract:
  `../operations/human-agent-working-contract.md`
- Claim vocabulary: `../reference/glossary.md`
