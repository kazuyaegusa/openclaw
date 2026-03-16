---
name: mixelpixx-kicad-mcp-server
description: "KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models"
homepage: https://github.com/mixelpixx/KiCAD-MCP-Server
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["curl", "git", "node", "npm", "pip", "pip3", "python3"]
---

# Mixelpixx Kicad Mcp Server

The [Model Context Protocol](https://modelcontextprotocol.io/) is an open standard from Anthropic that allows AI assistants to securely connect to external tools and data sources. This implementation provides a standardized bridge between AI assistants and KiCAD, enabling natural language control of PCB design operations.

**Key Capabilities:**

- 64 fully-documented tools with JSON Schema validation
- Smart tool discovery with router pattern (reduces AI context by 70%)
- 8 dynamic resources
