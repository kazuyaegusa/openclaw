---
name: farama-foundation-pettingzoo
description: "An API standard for multi-agent reinforcement learning environments, with popular reference"
homepage: https://github.com/Farama-Foundation/PettingZoo
metadata:
  openclaw:
    emoji: "🕵️"
    auto_generated: true
    requires:
      bins: ["pettingzoo", "pip"]
---

# Farama Foundation Pettingzoo

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<p align="center">
    <a href = "https://pettingzoo.farama.org/" target = "_blank"><img src="https://raw.githubusercontent.com/Farama-Foundation/PettingZoo/master/pettingzoo-text.png" width="500px"/> </a>
</p>

PettingZoo is a Python library for cond

## Installation

To install the base PettingZoo library: `pip install pettingzoo`.

This does not include dependencies for all families of environments (some environments can be problematic to install on certain systems).

To install the dependencies for one family, use `pip install 'pettingzoo[atari]'`, or use `pip install 'pettingzoo[all]'` to install all dependencies.

We support and maintain PettingZoo for Python 3.9, 3.10, 3.11, and 3.12 on Linux and macOS. We will accept PRs related to Windows, but do not
