---
name: qdhenry-claude-command-suite
description: "Professional slash commands for Claude Code that provide structured workflows for software"
homepage: https://github.com/qdhenry/Claude-Command-Suite
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["curl", "git"]
---

# Qdhenry Claude Command Suite

# Claude Command Suite

## Usage

**Triggering skills:**

```
"What do I need to work on today?"  # Activates linear-todo-sync
"Deploy a cloudflare worker"        # Activates cloudflare-manager
"Set up WebMCP in this project"     # Activates webmcp
"Transcribe this audio file"        # Activates elevenlabs-transcribe
"Find and remove dead code"         # Activates remove-dead-code
```

**Creating skills:**

```
/skills:build-skill
```

**Documentation:**

- [Quick Start Guide](.claude/commands/skills/QUICKSTART.md) - Skill creation
