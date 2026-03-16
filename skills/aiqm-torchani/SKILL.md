---
name: aiqm-torchani
description: "TorchANI 2.0 is an open-source library that supports training, development, and research of"
homepage: https://github.com/aiqm/torchani
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["git", "pip", "torchani"]
---

# Aiqm Torchani

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/aiqm/torchani/main/front-logo-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/aiqm/torchani/main/front-logo-light.png">
  <img alt="TorchANI 2 logo" src="https://raw.githubusercontent.com/aiqm/torchani/main/torchani-logo-light.png">
</picture>
</div>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](http

## Installation

We recommend installing `torchani` inside a `conda|mamba` environment, or a `venv`.

⚠️ **Important**: _Please install torchani with pip if you want the latest version, even
if using a conda env since the torchani conda package is currently not maintained._

We also recommended you first install a specific torch version, with a specific CUDA
toolkit backend, for example:

```bash
pip install torch==2.8 --index-url https://download.pytorch.org/whl/cu129
```

for the version with CUDA 12.9. This
