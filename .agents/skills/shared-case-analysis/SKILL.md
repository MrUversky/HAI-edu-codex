---
name: shared-case-analysis
description: Run the second shared-case skill step and turn structured shared-case inputs into signal clusters, tensions, bottlenecks, and a design focus. Use when the user asks to analyze structured_inputs.md, find signals, surface tensions, or continue the shared-case chain after intake.
---

# Shared Case Analysis

## Goal
Turn the approved shared-case working set into a clear map of signals, tensions, bottlenecks, and design focus.

## Runtime Contract
- Step name: `Shared Case Analysis`
- Reads from: `shared_case/run_outputs/structured_inputs.md`
- Draft shown as: signal map draft in chat
- Approved file path: `shared_case/run_outputs/signal_map.md`
- State file: `shared_case/run_outputs/shared_case_state.md`
- Next skill: `shared-case-workflow`
- Human review question: `Подтвердить signal map или попросить правку?`

## Procedure
1. Read the approved `structured_inputs.md`.
2. Identify the main signal clusters.
3. Surface the key tensions and contradictions.
4. Separate likely bottlenecks from surface symptoms.
5. Explain why those bottlenecks matter.
6. Recommend a design focus without building the workflow yet.
7. Show the result as a draft first.
8. Save the approved result to `shared_case/run_outputs/signal_map.md` only after explicit approval or a direct save request.
9. Update `shared_case/run_outputs/shared_case_state.md` so it points to `shared-case-workflow`.

## Guardrails
- Do not invent evidence that is not present.
- Do not collapse uncertainty into false certainty.
- Do not build the workflow yet.
- Do not overstate causality.

## Handoff
Pass only the approved `shared_case/run_outputs/signal_map.md` artifact to `shared-case-workflow`.
