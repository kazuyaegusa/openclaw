---
name: grab-cursor-talk-to-figma-mcp
description: "TalkToFigma: MCP integration between AI Agent (Cursor, Claude Code) and Figma, allowing Agentic AI"
homepage: https://github.com/grab/cursor-talk-to-figma-mcp
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["curl", "go", "node"]
---

# Grab Cursor Talk To Figma Mcp

# Talk to Figma MCP

## Usage

1. Install Bun if you haven't already:

```bash
curl -fsSL https://bun.sh/install | bash
```

2. Run setup, this will also install MCP in your Cursor's active project

```bash
bun setup
```

3. Start the Websocket server

```bash
bun socket
```

4. **NEW** Install Figma plugin from [Figma community page](https://www.figma.com/community/plugin/1485687494525374295/cursor-talk-to-figma-mcp-plugin) or [install locally](#figma-plugin)
