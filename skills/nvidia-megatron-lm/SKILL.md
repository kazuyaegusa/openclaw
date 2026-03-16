---
name: nvidia-megatron-lm
description: "Ongoing research training transformer models at scale"
homepage: https://github.com/NVIDIA/Megatron-LM
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["git", "megatron-core", "pip"]
---

# Nvidia Megatron Lm

<div align="center">

# Megatron-LM and Megatron Core

<h4>GPU-optimized library for training transformer models at scale</h4>

[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](https://docs.nvidia.com/megatron-core/developer-guide/latest/index.html)
[![version](https://img.shields.io/badge/release-0.15.0-green)](./CHANGELOG.md)
[![license](https://img.shields.io/badge/license-Apache-blue)](./LICENSE)

<div align="left">

## Installation

**Install from PyPI:**

```bash
uv pip install megatron-core
```

**Or clone and install from source:**

```bash
git clone https://github.com/NVIDIA/Megatron-LM.git
cd Megatron-LM
uv pip install -e .
```

> **Note:** Building from source can use a lot of memory. If the build runs out of memory, limit parallel compilation jobs by setting `MAX_JOBS` (e.g. `MAX_JOBS=4 uv pip install -e .`).

For NGC container setup and all installation options, see the \*\*[Installation Guide](https://docs.nvidia.com
