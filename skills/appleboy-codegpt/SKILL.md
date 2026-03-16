---
name: appleboy-codegpt
description: "A CLI written in Go language that writes git commit messages or do a code review brief for you"
homepage: https://github.com/appleboy/CodeGPT
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["codegpt", "curl", "git", "go"]
---

# Appleboy Codegpt

# CodeGPT

## Installation

To install the hook in the Git repository:

```sh
codegpt hook install
```

## Usage

There are two methods for generating a commit message using the `codegpt` command: CLI mode and Git Hook.
