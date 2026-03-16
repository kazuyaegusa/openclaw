---
name: modelcontextprotocol-typescript-sdk
description: "The official TypeScript SDK for Model Context Protocol servers and clients"
homepage: https://github.com/modelcontextprotocol/typescript-sdk
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["client", "express", "git", "hono", "node", "npm", "server"]
---

# Modelcontextprotocol Typescript Sdk

The Model Context Protocol (MCP) allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction.

This repository contains the TypeScript SDK implementation of the MCP specification. It runs on **Node.js**, **Bun**, and **Deno**, and ships:

- MCP **server** libraries (tools/resources/prompts, Streamable HTTP, stdio, auth helpers)
- MCP **client** libraries (transports, high-level helpers, OAuth helpers)
- Optio
