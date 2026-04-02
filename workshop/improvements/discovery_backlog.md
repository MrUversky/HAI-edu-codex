# Discovery Backlog

## External scoring loop for participant outputs

### Objective
Собрать артефакты участников, отправить во внешний сервис оценки, получить score/комментарии обратно и сохранить локально.

### Open questions
1. Какие артефакты обязательны для отправки (`participant_setup`, `created_or_adapted_agent`, `validation_report`, `final_action_card`)?
2. В каком формате отправляем пакет (JSON, zip, markdown bundle)?
3. Какая схема ответа сервиса (общий verdict, category scores, comments)?
4. Как выполняется отправка из workshop-репо (CLI script, webhook, API client)?
5. Где сохраняем результат локально (`participants/<name>/evaluation/`)?
6. Нужен ли повторный запуск оценки и версия результатов?

### Minimal pilot proposal
- Export: собрать markdown-артефакты участника в единый JSON payload.
- Send: POST в внешний endpoint.
- Receive: verdict + scores + comments.
- Save: `participants/<name>/evaluation/eval_<date>.md`.

### Status
captured, not implemented
