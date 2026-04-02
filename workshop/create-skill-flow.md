# Create or Adapt Skill Flow

Goal: participants either:
1. create one bounded skill for their own repeated work situation,
2. or adapt one of the offered workshop skill scenarios.

Stage framing:
- Current stage: `create or adapt skill`
- What is already done: setup, shared case, architecture unpacking
- What we are doing now: design one bounded participant skill
- Expected artifact: `.agents/skills/<skill-name>/SKILL.md`

Participant-facing start:
- `помоги создать skill`
- `хочу адаптировать skill`
- `давай выберем skill-сценарий`

Participant flow:
1. announce the stage explicitly;
2. use `.agents/skills/skill-builder/SKILL.md` as the guided runtime entrypoint;
3. offer a short scenario catalog;
3. ask one practical question at a time;
4. draft the skill in markdown;
5. add integration or fallback notes only if needed;
6. send the draft to validation.

Required outputs:
- one skill folder in `.agents/skills/<skill-name>/`,
- `SKILL.md`,
- optional integration or stub notes,
- `validation_report.md`.

Scenario catalog for `v1.1`:
- `telegram-digest`
- `review-monitor`
- `notion-sync`
- `resume-analysis`

Important:
- use one bounded scenario, not a broad system;
- live integrations are optional and must be labeled clearly;
- validation is mandatory before final submission.
