---
name: covibes-zeroshot
description: "Your autonomous engineering team in a CLI. Point Zeroshot at an issue, walk away, and return to"
homepage: https://github.com/covibes/zeroshot
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["cargo", "cargo-watch", "docker", "gh", "git", "node", "npm", "npx", "tsc", "zeroshot"]
---

# Covibes Zeroshot

# zeroshot CLI

## Usage

```bash
zeroshot run 123                    # GitHub issue number
zeroshot run feature.md             # Markdown file
zeroshot run "Add dark mode"        # Inline text
```

Or describe a complex task inline:

```bash
zeroshot run "Add optimistic locking with automatic retry: when updating a user,
retry with exponential backoff up to 3 times, merge non-conflicting field changes,
and surface conflicts with details. Handle the ABA problem where version goes A->B->A."
```
