---
name: validate-skill
description: Validate a created or adapted workshop skill and generate a structured validation report. Use when the user asks to validate a skill, check a created skill, run validation, or produce a validation_report.md for a workshop skill.
---

# Validate Skill

## Goal
Run the workshop validation workflow over a created or adapted skill and return one clear validation report.

Internal orchestrator:
- `.codex/agents/validation-orchestrator.toml`

## Runtime Contract
- Step name: `Validate Skill`
- Reads from:
  - target skill folder in `.agents/skills/<skill-name>/`
  - `SKILL.md`
  - optional `references/` or `scripts/`
  - optional integration or stub notes if present
- Draft shown as: concise findings summary in chat
- Approved file path: `.agents/skills/<skill-name>/validation_report.md`
- Human review question: `Сохранить validation report или сначала внести правки?`

## Procedure
1. Identify the target skill folder.
2. Read the target `SKILL.md` and any directly relevant bundled resources.
3. Hand off runtime orchestration to `.codex/agents/validation-orchestrator.toml`.
4. Evaluate the skill against:
   - role clarity and scope
   - reusable logic and extractability
   - safety and integration realism
   - architectural fit
   - canonical skill layout
   - required artifacts and handoff pattern
5. Produce one structured validation report with verdict, strengths, required revisions, and total score.
6. Show the report as a draft first.
7. Save the approved report to `.agents/skills/<skill-name>/validation_report.md` only after explicit approval or a direct save request.

## Required Checks
- `SKILL.md` uses valid skill frontmatter with `name` and `description`.
- The skill has a clear trigger description, input/output contract, and human review path where needed.
- The skill does not claim live access it does not actually have.
- Optional integrations are either real, clearly guided, or explicitly marked as fallback/stub.
- The skill fits the lesson architecture and does not sprawl into a broad transformation.

## Handoff
Use this skill as the participant-facing validation entrypoint. Treat `.codex/agents/validation-orchestrator.toml` as the internal runtime coordinator, and treat `validators/*` plus `evals/run_evaluation_flow.md` as source material for the evaluation logic.
