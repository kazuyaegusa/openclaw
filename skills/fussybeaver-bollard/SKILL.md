---
name: fussybeaver-bollard
description: "Docker daemon API in Rust"
homepage: https://github.com/fussybeaver/bollard
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["cargo", "docker"]
---

# Fussybeaver Bollard

[![crates.io](https://img.shields.io/crates/v/bollard.svg)](https://crates.io/crates/bollard)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![circle-ci](https://circleci.com/gh/fussybeaver/bollard/tree/master.svg?style=svg)](https://circleci.com/gh/fussybeaver/bollard/tree/master)
[![appveyor](https://ci.appveyor.com/api/projects/status/n5khebyfae0u1sbv/branch/master?svg=true)](https://ci.appveyor.com/project/fussybeaver/boo

## Installation

Add the following to your `Cargo.toml` file

```nocompile
[dependencies]
bollard = "*"
```

## Usage

| Use Case                    | Cargo.toml                                                       |
| --------------------------- | ---------------------------------------------------------------- |
| Local Docker (Unix/Windows) | `bollard = "*"` _(defaults work)_                                |
| Remote Docker over HTTPS    | `bollard = { version = "*", features = ["ssl"] }`                |
| SSH tunnel to remote Docker | `bollard = { version = "*", features = ["ssh"] }`                |
| BuildKit image builds       | `bollard = { version = "*", features = ["buildkit", "chrono"] }` |
| WebSocket container attach  | `bollard = { version = "*", features = ["websocket"] }`          |
| Minimal binary size         | `bollard                                                         |
