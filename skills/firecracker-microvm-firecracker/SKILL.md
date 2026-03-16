---
name: firecracker-microvm-firecracker
description: "Secure and fast microVMs for serverless computing."
homepage: https://github.com/firecracker-microvm/firecracker
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["git", "go"]
---

# Firecracker Microvm Firecracker

<picture>
   <source media="(prefers-color-scheme: dark)" srcset="docs/images/fc_logo_full_transparent-bg_white-fg.png">
   <source media="(prefers-color-scheme: light)" srcset="docs/images/fc_logo_full_transparent-bg.png">
   <img alt="Firecracker Logo Title" width="750" src="docs/images/fc_logo_full_transparent-bg.png">
</picture>

Our mission is to enable secure, multi-tenant, minimal-overhead execution of
container and function workloads.

Read more about the Firecracker Charter [here](CHART

## Installation

To get started with Firecracker, download the latest
[release](https://github.com/firecracker-microvm/firecracker/releases) binaries
or build it from source.

You can build Firecracker on any Unix/Linux system that has Docker running (we
use a development container) and `bash` installed, as follows:

```bash
git clone https://github.com/firecracker-microvm/firecracker
cd firecracker
tools/devtool build
toolchain="$(uname -m)-unknown-linux-musl"
```

The Firecracker binary will be placed at
`buil
