---
name: googleworkspace-cli
description: "Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin,"
homepage: https://github.com/googleworkspace/cli
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["cargo", "cli", "curl", "googleworkspace-cli", "jq", "npm", "npx", "skills"]
---

# Googleworkspace Cli

<h1 align="center">gws</h1>

**One CLI for all of Google Workspace — built for humans and AI agents.**<br>
Drive, Gmail, Calendar, and every Workspace API. Zero boilerplate. Structured JSON output. 40+ agent skills included.

> [!NOTE]
> This is **not** an officially supported Google product.

<p>
  <a href="https://www.npmjs.com/package/@googleworkspace/cli"><img src="https://img.shields.io/npm/v/@googleworkspace/cli" alt="npm version"></a>
  <a href="https://github.com/googleworkspace/cli/blob

## Installation

```bash
npm install -g @googleworkspace/cli
```

> The npm package bundles pre-built native binaries for your OS and architecture.
> No Rust toolchain required.

Pre-built binaries are also available on the [GitHub Releases](https://github.com/googleworkspace/cli/releases) page.

Or build from source:

```bash
cargo install --git https://github.com/googleworkspace/cli --locked
```

A Nix flake is also available at `github:googleworkspace/cli`

```bash
nix run github:googleworkspace/cli
```

On m

## Usage

```bash
gws auth setup     # walks you through Google Cloud project config
gws auth login     # subsequent OAuth login
gws drive files list --params '{"pageSize": 5}'
```
