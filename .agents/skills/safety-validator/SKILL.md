---
name: safety-validator
description: Review a workshop skill for safety, guardrails, integration honesty, and risky external actions. Use inside the validation workflow when safety and external-system realism must be checked.
---

# Safety Validator

## Goal
Check whether the skill is honest about access, safe about outputs, and explicit about risky actions.

## Check
- Does the skill claim access it does not have?
- Are sensitive or external write actions gated?
- Are fallback and stub paths labeled clearly?
- Are risky outputs reviewed by a human?
- Are data handling and permissions defined well enough for workshop mode?

## Output
Return:
1. safety verdict: `pass`, `revise`, or `block`
2. sensitive-risk summary
3. missing guardrails
4. unsafe claims
5. required changes

## Hard fail conditions
- pretends a stub is a live integration
- external write path without approval
- undefined sensitive-data handling
- unsafe user-facing output without review
