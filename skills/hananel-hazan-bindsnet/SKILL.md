---
name: hananel-hazan-bindsnet
description: "Simulation of spiking neural networks (SNNs) using PyTorch."
homepage: https://github.com/BindsNET/bindsnet
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["docker", "pip"]
---

# Hananel Hazan Bindsnet

<p align="center"><img width="25%" src="docs/logo.png"/></p>

A Python package used for simulating spiking neural networks (SNNs) on CPUs or GPUs using [PyTorch](http://pytorch.org/) `Tensor` functionality.

BindsNET is a spiking neural network simulation library geared towards the development of biologically inspired algorithms for machine learning.

This package is used as part of ongoing research on applying SNNs, machine learning (ML) and reinforcement learning (RL) problems in the [Biologic

## Installation

To run a near-replication of the SNN from [this paper](https://www.frontiersin.org/articles/10.3389/fncom.2015.00099/full#), issue

```
cd examples/mnist
python eth_mnist.py
```

There are a number of optional command-line arguments which can be passed in, including `--plot` (displays useful monitoring figures), `--n_neurons [int]` (number of excitatory, inhibitory neurons simulated), `--mode ['train' | 'test']` (sets network operation to the training or testing phase), and more. Run the script
