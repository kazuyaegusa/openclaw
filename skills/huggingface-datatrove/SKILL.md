---
name: huggingface-datatrove
description: "Freeing data processing from scripting madness by providing a set of platform-agnostic customizable"
homepage: https://github.com/huggingface/datatrove
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["git", "go", "pip"]
---

# Huggingface Datatrove

# DataTrove

## Installation

```bash
pip install datatrove[FLAVOUR]
```

Available flavours (combine them with `,` i.e. `[processing,s3]`):

- `all` installs everything: `pip install datatrove[all]`
- `io` dependencies to read `warc/arc/wet` files and arrow/parquet/[Optimized-parquet](https://huggingface.co/docs/hub/en/datasets-libraries#optimized-parquet-files) formats: `pip install datatrove[io]`
- `processing` dependencies for text extraction, filtering and tokenization: `pip install datatrove[processing]`
- `s3` s3 suppor
