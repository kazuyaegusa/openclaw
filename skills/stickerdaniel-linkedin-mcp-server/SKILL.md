---
name: stickerdaniel-linkedin-mcp-server
description: "This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn"
homepage: https://github.com/stickerdaniel/linkedin-mcp-server
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "git"]
---

# Stickerdaniel Linkedin Mcp Server

# LinkedIn MCP Server

## Installation

**Step 1: Create a session (first time only)**

```bash
uvx linkedin-scraper-mcp --login
```

This opens a browser for you to log in manually (5 minute timeout for 2FA, captcha, etc.). The browser profile is saved to `~/.linkedin-mcp/profile/`.

**Step 2: Client Configuration:**

```json
{
  "mcpServers": {
    "linkedin": {
      "command": "uvx",
      "args": ["linkedin-scraper-mcp"]
    }
  }
}
```

> [!NOTE]
> Sessions may expire over time. If you encounter authentication issues, run `uvx l
