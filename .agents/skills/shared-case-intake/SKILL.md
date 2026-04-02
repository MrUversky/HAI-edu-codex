---
name: shared-case-intake
description: Run the first shared-case skill step and convert workshop raw inputs into a structured working set. Use when the user asks to process shared-case raw data, start the shared-case chain, run the intake step, generate structured_inputs.md from shared_case/inputs/*, or structure one external raw_packet.md in strict mode.
---

# Shared Case Intake

## Goal
Convert the shared-case raw inputs into a stable structured working set for the rest of the lesson.

## Runtime Contract
- Step name: `Shared Case Intake`
- Reads from:
  - `shared_case/inputs/raw_meeting_notes.md`
  - `shared_case/inputs/colleague_messages.md`
  - `shared_case/inputs/constraints.md`
  - `shared_case/inputs/raw_tasks.md`
  - `shared_case/inputs/user_signals.md`
- Draft shown as: structured working set in chat
- Approved file path: `shared_case/run_outputs/structured_inputs.md`
- State file: `shared_case/run_outputs/shared_case_state.md`
- Next skill: `shared-case-analysis`
- Human review question: `Подтвердить structured inputs или попросить правку?`

## Strict External Raw Packet Mode
Use this mode when the input is one provided `raw_packet.md`, export, or other bounded external raw bundle rather than the canonical shared-case files.

- Read only the provided external packet.
- Do not rely on previous shared-case outputs.
- Do not rely on previous conversational context or repo-wide lesson context.
- Save the approved result next to the source packet unless the user gives another path:
  - `structured_inputs.md`
  - optional `intake_trace.md`
- Continue to `shared-case-analysis` only if the user explicitly wants the external packet to go through the rest of the chain.

## Procedure
1. Read every listed input fully before writing.
2. Separate the material into:
   - core objective
   - success conditions
   - audience realities
   - repeated signals
   - design tensions
   - constraints
   - open questions
3. Collapse obvious duplicates without hiding contradictions.
4. Normalize the wording into clean workshop language.
5. Show the result as a draft first.
6. Save the approved result to `shared_case/run_outputs/structured_inputs.md` only after explicit approval or a direct save request.
7. Update `shared_case/run_outputs/shared_case_state.md` so it points to `shared-case-analysis`.

## Guardrails
- Do not diagnose root causes yet.
- Do not propose workflow steps yet.
- Do not prioritize unless priority is explicit in the inputs.
- Do not hide ambiguity or contradictions.
- In strict external mode, do not pull in previous repo context, earlier lesson outputs, or memory from the broader conversation.
- In strict external mode, keep traceability between each output block and observable content from the provided packet.

## Handoff
Pass only the approved `shared_case/run_outputs/structured_inputs.md` artifact to `shared-case-analysis`.
