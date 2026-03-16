---
name: mrexodia-ida-pro-mcp
description: "AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP."
homepage: https://github.com/mrexodia/ida-pro-mcp
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["git", "npx", "pip"]
---

# Mrexodia Ida Pro Mcp

# IDA Pro MCP

## Installation

Install the latest version of the IDA Pro MCP package:

```sh
pip uninstall ida-pro-mcp
pip install https://github.com/mrexodia/ida-pro-mcp/archive/refs/heads/main.zip
```

Configure the MCP servers and install the IDA Plugin:

```
ida-pro-mcp --install
```

**Important**: Make sure you completely restart IDA and your MCP client for the installation to take effect. Some clients (like Claude) run in the background and need to be quit from the tray icon.

https://github.com/user-attachments/assets
