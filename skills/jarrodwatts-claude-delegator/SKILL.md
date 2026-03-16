---
name: jarrodwatts-claude-delegator
description: "Delegate tasks to Codex GPT 5.2 directly from within Claude Code."
homepage: https://github.com/jarrodwatts/claude-delegator
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["codex", "gemini-cli", "git", "node", "npm"]
---

# Jarrodwatts Claude Delegator

# Claude Delegator

## Installation

Inside a Claude Code instance, run the following commands:

**Step 1: Add the marketplace**

```
/plugin marketplace add jarrodwatts/claude-delegator
```

**Step 2: Install the plugin**

```
/plugin install claude-delegator
```

**Step 3: Run setup**

```
/claude-delegator:setup
```

Done! Claude now routes complex tasks to GPT experts automatically.

> **Note**: Requires [Codex CLI](https://github.com/openai/codex) or [Gemini CLI](https://github.com/google/gemini-cli). Setup guides you through ins
