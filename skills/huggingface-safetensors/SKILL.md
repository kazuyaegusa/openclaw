---
name: huggingface-safetensors
description: "Simple, safe way to store and distribute tensors"
homepage: https://github.com/huggingface/safetensors
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["curl", "git", "go", "pip", "safetensors", "setuptools_rust"]
---

# Huggingface Safetensors

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://huggingface.co/datasets/safetensors/assets/raw/main/banner-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://huggingface.co/datasets/safetensors/assets/raw/main/banner-light.svg">
    <img alt="Hugging Face Safetensors Library" src="https://huggingface.co/datasets/safetensors/assets/raw/main/banner-light.svg" style="max-width: 100%;">
  </picture>
  <br/>
  <br/>
</p>

Pytho

## Installation

```python
import torch
from safetensors import safe_open
from safetensors.torch import save_file

tensors = {
   "weight1": torch.zeros((1024, 1024)),
   "weight2": torch.zeros((1024, 1024))
}
save_file(tensors, "model.safetensors")

tensors = {}
with safe_open("model.safetensors", framework="pt", device="cpu") as f:
   for key in f.keys():
       tensors[key] = f.get_tensor(key)
```

[Python documentation](https://huggingface.co/docs/safetensors/index)
