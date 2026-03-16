---
name: leondz-garak
description: "the LLM vulnerability scanner"
homepage: https://github.com/NVIDIA/garak
metadata:
  openclaw:
    emoji: "🔒"
    auto_generated: true
    requires:
      bins: ["gh", "git", "go", "pip", "python3"]
---

# Leondz Garak

# garak, LLM vulnerability scanner

## Installation

The general syntax is:

`garak <options>`

`garak` needs to know what model to scan, and by default, it'll try all the probes it knows on that model, using the vulnerability detectors recommended by each probe. You can see a list of probes using:

`garak --list_probes`

To specify a generator, use the `--target_type` and, optionally, the `--target_name` options. Model type specifies a model family/interface; model name specifies the exact model to be used. The "Intro to generators" section below

## Usage

Probe a commercial model for encoding-based prompt injection (OSX/\*nix) (replace example value with a real OpenAI API key)

```
export OPENAI_API_KEY="sk-123XXXXXXXXXXXX"
python3 -m garak --target_type openai --target_name gpt-5-nano --probes encoding
```

See if the Hugging Face version of GPT2 is vulnerable to DAN 11.0

```
python3 -m garak --target_type huggingface --target_name gpt2 --probes dan.Dan_11_0
```
