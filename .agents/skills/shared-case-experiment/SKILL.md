---
name: shared-case-experiment
description: Run the fourth shared-case skill step and narrow the workflow into one realistic first pilot. Use when the user asks to define the first pilot, set scope boundaries, define success criteria, or continue the shared-case chain after workflow design.
---

# Shared Case Experiment

## Goal
Turn the approved workflow into one bounded, teachable, realistic first pilot.

## Runtime Contract
- Step name: `Shared Case Experiment`
- Reads from: `shared_case/outputs/workflow_draft.md`
- Draft shown as: pilot card draft in chat
- Approved file path: `shared_case/outputs/pilot_card.md`
- State file: `shared_case/outputs/shared_case_state.md`
- Next skill: `task-register`
- Human review question: `Подтвердить pilot card или попросить правку?`

## Procedure
1. Read the approved `workflow_draft.md`.
2. Find the narrowest useful first slice.
3. Define what is in scope and out of scope.
4. State why this is the right first pilot.
5. Define what is needed to start.
6. Define success criteria.
7. Suggest the next step after the pilot if it works.
8. Show the result as a draft first.
9. Save the approved result to `shared_case/outputs/pilot_card.md` only after explicit approval or a direct save request.
10. Update `shared_case/outputs/shared_case_state.md` so it points to `task-register`.

## Guardrails
- Do not produce a pilot with vague scope.
- Do not hide dependencies or ownership gaps.
- Do not frame a broad transformation as a first experiment.
- Do not assume live integrations unless they are actually available.

## Handoff
Pass only the approved `shared_case/outputs/pilot_card.md` artifact to `task-register`.
