---
name: gitleaks-gitleaks
description: "Find secrets with Gitleaks 🔑"
homepage: https://github.com/gitleaks/gitleaks
metadata:
  openclaw:
    emoji: "🔒"
    auto_generated: true
    requires:
      bins: ["docker", "git", "gitleaks", "go"]
---

# Gitleaks Gitleaks

# Gitleaks

## Installation

Gitleaks can be installed using Homebrew, Docker, or Go. Gitleaks is also available in binary form for many popular platforms and OS types on the [releases page](https://github.com/gitleaks/gitleaks/releases). In addition, Gitleaks can be implemented as a pre-commit hook directly in your repo or as a GitHub action using [Gitleaks-Action](https://github.com/gitleaks/gitleaks-action).

## Usage

```
Gitleaks scans code, past or present, for secrets

Usage:
  gitleaks [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  dir         scan directories or files for secrets
  git         scan git repositories for secrets
  help        Help about any command
  stdin       detect secrets from stdin
  version     display gitleaks version

Flags:
  -b, --baseline-path string          path to baseline with issues that can be ignored
  -c, --conf

```
