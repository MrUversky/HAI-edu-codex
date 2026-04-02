---
name: skill-builder
description: Guide a participant through creating or adapting one bounded workshop skill from a small set of approved scenarios. Use when the user wants to create a skill, adapt a skill, choose a skill scenario, or draft a new workshop skill for validation.
---

# Skill Builder

## Goal
Guide the participant through one bounded skill design and produce a draft skill spec ready for validation.

## Runtime Contract
- Step name: `Create or Adapt Skill`
- Reads from:
  - `practice/create_or_adapt_skill/task_options.md`
  - `practice/create_or_adapt_skill/skill_spec_template.md`
  - `practice/create_or_adapt_skill/integration_stub_template.md`
  - one selected scenario guide in `references/`
- Draft shown as: draft skill spec in chat
- Approved file path: `.agents/skills/<skill-name>/SKILL.md`
- Next step: `validate-skill`
- Human review question: `Подтвердить draft skill spec или уточнить?`

## Procedure
1. Announce the stage explicitly.
2. Offer only these four scenarios:
   - `telegram-digest`
   - `review-monitor`
   - `notion-sync`
   - `resume-analysis`
3. Ask one short practical question at a time.
4. Establish:
   - the repeated work situation
   - the usual inputs
   - the desired output
   - the human review point
   - whether the workshop should use direct input, export, guided integration, or a stub
5. Use the selected scenario guide to draft the skill.
6. Add fallback or integration notes only when needed.
7. Keep the first version narrow and ready for validation.

## Guardrails
- Do not offer a broad “build anything” flow.
- Do not force live integrations by default.
- Do not ask the participant to write code unless they explicitly want the optional technical layer.
- Do not skip validation.
