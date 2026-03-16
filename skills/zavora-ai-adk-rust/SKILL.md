---
name: zavora-ai-adk-rust
description: "Rust Agent Development Kit (ADK-Rust): Build AI agents in Rust with modular components for models,"
homepage: https://github.com/zavora-ai/adk-rust
metadata:
  openclaw:
    emoji: "🕵️"
    auto_generated: true
    requires:
      bins: ["adk-studio", "adk-ui-react", "cargo", "docker", "git", "node", "npm", "sccache"]
---

# Zavora Ai Adk Rust

ADK-Rust provides a comprehensive framework for building AI agents in Rust, featuring:

- **Type-safe agent abstractions** with async execution and event streaming
- **Multiple agent types**: LLM agents, workflow agents (sequential, parallel, loop), and custom agents
- **Realtime voice agents**: Bidirectional audio streaming with OpenAI Realtime API and Gemini Live API
- **Tool ecosystem**: Function tools, Google Search, MCP (Model Context Protocol) integration
- **RAG pipeline**: Document chunk

## Installation

Requires Rust 1.85 or later (Rust 2024 edition). Add to your `Cargo.toml`:

```toml
[dependencies]
adk-rust = "0.3.2"



## Usage

See [examples/](examples/) directory for complete, runnable examples:

**Getting Started**
- `quickstart/` - Basic agent setup and chat loop
- `function_tool/` - Custom tool implementation
- `multiple_tools/` - Agent with multiple tools
- `agent_tool/` - Use agents as callable tools

**Multimodal (Image/Audio/PDF)**
- `gemini_multimodal/` - Inline image analysis, multi-image comparison, vision agent
- `anthropic_multimodal/` - Image analysis with Claude (requires `--features anthropic`)

**OpenA

```
