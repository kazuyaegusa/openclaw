---
name: frankbria-ralph-claude-code
description: "Autonomous AI development loop for Claude Code with intelligent exit detection"
homepage: https://github.com/frankbria/ralph-claude-code
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["bats", "claude-code", "coreutils", "curl", "git", "jq", "npm", "npx", "tmux"]
---

# Frankbria Ralph Claude Code

# Ralph for Claude Code

## Usage

Ralph has two phases: **one-time installation** and **per-project setup**.

```
INSTALL ONCE              USE MANY TIMES
+-----------------+          +----------------------+
| ./install.sh    |    ->    | ralph-setup project1 |
|                 |          | ralph-enable         |
| Adds global     |          | ralph-import prd.md  |
| commands        |          | ...                  |
+-----------------+          +----------------------+
```
