---
name: vercel-labs-agent-browser
description: "Browser automation CLI for AI agents"
homepage: https://github.com/vercel-labs/agent-browser
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["agent-browser", "appium", "cargo", "git", "npm", "npx", "pnpm", "skills"]
---

# Vercel Labs Agent Browser

# agent-browser

## Installation

```bash
agent-browser install                 # Download Chrome from Chrome for Testing (Google's official automation channel)
agent-browser install --with-deps     # Also install system deps (Linux)
```

## Usage

```bash
agent-browser open example.com
agent-browser snapshot                    # Get accessibility tree with refs
agent-browser click @e2                   # Click by ref from snapshot
agent-browser fill @e3 "test@example.com" # Fill by ref
agent-browser get text @e1                # Get text by ref
agent-browser screenshot page.png
agent-browser close
```
