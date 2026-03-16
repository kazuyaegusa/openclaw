---
name: flux159-mcp-server-kubernetes
description: "MCP Server for kubernetes management commands"
homepage: https://github.com/Flux159/mcp-server-kubernetes
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["docker", "git", "go", "inspector", "mcp-chat", "mcp-server-kubernetes", "node", "npx"]
---

# Flux159 Mcp Server Kubernetes

# MCP Server Kubernetes

## Usage

Enable observability with environment variables:

```bash
export ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

npx mcp-server-kubernetes
```
