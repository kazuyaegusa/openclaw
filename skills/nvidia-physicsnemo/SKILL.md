---
name: nvidia-physicsnemo
description: "Open-source deep-learning framework for building, training, and fine-tuning deep learning models"
homepage: https://github.com/NVIDIA/physicsnemo
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["docker", "git", "nvidia-modulus", "nvidia-physicsnemo", "pip", "warp-lang"]
---

# Nvidia Physicsnemo

# NVIDIA PhysicsNeMo

## Installation

You can install PhysicsNeMo in two supported ways: **via pip** (native pip or
**uv**) or by using the **NVIDIA container image**. Choose the method that fits your
environment and workflow.

The following instructions cover the base PhysicsNeMo modules. Optional dependencies
are listed in [`pyproject.toml`](./pyproject.toml). The [training recipes](./examples)
are not bundled in the pip wheels or container; clone the repo and use the examples
as a starting point. Many examples have a `requirement
