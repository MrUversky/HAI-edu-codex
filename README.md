# HAI Edu Codex Workshop Repo

This repository is the working environment for the agent systems workshop.

The lesson logic is:
1. setup and light personalization
2. shared case hands-on
3. architecture unpacking
4. create or adapt a skill
5. validate the result
6. define one personal next step
7. submit and evaluate

## Main folders
- `workshop/` — lesson flows and operating logic
- `.agents/skills/` — canonical Codex runtime layer for the workshop
- `reference/` — best-practice help layer for Codex
- `agents/` — legacy source material for migrated workshop logic
- `validators/` — legacy validation source material used by `validate-skill`
- `practice/` — create/adapt-skill tasks and templates
- `participants/` — participant templates and outputs
- `evals/` — scoring logic
- `sources/` — verified source notes

## How to use this repo in Codex
Start from [setup-flow.md](/Users/Igor/DemoHAI_V1/workshop/setup-flow.md), then move through the flows in order.
Use [dispatch-catalog.md](/Users/Igor/DemoHAI_V1/workshop/dispatch-catalog.md) as the canonical mapping from short participant commands to workshop runtime steps.

Do not jump straight into the participant's personal business case.
First: observe.
Then: understand.
Then: touch the mechanics.
Only then: apply to self.

## Canonical runtime
The workshop now treats Codex `skills` as the canonical execution format.

Use these `v1` workshop skills:
- `.agents/skills/shared-case-intake/`
- `.agents/skills/shared-case-analysis/`
- `.agents/skills/shared-case-workflow/`
- `.agents/skills/shared-case-experiment/`
- `.agents/skills/task-register/`
- `.agents/skills/skill-builder/`
- `.agents/skills/validate-skill/`
- `.agents/skills/personal-next-step/`

Hybrid validation runtime:
- participant-facing validation entry: `.agents/skills/validate-skill/`
- internal orchestrator: `.codex/agents/validation-orchestrator.toml`
- validation support skills:
  - `.agents/skills/reviewer-role/`
  - `.agents/skills/safety-validator/`
  - `.agents/skills/architecture-validator/`
  - `.agents/skills/skill-structure-check/`

Treat `agents/*` and `validators/*` as legacy source material and references during the migration period.
