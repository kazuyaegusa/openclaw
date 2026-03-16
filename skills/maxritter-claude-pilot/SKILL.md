---
name: maxritter-claude-pilot
description: "Claude Code is powerful. Pilot makes it reliable. Start a task, grab a coffee, come back to"
homepage: https://github.com/maxritter/claude-pilot
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["curl", "git", "go"]
---

# Maxritter Claude Pilot

<div align="center">

<img src="docs/img/logo.png" alt="Pilot Shell" width="400">

**The professional development environment for [Claude Code](https://docs.anthropic.com/en/docs/claude-code)**

## Installation

**Works with any existing project.** Pilot Shell doesn't scaffold or restructure your code — it installs globally and adapts to your conventions.

```bash
curl -fsSL https://raw.githubusercontent.com/maxritter/pilot-shell/main/install.sh | bash
```

Installs globally on macOS, Linux, and Windows (WSL2). All tools and rules go to `~/.pilot/` and `~/.claude/`. After installation, `cd` into any project and run `pilot` or `ccp` to start.

<details>
<summary><b>What the installer does</b></summary>
