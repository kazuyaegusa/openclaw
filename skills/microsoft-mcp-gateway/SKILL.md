---
name: microsoft-mcp-gateway
description: "MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable,"
homepage: https://github.com/microsoft/mcp-gateway
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["docker", "go"]
---

# Microsoft Mcp Gateway

This project provides:

- A data gateway for routing traffic to MCP servers with session affinity.
- A control plane for managing the MCP server lifecycle (deploy, update, delete).
- Enterprise-ready integration points including telemetry, access control and observability.
