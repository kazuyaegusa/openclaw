---
name: huggingface-trl
description: "Train transformer language models with reinforcement learning."
homepage: https://github.com/huggingface/trl
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["git", "pip", "trl"]
---

# Huggingface Trl

TRL is a cutting-edge library designed for post-training foundation models using advanced techniques like Supervised Fine-Tuning (SFT), Group Relative Policy Optimization (GRPO), and Direct Preference Optimization (DPO). Built on top of the [🤗 Transformers](https://github.com/huggingface/transformers) ecosystem, TRL supports a variety of model architectures and modalities, and can be scaled-up across various hardware setups.

## Usage

For more flexibility and control over training, TRL provides dedicated trainer classes to post-train language models or PEFT adapters on a custom dataset. Each trainer in TRL is a light wrapper around the 🤗 Transformers trainer and natively supports distributed training methods like DDP, DeepSpeed ZeRO, and FSDP.
