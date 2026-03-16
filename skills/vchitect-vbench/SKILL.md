---
name: vchitect-vbench
description: "[CVPR2024 Highlight] VBench - We Evaluate Video Generation"
homepage: https://github.com/Vchitect/VBench
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["git", "pip", "torch", "vbench"]
---

# Vchitect Vbench

![vbench_logo](https://raw.githubusercontent.com/Vchitect/VBench/master/asset/vbench_logo_github_20240605.jpg)

<!-- [![arXiv](https://img.shields.io/badge/arXiv-2311.99999-b31b1b.svg)](https://arxiv.org/abs/2311.99999) -->

[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Leaderboard-blue)](https://huggingface.co/spaces/Vchitect/VBench_Leaderboard)
[![VBench Arena (View Generated Videos Here!)](https://img.shields.io/badge/%F0%9F%A4%97%20VBench%20Arena-blue)](https://h

## Usage

Use VBench to evaluate videos, and video generative models.

- A Side Note: VBench is designed for evaluating different models on a standard benchmark. Therefore, by default, we enforce evaluation on the **standard VBench prompt lists** to ensure **fair comparisons** among different video generation models. That's also why we give warnings when a required video is not found. This is done via defining the set of prompts in [VBench_full_info.json](https://github.com/Vchitect/VBench/blob/master/vben
