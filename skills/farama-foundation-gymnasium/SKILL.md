---
name: farama-foundation-gymnasium
description: "An API standard for single-agent reinforcement learning environments, with popular reference"
homepage: https://github.com/Farama-Foundation/Gymnasium
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["gymnasium", "pip"]
---

# Farama Foundation Gymnasium

[![Python](https://img.shields.io/pypi/pyversions/gymnasium.svg)](https://badge.fury.io/py/gymnasium)
[![PyPI](https://badge.fury.io/py/gymnasium.svg)](https://badge.fury.io/py/gymnasium)
[![arXiv](https://img.shields.io/badge/arXiv-2407.17032-b31b1b.svg)](https://arxiv.org/abs/2407.17032)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![License](https://img.shields.io/github/license/Farama-Foundation/Gymnas

## Installation

To install the base Gymnasium library, use `pip install gymnasium`

This does not include dependencies for all families of environments (there's a massive number, and some can be problematic to install on certain systems). You can install these dependencies for one family like `pip install "gymnasium[atari]"` or use `pip install "gymnasium[all]"` to install all dependencies.

We support and test for Python 3.10, 3.11, 3.12 and 3.13 on Linux and macOS. We will accept PRs related to Windows, but d
