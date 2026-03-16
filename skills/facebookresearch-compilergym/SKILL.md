---
name: facebookresearch-compilergym
description: "Reinforcement learning environments for compiler and program optimization tasks"
homepage: https://github.com/facebookresearch/CompilerGym
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["pip"]
---

# Facebookresearch Compilergym

![CompilerGym](https://github.com/facebookresearch/CompilerGym/raw/development/docs/source/_static/img/logo-padded.png)

<p align="center">
  <!-- Getting started colab -->
  <a href="https://colab.research.google.com/github/facebookresearch/CompilerGym/blob/stable/examples/getting-started.ipynb">
      <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Colab" height="20">
  </a>
  <!-- Supported python versions list -->
  <a href="https://pypi.org/project/compiler-gym/">


## Installation

Install the latest CompilerGym release using:

    pip install -U compiler_gym

See
[INSTALL.md](https://github.com/facebookresearch/CompilerGym/blob/development/INSTALL.md)
for further details.

## Usage

Starting with CompilerGym is simple. If you not already familiar with the gym
interface, refer to the [getting started
guide](http://facebookresearch.github.io/CompilerGym/getting_started.html) for
an overview of the key concepts.

In Python, import `compiler_gym` to use the environments:

```py
>>> import compiler_gym                      # imports the CompilerGym environments
>>> env = compiler_gym.make(                 # creates a new environment (same as gym.make)
...     "llvm-v0",

```
