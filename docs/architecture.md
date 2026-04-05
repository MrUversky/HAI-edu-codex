# Архитектура Repo

## Основные слои

### 1. Agent layer

Файлы:
- [.codex/agents](/Users/Igor/DemoHAI_V1/.codex/agents)

Роль:
- orchestration нескольких шагов
- короткий запуск через короткую команду пользователя

### 2. Skill layer

Файлы:
- [.agents/skills](/Users/Igor/DemoHAI_V1/.agents/skills)

Роль:
- повторяемые bounded operations
- понятные входы и выходы

### 3. Adapter / integration layer

Роль:
- тонкий доступ во внешний мир
- без бизнес-логики

Пример:
- [send_telegram_message.py](/Users/Igor/DemoHAI_V1/.agents/skills/send-telegram-message/scripts/send_telegram_message.py)

Live Telegram для workshop:
- значения можно передать через чат Codex
- затем они должны быть сохранены только локально в `.env.local`
- `.env.local` не должен попадать в git

### 4. Workshop helper layer

Файлы:
- [scripts/init_skill.py](/Users/Igor/DemoHAI_V1/scripts/init_skill.py)
- [scripts/quick_validate.py](/Users/Igor/DemoHAI_V1/scripts/quick_validate.py)

Роль:
- создать стартовый каркас нового skill
- быстро проверить generated skill на соответствие workshop contract

### 5. Example and artifact layer

Файлы:
- [examples](/Users/Igor/DemoHAI_V1/examples)
- [drafts](/Users/Igor/DemoHAI_V1/drafts)
- [outputs](/Users/Igor/DemoHAI_V1/outputs)

Роль:
- показать глазами вход
- показать промежуточный результат
- показать финальный результат

Для demo сюда также входит явный hiring brief:
- [demo_role_brief.md](/Users/Igor/DemoHAI_V1/examples/demo_role_brief.md)

## Поток demo

`Gmail -> fetch-gmail-resumes -> demo_role_brief -> evaluate-resume-batch -> send-telegram-message`

Оркеструет:
- `resume-processing-agent`

Если резюме лежит только в PDF-вложении, teacher demo может добавлять локальный attachment path:

`Gmail -> download attachment -> extract PDF text -> evaluate-resume-batch`

## Поток exercise

Человекочитаемо:

`взять заметки встречи -> собрать задачи, вопросы и риски -> показать и сохранить результат -> отправить блок задач`

Технически:

`meeting_raw.txt -> <generated skill> -> outputs/exercise/meeting_actions.md -> send-telegram-message`

Оркестрация здесь ручная, чтобы участник увидел композицию skills.
