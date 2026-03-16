---
name: nvidia-nemo-guardrails
description: "NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based"
homepage: https://github.com/NVIDIA-NeMo/Guardrails
metadata:
  openclaw:
    emoji: "🖥️"
    auto_generated: true
    requires:
      bins: ["nemoguardrails", "pip"]
---

# Nvidia Nemo Guardrails

<!-- start-documentation-reuse -->

NeMo Guardrails enables developers building LLM-based applications to easily add **programmable guardrails** between the application code and the LLM.

<div align="center">
  <img src="https://github.com/NVIDIA-NeMo/Guardrails/raw/develop/docs/_static/images/programmable_guardrails.png"  width="75%" alt="Programmable Guardrails">
</div>

Key benefits of adding _programmable guardrails_ include:

- \*\*Building Trustworthy, Safe, and Secure LLM-based Applications

## Installation

To install using pip:

```bash
> pip install nemoguardrails
```

For more detailed instructions, see the [Installation Guide](https://docs.nvidia.com/nemo/guardrails/getting-started/installation-guide.html).

## Usage

To add programmable guardrails to your application you can use the Python API or a guardrails server (see the [Server Guide](https://docs.nvidia.com/nemo/guardrails/user-guides/server-guide.html) for more details). Using the Python API is similar to using the LLM directly. Calling the guardrails layer instead of the LLM requires only minimal changes to the code base, and it involves two simple steps:

1. Loading a guardrails configuration and creating an `LLMRails` instance.
2. Making the calls
