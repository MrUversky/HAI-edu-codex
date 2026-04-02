---
name: shared-case-workflow
description: Run the third shared-case skill step and turn the shared-case signal map into a practical lesson workflow. Use when the user asks to design the process, define the lesson sequence, make the human/AI boundary explicit, or continue the shared-case chain after analysis.
---

# Shared Case Workflow

## Goal
Convert the approved signal map into a practical, teachable, bounded workflow for the lesson.

## Runtime Contract
- Step name: `Shared Case Workflow`
- Reads from: `shared_case/outputs/signal_map.md`
- Draft shown as: workflow draft in chat
- Approved file path: `shared_case/outputs/workflow_draft.md`
- State file: `shared_case/outputs/shared_case_state.md`
- Next skill: `shared-case-experiment`
- Human review question: `Подтвердить workflow draft или попросить правку?`

## Procedure
1. Read the approved `signal_map.md`.
2. Define the workflow goal.
3. Break the lesson into a small number of teachable steps.
4. Make the human/AI boundary explicit.
5. Mark critical checkpoints and quality gates.
6. Explain what makes the workflow repeatable.
7. Keep the workflow bounded enough for one workshop session.
8. Show the result as a draft first.
9. Save the approved result to `shared_case/outputs/workflow_draft.md` only after explicit approval or a direct save request.
10. Update `shared_case/outputs/shared_case_state.md` so it points to `shared-case-experiment`.

## Guardrails
- Do not overengineer the workflow.
- Do not remove human judgment where it matters.
- Do not expand the workflow into a company-wide transformation map.
- Do not assume integrations unless they are explicitly available or clearly marked as stubs.

## Handoff
Pass only the approved `shared_case/outputs/workflow_draft.md` artifact to `shared-case-experiment`.
