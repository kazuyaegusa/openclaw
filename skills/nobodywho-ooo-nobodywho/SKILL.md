---
name: nobodywho-ooo-nobodywho
description: "NobodyWho is an inference engine that lets you run LLMs locally and efficiently on any device."
homepage: https://github.com/nobodywho-ooo/nobodywho
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["go", "nobodywho", "pip"]
---

# Nobodywho Ooo Nobodywho

![Nobody Who](./assets/banner.png)

[![Discord](https://img.shields.io/discord/1308812521456799765?logo=discord&style=flat-square)](https://discord.gg/qhaMc2qCYB)
[![Matrix](https://img.shields.io/badge/Matrix-000?logo=matrix&logoColor=fff)](https://matrix.to/#/#nobodywho:matrix.org)
[![Mastodon](https://img.shields.io/badge/Mastodon-6364FF?logo=mastodon&logoColor=fff&style=flat-square)](https://mastodon.gamedev.place/@nobodywho)
[![Godot Engine](https://img.shields.io/badge/Godot-%23FFFFFF.svg?

## Usage

Start by installing NobodyWho. This is simply

```sh
pip install nobodywho
```

Next download a model. For a quick start we recommend [this one](https://huggingface.co/bartowski/Qwen_Qwen3-0.6B-GGUF/resolve/main/Qwen_Qwen3-0.6B-Q4_K_M.gguf). It is quite small, but will get the job done.

Then you start generating a response from the model with the following code snippet:

```python
from nobodywho import Chat
chat = Chat("./path/to/your/model.gguf")
response = chat.ask("Is water wet?")
for token

```
