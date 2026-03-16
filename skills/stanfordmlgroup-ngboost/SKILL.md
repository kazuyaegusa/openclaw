---
name: stanfordmlgroup-ngboost
description: "Natural Gradient Boosting for Probabilistic Prediction"
homepage: https://github.com/stanfordmlgroup/ngboost
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["pip"]
---

# Stanfordmlgroup Ngboost

# NGBoost: Natural Gradient Boosting for Probabilistic Prediction

## Installation

```sh
via pip

pip install --upgrade ngboost

via conda-forge

conda install -c conda-forge ngboost
```

## Usage

Probabilistic regression example on the Boston housing dataset:

```python
from ngboost import NGBRegressor

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

```
