---
name: evaluate-resume-batch
description: Evaluate a small batch of resume summaries and produce a readable workshop scorecard with recommendation and rationale.
---

# Evaluate Resume Batch

## Goal

Дать короткую и читаемую оценку небольшому пакету кандидатов относительно явного hiring brief, чтобы результат можно было показать на уроке и отправить в Telegram.

## Inputs

- пакет кандидатов из `drafts/demo/resume_review_draft.md`
- hiring brief из `examples/demo_role_brief.md`

## Outputs

- финальный результат в `outputs/demo/resume_review.md`
- короткая scorecard по каждому кандидату относительно выбранной роли
- итоговая рекомендация

## Success Criteria

- оценка читается глазами за 1-2 минуты
- выводы опираются на реальные сигналы из письма или резюме
- выводы явно соотносятся с hiring brief, а не висят в вакууме
- есть короткая рекомендация, что делать дальше

## Out of Scope

- глубокий HR scoring framework
- автоматический hiring decision
- сравнение десятков кандидатов

## Procedure

1. Прочитай hiring brief из `examples/demo_role_brief.md`.
2. Прочитай пакет кандидатов.
3. Для каждого кандидата оцени:
  - match относительно роли
  - релевантность опыта
  - сильные стороны под эту вакансию
  - риски, пробелы или вопросы
4. Не оценивай “вообще хорош ли кандидат”; оцени, насколько он подходит именно под текущий hiring brief.
5. Собери компактную scorecard.
6. В конце добавь одну рекомендацию:
  - `позвать на следующий шаг`
  - `нужно уточнение`
  - `пока не приоритет`
7. Сохрани итог в `outputs/demo/resume_review.md`.

## Human Review

Если данных мало или hiring brief слишком общий, не делай сильных выводов. Лучше явно написать, чего не хватает для решения.

## Example Usage

`Оцени этот пакет резюме относительно demo role brief и дай короткую рекомендацию`
