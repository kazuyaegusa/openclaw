---
name: pulp-platform-bender
description: "A dependency management tool for hardware projects."
homepage: https://github.com/pulp-platform/bender
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["bender", "cargo", "curl", "git"]
---

# Pulp Platform Bender

# bender

## Installation

To use Bender for a single project, the simplest is to download and use a precompiled binary. We provide binaries for all current versions of Ubuntu and CentOS, as well as generic Linux, on each release. Open a terminal and enter the following command:

```sh
curl --proto '=https' --tlsv1.2 https://pulp-platform.github.io/bender/init -sSf | sh
```

The command downloads and executes a script that detects your distribution and downloads the appropriate `bender` binary of the latest release to you
