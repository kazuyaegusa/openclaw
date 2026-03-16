---
name: steipete-claude-code-mcp
description: "Claude Code as one-shot MCP server to have an agent in your agent."
homepage: https://github.com/steipete/claude-code-mcp
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["claude-code", "git", "npm", "npx"]
---

# Steipete Claude Code Mcp

This MCP server provides one tool that can be used by LLMs to interact with Claude Code. When integrated with Claude Desktop or other MCP clients, it allows LLMs to:

- Run Claude Code with all permissions bypassed (using `--dangerously-skip-permissions`)
- Execute Claude Code with any prompt without permission interruptions
- Access file editing capabilities directly
- Enable specific tools by default

## Usage

Here are some visual examples of the server in action:

<img src="assets/claude_tool_git_example.png" alt="Claude Tool Git Example" width="50%">

<img src="assets/additional_claude_screenshot.png" alt="Additional Claude Screenshot" width="50%">

<img src="assets/cursor-screenshot.png" alt="Cursor Screenshot" width="50%">
