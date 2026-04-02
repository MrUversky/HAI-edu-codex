# Workshop Dispatch Catalog

Purpose: canonical mapping from short participant commands to workshop runtime steps.

Use this file together with `AGENTS.md`.

## Dispatch rules

### Action: start-shared-case
- Intent patterns:
  - `запусти shared case`
  - `давай начнем shared case`
  - `запусти общую цепочку`
- Entry skill: `.agents/skills/shared-case-intake/SKILL.md`
- Reads from: `shared_case/inputs/*`
- Draft shown as: `structured_inputs` draft
- Approved file path: `shared_case/outputs/structured_inputs.md`
- Next step: `shared-case-analysis`

### Action: process-raw-data
- Intent patterns:
  - `обработай сырые данные`
  - `запусти intake`
  - `покажи первый результат`
- Entry skill: `.agents/skills/shared-case-intake/SKILL.md`
- Reads from: `shared_case/inputs/*`
- Draft shown as: `structured_inputs` draft
- Approved file path: `shared_case/outputs/structured_inputs.md`
- Next step: `shared-case-analysis`

### Action: show-next-step
- Intent patterns:
  - `покажи следующий шаг`
  - `что дальше`
  - `какой следующий этап`
- Entry source: `shared_case/outputs/shared_case_state.md` if present, otherwise infer from approved artifacts
- Expected behavior:
  - state current stage explicitly
  - name the next skill or workflow step
  - name the next expected artifact

### Action: run-task-register
- Intent patterns:
  - `сделай task register`
  - `собери план задач`
  - `добавь финальный рабочий план`
- Entry skill: `.agents/skills/task-register/SKILL.md`
- Reads from: `shared_case/outputs/pilot_card.md`
- Draft shown as: `task_register` draft
- Approved file path: `shared_case/outputs/task_register.md`
- Next step: `architecture unpacking`

### Action: validate-skill
- Intent patterns:
  - `проверь мой skill`
  - `запусти валидацию`
  - `сделай validation report`
- Entry workflow:
  - participant-facing skill: `.agents/skills/validate-skill/SKILL.md`
  - internal orchestrator: `.codex/agents/validation-orchestrator.toml`
- Reads from: target skill folder in `.agents/skills/<skill-name>/`
- Draft shown as: validation summary draft
- Approved file path: `.agents/skills/<skill-name>/validation_report.md`
- Next step: `personal-next-step`

### Action: create-or-adapt-skill
- Intent patterns:
  - `помоги создать skill`
  - `хочу сделать свой skill`
  - `давай адаптируем skill`
- Entry skill: `.agents/skills/skill-builder/SKILL.md`
- Reads from:
  - `practice/create_or_adapt_skill/task_options.md`
  - selected scenario guide in `.agents/skills/skill-builder/references/`
- Draft shown as: draft skill spec
- Approved file path: `.agents/skills/<skill-name>/SKILL.md`
- Next step: `validate-skill`

### Action: personal-next-step
- Intent patterns:
  - `помоги мне определить следующий шаг`
  - `давай сформулируем мой personal next step`
  - `соберем final action card`
- Entry skill: `.agents/skills/personal-next-step/SKILL.md`
- Reads from:
  - `participants/<name>/participant_setup.md`
  - selected skill artifacts
  - optional validation report
- Draft shown as: guided reflection draft
- Approved file paths:
  - `participants/<name>/personal_next_step.md`
  - `participants/<name>/final_action_card.md`
- Next step: `closing`

## Fallback rule
If the command is ambiguous:
1. infer the most likely action only when one mapping is clearly dominant;
2. otherwise list the available actions and ask the user to choose one;
3. never silently jump across lesson stages without naming the stage transition.
