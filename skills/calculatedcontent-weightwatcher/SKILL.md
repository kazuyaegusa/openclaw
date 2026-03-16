---
name: calculatedcontent-weightwatcher
description: "The WeightWatcher tool for predicting the accuracy of Deep Neural Networks"
homepage: https://github.com/CalculatedContent/WeightWatcher
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["git", "pip", "python3", "weightwatcher"]
---

# Calculatedcontent Weightwatcher

[![Downloads](http://pepy.tech/badge/weightwatcher)](http://pepy.tech/project/weightwatcher)
[![PyPI](https://img.shields.io/pypi/v/weightwatcher?color=teal&label=release)](https://pypi.org/project/weightwatcher/)
[![GitHub](https://img.shields.io/github/license/calculatedcontent/weightwatcher?color=blue)](./LICENSE.txt)
[![Published in Nature](https://img.shields.io/badge/Published%20in-Nature-teal)](https://nature.com/articles/s41467-021-24025-8)
[![Video Tutorial](https://img.shields.io/badge

## Usage

```python
import weightwatcher as ww
import torchvision.models as models

model = models.vgg19_bn(pretrained=True)
watcher = ww.WeightWatcher(model=model)
details = watcher.analyze()
summary = watcher.get_summary(details)
```

It is as easy to run and generates a pandas dataframe with details (and plots) for each layer

![Sample Details Dataframe](./img/sample-ww-details.png)

and `summary` dictionary of generalization metrics

```python
    {'log_norm': 2.11,      'alpha': 3.06,
      'alpha_we

```
