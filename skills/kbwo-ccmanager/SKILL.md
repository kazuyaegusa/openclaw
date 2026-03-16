---
name: kbwo-ccmanager
description: "Coding Agent Session Manager for Claude Code / Gemini CLI / Codex CLI / Cursor Agent / Copilot CLI"
homepage: https://github.com/kbwo/ccmanager
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["ccmanager", "git", "npm", "npx"]
---

# Kbwo Ccmanager

Status hooks allow you to:

- Get notified when Claude needs your input
- Track time spent in different states
- Trigger automations based on session activity
- Integrate with notification systems like [noti](https://github.com/variadico/noti)

For detailed setup instructions, see [docs/state-hooks.md](docs/status-hooks.md).

## Installation

```bash
npm install -g ccmanager
```

## Usage

```bash
ccmanager
```

Or run without installing:

```bash
npx ccmanager
```
