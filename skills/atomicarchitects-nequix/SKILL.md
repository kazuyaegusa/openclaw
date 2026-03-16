---
name: atomicarchitects-nequix
description: "[NeurIPS'25 AI4Mat] Nequix: Training a foundation model for materials on a budget and [arXiv'26]"
homepage: https://github.com/atomicarchitects/nequix
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["git", "nequix", "node", "openequivariance_extjax", "pip"]
---

# Atomicarchitects Nequix

<h1 align='center'>Nequix</h1>

Source code and model weights for the [Nequix foundation model](https://arxiv.org/abs/2508.16067), and [Phonon fine-tuning (PFT)](https://arxiv.org/abs/2601.07742).

| Model             | Dataset           | Theory               | Reference                                  |
| ----------------- | ----------------- | -------------------- | ------------------------------------------ |
| `nequix-mp-1`     | MPtrj             | DFT (PBE+U)          | [Nequix](https://arxiv.org/abs/2508.16067) |
| `nequix-mp-1-pft` | MPtrj, MDR Phonon | DFT (PBE+U)          | [PFT](https://arxiv.org/abs/2601.07742)    |
| `nequix-omat-1`   | OMat24            | DFT (PBE+U, VASP 54) | [PFT](https:/                              |

## Installation

```bash
pip install nequix
```

to use [OpenEquivariance](https://github.com/PASSIONLab/OpenEquivariance) kernels,

```bash
pip install nequix[oeq]



```
