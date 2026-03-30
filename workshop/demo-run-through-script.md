# Codex Demo Run-Through Script

## Goal
Use this script to run one complete workshop path inside Codex without improvising the structure.

## Start prompt for Codex

```text
Read README.md, AGENTS.md and WORKSHOP_BUILD_TRACKER.md first.
Then read the files in workshop/ in the intended order.
Act as a workshop guide.
Do not jump to my personal use case too early.
First help me orient myself, then move me through the shared case, then mini-practice, then create/adapt-agent, then validation, and only then personal next step.
Be practical, concise, and file-oriented.
Always tell me which file we are using.
```

## Recommended run order

### Step 1. Orientation
Ask Codex:

```text
Read README.md, AGENTS.md, workshop/setup-flow.md and explain the lesson path to me in 6–8 bullets.
```

### Step 2. Setup
Ask Codex:

```text
Run the setup flow with me using participants/templates/participant_setup_template.md.
Ask one question at a time and create participants/demo_user/participant_setup.md.
```

### Step 3. Shared case
Ask Codex:

```text
Read workshop/shared-case-flow.md and the files in shared_case/inputs/.
Then explain what each core agent should do before showing me the prepared outputs in shared_case/outputs/.
```

### Step 4. Architecture unpacking
Ask Codex:

```text
Using agents/core/*.md and shared_case/outputs/*, explain why the workflow is split across four agents instead of one.
Keep it practical.
```

### Step 5. Mini-practice
Ask Codex:

```text
Pick one file from practice/mini_cases/ and guide me through one small transformation only.
Do not overcomplicate it.
```

### Step 6. Create or adapt agent
Ask Codex:

```text
Read workshop/create-agent-flow.md, practice/create_or_adapt_agent/task_options.md and agents/elective/*.
Help me choose one elective agent to adapt.
Then use practice/create_or_adapt_agent/agent_spec_template.md to draft a first version.
```

### Step 7. Add stub integration if needed
Ask Codex:

```text
If my agent needs an external system, use one of the integration stub examples in practice/create_or_adapt_agent/stubs/ and help me adapt it safely.
```

### Step 8. Validation
Ask Codex:

```text
Run the evaluation sequence from evals/run_evaluation_flow.md against my created_or_adapted_agent.md and produce a validation report.
```

### Step 9. Personal next step
Ask Codex:

```text
Now switch to workshop/personal-next-step-flow.md.
Use participants/templates/personal_next_step_template.md and participants/templates/final_action_card_template.md.
Help me identify one realistic next step only.
```

## Facilitator note
If the live run starts drifting, stop and reset to the current stage. The order matters more than stylistic smoothness.
