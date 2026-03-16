---
name: bruin-data-ingestr
description: "ingestr is a CLI tool to copy data between any databases with a single command seamlessly."
homepage: https://github.com/bruin-data/ingestr
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["pip", "uv"]
---

# Bruin Data Ingestr

<div align="center">
    <img src="https://github.com/bruin-data/ingestr/blob/main/resources/ingestr.svg?raw=true" width="500" />
    <p>Copy data from any source to any destination without any code</p>
    <img src="https://github.com/bruin-data/ingestr/blob/main/resources/demo.gif?raw=true" width="750" />
</div>

<div align="center" style="margin-top: 24px;">
  <a target="_blank" href="https://join.slack.com/t/bruindatacommunity/shared_invite/zt-2dl2i8foy-bVsuMUauHeN9M2laVm3ZVg" style="backgro

## Installation

We recommend using [uv](https://github.com/astral-sh/uv) to run `ingestr`.

```
pip install uv
uvx ingestr
```

Alternatively, if you'd like to install it globally:

```
uv pip install --system ingestr
```

While installation with vanilla `pip` is possible, it's an order of magnitude slower.
