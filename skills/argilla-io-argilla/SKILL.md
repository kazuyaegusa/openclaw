---
name: argilla-io-argilla
description: "Argilla is a collaboration tool for AI engineers and domain experts to build high-quality datasets"
homepage: https://github.com/argilla-io/argilla
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["argilla", "datasets", "pip"]
---

# Argilla Io Argilla

> [!IMPORTANT]
> The original authors have moved on to exciting new projects! The codebase is mature and stable, having served users reliably for years. While we won't be adding new features going forward, we're committed to solve bug fixes and publish patches as needed.
> If you're interested in helping maintain or extend this project, we'd love to hear from you! Please open an issue to discuss becoming a maintainer - we're looking for dedicated contributors who can take ownership of the project's

## Installation

First things first! You can install the SDK with pip as follows:

```console
pip install argilla
```

After that, you will need to deploy Argilla Server. The easiest way to do this is through our [free Hugging Face Spaces deployment integration](https://huggingface.co/new-space?template=argilla/argilla-template-space).

To use the client, you need to import the `Argilla` class and instantiate it with the API URL and API key.

```python
import argilla as rg

client = rg.Argilla(api_url="https://[



```
