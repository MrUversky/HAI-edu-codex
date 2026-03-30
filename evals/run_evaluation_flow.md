# Run Evaluation Flow

Goal: turn a created or adapted agent into a structured evaluation result.

## Inputs
Expected package:
- created_or_adapted_agent.md
- optional integration_stub.md
- optional session_log_excerpt.md
- final_action_card.md

## Validation sequence
1. Run `validators/agent-curator.md`
2. Run `validators/skill-curator.md`
3. Run `validators/safety-validator.md`
4. Run `validators/architecture-validator.md`
5. Run `validators/eval-orchestrator.md`

## Expected outputs
- validation_report.md
- total_score
- final verdict: pass / revise / strong pass

## Rules
- A strong average must not hide a critical safety failure.
- A good concept with weak boundaries should still receive revise.
- Stub integrations must be labeled clearly, or safety validation should fail.

## Recommended human review points
- before accepting a live integration claim
- before approving customer-facing or external write actions
- before accepting a pilot with broad or unclear scope
