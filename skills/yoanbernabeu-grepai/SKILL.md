---
name: yoanbernabeu-grepai
description: "Semantic Search & Call Graphs for AI Agents (100% Local)"
homepage: https://github.com/yoanbernabeu/grepai
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["curl", "grepai"]
---

# Yoanbernabeu Grepai

<div align="center">

## Installation

**Homebrew (macOS):**

```bash
brew install yoanbernabeu/tap/grepai
```

**Linux/macOS:**

```bash
curl -sSL https://raw.githubusercontent.com/yoanbernabeu/grepai/main/install.sh | sh
```

**Windows (PowerShell):**

```powershell
irm https://raw.githubusercontent.com/yoanbernabeu/grepai/main/install.ps1 | iex
```

Requires an embedding provider — [Ollama](https://ollama.ai) (default), [LM Studio](https://lmstudio.ai), or OpenAI.

**Ollama (recommended):**

```bash
ollama pull nomic-embed-text
```

## Usage

```bash
grepai init                        # Initialize in your project
grepai watch                       # Start indexing daemon
grepai search "error handling"     # Search semantically
grepai trace callers "Login"       # Find who calls a function
```
