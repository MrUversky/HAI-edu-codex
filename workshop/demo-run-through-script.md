# Codex Demo Run-Through Script

## Goal
Use this script to run one complete workshop path inside Codex without improvising the structure.

## Start prompt for Codex

```text
Read README.md, AGENTS.md and WORKSHOP_BUILD_TRACKER.md first.
Then read the files in workshop/ in the intended order, starting with workshop/dispatch-catalog.md.
Act as a workshop guide.
Do not jump to my personal use case too early.
First help me orient myself, then move me through the shared case hands-on, then architecture unpacking, then create/adapt-skill, then validation, and only then personal next step.
Be practical, concise, and file-oriented.
Always tell me which file we are using.
Use Russian in participant-facing guidance.
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
Read workshop/shared-case-flow.md, workshop/dispatch-catalog.md, .agents/skills/shared-case-*/SKILL.md, .agents/skills/task-register/SKILL.md and the files in shared_case/inputs/.
Then run the shared-case skill chain with me step by step, showing a draft first and saving only approved artifacts to shared_case/run_outputs/.
```

### Step 4. Architecture unpacking
Ask Codex:

```text
Using workshop/architecture-unpacking-flow.md, .agents/skills/shared-case-*/SKILL.md, .agents/skills/task-register/SKILL.md and shared_case/run_outputs/*, explain why the workflow is split across several skills instead of one long chat.
Keep it practical.
```

### Step 5. Create or adapt skill
Ask Codex:

```text
Read workshop/create-skill-flow.md, workshop/dispatch-catalog.md and .agents/skills/skill-builder/SKILL.md.
Help me choose one skill scenario and then use practice/create_or_adapt_skill/skill_spec_template.md to draft a first version.
```

### Step 6. Add integration or fallback notes if needed
Ask Codex:

```text
If my skill needs an external system, use practice/create_or_adapt_skill/integration_stub_template.md and help me document the safest fallback.
```

### Step 7. Validation
Ask Codex:

```text
Use workshop/dispatch-catalog.md, .agents/skills/validate-skill/SKILL.md and .codex/agents/validation-orchestrator.toml to validate my created skill and produce a validation report.
Make the validation agent visible and show a short validation trace before the final report.
```

### Step 8. Practice check
Ask Codex:

```text
If the skill is ready, run one practical check on one real or test input and save the skill-specific runtime artifact only after approval.
```

### Step 9. Personal next step
Ask Codex:

```text
Now switch to workshop/personal-next-step-flow.md and .agents/skills/personal-next-step/SKILL.md.
Use participants/templates/personal_next_step_template.md and participants/templates/final_action_card_template.md.
Help me identify one realistic next step only.
```

## Facilitator note
If the live run starts drifting, stop and reset to the current stage. The order matters more than stylistic smoothness.
