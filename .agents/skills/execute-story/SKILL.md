---
name: execute-story
description: Implement a Ready AI robot backlog story through code, documentation, tests, device work, and evidence until it is Done or honestly Blocked. Use when executing a specific US-NNN story; preserve platform ownership and physical approval gates.
---

# Execute Story

Read the story, its `implementation-plan.md`, [`docs/backlog/workflow.md`](../../../docs/backlog/workflow.md),
the consequential decision and meaningful handoff sections of the
[human-agent contract](../../../docs/operations/human-agent-working-contract.md),
and the nearest platform `AGENTS.md` before editing.

## Start

- Confirm status is Ready and every `blocks` dependency is Done.
- State the subsystem boundary, implementation pattern, engineering reason, and
  evidence level required by the claims.
- Change status to In Progress and regenerate the backlog index.
- Stop for explicit approval before any physical action named by the
  human-agent contract. Do not broaden task authority.

## Execute And Verify

- Edit only the owning parent or child repository; update shared docs with any
  protocol, wiring, safety, or ownership change.
- Execute the task DAG and update task status honestly. Work in small observable slices. Use the repository-owned platform command or
  `tools/robot.py` scenario when available.
- Distinguish static/host, runtime, connected-device, bench/HIL, and ground
  motion evidence. A lower level never qualifies a higher-level claim.
- Explain unfamiliar embedded concepts briefly when they affect a choice:
  physical reason, failure symptom, expected observation, tool limits, and
  authoritative source.
- Retain physical observations in a new append-only evidence bundle. Link
  evidence from the story instead of pasting large logs.
- Continue routine implementation decisions within the approved plan. If a
  discovery materially changes scope, architecture, ownership, safety,
  acceptance evidence, destructive action, or cost, record the pending decision
  and pause only dependent work. Use the contract's contextual decision request
  before asking; persist the answer and reconcile the plan before resuming.

## Finish

Run fresh checks that prove each completion claim, inspect their full results,
and review the acceptance criteria. Change the story directly from In Progress
to Done only when its required evidence exists. Otherwise leave it In Progress
with explicit unverified work, or mark it Blocked with the blocker owner and
unblock condition. Regenerate and validate the backlog index.

Use the meaningful-handoff template to distinguish implemented, verified,
unverified, blocked, and remaining work; name the preserved boundary, evidence
level, owner decisions or approvals, and next dependent action.
