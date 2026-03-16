---
name: severity1-claude-code-prompt-improver
description: "Intelligent prompt improver hook for Claude Code. Type vibes, ship precision."
homepage: https://github.com/severity1/claude-code-prompt-improver
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Severity1 Claude Code Prompt Improver

# Claude Code Prompt Improver

## Installation

**Requirements:** Claude Code 2.0.22+ (uses AskUserQuestion tool for targeted clarifying questions)

## Usage

**Normal use:**

```bash
claude "fix the bug"      # Hook evaluates, may ask questions
claude "add tests"        # Hook evaluates, may ask questions
```

**Bypass prefixes:**

```bash
claude "* add dark mode"                    # * = skip evaluation
claude "/help"                              # / = slash commands bypass
claude "# remember to use rg over grep"     # # = memorize bypass
```

**Vague prompt:**

```bash
$ claude "fix the error"
```

Claude asks:

```
Which error needs fixing?
  ○ TypeEr

```
