---
name: openrlhf-openrlhf
description: "An Easy-to-use, Scalable and High-performance Agentic RL Framework based on Ray (PPO & DAPO &"
homepage: https://github.com/OpenRLHF/OpenRLHF
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["docker", "git", "node", "openrlhf", "pip", "python3"]
---

# Openrlhf Openrlhf

<div align="center">
    <img alt="OpenRLHF logo" src="./docs/logo.png" style="height: 140px;" />
</div>
<div align="center">
<p align="center">
      <a href="https://github.com/OpenRLHF/OpenRLHF/graphs/contributors">
        <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/OpenRLHF/OpenRLHF" />
      </a>
      <a href="https://github.com/OpenRLHF/OpenRLHF/issues">
        <img alt="Issues" src="https://img.shields.io/github/issues/OpenRLHF/OpenRLHF?color=0088ff"

## Installation

**Recommended**: Use Docker for hassle-free setup

````bash



## Usage

```bash
ray job submit --address="http://127.0.0.1:8265" \
  --runtime-env-json='{"working_dir": "/openrlhf"}' \
  -- python3 -m openrlhf.cli.train_ppo_ray \
  --pretrain meta-llama/Meta-Llama-3-8B \
  --use_dynamic_batch \
  --remote_rm_url /path/to/reward_func.py \
  --label_key answer \
  --prompt_data your_prompt_dataset \
  ... # other training args
````

**Key Parameter**: `--label_key answer` passes the "answer" field from your dataset to `reward_func` as `labels`.

> [!TIP] \*_Use Cases_
