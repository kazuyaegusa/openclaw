---
name: ml-explore-mlx-lm
description: "Run LLMs with MLX"
homepage: https://github.com/ml-explore/mlx-lm
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["mlx-lm", "pip"]
---

# Ml Explore Mlx Lm

## MLX LM

## Usage

To generate text with an LLM use:

```bash
mlx_lm.generate --prompt "How tall is Mt Everest?"
```

To chat with an LLM use:

```bash
mlx_lm.chat
```

This will give you a chat REPL that you can use to interact with the LLM. The
chat context is preserved during the lifetime of the REPL.

Commands in `mlx-lm` typically take command line options which let you specify
the model, sampling parameters, and more. Use `-h` to see a list of available
options for a command, e.g.:

```bash
mlx_lm.generate -

```
