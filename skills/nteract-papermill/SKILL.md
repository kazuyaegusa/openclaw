---
name: nteract-papermill
description: "📚 Parameterize, execute, and analyze notebooks"
homepage: https://github.com/nteract/papermill
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["papermill", "pip"]
---

# Nteract Papermill

# <a href="https://github.com/nteract/papermill"><img src="https://media.githubusercontent.com/media/nteract/logos/master/nteract_papermill/exports/images/png/papermill_logo_wide.png" height="48px" /></a>

## Installation

From the command line:

```{.sourceCode .bash}
pip install papermill
```

For all optional io dependencies, you can specify individual bundles
like `s3`, or `azure` -- or use `all`. To use Black to format parameters you can add as an extra requires ['black'].

```{.sourceCode .bash}
pip install papermill[all]
```
