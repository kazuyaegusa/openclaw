---
name: rust-lang-docs-rs
description: "crates.io documentation generator"
homepage: https://github.com/rust-lang/docs.rs
metadata:
  openclaw:
    emoji: "📄"
    auto_generated: true
    requires:
      bins: ["browser-ui-test", "cargo", "docker", "git", "node", "npm"]
---

# Rust Lang Docs Rs

# Docs.rs

## Installation

Make sure you have docker-compose and are able to download ~10GB data on the first run. Also ensure that
docker is installed and the service is running.

```sh
git clone https://github.com/rust-lang/docs.rs.git docs.rs
cd docs.rs
git submodule update --init



```
