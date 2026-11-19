---
name: review-story
description: Review an AI robot story for readiness or review its implementation and evidence for completion. Use for substantive review of requirements, diffs, protocols, control behavior, electronics, mechanics, safety, documentation, or Done claims; do not mutate or post feedback unless requested.
---

# Review Story

Review against the story, [`docs/backlog/workflow.md`](../../../docs/backlog/workflow.md),
system ownership boundaries, and the actual changed files and evidence. Lead
with actionable findings rather than a walkthrough.

## Select The Review

- **Readiness:** review definition and plan separately: outcome, current/target separation, ownership, dependencies,
  non-goals, risk, questions, acceptance, evidence depth, approvals, learning,
  diagram usefulness, pattern decision, task DAG, AC coverage, test modes,
  doubles and limitations, evidence depth, and physical gates.
- **Delivery:** requirement fit, correctness, regression risk, tests, runtime or
  physical evidence, documentation agreement, and honest claim level.

Select only relevant lenses:

- software architecture and maintainability;
- protocol compatibility, framing, freshness, and recovery;
- real-time control, motor authority, watchdog, stop, and degraded behavior;
- electrical identity, ratings, protection, measurement topology, and wiring;
- mechanical fit, load path, tolerance, fastening, workholding, and fabrication;
- safety gates, stop conditions, and evidence integrity;
- documentation, diagrams, and decision-relevant learning.

For broad, cross-subsystem, or safety-relevant work, use a fresh isolated
reviewer when delegation is available and authorized. Give it the story, diff,
raw evidence, and relevant contracts—not the implementing agent's conclusions.
The coordinating agent must verify findings before reporting them.

Order findings by severity and cite files, lines, concrete code paths, physical
principles, or missing evidence. Separate demonstrated defects, concerns, and
questions. Never infer device or bench qualification from builds or agent
reports. If no findings remain, state the exact evidence reviewed and any
residual limitations.
