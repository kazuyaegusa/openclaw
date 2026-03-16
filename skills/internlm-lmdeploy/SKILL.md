---
name: internlm-lmdeploy
description: "LMDeploy is a toolkit for compressing, deploying, and serving LLMs."
homepage: https://github.com/InternLM/lmdeploy
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["lmdeploy", "modelscope", "openmind_hub", "pip"]
---

# Internlm Lmdeploy

<div align="center">
  <img src="docs/en/_static/image/lmdeploy-logo.svg" width="450"/>

[![PyPI](https://img.shields.io/pypi/v/lmdeploy)](https://pypi.org/project/lmdeploy)
![PyPI - Downloads](https://img.shields.io/pypi/dm/lmdeploy)
[![license](https://img.shields.io/github/license/InternLM/lmdeploy.svg)](https://github.com/InternLM/lmdeploy/tree/main/LICENSE)
[![issue resolution](https://img.shields.io/github/issues-closed-raw/InternLM/lmdeploy)](https://github.com/InternLM/lmdeploy/issues)
[

## Installation

It is recommended installing lmdeploy using pip in a conda environment (python 3.10 - 3.13):

```shell
conda create -n lmdeploy python=3.10 -y
conda activate lmdeploy
pip install lmdeploy
```

The default prebuilt package is compiled on **CUDA 12** since v0.3.0.

For the GeForce RTX 50 series, please install the LMDeploy prebuilt package complied with **CUDA 12.8**

```shell
export LMDEPLOY_VERSION=0.12.1
export PYTHON_VERSION=310
pip install https://github.com/InternLM/lmdeploy/releases/downloa



```
