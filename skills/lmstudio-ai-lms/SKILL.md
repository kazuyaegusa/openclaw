---
name: lmstudio-ai-lms
description: "LM Studio CLI"
homepage: https://github.com/lmstudio-ai/lms
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["git", "lmstudio", "node", "npm", "npx"]
---

# Lmstudio Ai Lms

<p align="center">
  <br/>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://files.lmstudio.ai/lms-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="https://files.lmstudio.ai/lms-light.png">
    <img alt="lmstudio cli logo" src="https://files.lmstudio.ai/lms-light.png" width="180">
  </picture>
  <br/>
  <br/>
</p>

<p align="center"><bold><code>lms</code> - Command Line Tool for <a href="https://lmstudio.ai/">LM Studio</a></bold></p>
<p align="cente

## Installation

`lms` ships with [LM Studio](https://lmstudio.ai/) 0.2.22 and newer.

If you have trouble running the command, try running `npx lmstudio install-cli` to add it to path.

To check if the bootstrapping was successful, run the following in a **👉 new terminal window 👈**:

```shell
lms
```

## Usage

You can use `lms --help` to see a list of all available subcommands.

For details about each subcommand, run `lms <subcommand> --help`.

Here are some frequently used commands:

- `lms status` - To check the status of LM Studio.
- `lms server start` - To start the local API server.
- `lms server stop` - To stop the local API server.
- `lms ls` - To list all downloaded models.
  - `lms ls --json` - To list all downloaded models in machine-readable JSON format.
- `lms ps` - To list all loaded mode
