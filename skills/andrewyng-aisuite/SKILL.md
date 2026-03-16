---
name: andrewyng-aisuite
description: "Simple, unified interface to multiple Generative AI providers"
homepage: https://github.com/andrewyng/aisuite
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["aisuite", "npm", "pip", "server-filesystem"]
---

# Andrewyng Aisuite

# aisuite

## Installation

You can install just the base `aisuite` package, or install a provider's package along with `aisuite`.

Install just the base package without any provider SDKs:

```shell
pip install aisuite
```

Install aisuite with a specific provider (e.g., Anthropic):

```shell
pip install 'aisuite[anthropic]'
```

Install aisuite with all provider libraries:

```shell
pip install 'aisuite[all]'
```
