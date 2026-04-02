# Каталог Команд Урока

Назначение: каноническая карта коротких команд участника и ведущего.

Использовать вместе с `AGENTS.md`.

## Правила маршрутизации

### Action: start-participant-lesson
- Intent patterns:
  - `запусти урок для участника`
  - `проведи меня по уроку`
  - `давай начнем урок`
- Entry source: `workshop/start-prompt-participant.md`
- Expected behavior:
  - коротко объяснить маршрут урока
  - начать с этапа `setup`
  - назвать первый ожидаемый артефакт

### Action: start-facilitator-lesson
- Intent patterns:
  - `запусти урок для ведущего`
  - `помогай мне вести урок`
  - `запусти режим ведущего`
- Entry source: `workshop/start-prompt-facilitator.md`
- Expected behavior:
  - коротко объяснить маршрут урока для ведущего
  - подсказать, какой файл открыть первым
  - начать с этапа `setup`

### Action: start-shared-case
- Intent patterns:
  - `запусти общий кейс`
  - `давай начнем общий кейс`
  - `запусти общую цепочку`
- Entry skill: `.agents/skills/shared-case-intake/SKILL.md`
- Reads from: `shared_case/inputs/*`
- Draft shown as: `structured_inputs` draft
- Approved file path: `shared_case/run_outputs/structured_inputs.md`
- Next step: `shared-case-analysis`

### Action: process-raw-data
- Intent patterns:
  - `обработай сырые данные`
  - `запусти intake`
  - `покажи первый результат`
- Entry skill: `.agents/skills/shared-case-intake/SKILL.md`
- Reads from: `shared_case/inputs/*`
- Draft shown as: `structured_inputs` draft
- Approved file path: `shared_case/run_outputs/structured_inputs.md`
- Next step: `shared-case-analysis`

### Action: show-next-step
- Intent patterns:
  - `покажи следующий шаг`
  - `что дальше`
  - `какой следующий этап`
- Entry source: `shared_case/run_outputs/shared_case_state.md` if present, otherwise infer from approved runtime artifacts
- Expected behavior:
  - явно назвать, что уже сохранено
  - назвать следующий этап
  - назвать следующий ожидаемый артефакт

### Action: run-task-register
- Intent patterns:
  - `собери рабочий план`
  - `собери план задач`
  - `добавь финальный рабочий план`
- Entry skill: `.agents/skills/task-register/SKILL.md`
- Reads from: `shared_case/run_outputs/pilot_card.md`
- Draft shown as: `task_register` draft
- Approved file path: `shared_case/run_outputs/task_register.md`
- Next step: `architecture unpacking`

### Action: validate-skill
- Intent patterns:
  - `проверь мой навык`
  - `проверь мой skill`
  - `запусти валидацию`
  - `сделай отчёт валидации`
  - `сделай validation report`
- Entry workflow:
  - participant-facing skill: `.agents/skills/validate-skill/SKILL.md`
  - internal orchestrator: `.codex/agents/validation-orchestrator.toml`
- Reads from: target skill folder in `.agents/skills/<skill-name>/`
- Draft shown as:
  - запуск агента валидации
  - короткий trace внутренних проверок
  - итоговый validation summary draft
- Approved file paths:
  - `.agents/skills/<skill-name>/validation_trace.md`
  - `.agents/skills/<skill-name>/validation_report.md`
- Next step: `practice-check-skill`

### Action: create-or-adapt-skill
- Intent patterns:
  - `помоги создать навык`
  - `хочу сделать свой навык`
  - `давай адаптируем навык`
- Entry skill: `.agents/skills/skill-builder/SKILL.md`
- Reads from:
  - `practice/create_or_adapt_skill/task_options.md`
  - selected scenario guide in `.agents/skills/skill-builder/references/`
- Draft shown as: draft skill spec
- Approved file path: `.agents/skills/<skill-name>/SKILL.md`
- Next step: `validate-skill`

### Action: practice-check-skill
- Intent patterns:
  - `проверь навык на практике`
  - `прогони навык на одном входе`
  - `дай тестовый прогон навыка`
- Entry workflow:
  - use the selected skill
  - use one real or test input provided by the participant
- Reads from:
  - `.agents/skills/<skill-name>/SKILL.md`
  - one provided export, transcript, note bundle, or other bounded input
- Draft shown as:
  - один практический прогон навыка
  - skill-specific runtime artifact draft
- Approved file path: the runtime artifact declared by the selected skill
- Next step: `personal-next-step`

### Action: personal-next-step
- Intent patterns:
  - `помоги мне определить следующий шаг`
  - `давай сформулируем мой следующий шаг`
  - `соберем итоговую карточку действия`
- Entry skill: `.agents/skills/personal-next-step/SKILL.md`
- Reads from:
  - `participants/<name>/participant_setup.md`
  - selected skill artifacts
  - optional validation report and validation trace
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
