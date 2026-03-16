---
name: othmanadi-planning-with-files
description: "Claude Code skill implementing Manus-style persistent markdown planning — the workflow pattern"
homepage: https://github.com/OthmanAdi/planning-with-files
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["git", "npx", "skills"]
---

# Othmanadi Planning With Files

# Planning with Files

## Usage

Once installed, the AI agent will:

1. **Ask for your task** if no description is provided
2. **Create `task_plan.md`, `findings.md`, and `progress.md`** in your project directory
3. **Re-read plan** before major decisions (via PreToolUse hook)
4. **Remind you** to update status after file writes (via PostToolUse hook)
5. **Store findings** in `findings.md` instead of stuffing context
6. **Log errors** for future reference
7. **Verify completion** before stopping (via Stop hook)

Invoke with:

-
