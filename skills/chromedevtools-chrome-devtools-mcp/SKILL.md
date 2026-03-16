---
name: chromedevtools-chrome-devtools-mcp
description: "Chrome DevTools for coding agents"
homepage: https://github.com/ChromeDevTools/chrome-devtools-mcp
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["chrome-devtools-mcp", "go", "npx"]
---

# Chromedevtools Chrome Devtools Mcp

# Chrome DevTools MCP

## Installation

Add the following config to your MCP client:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

> [!NOTE]  
> Using `chrome-devtools-mcp@latest` ensures that your MCP client will always use the latest version of the Chrome DevTools MCP server.

If you are interested in doing only basic browser tasks, use the `--slim` mode:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",




```
