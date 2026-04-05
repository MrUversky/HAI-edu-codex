# Карта Урока

## Зачем нужен этот repo

Он помогает показать агентный подход на маленьком и читаемом примере.

## Маршрут урока

### Поток преподавателя

1. `setup`
- собрать лёгкий контекст участника
- сохранить `participants/<name>/participant_setup.md`

2. `world model`
- объяснить разницу между agent, skill, tool и MCP

3. `demo`
- запустить `resume-processing-agent`
- показать полный workflow `Gmail -> resume evaluation -> Telegram`

4. `architecture`
- коротко показать, из каких слоёв собран demo

### Поток участника

1. `setup`
- собрать лёгкий контекст участника
- сохранить `participants/<name>/participant_setup.md`

2. `world model`
- объяснить разницу между agent, skill, tool и MCP

3. `exercise`
- собрать контракт нового skill через вопросы в чате
- подготовить prompt для `/skill-creator`
- запустить `/skill-creator`
- прогнать `scripts/quick_validate.py`
- если нужно, нормализовать имя и frontmatter через `scripts/normalize_skill.py`
- открыть созданный `SKILL.md` и проверить контракт
- свериться с reference skill
- прогнать созданный skill на `examples/meeting_raw.txt`
- показать результат на экране и сохранить `outputs/exercise/meeting_actions.md`
- при необходимости передать Telegram token и chat id через чат Codex для локального сохранения в `.env.local`
- отправить блок задач через `send-telegram-message`

## Ожидаемые артефакты

- `participants/<name>/participant_setup.md`
- `outputs/demo/resume_review.md`
- `outputs/demo/telegram_message.md`
- `outputs/exercise/meeting_actions.md`
