---
name: knoxgraeme-skillfish
description: "The skill manager for AI coding agents. Install, update, and sync skills across Claude Code,"
homepage: https://github.com/knoxgraeme/skillfish
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["git", "npm", "npx", "skillfish"]
---

# Knoxgraeme Skillfish

<p align="center">
  <img src="https://raw.githubusercontent.com/knoxgraeme/skillfish/main/assets/logo.png" alt="skillfish" width="600">
</p>

<p align="center">
  <a href="https://npmjs.com/package/skillfish"><img src="https://img.shields.io/npm/v/skillfish" alt="npm"></a>
  <a href="https://npmjs.com/package/skillfish"><img src="https://img.shields.io/npm/dm/skillfish" alt="downloads"></a>
  <a href="LICENSE"><img src="https://img.shields.io/npm/l/skillfish" alt="license"></a>
  <a href="packa

## Installation

Install skills from a `skillfish.json` manifest.

```bash
skillfish install                    # Install from manifest (auto-detects location)
skillfish install --project          # Install from ./skillfish.json
skillfish install --global           # Install from ~/skillfish.json
skillfish install --dry-run          # Preview changes without installing
skillfish install --yes              # Skip confirmation prompts
```

When a skill is removed from the manifest, `skillfish install` removes it f

## Usage

```bash

```
