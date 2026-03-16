---
name: perpetual-ml-perpetual
description: "A self-generalizing gradient boosting machine that doesn't need hyperparameter optimization"
homepage: https://github.com/perpetual-ml/perpetual
metadata:
  openclaw:
    emoji: "⚡"
    auto_generated: true
    requires:
      bins: ["cargo", "pip"]
---

# Perpetual Ml Perpetual

<!-- markdownlint-disable MD033 -->

## Usage

You can use the algorithm like in the example below. Check examples folders for both Rust and Python.

```python
from perpetual import PerpetualBooster

model = PerpetualBooster(objective="SquaredLoss", budget=0.5)
model.fit(X, y)
```
