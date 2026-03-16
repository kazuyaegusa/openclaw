---
name: jarrodwatts-claude-hud
description: "A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and"
homepage: https://github.com/jarrodwatts/claude-hud
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["git", "npm"]
---

# Jarrodwatts Claude Hud

# Claude HUD

## Installation

Inside a Claude Code instance, run the following commands:

**Step 1: Add the marketplace**

```
/plugin marketplace add jarrodwatts/claude-hud
```

**Step 2: Install the plugin**

<details>
<summary><strong>⚠️ Linux users: Click here first</strong></summary>

On Linux, `/tmp` is often a separate filesystem (tmpfs), which causes plugin installation to fail with:

```
EXDEV: cross-device link not permitted
```

**Fix**: Set TMPDIR before installing:

```bash
mkdir -p ~/.cache/tmp && TMPDIR=~/.cache/



```
