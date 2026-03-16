---
name: owloops-claude-powerline
description: "Beautiful vim-style powerline statusline for Claude Code"
homepage: https://github.com/Owloops/claude-powerline
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["curl", "git", "npm", "npx", "overhead"]
---

# Owloops Claude Powerline

<div align="center">

## Installation

Requires Node.js 18+, Claude Code, and Git 2.0+. For best display, install a [Nerd Font](https://www.nerdfonts.com/) or use `--charset=text` for ASCII-only symbols.

**1. Add to your Claude Code `settings.json`:**

```json
{
  "statusLine": {
    "type": "command",
    "command": "npx -y @owloops/claude-powerline@latest --style=powerline"
  }
}
```

**2. Start a Claude session** - the statusline appears at the bottom during conversations.

![Claude Code with powerline](images/claude-interface-wi

## Usage

Once added to Claude Code settings, the statusline runs automatically. For customization:

**CLI Options** (both `--arg value` and `--arg=value` syntax supported):

- `--theme` - `dark` (default), `light`, `nord`, `tokyo-night`, `rose-pine`, `gruvbox`, `custom`
- `--style` - `minimal` (default), `powerline`, `capsule`
- `--charset` - `unicode` (default), `text`
- `--config` - Custom config file path
- `--help` - Show help

**Examples:**

```bash
claude-powerline --theme=nord --style=powerline
cl

```
