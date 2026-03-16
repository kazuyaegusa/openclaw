---
name: cj-vana-claude-swarm
description: "MCP server for orchestrating parallel Claude Code worker swarms with protocol-based behavioral"
homepage: https://github.com/cj-vana/claude-swarm
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["cargo", "curl", "git", "go", "jest", "node", "npm", "npx", "tmux", "tsc", "vitest"]
---

# Cj Vana Claude Swarm

<p align="center">
  <img src="assets/banner.png" alt="Claude Swarm - Parallel AI Workers" width="100%">
</p>

<p align="center">
  <strong>An MCP server for orchestrating parallel Claude Code worker swarms with protocol-based behavioral governance.</strong><br>
  Enables multi-hour autonomous coding sessions with persistent state, parallel workers, and runtime enforcement of behavioral constraints.
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#quick-start">Qu

## Installation

**One-liner install** (recommended):

```bash
curl -fsSL https://raw.githubusercontent.com/cj-vana/claude-swarm/main/install.sh | bash
```

This will clone the repo, build, register the MCP server, and install the `/swarm` skill.

<details>
<summary><strong>Manual installation</strong></summary>

```bash
git clone https://github.com/cj-vana/claude-swarm.git
cd claude-swarm
npm install
npm run build



## Usage

```
