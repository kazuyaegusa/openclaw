---
name: miantiao-me-github-stars
description: "A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your"
homepage: https://github.com/miantiao-me/github-stars
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
---

# Miantiao Me Github Stars

This project creates a searchable database of your GitHub starred repositories by:

1. Fetching all your starred repositories using the GitHub API
2. Extracting and processing the README files from each repository
3. Uploading the processed data to Cloudflare R2 storage
4. Using Cloudflare AutoRAG to create embeddings for efficient searching
5. Exposing a MCP Server that allows querying these repositories via natural language

## Usage

Once deployed, you can interact with the MCP Server using any MCP-compatible client:
