---
name: skill-structure-check
description: Check whether a workshop skill follows the canonical Codex skill layout and runtime contract. Use inside the validation workflow when structure, file layout, handoff, and required artifacts must be checked.
---

# Skill Structure Check

## Goal
Verify that the skill is laid out and documented in the canonical workshop format.

## Check
- Is the skill in `.agents/skills/<skill-name>/`?
- Does it contain a valid `SKILL.md` with `name` and `description` frontmatter?
- Does the skill define input/output contract?
- Does it define a human review point?
- Does it define approved artifact and handoff logic where relevant?
- Are optional `references/` and `scripts/` placed correctly?
- Is there enough fallback or integration guidance if an external system is involved?

## Output
Return:
1. structure verdict: `pass` or `revise`
2. layout issues
3. missing artifacts
4. handoff issues
5. required structural fixes

## Hard fail conditions
- missing `SKILL.md`
- invalid frontmatter
- no runtime contract for a workflow skill
- no human review point where one is required
