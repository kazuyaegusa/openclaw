---
name: lightly-ai-lightly-train
description: "All-in-one training for vision models (YOLO, ViTs, RT-DETR, DINOv3): pretraining, fine-tuning,"
homepage: https://github.com/lightly-ai/lightly-train
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["lightly-train", "pip"]
---

# Lightly Ai Lightly Train

# LightlyTrain - SOTA Pretraining, Fine-tuning and Distillation

## Installation

Install Lightly**Train** on Python 3.8+ for Windows, Linux or MacOS with:

```bash
pip install lightly-train
```

## Usage

[![Documentation](https://img.shields.io/badge/Documentation-blue)](https://docs.lightly.ai/train/stable/object_detection.html)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lightly-ai/lightly-train/blob/main/examples/notebooks/object_detection.ipynb)

```python
import lightly_train

if __name__ == "__main__":
    # Train an object detection model with a DINOv3 backbone
    lightly_train.train_object_detection(
        out="out/my_e

```
