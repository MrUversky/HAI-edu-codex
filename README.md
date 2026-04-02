# HAI Edu Codex Workshop Repo

Этот репозиторий — рабочая среда для воркшопа по skill-based workflows.

Логика урока такая:
1. `setup` и лёгкая персонализация
2. общий кейс
3. разбор архитектуры
4. создать или адаптировать навык
5. провалидировать результат
6. определить один личный следующий шаг
7. собрать итоговый пакет

## Основные папки
- `workshop/` — сценарии урока и операционная логика
- `.agents/skills/` — канонический runtime-слой воркшопа в Codex
- `reference/` — справочный слой и best practices
- `agents/` — legacy source material из ранней структуры
- `validators/` — legacy source material для validation logic
- `practice/` — задания и шаблоны для этапа create/adapt
- `participants/` — шаблоны и participant-артефакты
- `evals/` — логика оценки
- `sources/` — verified source notes

## Как использовать репозиторий в Codex
Начинайте с [setup-flow.md](/Users/Igor/DemoHAI_V1/workshop/setup-flow.md), затем идите по flow-файлам по порядку.
Используйте [dispatch-catalog.md](/Users/Igor/DemoHAI_V1/workshop/dispatch-catalog.md) как каноническую карту коротких participant-команд.

Не уходите сразу в личный рабочий кейс участника.
Сначала:
1. посмотреть
2. понять
3. попробовать механику
4. только потом применить к себе

## Канонический runtime
Воркшоп использует Codex `skills` как канонический формат исполнения.

Используйте эти workshop-skills `v1`:
- `.agents/skills/shared-case-intake/`
- `.agents/skills/shared-case-analysis/`
- `.agents/skills/shared-case-workflow/`
- `.agents/skills/shared-case-experiment/`
- `.agents/skills/task-register/`
- `.agents/skills/skill-builder/`
- `.agents/skills/validate-skill/`
- `.agents/skills/personal-next-step/`

Для внешних сырьевых пакетов используйте тот же `.agents/skills/shared-case-intake/`, но в строгом режиме:
- вход = только один переданный `raw_packet.md` или другой ограниченный сырой пакет;
- helper не подтягивает прошлый conversational context и старые shared-case outputs;
- `structured_inputs.md` сохраняется рядом с источником, если не задан другой путь.

Validation runtime:
- participant-facing вход: `.agents/skills/validate-skill/`
- internal orchestrator: `.codex/agents/validation-orchestrator.toml`
- skills поддержки validation:
  - `.agents/skills/reviewer-role/`
  - `.agents/skills/safety-validator/`
  - `.agents/skills/architecture-validator/`
  - `.agents/skills/skill-structure-check/`

Во время migration-периода трактуйте `agents/*` и `validators/*` как legacy source material и references.
