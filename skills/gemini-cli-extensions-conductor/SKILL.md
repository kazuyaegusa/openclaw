---
name: gemini-cli-extensions-conductor
description: "Conductor is a Gemini CLI extension that allows you to specify, plan, and implement software"
homepage: https://github.com/gemini-cli-extensions/conductor
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Gemini Cli Extensions Conductor

# Conductor Extension for Gemini CLI

## Installation

Install the Conductor extension by running the following command from your terminal:

```bash
gemini extensions install https://github.com/gemini-cli-extensions/conductor --auto-update
```

The `--auto-update` is optional: if specified, it will update to new versions as they are released.

## Usage

Conductor is designed to manage the entire lifecycle of your development tasks.

**Note on Token Consumption:** Conductor's context-driven approach involves reading and analyzing your project's context, specifications, and plans. This can lead to increased token consumption, especially in larger projects or during extensive planning and implementation phases. You can check the token consumption in the current session by running `/stats model`.
