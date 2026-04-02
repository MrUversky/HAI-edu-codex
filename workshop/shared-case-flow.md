# Shared Case Flow

Goal: everyone runs a shared skill chain on common data and sees how bounded skills hand work to one another.

Sequence:
1. `shared-case-intake`
2. `shared-case-analysis`
3. `shared-case-workflow`
4. `shared-case-experiment`
5. `task-register`

Outputs:
- structured_inputs.md
- signal_map.md
- workflow_draft.md
- pilot_card.md
- task_register.md
- shared_case_state.md

Runtime pattern for every step:
1. run one skill,
2. inspect the draft,
3. approve or revise,
4. save the approved artifact,
5. pass the approved artifact to the next skill.

Canonical runtime files:
- dispatch mapping: `workshop/dispatch-catalog.md`
- state summary: `shared_case/outputs/shared_case_state.md`

Operating model:
- `Ведущий` показывает, какой шаг цепочки идёт сейчас и какой артефакт должен появиться.
- `Участник` запускает тот же шаг локально у себя.
- `Codex-помощник` выполняет skill step, показывает draft, сохраняет approved artifact и называет следующий шаг.

Teaching emphasis:
- skills are bounded roles, not magic;
- handoff matters;
- the workflow is grounded in shared data;
- the point is to understand mechanics before applying them personally;
- the process should feel like a chain of approved artifacts, not a long chat.

Stage transitions:
- Before each step, state:
  - current stage
  - completed artifacts
  - current skill
  - next expected artifact
- Use `shared_case/outputs/shared_case_state.md` as the default source of truth for "what is next".

Participant-facing commands:
- `запусти shared case`
- `обработай сырые данные`
- `покажи следующий шаг`
- `сделай task register`
