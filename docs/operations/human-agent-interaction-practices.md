# Human-Agent Interaction Practices

## Purpose And Review Window

This note records recent external practices adapted for consequential questions,
planning decisions, approval boundaries, and lifecycle handoffs. Sources were
reviewed on 2026-11-20. The review admitted material published or actively
maintained since 2026-05-20 and favors primary project or vendor sources.

The project contract remains authoritative. External practices inform it; they
do not import another project's lifecycle or approval model wholesale.

## Practices Adapted

| Source | Recent basis | Practice retained | Project adaptation |
| --- | --- | --- | --- |
| [GitHub Spec Kit clarification workflow](https://github.com/github/spec-kit/blob/main/templates/commands/clarify.md) | Current maintained command reviewed 2026-11-20 | Ask only material questions; explain why each matters; recommend with reasoning; persist accepted answers into the spec. | Applies across story definition, plan, execution reconciliation, and review routing. |
| [Microsoft HVE Core RPI planning](https://github.com/microsoft/hve-core/blob/main/.github/skills/rpi/rpi-plan/references/planning.md) and [RPI rationale](https://github.com/microsoft/hve-core/blob/main/docs/rpi/why-rpi.md) | Current maintained guidance reviewed 2026-11-20 | Separate research gaps from user decisions; group only decisions sharing evidence and consequences; pause dependent work; record readiness effect. | Uses the existing Draft-to-Done lifecycle rather than adopting RPI artifacts or agents. |
| [Superpowers brainstorming redesign](https://github.com/obra/superpowers/blob/main/docs/superpowers/specs/2026-10-05-brainstorming-rebuild-design.md) | Dated 2026-10-05 | Avoid checklist interrogation and leading menus; play back intent; distinguish owner-selected design from delegated implementation detail; keep trivial work cheap. | Menus remain useful after contextual explanation because Codex supports compact structured choices. |
| [Microsoft VS Code context-engineering guide](https://github.com/microsoft/vscode-docs/blob/main/docs/agents/guides/context-engineering-guide.md) | Current maintained guide reviewed 2026-11-20 | Ground planning in code and documentation, clarify before planning when needed, pause for review, and hand a durable plan to implementation. | Repository skills remain the entry points; no separate persistent planning agent is added. |
| [Anthropic agentic coding research](https://www.anthropic.com/research/claude-code-expertise) | Published 2026-06-16; approximately 400,000 sessions studied | Humans made most planning decisions while the agent made most execution decisions. | Evidence supports owner control of consequential intent and tradeoffs, not a fixed percentage or a ban on agent recommendations. |
| [OpenAI guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) | Current maintained guidance reviewed 2026-11-20 | Pause ambiguous or high-risk actions at the action boundary and resume after approval. | Existing robot physical gates remain stricter and authoritative for power, motion, fabrication, and destructive work. |

## Deliberate Differences

- The robot workflow permits a batch of up to three tightly related decisions.
  It does not adopt Spec Kit or Superpowers' strict one-question-at-a-time rule.
- Not every plan requires owner approval. Owner input is required only by the
  decision triggers, an applicable project gate, or an explicit request.
- A question is not a substitute for investigation. Discoverable facts remain
  agent work, and absent evidence is reported rather than converted into a
  preference poll.
- Emoji improve conversational scanning but do not become schema fields or
  mandatory decoration in durable engineering artifacts.
- Completed historical stories are not rewritten when practices evolve. Future
  relevant stories may cite this note in their `references` metadata.

## Re-Review Trigger

Revisit these adaptations after a repeated interaction failure, a material
change to the Codex question interface, or a new project workflow revision.
Record newer sources and their review dates rather than silently replacing the
historical rationale.
