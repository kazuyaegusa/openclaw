---
name: huggingface-candle
description: "Minimalist ML framework for Rust"
homepage: https://github.com/huggingface/candle
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["cargo", "curl", "git"]
---

# Huggingface Candle

# candle

[![discord server](https://dcbadge.limes.pink/api/server/hugging-face-879548962464493619)](https://discord.gg/hugging-face-879548962464493619)
[![Latest version](https://img.shields.io/crates/v/candle-core.svg)](https://crates.io/crates/candle-core)
[![Documentation](https://docs.rs/candle-core/badge.svg)](https://docs.rs/candle-core)
[![License](https://img.shields.io/github/license/base-org/node?color=blue)](https://github.com/huggingface/candle/blob/main/LICENSE-MIT)
[![License](http

## Usage

<!--- ANCHOR: cheatsheet --->

Cheatsheet:

|          | Using PyTorch                    | Using Candle                                          |
| -------- | -------------------------------- | ----------------------------------------------------- |
| Creation | `torch.Tensor([[1, 2], [3, 4]])` | `Tensor::new(&[[1f32, 2.], [3., 4.]], &Device::Cpu)?` |
| Creation | `torch.zeros((2, 2))`            | `Tensor::zeros((2, 2), DT                             |
