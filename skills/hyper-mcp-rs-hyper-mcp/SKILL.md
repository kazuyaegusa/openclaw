---
name: hyper-mcp-rs-hyper-mcp
description: "📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins."
homepage: https://github.com/hyper-mcp-rs/hyper-mcp
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
---

# Hyper Mcp Rs Hyper Mcp

<div align="center">
  <picture>
    <img alt="hyper-mcp logo" src="./assets/logo.png" width="50%">
  </picture>
</div>

<div align="center">

[![Rust](https://img.shields.io/badge/rust-%23000000.svg?logo=rust&logoColor=white)](https://crates.io/crates/hyper-mcp)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue)](#license)
[![Issues - hyper-mcp](https://img.shields.io/github/issues/hyper-mcp-rs/hyper-mcp)](https://github.com/hyper-mcp-rs/hyper-mcp/issues)
![GitHub Release](https

## Installation

1. Create your config file:
   - Linux: `$HOME/.config/hyper-mcp/config.json`
   - Windows: `{FOLDERID_RoamingAppData}\hyper-mcp\config.json`. Eg: `C:\Users\Alice\AppData\Roaming\hyper-mcp\config.json`
   - macOS: `$HOME/Library/Application Support/hyper-mcp/config.json`

```json
{
  "plugins": {
    "time": {
      "url": "oci://ghcr.io/hyper-mcp-rs/time-plugin:latest",
      "description": "Get current time and do time calculations"
    },
    "qr_code": {
      "url": "oci://ghcr.io/hyper-mcp



```
