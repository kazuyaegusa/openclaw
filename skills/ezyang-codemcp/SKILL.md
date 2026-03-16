---
name: ezyang-codemcp
description: "Coding assistant MCP for Claude Desktop"
homepage: https://github.com/ezyang/codemcp
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["go"]
---

# Ezyang Codemcp

NOTICE: claude code is available with Anthropic's $20/mo subscription, so I consider
codemcp fully obsolete. However, there are some good design ideas (especially around
the Git-versioning scheme) that I eventually want to port into the current generation
of agentic coding clis.

## Installation

I recommend this specific way of installing and using codemcp:

1. Install `uv` and install git, if they are not installed already.

2. Install [claude-mcp](https://chromewebstore.google.com/detail/mcp-for-claudeai/jbdhaamjibfahpekpnjeikanebpdpfpb) on your browser.
   This enables you to connect to SSE MCP servers directly from the website,
   which means you don't need to use Claude Desktop and can easily have
   multiple chat windows going in parallel. We expect this extension should
   be so

## Usage

First, you must create a `codemcp.toml` file in the Git repository checkout
you want to work on. If you want the agent to be able to do things like run
your formatter or run tests, add the commands to execute them in the commands
section (note: these commands need to appropriately setup any virtual
environment they need):

```toml
format = ["./run_format.sh"]
test = ["./run_test.sh"]
```

The `format` command is special; it is always run after every file edit.

Next, in Claude Desktop, we rec
