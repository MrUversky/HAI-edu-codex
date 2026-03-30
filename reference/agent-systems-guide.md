# Agent Systems Guide (March 2026, workshop edition)

This guide is a workshop-adapted synthesis grounded in official GitHub-visible materials from:
- OpenAI Agents SDK (`openai/openai-agents-python`)
- Anthropic Claude Cookbooks (`anthropics/claude-cookbooks`)
- Google Gemini API Cookbook (`google-gemini/cookbook`)

Where this file gives a recommendation for **this workshop architecture**, that recommendation is an adaptation on top of vendor materials, not a verbatim vendor claim.

## What is an agent in practical terms?

For this workshop, an agent is not just any prompt.
An agent has:
1. a role
2. a job to be done
3. known inputs
4. constrained outputs
5. optional tools
6. optional handoffs or sub-agents
7. guardrails
8. a clear point where human judgment stays in the loop

## The most useful orchestration split

OpenAI's official docs distinguish between:
- LLM-led orchestration
- code-led orchestration

For this workshop, the safest default is **hybrid orchestration**:
- code decides the macro-flow of the lesson
- the model does bounded reasoning inside each step

This is easier to teach, debug, and recover live.

## The two most important multi-agent patterns

### Agents as tools
A manager agent keeps control and calls specialist agents as bounded helpers.
Use this when one manager should own the final answer and central guardrails matter.

### Handoffs
A triage or router agent routes the turn to a specialist, and that specialist becomes active.
Use this when routing itself is part of the workflow.

### Workshop recommendation
Use manager + agents-as-tools for the shared demo.
Use handoffs sparingly, mainly when teaching routing explicitly.

## When to use one agent vs several

Keep one agent when the task is narrow and outputs are simple.
Split into several agents when:
- different steps need different instructions or tools
- one part is analytical and another executional
- review should be separate from generation
- a clean handoff improves repeatability

A good rule:
Split when the boundary improves quality, safety, or repeatability — not just elegance.

## Skills vs tools vs agents

- **Skills** are reusable procedures or rule sets.
- **Tools** fetch or act.
- **Agents** are reasoning units with role framing and output contracts.

If logic is reusable, procedural, and stable, it is often a skill rather than a full agent.

## Guardrails in practice

OpenAI explicitly distinguishes input, output, and tool guardrails.
For this workshop, validate on 3 layers:
1. input safety and scope
2. tool or integration safety
3. output completeness and structure

## Human in the loop

Do not remove human judgment too early.
Keep approval points before:
- real write-back into systems
- customer-facing communications
- ambiguous business decisions
- pilots with too much scope

## Sessions, memory, and state

For a live workshop, prefer visible file-backed state over opaque hidden memory.
Examples:
- `participant_setup.md`
- `personal_next_step.md`
- `final_action_card.md`

This is better for teaching and recovery.

## Structured outputs and evals

Across OpenAI and Anthropic materials, structured outputs and evals are not optional if you want reliable agent systems.
Every serious workshop agent should be evaluable on at least:
- clarity
- usefulness
- scope discipline
- structure
- safety
- architectural fit

## Grounding and observability

Google's official cookbook strongly emphasizes grounding, file search, code execution, browser-as-tool, logs and datasets.
The broad lesson is simple:
agentic quality comes from grounded, tool-augmented, inspectable work — not from generic prompting alone.
