---
name: huggingface-nanotron
description: "Minimalistic large language model 3D-parallelism training"
homepage: https://github.com/huggingface/nanotron
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["datasets", "ninja", "node", "pip", "torch"]
---

# Huggingface Nanotron

<h1 align="center">⚡️ Nanotron</h1>

<p align="center">
    <a href="https://github.com/huggingface/nanotron/releases">
        <img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/nanotron.svg">
    </a>
    <a href="https://github.com/huggingface/nanotron/blob/master/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/huggingface/nanotron.svg?color=green">
    </a>
</p>

<h4 align="center">
    <p>
        <a href="#installation">Installa

## Installation

To run the code in this project, first create a Python virtual environment using e.g. `uv`:

```shell
uv venv nanotron --python 3.11 && source nanotron/bin/activate && uv pip install --upgrade pip
```

> [!TIP]
> For Hugging Face cluster users, add `export UV_LINK_MODE=copy` to your `.bashrc` to suppress cache warnings from `uv`

Next, install Pytorch:

```shell
uv pip install torch --index-url https://download.pytorch.org/whl/cu124
```

Then install the core dependencies with:

```shell
uv pip



```
