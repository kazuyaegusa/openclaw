---
name: tmbdev-webdataset
description: "A high-performance Python-based I/O system for large (and small) deep learning problems, with"
homepage: https://github.com/webdataset/webdataset
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["curl", "pip", "webdataset"]
---

# Tmbdev Webdataset

[![Test](https://github.com/tmbdev/webdataset/workflows/CI/badge.svg)](https://github.com/tmbdev/webdataset/actions?query=workflow%3ACI)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/tmbdev/webdataset/?ref=repository-badge)

```python
%matplotlib inline
import matplotlib.pyplot as plt
import torch.utils.data
import torch.nn
from random import randrange
import os
os.environ["WDS_VERBOSE_CACHE"] = "1"
os.environ["GOPEN_VERBOSE"] = "0"
```
