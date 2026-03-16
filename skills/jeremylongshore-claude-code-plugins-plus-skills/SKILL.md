---
name: jeremylongshore-claude-code-plugins-plus-skills
description: "270+ Claude Code plugins with 739 agent skills. Production orchestration patterns, interactive"
homepage: https://github.com/jeremylongshore/claude-code-plugins-plus-skills
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["python3"]
---

# Jeremylongshore Claude Code Plugins Plus Skills

Generates idempotent Ansible playbooks following infrastructure-as-code best practices.

## Usage

**Option 1: CLI (Recommended)**

```bash
pnpm add -g @intentsolutionsio/ccpi
ccpi search devops              # Find plugins by keyword
ccpi install devops-automation-pack
ccpi list --installed           # See what's installed
ccpi update                     # Pull latest versions
```

**Option 2: Claude Built-in Commands**

```bash
/plugin marketplace add jeremylongshore/claude-code-plugins
/plugin install devops-automation-pack@claude-code-plugins-plus
```

> Already using an older install? Run `
