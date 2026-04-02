# V1.1 Runtime Smoke Test

Purpose: record one end-to-end dry run over the new runtime entrypoints after the `v1.1` stabilization pass.

## Scope
Checked:
- stage order
- dispatch entrypoints
- shared-case chain
- `task-register` handoff
- hybrid validation wiring
- guided personal-next-step entry

Not checked:
- external scoring/export loop
- live MCP integrations
- multi-participant facilitation timing under real workshop pressure

## Walkthrough result

### 1. Setup
- Entry used: `workshop/setup-flow.md`
- Participant-facing trigger tested: `Давай начнем setup`
- Expected artifact: `participants/<name>/participant_setup.md`
- Status: pass

### 2. Shared case hands-on
- Entry used: `workshop/shared-case-flow.md`
- Dispatch source: `workshop/dispatch-catalog.md`
- Participant-facing triggers tested:
  - `запусти shared case`
  - `обработай сырые данные`
  - `покажи следующий шаг`
- Expected artifacts:
  - `structured_inputs.md`
  - `signal_map.md`
  - `workflow_draft.md`
  - `pilot_card.md`
  - `task_register.md`
  - `shared_case_state.md`
- Status: pass

### 3. Architecture unpacking
- Entry used: `workshop/architecture-unpacking-flow.md`
- Expected teaching focus: explain the five-skill chain and the `draft -> review -> approve -> save -> handoff` pattern
- Status: pass

### 4. Create or adapt skill
- Entry used: `workshop/create-skill-flow.md`
- Runtime entry skill: `.agents/skills/skill-builder/SKILL.md`
- Participant-facing triggers tested:
  - `помоги создать skill`
  - `хочу адаптировать skill`
- Scenario coverage checked:
  - `telegram-digest`
  - `review-monitor`
  - `notion-sync`
  - `resume-analysis`
- Status: pass

### 5. Validation
- Participant-facing entry: `.agents/skills/validate-skill/SKILL.md`
- Internal orchestrator: `.codex/agents/validation-orchestrator.toml`
- Validation skills checked:
  - `reviewer-role`
  - `safety-validator`
  - `architecture-validator`
  - `skill-structure-check`
- Expected artifact: `.agents/skills/<skill-name>/validation_report.md`
- Status: pass

### 6. Personal next step
- Entry used: `workshop/personal-next-step-flow.md`
- Participant-facing trigger tested: `помоги мне определить следующий шаг`
- Expected artifacts:
  - `participants/<name>/personal_next_step.md`
  - `participants/<name>/final_action_card.md`
- Status: pass

## Findings
1. The new runtime path is coherent from `setup` through `personal next step`.
2. `task-register` closes the main shared-case gap and makes the flow feel more operational.
3. `dispatch-catalog.md` is now the main glue layer for short participant commands.
4. Hybrid validation is structurally wired correctly; real live usage should still be observed in the next workshop pass.
5. Stage framing is now explicit in the main flow files, but facilitator delivery quality still depends on live pacing.

## Remaining follow-up
1. Run one real facilitator dry run using the new wording exactly as written.
2. Capture any remaining participant-facing phrasing friction back into `feedback_log.md`.
3. Decide whether to add an external scoring/export loop in the next iteration.
