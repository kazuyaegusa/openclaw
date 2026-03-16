---
name: anton-abyzov-specweave
description: "Spec-driven development framework for AI coding agents. 100+ skills for Claude Code, Cursor,"
homepage: https://github.com/anton-abyzov/specweave
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["npm", "specweave"]
---

# Anton Abyzov Specweave

# SpecWeave

## Installation

```bash
npm install -g specweave
cd your-project
specweave init .
```

Init automatically detects your project setup:

- **Git provider** — GitHub, Azure DevOps, or Bitbucket from `.git/config`
- **Umbrella structure** — discovers all child repos in `repositories/` and configures multi-repo coordination
- **AI tool** — Claude Code, Cursor, Copilot, Codex, or generic

The `specweave` CLI ships with 49 commands — project init, LSP code intelligence, skill management, dashboard, plugin marketplace,
