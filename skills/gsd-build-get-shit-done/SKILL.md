---
name: gsd-build-get-shit-done
description: "A light-weight and powerful meta-prompting, context engineering and spec-driven development system"
homepage: https://github.com/gsd-build/get-shit-done
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["get-shit-done-cc", "git", "go", "node", "npx"]
---

# Gsd Build Get Shit Done

<div align="center">

## Installation

```bash
npx get-shit-done-cc@latest
```

The installer prompts you to choose:

1. **Runtime** — Claude Code, OpenCode, Gemini, Codex, or all
2. **Location** — Global (all projects) or local (current project only)

Verify with:

- Claude Code / Gemini: `/gsd:help`
- OpenCode: `/gsd-help`
- Codex: `$gsd-help`

> [!NOTE]
> Codex installation uses skills (`skills/gsd-*/SKILL.md`) rather than custom prompts.
