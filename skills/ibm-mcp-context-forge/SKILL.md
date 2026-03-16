---
name: ibm-mcp-context-forge
description: "A Model Context Protocol (MCP) Gateway & Registry. Serves as a central management point for tools,"
homepage: https://github.com/IBM/mcp-context-forge
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins:
        [
          "curl",
          "docker",
          "git",
          "go",
          "jq",
          "libpq",
          "mcp-contextforge-gateway",
          "npx",
          "pip",
          "python3",
          "uv",
        ]
---

# Ibm Mcp Context Forge

# ContextForge

## Installation

```bash
make venv install          # create .venv + install deps
make serve                 # gunicorn on :4444
```

<details>
<summary><strong>Alternative: UV or pip</strong></summary>

```bash



```
