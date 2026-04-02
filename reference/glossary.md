# Glossary

- **Agentic role**: a role-bounded reasoning unit with instructions, optional tools, and defined outputs. In this repo, these roles are usually implemented as skills.
- **Tool**: an action or retrieval capability a skill or agentic role can call.
- **Skill**: the canonical Codex runtime format for a reusable workflow, procedure, or bounded role in this repo.
- **Handoff**: passing an approved artifact or control point from one bounded step to another.
- **Agents-as-tools**: calling a specialist helper while a manager or orchestrator retains control.
- **Guardrail**: a validation or safety check on input, tool invocation, or output.
- **Tripwire**: a condition that blocks or halts execution when violated.
- **Evaluator / Validator**: a reviewing agent or pipeline that scores quality, safety, and fitness.
- **Tracing**: capturing structured visibility into runs, steps, and outputs.
- **Grounding**: anchoring outputs in external data, files, search, or other verifiable context.
- **Prompt caching**: reusing large stable context instead of rebuilding it every run.
