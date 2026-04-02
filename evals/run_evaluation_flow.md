# Run Evaluation Flow

Goal: turn a created or adapted skill into a structured evaluation result.

## Inputs
Expected package:
- `.agents/skills/<skill-name>/SKILL.md`
- optional integration_stub.md
- optional session_log_excerpt.md
- final_action_card.md

## Validation sequence
Participant-facing entry:
- `.agents/skills/validate-skill/SKILL.md`

Internal orchestrator:
- `.codex/agents/validation-orchestrator.toml`

Validation skills:
1. `.agents/skills/reviewer-role/SKILL.md`
2. `.agents/skills/safety-validator/SKILL.md`
3. `.agents/skills/architecture-validator/SKILL.md`
4. `.agents/skills/skill-structure-check/SKILL.md`

Legacy source material:
- `validators/agent-curator.md`
- `validators/skill-curator.md`
- `validators/safety-validator.md`
- `validators/architecture-validator.md`
- `validators/eval-orchestrator.md`

## Expected outputs
- validation_trace.md
- validation_report.md
- total_score
- final verdict: pass / revise / strong pass

## Rules
- A strong average must not hide a critical safety failure.
- A good concept with weak boundaries should still receive revise.
- Stub integrations must be labeled clearly, or safety validation should fail.
- Canonical skill layout and handoff pattern should be checked together with the spec itself.
- Validation should feel like one participant-facing command, not like a manual walk through validator files.
- The participant should see that one validation agent ran several checks in sequence and assembled the result.

## Recommended human review points
- before accepting a live integration claim
- before approving customer-facing or external write actions
- before accepting a pilot with broad or unclear scope
