---
name: wirasm-prps-agentic-eng
description: "Prompts, workflows and more for agentic engineering"
homepage: https://github.com/Wirasm/PRPs-agentic-eng
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Wirasm Prps Agentic Eng

# PRP (Product Requirement Prompts)

## Installation

The stop hook must be configured in `.claude/settings.local.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/prp-ralph-stop.sh"
          }
        ]
      }
    ]
  }
}
```

## Usage

```bash

```
