---
name: eleutherai-lm-evaluation-harness
description: "A framework for few-shot evaluation of language models."
homepage: https://github.com/EleutherAI/lm-evaluation-harness
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["docker", "git", "node", "pip"]
---

# Eleutherai Lm Evaluation Harness

This project provides a unified framework to test generative language models on a large number of different evaluation tasks.

**Features:**

- Over 60 standard academic benchmarks for LLMs, with hundreds of subtasks and variants implemented.
- Support for models loaded via [transformers](https://github.com/huggingface/transformers/) (including quantization via [GPTQModel](https://github.com/ModelCloud/GPTQModel) and [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ)), [GPT-NeoX](https://github.co

## Installation

To install the `lm-eval` package from the github repository, run:

```bash
git clone --depth 1 https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness
pip install -e .
```
