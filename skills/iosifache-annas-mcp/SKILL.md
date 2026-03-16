---
name: iosifache-annas-mcp
description: "MCP server and CLI tool for searching and downloading documents from Anna's Archive"
homepage: https://github.com/iosifache/annas-mcp
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
---

# Iosifache Annas Mcp

# Anna's Archive MCP Server (and CLI Tool)

## Installation

Download the appropriate binary from [the GitHub Releases section](https://github.com/iosifache/annas-mcp/releases).

If you plan to use the tool for its MCP server functionality, you need to integrate it into your MCP client. If you are using Claude Desktop, please consider the following example configuration:

```json
"anna-mcp": {
    "command": "/Users/iosifache/Downloads/annas-mcp",
    "args": ["mcp"],
    "env": {
        "ANNAS_SECRET_KEY": "feedfacecafebeef",
        "ANNAS_DOWNLOAD_PAT



```
