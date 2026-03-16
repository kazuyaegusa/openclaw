---
name: peonping-peon-ping
description: "Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, and other IDEs. Stop"
homepage: https://github.com/PeonPing/peon-ping
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["curl", "fswatch", "git", "peon-ping", "python3", "terminal-notifier"]
---

# Peonping Peon Ping

# peon-ping

<div align="center">

## Installation

Add to your MCP client config (Claude Desktop, Cursor, etc.):

```json
{
  "mcpServers": {
    "peon-ping": {
      "command": "node",
      "args": ["/path/to/peon-ping/mcp/peon-mcp.js"]
    }
  }
}
```

If installed via Homebrew: `$(brew --prefix peon-ping)/libexec/mcp/peon-mcp.js`. See [`mcp/README.md`](mcp/README.md) for full setup instructions.

## Usage

```bash
peon trainer on              # enable trainer
peon trainer goal 200        # set daily goal (default: 300/300)

```
