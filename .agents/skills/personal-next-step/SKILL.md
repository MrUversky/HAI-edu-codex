---
name: personal-next-step
description: Run the final guided reflection of the workshop and turn the participant's validated idea into one realistic next step and action card. Use when the user asks for a personal next step, wants help identifying what to try next, or wants to produce personal_next_step.md and final_action_card.md.
---

# Personal Next Step

## Goal
Guide the participant to one realistic next step based on their role, chosen skill, and validated workshop outcome.

## Runtime Contract
- Step name: `Personal Next Step`
- Reads from:
  - `participants/<name>/participant_setup.md`
  - optional created or adapted skill artifacts
  - optional validation report
  - `participants/templates/personal_next_step_template.md`
  - `participants/templates/final_action_card_template.md`
- Draft shown as: short guided reflection and draft summary in chat
- Approved file paths:
  - `participants/<name>/personal_next_step.md`
  - `participants/<name>/final_action_card.md`
- Human review question: `Подтвердить следующий шаг и action card или уточнить?`

## Procedure
1. Start the stage explicitly and say that the goal is one realistic next step, not a broad strategy.
2. Use the participant's role, lesson goal, chosen skill, and validation context to tailor the questions.
3. Ask one short question at a time.
4. Focus on:
   - one repeating work situation
   - the usual inputs
   - what is done manually today
   - what repeats
   - one small first scenario worth testing
   - what success would look like in the next 7 days
5. Draft `personal_next_step.md` first.
6. Then derive `final_action_card.md` from the approved reflection.
7. Save only after explicit approval or a direct save request.

## Guardrails
- Do not drift into full transformation strategy.
- Do not ask generic reflection questions when role-specific phrasing is possible.
- Do not propose more than one first scenario.
- Do not skip the action-card step.
