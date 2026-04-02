---
name: task-register
description: Turn an approved shared-case pilot card into a concrete task register for the first sprint. Use when the user asks to turn the pilot into tasks, build the first sprint plan, or produce shared_case/outputs/task_register.md.
---

# Task Register

## Goal
Convert an approved pilot card into a bounded first-sprint task register.

## Runtime Contract
- Step name: `Task Register`
- Reads from:
  - `shared_case/outputs/pilot_card.md`
  - optional `shared_case/outputs/workflow_draft.md`
- Draft shown as: task register draft in chat
- Approved file path: `shared_case/outputs/task_register.md`
- State file: `shared_case/outputs/shared_case_state.md`
- Next step: `architecture unpacking`
- Human review question: `Подтвердить task register или попросить правку?`

## Procedure
1. Read the approved `pilot_card.md`.
2. Restate the first sprint goal in one sentence.
3. Break the pilot into a small set of concrete first-sprint tasks.
4. Separate in-scope tasks from out-of-scope tasks.
5. Add owner placeholders where needed.
6. Mark dependencies, blockers, or unknowns.
7. Define the first review checkpoint.
8. Restate sprint success criteria in observable terms.
9. Show the result as a draft first.
10. Save the approved result to `shared_case/outputs/task_register.md` only after explicit approval or a direct save request.
11. Update `shared_case/outputs/shared_case_state.md` so the next stage points to `architecture unpacking`.

## Output format
Return these sections:
1. First sprint goal
2. In-scope tasks
3. Out-of-scope tasks
4. Owner placeholders
5. Dependencies and blockers
6. First review checkpoint
7. Sprint success criteria

## Guardrails
- Do not invent confirmed owners when ownership is unknown.
- Do not hide blockers or external dependencies.
- Do not expand the sprint beyond a realistic first slice.
- Do not turn a pilot into a broad transformation roadmap.
- Do not assume live integrations unless they are explicitly available.
