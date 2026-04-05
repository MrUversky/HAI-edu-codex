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

### 4. Example and artifact layer

Файлы:
- [examples](/Users/Igor/DemoHAI_V1/examples)
- [drafts](/Users/Igor/DemoHAI_V1/drafts)
- [outputs](/Users/Igor/DemoHAI_V1/outputs)

Роль:
- показать глазами вход
- показать промежуточный результат
- показать финальный результат

## Поток demo

`Gmail -> fetch-gmail-resumes -> evaluate-resume-batch -> send-telegram-message`

Оркеструет:
- `resume-processing-agent`

## Поток exercise

`meeting_raw.txt -> extract-meeting-actions -> outputs/exercise/meeting_actions.md -> send-telegram-message`

Оркестрация здесь ручная, чтобы участник увидел композицию skills.
