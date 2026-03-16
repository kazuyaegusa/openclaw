---
name: makenotion-notion-mcp-server
description: "Official Notion MCP Server"
homepage: https://github.com/makenotion/notion-mcp-server
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "notion-mcp-server", "npm", "npx"]
---

# Makenotion Notion Mcp Server

# Notion MCP Server

## Usage

1. Using the following instruction

```text
Comment "Hello MCP" on page "Getting started"
```

AI will correctly plan two API calls, `v1/search` and `v1/comments`, to achieve the task

1. Similarly, the following instruction will result in a new page named "Notion MCP" added to parent page "Development"

```text
Add a page titled "Notion MCP" to page "Development"
```

1. You may also reference content ID directly

```text
Get the content of page 1a6b35e6e67f802fa7e1d27686f017f2
```
