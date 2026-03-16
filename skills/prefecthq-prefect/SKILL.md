---
name: prefecthq-prefect
description: "Prefect is a workflow orchestration framework for building resilient data pipelines in Python."
homepage: https://github.com/PrefectHQ/prefect
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["go", "pip"]
---

# Prefecthq Prefect

<p align="center"><img src="https://github.com/PrefectHQ/prefect/assets/3407835/c654cbc6-63e8-4ada-a92a-efd2f8f24b85" width=1000></p>

<p align="center">
    <a href="https://pypi.org/project/prefect/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect?color=0052FF&labelColor=090422" />
    </a>
    <a href="https://pypi.org/project/prefect/" alt="PyPI downloads/month">
        <img alt="Downloads" src="https://img.shields.io/pypi/dm/prefect?color=0052FF&label

## Installation

Prefect requires Python 3.10+. To [install the latest version of Prefect](https://docs.prefect.io/v3/get-started/install), run one of the following commands:

```bash
pip install -U prefect
```

```bash
uv add prefect
```

Then create and run a Python file that uses Prefect `flow` and `task` decorators to orchestrate and observe your workflow - in this case, a simple script that fetches the number of GitHub stars from a repository:

```python
from prefect import flow, task
import httpx


@task(l



```
