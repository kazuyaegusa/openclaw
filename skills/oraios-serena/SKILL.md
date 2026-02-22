---
name: oraios-serena
description: "A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server &"
homepage: https://github.com/oraios/serena
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
---

# Oraios Serena

<p align="center" style="text-align:center">
  <img src="resources/serena-logo.svg#gh-light-mode-only" style="width:500px">
  <img src="resources/serena-logo-dark-mode.svg#gh-dark-mode-only" style="width:500px">
</p>

- :rocket: Serena is a powerful **coding agent toolkit** capable of turning an LLM into a fully-featured agent that works **directly on your codebase**.
  Unlike most other tools, it is not tied to an LLM, framework or an interface, making it easy to use it in a variety of ways.
-

## Usage

**Prerequisites**. Serena is managed by _uv_. If you don’t already have it, you need to [install uv](https://docs.astral.sh/uv/getting-started/installation/) before proceeding.

**Starting the MCP Server**. The easiest way to start the Serena MCP server is by running the latest version from GitHub using uvx.
Issue this command to see available options:

```bash
uvx --from git+https://github.com/oraios/serena serena start-mcp-server --help
```

**Configuring Your Client**. To connect Serena to yo
