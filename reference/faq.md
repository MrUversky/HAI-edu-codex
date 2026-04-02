# FAQ

Implementation note:
in this repo, reusable workshop runtime steps are implemented as Codex `skills`, even when the lesson explains them as agentic roles.

## When should I create a new skill instead of extending an existing one?
Create a new skill when the new job:
- needs a different role,
- needs different tools,
- needs different guardrails,
- or should be evaluated separately.

Extend an existing skill when the change is mostly formatting, a small policy change, or one more reusable rule.

## When should I use handoffs?
Use handoffs when you want the next specialist to become the active agent.
For workshop V1, prefer manager-style orchestration unless routing itself is what you want to teach.

## When should I use agents-as-tools?
Use agents-as-tools when one manager should keep control and specialists should only help on bounded subtasks.

## When do I need a validator?
Always, if the skill touches external systems, produces structured outputs used downstream, or could drift into too-broad solutions.

## How do I know a pilot is too broad?
It is too broad if it depends on multiple live integrations at once, has no clear owner, has no measurable output, or tries to transform an entire department at once.
