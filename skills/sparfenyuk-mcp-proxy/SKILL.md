---
name: sparfenyuk-mcp-proxy
description: "A bridge between Streamable HTTP and stdio MCP transports"
homepage: https://github.com/sparfenyuk/mcp-proxy
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["docker", "git", "pip", "python3"]
---

# Sparfenyuk Mcp Proxy

The `mcp-proxy` is a tool that lets you switch between server transports. There are two supported modes:

1. stdio to SSE/StreamableHTTP
2. SSE to stdio
