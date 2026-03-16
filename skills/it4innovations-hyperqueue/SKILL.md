---
name: it4innovations-hyperqueue
description: "User-friendly Scheduler for sub-node tasks for HPC systems"
homepage: https://github.com/It4innovations/hyperqueue
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["node"]
---

# It4innovations Hyperqueue

<p align="center">
<img src="docs/imgs/hq.png">
</p>

![Tests](https://github.com/it4innovations/hyperqueue/actions/workflows/test.yml/badge.svg) [![DOI paper](https://img.shields.io/badge/Paper-10.1016/j.softx.2024.101814-blue.svg)](https://www.sciencedirect.com/science/article/pii/S2352711024001857) [![DOI software](https://zenodo.org/badge/349152473.svg)](https://zenodo.org/badge/latestdoi/349152473)

**HyperQueue** is a tool designed to simplify execution of large workflows (task graphs) on

## Installation

- Download the latest binary distribution from this [link](https://github.com/It4innovations/hyperqueue/releases/latest).
- Unpack the downloaded archive:

  ```bash
  $ tar -xvzf hq-<version>-linux-x64.tar.gz
  ```

- That's it! Just use the unpacked `hq` binary.

> If you want to try the newest features, you can also download a nightly
> [build](https://github.com/It4innovations/hyperqueue/releases/nightly).
