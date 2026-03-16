---
name: cranot-claude-code-guide
description: "The Complete Claude Code CLI Guide - Live & Auto-Updated Every 2 Days"
homepage: https://github.com/Cranot/claude-code-guide
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins:
        [
          "claude-code",
          "claude-ignore",
          "curl",
          "gh",
          "git",
          "go",
          "jq",
          "npm",
          "npx",
          "pip",
          "server-github",
        ]
---

# Cranot Claude Code Guide

# The Complete Claude Code CLI Guide

## Installation

claude mcp add --transport stdio github -- npx -y @modelcontextprotocol/server-github

## Usage

Read file_path="/src/app.ts"
Read file_path="/docs/screenshot.png" # Can read images!
Read file_path="/docs/guide.pdf" # Can read PDFs!
Read file_path="/docs/guide.pdf" pages="1-5" # Read specific PDF pages [NEW v2.1.30]

```

**Capabilities:**
- Reads any text file (code, configs, logs, etc.)
- Handles images (screenshots, diagrams, charts)
- Processes PDFs - extracts text and visual content
- Parses Jupyter notebooks (.ipynb files)
- Returns content with line numbers (`cat -n` format)
-

```
