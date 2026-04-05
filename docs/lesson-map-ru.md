# Карта Урока

## Зачем нужен этот repo

Он помогает показать агентный подход на маленьком и читаемом примере.

## Маршрут урока

1. `setup`
- собрать лёгкий контекст участника
- сохранить `participants/<name>/participant_setup.md`

2. `world model`
- объяснить разницу между agent, skill, tool и MCP

3. `demo`
- запустить `resume-processing-agent`
- показать полный workflow `Gmail -> resume evaluation -> Telegram`

4. `exercise`
- собрать контракт нового skill через вопросы в чате
- подготовить prompt для `/skill-creator`
- запустить `/skill-creator`
- открыть созданный `SKILL.md` и проверить контракт
- свериться с reference skill
- прогнать созданный skill на `examples/meeting_raw.txt`
- сохранить `outputs/exercise/meeting_actions.md`
- отправить блок задач через `send-telegram-message`

5. `after lesson`
- показать участнику, как выбрать одну повторяющуюся рабочую ситуацию и сделать свой первый bounded skill

## Ожидаемые артефакты

- `participants/<name>/participant_setup.md`
- `outputs/demo/resume_review.md`
- `outputs/demo/telegram_message.md`
- `outputs/exercise/meeting_actions.md`
