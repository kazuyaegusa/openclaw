---
name: optimalscale-lmflow
description: "An Extensible Toolkit for Finetuning and Inference of Large Foundation Models. Large Models for All."
homepage: https://github.com/OptimalScale/LMFlow
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["git", "gradio", "pip"]
---

# Optimalscale Lmflow

<p align="center" width="50%">
<img src="docs/assets/logo.png" alt="LMFlow" style="width: 50%; min-width: 200px; display: block; margin: auto; background-color: transparent;">
</p>

## Installation

Our package has been tested on Linux OS (Ubuntu 20.04). Other OS platforms (MacOS, Windows) are not fully tested, where you may encounter unexpected errors. If you are using LMFlow for the first time, we recommend you to try on a Linux machine or Google Colab.

```bash
git clone -b v1.0.0 https://github.com/OptimalScale/LMFlow.git
cd LMFlow
conda create -n lmflow python=3.9 -y
conda activate lmflow
conda install mpi4py
pip install -e .
```

<details><summary> Looking for a previous version? </su
