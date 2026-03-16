---
name: cvxgrp-cvxpylayers
description: "Differentiable convex optimization layers"
homepage: https://github.com/cvxpy/cvxpylayers
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["cvxpylayers", "pip", "pytest"]
---

# Cvxgrp Cvxpylayers

# CVXPYlayers

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install
cvxpylayers.

```bash
pip install cvxpylayers
```

Our package includes convex optimization layers for
PyTorch, JAX, and MLX;
the layers are functionally equivalent. You will need to install
[PyTorch](https://pytorch.org),
[JAX](https://github.com/google/jax), or
[MLX](https://github.com/ml-explore/mlx)
separately, which can be done by following the instructions on their websites.

CVXPYlayers has the following dependencies

## Usage

Below are usage examples of our PyTorch and JAX layers.
Note that the parametrized convex optimization problems must be constructed
in CVXPY, using
[DPP](https://www.cvxpy.org/tutorial/advanced/index.html#disciplined-parametrized-programming).
