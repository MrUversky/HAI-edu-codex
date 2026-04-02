# Скрипт Контрольного Прогона В Codex

## Цель
Использовать этот сценарий, чтобы прогнать полный путь урока внутри Codex без импровизации и расползания структуры.

## Стартовый промпт для Codex

```text
Сначала прочитай README.md, AGENTS.md и WORKSHOP_BUILD_TRACKER.md.
Потом прочитай файлы в `workshop/` в правильном порядке, начиная с `workshop/dispatch-catalog.md`.
Действуй как проводник по уроку.
Не уходи в мой личный кейс слишком рано.
Сначала помоги мне сориентироваться, потом проведи через общий кейс, затем разбор архитектуры, затем create/adapt-skill, затем validation и только потом personal next step.
Будь практичным, кратким и файлово-ориентированным.
Всегда говори, какой файл мы используем сейчас.
В participant-facing guidance отвечай по-русски.
```

## Рекомендуемый порядок прогона

### Шаг 1. Ориентация
Попросите Codex:

```text
Read README.md, AGENTS.md, workshop/setup-flow.md and explain the lesson path to me in 6–8 bullets.
```

### Шаг 2. Setup
Попросите Codex:

```text
Run the setup flow with me using participants/templates/participant_setup_template.md.
Ask one question at a time and create participants/demo_user/participant_setup.md.
```

### Шаг 3. Общий кейс
Попросите Codex:

```text
Read workshop/shared-case-flow.md, workshop/dispatch-catalog.md, .agents/skills/shared-case-*/SKILL.md, .agents/skills/task-register/SKILL.md and the files in shared_case/inputs/.
Then run the shared-case skill chain with me step by step, showing a draft first and saving only approved artifacts to shared_case/run_outputs/.
```

### Шаг 4. Разбор архитектуры
Попросите Codex:

```text
Using workshop/architecture-unpacking-flow.md, .agents/skills/shared-case-*/SKILL.md, .agents/skills/task-register/SKILL.md and shared_case/run_outputs/*, explain why the workflow is split across several skills instead of one long chat.
Keep it practical.
```

### Шаг 5. Create or adapt skill
Попросите Codex:

```text
Read workshop/create-skill-flow.md, workshop/dispatch-catalog.md and .agents/skills/skill-builder/SKILL.md.
Help me choose one skill scenario and then use practice/create_or_adapt_skill/skill_spec_template.md to draft a first version.
```

### Шаг 6. Добавить integration или fallback notes при необходимости
Попросите Codex:

```text
If my skill needs an external system, use practice/create_or_adapt_skill/integration_stub_template.md and help me document the safest fallback.
```

### Шаг 7. Validation
Попросите Codex:

```text
Use workshop/dispatch-catalog.md, .agents/skills/validate-skill/SKILL.md and .codex/agents/validation-orchestrator.toml to validate my created skill and produce a validation report.
Make the validation agent visible and show a short validation trace before the final report.
```

### Шаг 8. Практическая проверка
Попросите Codex:

```text
If the skill is ready, run one practical check on one real or test input and save the skill-specific runtime artifact only after approval.
```

### Шаг 9. Личный следующий шаг
Попросите Codex:

```text
Now switch to workshop/personal-next-step-flow.md and .agents/skills/personal-next-step/SKILL.md.
Use participants/templates/personal_next_step_template.md and participants/templates/final_action_card_template.md.
Help me identify one realistic next step only.
```

## Замечание для ведущего
Если live run начинает уплывать, остановите его и вернитесь к текущему этапу. Порядок шагов важнее стилистической гладкости.
