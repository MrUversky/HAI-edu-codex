# Branching Strategy (Workshop)

Goal: разделять изменения каркаса урока и данные конкретных прогонов.

## Branch types
1. Framework branch
- Prefix: `codex/framework-...`
- Contains: только улучшения lesson framework (flows, templates, validators, scripts, prompts).

2. Session data branch
- Prefix: `codex/run-...`
- Contains: только артефакты прогонов (participant files, run outputs, draft notes).

## Path ownership
- Framework-only paths:
  - `workshop/`
  - `facilitator/`
  - `agents/`
  - `validators/`
  - `evals/`
  - `reference/`
  - `practice/`
  - `submissions/templates/`

- Session-data paths:
  - `participants/<name>/`
  - `shared_case/outputs/` (только если это результат прогона, не канонический шаблон)

## Commit rule
- Never mix framework + session data in one commit.
- If mixed locally, split by staging paths and create separate commits.

## Feedback flow
1. Capture observations in `workshop/improvements/feedback_log.md`.
2. Shortlist and convert to concrete patch tasks.
3. Implement on framework branch.
4. Keep run artifacts in session-data branch.
