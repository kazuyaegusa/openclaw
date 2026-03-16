---
name: anthropics-claude-code-security-review
description: "An AI-powered security review GitHub Action using Claude to analyze code changes for security"
homepage: https://github.com/anthropics/claude-code-security-review
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
---

# Anthropics Claude Code Security Review

# Claude Code Security Reviewer

## Usage

Add this to your repository's `.github/workflows/security.yml`:

```yaml
name: Security Review

permissions:
  pull-requests: write # Needed for leaving PR comments
  contents: read

on:
  pull_request:

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha || github.sha }}
          fetch-depth: 2

      - uses: anthropics/claude-code-security-review@main
        with: commen
```
