---
name: grafana-mcp-grafana
description: "MCP server for Grafana"
homepage: https://github.com/grafana/mcp-grafana
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "go", "mcp-grafana"]
---

# Grafana Mcp Grafana

# Grafana MCP server

## Usage

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/). Add the following to your MCP client configuration (e.g. Claude Desktop, Cursor):

```json
{
  "mcpServers": {
    "grafana": {
      "command": "uvx",
      "args": ["mcp-grafana"],
      "env": {
        "GRAFANA_URL": "http://localhost:3000",
        "GRAFANA_SERVICE_ACCOUNT_TOKEN": "<your service account token>"
      }
    }
  }
}
```

For Grafana Cloud, replace `GRAFANA_URL` with your instance URL (e.g. `https://myinst
