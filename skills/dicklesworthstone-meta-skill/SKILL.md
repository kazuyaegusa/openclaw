---
name: dicklesworthstone-meta-skill
description: "Local-first skill management platform for AI coding agents: dual SQLite+Git persistence, semantic"
homepage: https://github.com/Dicklesworthstone/meta_skill
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["cargo", "gh", "git", "npm"]
---

# Dicklesworthstone Meta Skill

Use `Result<T, E>` and propagate errors with `?`. Define custom error types for domain logic.

## Usage

```rust
fn read_config(path: &str) -> Result<Config, ConfigError> {
    let contents = std::fs::read_to_string(path)?;
    toml::from_str(&contents).map_err(ConfigError::Parse)
}
```
