# Базовые Понятия

## Агент

Агент управляет процессом.

Он:
- решает, какой шаг идти следующим
- вызывает нужные skills
- собирает итог
- следит за переходами между шагами

В этом repo агентом является:
- [resume-processing-agent.toml](/Users/Igor/DemoHAI_V1/.codex/agents/resume-processing-agent.toml)

## Skill

Skill — это инструкция для повторяемой операции.

Хороший skill:
- имеет понятный вход
- имеет понятный выход
- ограничен по задаче
- не пытается быть системой на всё

В этом repo skills лежат в:
- [.agents/skills](/Users/Igor/DemoHAI_V1/.agents/skills)
- пример skill: [evaluate-resume-batch/SKILL.md](/Users/Igor/DemoHAI_V1/.agents/skills/evaluate-resume-batch/SKILL.md)

## Tool

Tool — это действие, которое агент или skill может выполнить.

Примеры:
- прочитать письмо
- сохранить markdown-файл
- отправить сообщение через API

В repo это можно увидеть на примере:
- Telegram adapter: [send_telegram_message.py](/Users/Igor/DemoHAI_V1/.agents/skills/send-telegram-message/scripts/send_telegram_message.py)

## MCP / интеграция

MCP или другая интеграция — это мост во внешний мир.

В этом repo:
- Gmail используется как live source для demo
- Telegram используется как live destination через тонкий adapter

Связанные файлы:
- demo agent: [resume-processing-agent.toml](/Users/Igor/DemoHAI_V1/.codex/agents/resume-processing-agent.toml)
- Telegram skill: [send-telegram-message/SKILL.md](/Users/Igor/DemoHAI_V1/.agents/skills/send-telegram-message/SKILL.md)
- demo examples: [gmail_resume_emails](/Users/Igor/DemoHAI_V1/examples/gmail_resume_emails)

## Один и тот же pipeline двумя способами

Человекочитаемо:

`взять письмо -> собрать пакет кандидата -> оценить -> отправить итог`

Технически:

`Gmail -> fetch-gmail-resumes -> evaluate-resume-batch -> send-telegram-message`

## Почему это разделено

Так участнику легче понять:
- где процесс
- где повторяемая инструкция
- где внешнее действие
