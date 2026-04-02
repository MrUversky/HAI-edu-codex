# Facilitator Demo Script by Minute

## 0–5 min
Frame the lesson.
Say explicitly:
- this is not an AI-overview session
- we will run a shared skill chain, understand it, then apply it
- the final outcome is one realistic next step

## 5–10 min
Run setup and light personalization.
Goal:
- participant feels oriented
- no personal business-case digging yet

## 10–15 min
Explain the route of the lesson in one slide or one short verbal map.
Checkpoint:
- participants know shared case comes before personal application

## 15–25 min
Show the raw shared-case inputs.
Use:
- `shared_case/inputs/*`
Goal:
- make the chaos feel real

## 25–35 min
Run the shared-case skills through `shared-case-intake` and `shared-case-analysis`.
Goal:
- participants run the same steps locally
- each step produces an approved artifact in `shared_case/run_outputs/`

## 35–45 min
Run `shared-case-workflow` and `shared-case-experiment`.
Goal:
- participants see the full transformation from chaos to a bounded pilot
- the chain feels like saved handoffs, not one long chat

## 45–50 min
Run `task-register`.
Goal:
- participants see the last hop from pilot concept to an operational first-sprint artifact
- the shared case ends on `task_register.md`, not on `pilot_card.md`

## 50–60 min
Unpack the architecture.
Explain:
- why there are multiple skills
- where human judgment stays
- why this is more than one prompt
- why `draft -> review -> approve -> save -> handoff` matters

## 60–70 min
Introduce create-or-adapt-skill practice.
Use:
- `.agents/skills/skill-builder/SKILL.md`
- `practice/create_or_adapt_skill/task_options.md`
- `practice/create_or_adapt_skill/skill_spec_template.md`
- `practice/create_or_adapt_skill/integration_stub_template.md`

## 70–95 min
Participants create or adapt one skill.
Facilitator rule:
keep scope narrow; one source, one transformation, one useful output.

## 95–105 min
Run validation.
Use:
- `.agents/skills/validate-skill/SKILL.md`
- `.codex/agents/validation-orchestrator.toml`
Goal:
- every participant gets structured feedback, not vague praise
- make the validation agent visible as one coordinator that runs several checks in sequence

## 105–118 min
Switch to personal next step.
Use:
- `participants/templates/personal_next_step_template.md`
- `participants/templates/final_action_card_template.md`
Goal:
- identify one bounded real use case and one next step

## 118–120 min
Close.
Repeat:
- one realistic use case
- one next step
- one action in the next 7 days

## Recovery switch points
- If shared-case demo breaks: switch at 25–45 min to the prepared files in `shared_case/outputs/`.
- If create/adapt scope explodes: intervene immediately at 65–95 min and force a smaller pilot.
