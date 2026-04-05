# Codex Agents Workshop Starter Repo

Этот репозиторий — учебный starter repo для воркшопа по агентам и Codex.

Он нужен для аудитории без сильного инженерного бэкграунда:

- менеджеры
- рекрутеры
- операционные роли
- исследователи
- люди, которым нужно понять agent workflow на практике

Главная идея репозитория:

- агент = менеджер процесса
- skill = инструкция для повторяемой операции
- tool = руки агента
- MCP / интеграции = мост во внешний мир

## Что здесь есть

В репозитории два уровня работы:

1. `demo`

- готовый workflow `Gmail -> разбор резюме -> оценка -> Telegram`
- его запускает один агент: [resume-processing-agent.toml](/Users/Igor/DemoHAI_V1/.codex/agents/resume-processing-agent.toml)

1. `exercise`

- практический workflow `meeting_raw.txt -> задачи / вопросы / риски -> сохранение результата -> отправка задач в Telegram`
- здесь участники создают новый skill `extract-meeting-actions`

## Как устроен репозиторий

- `.codex/agents/` — agent profiles для orchestration
- `.agents/skills/` — канонический runtime-слой skills
- `docs/` — короткая учебная документация
- `examples/` — компактные реалистичные входы и ожидаемые выходы
- `drafts/` — промежуточные черновики
- `outputs/` — финальные артефакты
- `templates/` — шаблоны новых skills и agents
- `participants/` — participant setup и пример стартового файла

## Как пройти по репозиторию

1. Открой [AGENTS.md](/Users/Igor/DemoHAI_V1/AGENTS.md).
2. Открой [docs/setup-flow-ru.md](/Users/Igor/DemoHAI_V1/docs/setup-flow-ru.md).
3. Открой [docs/lesson-map-ru.md](/Users/Igor/DemoHAI_V1/docs/lesson-map-ru.md).
4. Открой [docs/concepts-ru.md](/Users/Igor/DemoHAI_V1/docs/concepts-ru.md).
5. Для demo открой [resume-processing-agent.toml](/Users/Igor/DemoHAI_V1/.codex/agents/resume-processing-agent.toml).
6. Для practice открой [new_skill_template.md](/Users/Igor/DemoHAI_V1/templates/new_skill_template.md) и reference skill [extract-meeting-actions/SKILL.md](/Users/Igor/DemoHAI_V1/examples/reference_skills/extract-meeting-actions/SKILL.md).

## Как начать урок

Короткая команда старта:

`Запусти урок`

Или:

`Давай начнем урок`

Ожидаемое поведение:
- сначала Codex проводит лёгкий setup по одному вопросу за раз
- затем помогает сохранить `participants/<name>/participant_setup.md`
- после этого переводит к карте мира и demo

## Как запустить demo

Короткая команда для показа:

`Посмотри новые письма и разбери резюме`

Или:

`Запусти demo обработки резюме`

Ожидается, что Codex уже работает в этом репозитории и видит:

- [README.md](/Users/Igor/DemoHAI_V1/README.md)
- [AGENTS.md](/Users/Igor/DemoHAI_V1/AGENTS.md)
- [resume-processing-agent.toml](/Users/Igor/DemoHAI_V1/.codex/agents/resume-processing-agent.toml)

## Как проходит exercise

Участник не пишет skill вслепую и не идёт сразу в `/skill-creator`.

Сначала он пишет в чат:

`Хочу сделать skill, который из сырого текста встречи выделяет задачи, вопросы и риски, сохраняет результат в markdown, а потом позволяет отправить задачи через существующий Telegram skill. Сначала задай мне уточняющие вопросы по одному и помоги собрать хороший контракт.`

После этого:

1. Codex задаёт вопросы по одному
2. Codex собирает итоговый prompt для `/skill-creator`
3. вы копируете этот prompt и запускаете `/skill-creator`
4. создаётся новый `SKILL.md`
5. участник открывает файл и руками проверяет контракт
6. участник сверяется с reference skill в [examples/reference_skills/extract-meeting-actions/SKILL.md](/Users/Igor/DemoHAI_V1/examples/reference_skills/extract-meeting-actions/SKILL.md)
7. затем прогоняет созданный skill на [meeting_raw.txt](/Users/Igor/DemoHAI_V1/examples/meeting_raw.txt)
8. сохраняет результат в `outputs/exercise/meeting_actions.md`
9. отдельно отправляет блок задач через `send-telegram-message`

## Что делать после урока

Открой [docs/next-steps.md](/Users/Igor/DemoHAI_V1/docs/next-steps.md).

Там зафиксирован короткий post-lesson маршрут:

1. открыть одного агента
2. открыть два skill
3. выбрать одну повторяющуюся рабочую ситуацию
4. выбрать один источник
5. описать один желаемый результат
6. создать свой первый новый skill по шаблону
