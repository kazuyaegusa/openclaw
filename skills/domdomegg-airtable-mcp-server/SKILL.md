---
name: domdomegg-airtable-mcp-server
description: "🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable"
homepage: https://github.com/domdomegg/airtable-mcp-server
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["airtable-mcp-server", "git", "go", "npm", "npx"]
---

# Domdomegg Airtable Mcp Server

# airtable-mcp-server

## Installation

**Step 1**: [Create an Airtable personal access token by clicking here](https://airtable.com/create/tokens/new). Details:

- Name: Anything you want e.g. 'Airtable MCP Server Token'.
- Scopes: `schema.bases:read`, `data.records:read`, and optionally `schema.bases:write`, `data.records:write`, `data.recordComments:read`, and `data.recordComments:write`.
- Access: The bases you want to access. If you're not sure, select 'Add all resources'.

Keep the token handy, you'll need it in the next step. It
