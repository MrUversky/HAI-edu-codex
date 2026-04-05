---
name: evaluate-resume-batch
description: Evaluate a small batch of resume summaries and produce a readable workshop scorecard with recommendation and rationale.
---

# Evaluate Resume Batch

## Goal

Дать короткую и читаемую оценку небольшому пакету кандидатов, чтобы результат можно было показать на уроке и отправить в Telegram.

## Inputs

- пакет кандидатов из `drafts/demo/resume_review_draft.md`
- контекст вакансии или критериев, если он есть в письме

## Outputs

- финальный результат в `outputs/demo/resume_review.md`
- короткая scorecard по каждому кандидату
- итоговая рекомендация

## Success Criteria

- оценка читается глазами за 1-2 минуты
- выводы опираются на реальные сигналы из письма или резюме
- есть короткая рекомендация, что делать дальше

## Out of Scope

- глубокий HR scoring framework
- автоматический hiring decision
- сравнение десятков кандидатов

## Procedure

1. Прочитай пакет кандидатов.
2. Для каждого кандидата оцени:
   - релевантность роли
   - качество опыта
   - заметные сильные стороны
   - риски или пробелы
3. Собери компактную scorecard.
4. В конце добавь одну рекомендацию:
   - `позвать на следующий шаг`
   - `нужно уточнение`
   - `пока не приоритет`
5. Сохрани итог в `outputs/demo/resume_review.md`.

## Human Review

Если данных мало, не делай сильных выводов. Лучше явно написать, чего не хватает.

## Example Usage

`Оцени этот пакет резюме и дай короткую рекомендацию`
