---
name: deepspeedai-deepspeed
description: "DeepSpeed is a deep learning optimization library that makes distributed training and inference"
homepage: https://github.com/deepspeedai/DeepSpeed
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["deepspeed", "pip"]
---

# Deepspeedai Deepspeed

[![License Apache 2.0](https://badgen.net/badge/license/apache2.0/blue)](https://github.com/deepspeedai/DeepSpeed/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/deepspeed.svg)](https://pypi.org/project/deepspeed/)
[![Downloads](https://static.pepy.tech/badge/deepspeed)](https://pepy.tech/project/deepspeed)
[![Build](https://badgen.net/badge/build/check-status/blue)](#build-pipeline-status)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/9530/badge)](https://www.

## Installation

The quickest way to get started with DeepSpeed is via pip, this will install
the latest release of DeepSpeed which is not tied to specific PyTorch or CUDA
versions. DeepSpeed includes several C++/CUDA extensions that we commonly refer
to as our 'ops'. By default, all of these extensions/ops will be built
just-in-time (JIT) using [torch's JIT C++ extension loader that relies on
ninja](https://pytorch.org/docs/stable/cpp_extension.html) to build and
dynamically link them at runtime.
