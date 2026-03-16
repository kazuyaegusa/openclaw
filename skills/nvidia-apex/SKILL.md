---
name: nvidia-apex
description: "A PyTorch Extension: Tools for easy mixed precision and distributed training in Pytorch"
homepage: https://github.com/NVIDIA/apex
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["git", "pip"]
---

# Nvidia Apex

# Introduction

## Installation

Each [`apex.contrib`](./apex/contrib) module requires one or more install options other than `--cpp_ext` and `--cuda_ext`.
Note that contrib modules do not necessarily support stable PyTorch releases, some of them might only be compatible with nightlies.
