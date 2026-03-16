---
name: flagopen-flagembedding
description: "Retrieval and Retrieval-augmented LLMs"
homepage: https://github.com/FlagOpen/FlagEmbedding
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["finetune", "git", "pip"]
---

# Flagopen Flagembedding

[<img src="./imgs/FlagOpen.png">](https://flagopen.baai.ac.cn/)

<h1 align="center">⚡️BGE: One-Stop Retrieval Toolkit For Search and RAG</h1>

![bge_logo](./imgs/bge_logo.jpg)

<p align="center">
    <a href="https://huggingface.co/collections/BAAI/bge-66797a74476eb1f085c7446d">
        <img alt="Build" src="https://img.shields.io/badge/BGE_series-🤗-yellow">
    </a>
    <a href="https://github.com/FlagOpen/FlagEmbedding">
            <img alt="Build" src="https://img.shields.io/badge/Contributi

## Usage

First, load one of the BGE embedding model:

```
from FlagEmbedding import FlagAutoModel

model = FlagAutoModel.from_finetuned('BAAI/bge-base-en-v1.5',
                                      query_instruction_for_retrieval="Represent this sentence for searching relevant passages:",
                                      use_fp16=True)
```

Then, feed some sentences to the model and get their embeddings:

```
sentences_1 = ["I love NLP", "I love machine learning"]
sentences_2 = ["I love BGE", "I love

```
