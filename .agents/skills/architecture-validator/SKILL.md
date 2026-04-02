---
name: architecture-validator
description: Review a workshop skill for architectural fit, layering, and lesson alignment. Use inside the validation workflow when the skill may be too broad, split incorrectly, or mismatched to the workshop flow.
---

# Architecture Validator

## Goal
Check whether the skill is the right size and shape for the workshop architecture.

## Check
- Should this be one skill or several?
- Is the skill trying to do planning, execution, validation, and approval together?
- Does it fit the lesson flow cleanly?
- Does it have a clear place in the larger chain?
- Is there a missing human checkpoint or downstream handoff?

## Output
Return:
1. architecture verdict
2. better pattern if needed
3. overengineering risks
4. underengineering risks
5. suggested topology

## Hard fail conditions
- one skill doing planning, execution, validation, and approval together
- multi-step split with no meaningful role boundaries
- no evaluation path for high-stakes output
