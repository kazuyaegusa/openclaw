---
name: exa-labs-exa-mcp-server
description: "Exa MCP for web search and web crawling!"
homepage: https://github.com/exa-labs/exa-mcp-server
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["go", "npm"]
---

# Exa Labs Exa Mcp Server

# Exa MCP Server

## Installation

Connect to Exa's hosted MCP server:

```
https://mcp.exa.ai/mcp
```

[Get your API key](https://dashboard.exa.ai/api-keys)

<details>
<summary><b>Cursor</b></summary>

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "exa": {
      "url": "https://mcp.exa.ai/mcp"
    }
  }
}
```

</details>

<details>
<summary><b>VS Code</b></summary>

Add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "exa": {
      "type": "http",
      "url": "https://mcp.exa.ai/mcp"
    }
  }
}
```

</detail

## Usage

SEC filings for a company:

```
web_search_advanced_exa {
  "query": "Anthropic SEC filing S-1",
  "category": "financial report",
  "numResults": 10,
  "type": "auto"
}
```

Recent earnings reports:

```
web_search_advanced_exa {
  "query": "Q4 2025 earnings report technology",
  "category": "financial report",
  "startPublishedDate": "2025-10-01",
  "numResults": 20,
  "type": "auto"
}
```

Specific filing type:

```
web_search_advanced_exa {
  "query": "10-K annual report AI companies",
  "categ

```
