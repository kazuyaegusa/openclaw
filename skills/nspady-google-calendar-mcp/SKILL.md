---
name: nspady-google-calendar-mcp
description: "MCP integration for Google Calendar to manage events."
homepage: https://github.com/nspady/google-calendar-mcp
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["docker", "git", "google-calendar-mcp", "npm", "npx", "users"]
---

# Nspady Google Calendar Mcp

# Google Calendar MCP Server

## Installation

**Option 1: Use with npx (Recommended)**

Add to your Claude Desktop configuration:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "google-calendar": {
      "command": "npx",
      "args": ["@cocal/google-calendar-mcp"],
      "env": {
        "GOOGLE_OAUTH_CREDENTIALS": "/path/to/your/gcp-oauth.keys.json"
      }
    }
  }
}
```

**⚠️ Important Note for npx Users**: When us
