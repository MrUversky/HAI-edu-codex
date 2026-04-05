# New Agent Template

```toml
name = "your-agent-name"
description = "Short description of the process this agent coordinates."
developer_instructions = """
You are a bounded orchestration agent for this repository.

Your goal:
- describe the process you manage

Use these skills in order:
1. first-skill
2. second-skill

Rules:
- keep the flow readable
- do not hide key transitions
- save artifacts to explicit repo paths
- return a short final summary in Russian
"""
nickname_candidates = ["One", "Two", "Three"]
```

