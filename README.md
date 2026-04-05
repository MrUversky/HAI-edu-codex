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
- reference skill для самопроверки лежит в `examples/reference_skills/`

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

Есть два явных режима старта:

- `Запусти урок для преподавателя`
- `Запусти урок для участника`

Что происходит дальше:
- в режиме преподавателя: setup -> concepts -> demo -> короткий разбор архитектуры
- в режиме участника: setup -> concepts -> сразу exercise, без повторного demo

## Как запустить demo

Короткая команда для показа:

`Посмотри новые письма и разбери резюме`

Или:

`Запусти demo обработки резюме`

Ожидается, что Codex уже работает в этом репозитории и видит:

- [README.md](/Users/Igor/DemoHAI_V1/README.md)
- [AGENTS.md](/Users/Igor/DemoHAI_V1/AGENTS.md)
- [resume-processing-agent.toml](/Users/Igor/DemoHAI_V1/.codex/agents/resume-processing-agent.toml)

Человеческое описание demo-пайплайна:

`взять письмо -> собрать пакет кандидата -> оценить -> отправить итог в Telegram`

Техническое описание того же пайплайна:

`Gmail -> fetch-gmail-resumes -> evaluate-resume-batch -> send-telegram-message`

Постоянный вход для demo-оценки:

- [demo_role_brief.md](/Users/Igor/DemoHAI_V1/examples/demo_role_brief.md)

Если полезный текст кандидата лежит во вложенном PDF, для teacher demo можно добавить ещё два шага:

`download attachment -> extract PDF text`

Для этого в repo есть:
- [scripts/download_gmail_attachment.py](/Users/Igor/DemoHAI_V1/scripts/download_gmail_attachment.py)
- [scripts/extract_pdf_text.py](/Users/Igor/DemoHAI_V1/scripts/extract_pdf_text.py)

## Как проходит exercise

Участник не пишет skill вслепую и не идёт сразу в `/skill-creator`.

Сначала он пишет в чат:

`Хочу сделать skill extract-meeting-actions, который по итогам встречи собирает задачи, вопросы и риски. Помоги мне короткими вопросами собрать хороший контракт, а потом подготовь prompt для /skill-creator.`

После этого:

1. Codex задаёт вопросы по одному
2. Codex собирает итоговый prompt для `/skill-creator`
3. вы копируете этот prompt и запускаете `/skill-creator`
4. создаётся новый `SKILL.md`
5. сразу после генерации вы проверяете файл через [scripts/quick_validate.py](/Users/Igor/DemoHAI_V1/scripts/quick_validate.py)
6. если frontmatter или имя сломались, вы правите их через [scripts/normalize_skill.py](/Users/Igor/DemoHAI_V1/scripts/normalize_skill.py)
7. участник открывает файл и руками проверяет контракт
8. участник сверяется с reference skill в [examples/reference_skills/extract-meeting-actions/SKILL.md](/Users/Igor/DemoHAI_V1/examples/reference_skills/extract-meeting-actions/SKILL.md)
9. затем прогоняет созданный skill на [meeting_raw.txt](/Users/Igor/DemoHAI_V1/examples/meeting_raw.txt)
10. Codex показывает результат на экране и сохраняет его в файл
11. после этого участник отправляет в чат Codex `TELEGRAM_BOT_TOKEN` и `TELEGRAM_CHAT_ID`, Codex сохраняет их локально в `.env.local`
12. затем участник отправляет блок задач через `send-telegram-message`

Какие вопросы Codex должен задавать здесь:
- что обычно приходит на вход
- что должно получиться на выходе
- что обязательно должно попасть в markdown
- где человек смотрит и подтверждает результат

Какие вопросы Codex не должен задавать:
- должен ли skill сам вызывать Telegram skill
- нужна ли ещё одна skill для отправки
- вопросы про общую архитектуру, если repo уже зафиксировал решение

## Что делать после урока

Открой [docs/next-steps.md](/Users/Igor/DemoHAI_V1/docs/next-steps.md).

Там зафиксирован короткий post-lesson маршрут:

1. открыть одного агента
2. открыть два skill
3. выбрать одну повторяющуюся рабочую ситуацию
4. выбрать один источник
5. описать один желаемый результат
6. создать свой первый новый skill по шаблону

## Workshop helpers

В repo есть два общих helper script:

- [scripts/init_skill.py](/Users/Igor/DemoHAI_V1/scripts/init_skill.py)
- [scripts/quick_validate.py](/Users/Igor/DemoHAI_V1/scripts/quick_validate.py)
- [scripts/normalize_skill.py](/Users/Igor/DemoHAI_V1/scripts/normalize_skill.py)
- [scripts/download_gmail_attachment.py](/Users/Igor/DemoHAI_V1/scripts/download_gmail_attachment.py)
- [scripts/extract_pdf_text.py](/Users/Igor/DemoHAI_V1/scripts/extract_pdf_text.py)

Они нужны как workshop-утилиты:
- `init_skill.py` создаёт стартовый каркас skill
- `quick_validate.py` делает быстрый sanity check после генерации

Это не обязательный первый шаг урока, но это наши осознанные repo-specific helpers.
