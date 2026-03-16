---
name: layumi-person-reid-baseline-pytorch
description: ":bouncing_ball_person: Pytorch ReID: A tiny, friendly, strong pytorch implement of person re-id /"
homepage: https://github.com/layumi/Person_reID_baseline_pytorch
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["gdown", "git", "pip", "pretrainedmodels", "timm"]
---

# Layumi Person Reid Baseline Pytorch

<h1 align="center"> Pytorch ReID </h1>
<h2 align="center"> Strong, Small, Friendly </h2>

![Python3.6+](https://img.shields.io/badge/python-3.6+-green.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Citations](https://img.shields.io/badge/Citations-2500%2B-brightgreen)](https://scholar.google.com/scholar?cites=270746001988088124)
[![Stars](https://img.shields.io/github/stars/layumi/Person_reID_baseline_pytorch)](https://github.co

## Installation

- Install Pytorch from http://pytorch.org/
- Install required packages

```bash
pip install -r requirements.txt
```

- [Optional] You may skip it. Usually it comes with pytorch. Install Torchvision from the source

```bash
git clone https://github.com/pytorch/vision
cd vision
python setup.py install
```

- [Optional] You may skip it. Install apex from the source

```bash
git clone https://github.com/NVIDIA/apex.git
cd apex
python setup.py install --cuda_ext --cpp_ext
```

Because pytorch and torchvisi
