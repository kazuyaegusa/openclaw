---
name: max-sixty-worktrunk
description: "Worktrunk is a CLI for Git worktree management, designed for parallel AI agent workflows"
homepage: https://github.com/max-sixty/worktrunk
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["cargo", "gh", "git", "worktrunk"]
---

# Max Sixty Worktrunk

<!-- markdownlint-disable MD033 -->

<h1><img src="docs/static/logo.png" alt="Worktrunk logo" width="50" align="absmiddle">&nbsp;&nbsp;Worktrunk</h1>

[![Docs](https://img.shields.io/badge/docs-worktrunk.dev-blue?style=for-the-badge&logo=gitbook)](https://worktrunk.dev)
[![Crates.io](https://img.shields.io/crates/v/worktrunk?style=for-the-badge&logo=rust)](https://crates.io/crates/worktrunk)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](https://opensource.o

## Installation

**Homebrew (macOS & Linux):**

```bash
brew install worktrunk && wt config shell install
```

Shell integration allows commands to change directories.

**Cargo:**

```bash
cargo install worktrunk && wt config shell install
```

<details>
<summary><strong>Windows</strong></summary>

On Windows, `wt` defaults to Windows Terminal's command. Winget additionally installs Worktrunk as `git-wt` to avoid the conflict:

```bash
winget install max-sixty.worktrunk
git-wt config shell install
```

Alternati

## Usage

Create a worktree for a new feature:

```console
$ wt switch --create feature-auth
✓ Created branch feature-auth from main and worktree @ repo.feature-auth

```

This creates a new branch and worktree, then switches to it. Do your work, then check all worktrees with [`wt list`](https://worktrunk.dev/list/):

```console
$ wt list
  Branch        Status        HEAD±    main↕  Remote⇅  Commit    Age   Message
@ feature-auth  +   –      +53                         0e631add  1d    Initial commit
^ ma

```
