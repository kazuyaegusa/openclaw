---
name: huggingface-evaluate
description: "🤗 Evaluate: A library for easily evaluating machine learning models and datasets."
homepage: https://github.com/huggingface/evaluate
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["evaluate", "pip"]
---

# Huggingface Evaluate

<p align="center">
    <br>
    <img src="https://huggingface.co/datasets/evaluate/media/resolve/main/evaluate-banner.png" width="400"/>
    <br>
</p>

<p align="center">
    <a href="https://github.com/huggingface/evaluate/actions/workflows/ci.yml?query=branch%3Amain">
        <img alt="Build" src="https://github.com/huggingface/evaluate/actions/workflows/ci.yml/badge.svg?branch=main">
    </a>
    <a href="https://github.com/huggingface/evaluate/blob/master/LICENSE">
        <img al

## Usage

🤗 Evaluate's main methods are:

- `evaluate.list_evaluation_modules()` to list the available metrics, comparisons and measurements
- `evaluate.load(module_name, **kwargs)` to instantiate an evaluation module
- `results = module.compute(*kwargs)` to compute the result of an evaluation module
