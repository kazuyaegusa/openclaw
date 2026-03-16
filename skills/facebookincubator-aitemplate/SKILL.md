---
name: facebookincubator-aitemplate
description: "AITemplate is a Python framework which renders neural network into high performance CUDA/HIP C++"
homepage: https://github.com/facebookincubator/AITemplate
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["docker", "git", "go", "node", "pip"]
---

# Facebookincubator Aitemplate

# AITemplate

## Installation

**Hardware requirements:**

- **NVIDIA**: AIT is only tested on SM80+ GPUs (Ampere etc). Not all kernels work with old SM75/SM70 (T4/V100) GPUs.
- **AMD**: AIT is only tested on CDNA2 (MI-210/250) GPUs. There may be compiler issues for old CDNA1 (MI-100) GPUs.
