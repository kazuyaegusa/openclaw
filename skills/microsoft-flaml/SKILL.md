---
name: microsoft-flaml
description: "A fast library for AutoML and tuning. Join our Discord: https://discord.gg/Cppx2vSPVP."
homepage: https://github.com/microsoft/FLAML
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["flaml", "pip"]
---

# Microsoft Flaml

[![PyPI version](https://badge.fury.io/py/FLAML.svg)](https://badge.fury.io/py/FLAML)
![Conda version](https://img.shields.io/conda/vn/conda-forge/flaml)
[![Build](https://github.com/microsoft/FLAML/actions/workflows/python-package.yml/badge.svg)](https://github.com/microsoft/FLAML/actions/workflows/python-package.yml)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/FLAML)](https://pypi.org/project/FLAML/)
[![Downloads](https://pepy.tech/badge/flaml)](https://pepy.tech/project/f

## Installation

The latest version of FLAML requires **Python >= 3.10 and < 3.14**. While other Python versions may work for core components, full model support is not guaranteed. FLAML can be installed via `pip`:

```bash
pip install flaml
```

Minimal dependencies are installed without extra options. You can install extra options based on the feature you need. For example, use the following to install the dependencies needed by the [`automl`](https://microsoft.github.io/FLAML/docs/Use-Cases/Task-Oriented-Auto
