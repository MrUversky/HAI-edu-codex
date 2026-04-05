---

## name: send-telegram-message
description: Prepare a compact Telegram message from a bounded text block and send it through the shared Telegram adapter with live or dry-run mode.

# Send Telegram Message

## Goal

Подготовить короткое сообщение для Telegram и отправить его через общий adapter или сохранить dry-run результат.

## Inputs

- готовый текстовый блок
- краткий summary из demo или блок `Задачи` из exercise
- live Telegram settings, если они доступны

## Outputs

- итоговый текст сообщения в `outputs/demo/telegram_message.md` или `outputs/exercise/telegram_message.md`
- при dry-run: зафиксированный статус, что сообщение не было отправлено live

## Success Criteria

- сообщение короткое и читаемое
- текст подходит для группового чата
- live send и dry-run различаются явно

## Out of Scope

- сложная логика маршрутизации по множеству чатов
- форматирование на уровне полноценного notification service
- управление самим ботом

## Procedure

1. Возьми bounded текстовый блок.
2. Сожми его до короткого сообщения для группы.
3. Проверь, что в сообщении нет лишней служебной информации.
4. Если live Telegram settings доступны, отправь сообщение через adapter.
5. Если live send недоступен, сохрани dry-run результат и явно отметь это.
6. Сохрани итоговый текст в соответствующий файл outputs.

## Human Review

Перед live send можно показать финальный текст, если пользователь явно просит review. Для demo допускается silent send с финальным отчётом в конце.

## Example Usage

`Отправь это краткое сообщение в Telegram`