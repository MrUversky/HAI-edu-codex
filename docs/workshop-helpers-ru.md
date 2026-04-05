# Workshop Helpers

В repo есть несколько общих workshop helper scripts:

- [scripts/init_skill.py](/Users/Igor/DemoHAI_V1/scripts/init_skill.py)
- [scripts/quick_validate.py](/Users/Igor/DemoHAI_V1/scripts/quick_validate.py)
- [scripts/normalize_skill.py](/Users/Igor/DemoHAI_V1/scripts/normalize_skill.py)
- [scripts/download_gmail_attachment.py](/Users/Igor/DemoHAI_V1/scripts/download_gmail_attachment.py)
- [scripts/extract_pdf_text.py](/Users/Igor/DemoHAI_V1/scripts/extract_pdf_text.py)

## Network helpers

Некоторые workshop scripts ходят в сеть напрямую, а не через connector layer.

К ним относятся:
- [scripts/download_gmail_attachment.py](/Users/Igor/DemoHAI_V1/scripts/download_gmail_attachment.py)
- [send_telegram_message.py](/Users/Igor/DemoHAI_V1/.agents/skills/send-telegram-message/scripts/send_telegram_message.py)

Практическое правило:
- Gmail connector для поиска и чтения писем можно использовать в обычном режиме
- локальные helper scripts, которые сами делают HTTP-запросы к Gmail API или Telegram Bot API, нужно запускать сразу вне sandbox

Иначе первый запуск может падать не из-за логики repo, а из-за сетевого ограничения среды.

## init_skill.py

Нужен, чтобы быстро создать стартовый каркас нового skill по правилам этого workshop repo.

Он:
- создаёт skill folder
- создаёт `SKILL.md`
- подставляет канонические секции

## quick_validate.py

Нужен, чтобы быстро проверить generated skill.

Он:
- проверяет frontmatter
- проверяет обязательные секции
- проверяет ссылки на helper scripts
- предупреждает о сомнительных claims про внешние интеграции

## normalize_skill.py

Нужен для post-generation normalization после `/skill-creator`.

Он:
- исправляет сломанный frontmatter
- фиксирует каноническое имя skill
- оставляет body и секции на месте
- помогает быстро привести generated файл к workshop contract

## Важно

Это наши workshop-specific helpers.

Рекомендуемый порядок после `/skill-creator`:
1. запустить `quick_validate.py`
2. если сломаны имя или frontmatter, запустить `normalize_skill.py`
3. открыть `SKILL.md` и проверить содержательно

## Teacher demo helpers

Если у письма полезное содержимое лежит только в PDF-вложении:

1. скачать attachment через `download_gmail_attachment.py`
2. извлечь текст через `extract_pdf_text.py`
3. оценивать кандидата уже по тексту, а не только по body письма

Если Codex ссылается на такие скрипты, они должны реально существовать в этом repo. Если их нет, он не должен делать вид, что это обязательный путь.
