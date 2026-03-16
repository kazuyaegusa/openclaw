---
name: baryhuang-claude-code-by-agents
description: "Desktop app and API created in public for multi-agent Claude Code orchestration - coordinate local"
homepage: https://github.com/baryhuang/claude-code-by-agents
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["git", "npm"]
---

# Baryhuang Claude Code By Agents

# Claude Code Agentrooms UI + Remote Claude Code API

## Usage

**Single agent**: `@api-agent add user authentication`

- Direct HTTP call to agent endpoint
- No coordination overhead

**Multi-agent**: `"Create full auth system with frontend and backend"`

- Orchestrator analyzes and creates execution plan
- Coordinates file-based communication between agents
- Manages dependencies automatically
