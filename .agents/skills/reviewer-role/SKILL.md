---
name: reviewer-role
description: Review a workshop skill for clarity of role, bounded scope, realistic inputs and outputs, and useful human review points. Use inside the validation workflow when role or usefulness must be checked.
---

# Reviewer Role

## Goal
Judge whether the skill has a clear job, a bounded scope, and a useful output contract.

## Check
- Is the purpose explicit?
- Is the job narrow enough for a first workshop pilot?
- Are the inputs realistic?
- Are the outputs explicit and useful?
- Is there a clear human review point?

## Output
Return:
1. verdict: `pass` or `revise`
2. strengths
3. scope risks
4. missing pieces
5. recommended revisions

## Hard fail conditions
- multiple unrelated jobs combined
- no clear output contract
- impossible inputs
- no bounded scope
