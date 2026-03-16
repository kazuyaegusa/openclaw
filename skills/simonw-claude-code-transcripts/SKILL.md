---
name: simonw-claude-code-transcripts
description: "Tools for publishing transcripts for Claude Code sessions"
homepage: https://github.com/simonw/claude-code-transcripts
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["gh"]
---

# Simonw Claude Code Transcripts

# claude-code-transcripts

## Installation

Install this tool using `uv`:

```bash
uv tool install claude-code-transcripts
```

Or run it without installing:

```bash
uvx claude-code-transcripts --help
```

## Usage

This tool converts Claude Code session files into browseable multi-page HTML transcripts.

There are four commands available:

- `local` (default) - select from local Claude Code sessions stored in `~/.claude/projects`
- `web` - select from web sessions via the Claude API
- `json` - convert a specific JSON or JSONL session file
- `all` - convert all local sessions to a browsable HTML archive

The quickest way to view a recent local session:

```bash
claude-code-transcripts
```

This shows an int
