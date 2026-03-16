---
name: thedotmack-claude-mem
description: "A Claude Code plugin that automatically captures everything Claude does during your coding"
homepage: https://github.com/thedotmack/claude-mem
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["claude-mem", "curl", "npm"]
---

# Thedotmack Claude Mem

<p align="center">
  Official $CMEM Links: 
  <a href="https://bags.fm/2TsmuYUrsctE57VLckZBYEEzdokUF8j8e1GavekWBAGS">Bags.fm</a> •
  <a href="https://jup.ag/tokens/2TsmuYUrsctE57VLckZBYEEzdokUF8j8e1GavekWBAGS">Jupiter</a> •
  <a href="https://photon-sol.tinyastro.io/en/lp/6MzFAkWnac6GSK1EdFX93dZeukGfzrFq4UHWarhGSQyd">Photon</a> •
  <a href="https://dexscreener.com/solana/6mzfakwnac6gsk1edfx93dzeukgfzrfq4uhwarhgsqyd">DEXScreener</a>
</p>

<p align="center">Official CA: 2TsmuYUrsctE57VLckZBYEEzdok

## Installation

- **[Installation Guide](https://docs.claude-mem.ai/installation)** - Quick start & advanced installation
- **[Usage Guide](https://docs.claude-mem.ai/usage/getting-started)** - How Claude-Mem works automatically
- **[Search Tools](https://docs.claude-mem.ai/usage/search-tools)** - Query your project history with natural language
- **[Beta Features](https://docs.claude-mem.ai/beta-features)** - Try experimental features like Endless Mode

## Usage

Start a new Claude Code session in the terminal and enter the following commands:

```
/plugin marketplace add thedotmack/claude-mem

/plugin install claude-mem
```

Restart Claude Code. Context from previous sessions will automatically appear in new sessions.

> **Note:** Claude-Mem is also published on npm, but `npm install -g claude-mem` installs the **SDK/library only** — it does not register the plugin hooks or set up the worker service. To use Claude-Mem as a plugin, always install via the
