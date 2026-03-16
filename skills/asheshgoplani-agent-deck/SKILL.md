---
name: asheshgoplani-agent-deck
description: "Terminal session manager for AI coding agents. One TUI for Claude, Gemini, OpenCode, Codex, and"
homepage: https://github.com/asheshgoplani/agent-deck
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["agent-deck", "curl", "docker", "git", "go"]
---

# Asheshgoplani Agent Deck

<div align="center">

<!-- Status Grid Logo -->
<img src="site/logo.svg" alt="Agent Deck Logo" width="120">

## Installation

**Works on:** macOS, Linux, Windows (WSL)

```bash
curl -fsSL https://raw.githubusercontent.com/asheshgoplani/agent-deck/main/install.sh | bash
```

Then run: `agent-deck`

<details>
<summary>Other install methods</summary>

**Homebrew**

```bash
brew install asheshgoplani/tap/agent-deck
```

**Go**

```bash
go install github.com/asheshgoplani/agent-deck/cmd/agent-deck@latest
```

**From Source**

```bash
git clone https://github.com/asheshgoplani/agent-deck.git && cd agent-deck && make install
```

## Usage

```bash
agent-deck                        # Launch TUI
agent-deck add . -c claude        # Add current dir with Claude
agent-deck session fork my-proj   # Fork a Claude session
agent-deck mcp attach my-proj exa # Attach MCP to session
agent-deck skill attach my-proj docs --source pool --restart # Attach skill + restart
agent-deck web                    # Start web UI on http://127.0.0.1:8420
```
