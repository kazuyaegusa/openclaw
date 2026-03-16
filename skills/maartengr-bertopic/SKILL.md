---
name: maartengr-bertopic
description: "Leveraging BERT and c-TF-IDF to create easily interpretable topics."
homepage: https://github.com/MaartenGr/BERTopic
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["bertopic", "go", "pip"]
---

# Maartengr Bertopic

[![PyPI Downloads](https://static.pepy.tech/badge/bertopic)](https://pepy.tech/projects/bertopic)
[![PyPI - Python](https://img.shields.io/badge/python-v3.10+-blue.svg)](https://pypi.org/project/bertopic/)
[![Build](https://img.shields.io/github/actions/workflow/status/MaartenGr/BERTopic/testing.yml?branch=master)](https://github.com/MaartenGr/BERTopic/actions)
[![docs](https://img.shields.io/badge/docs-Passing-green.svg)](https://maartengr.github.io/BERTopic/)
[![PyPI - PyPi](https://img.shield

## Installation

Installation, with sentence-transformers, can be done using [uv](https://docs.astral.sh/uv/):

```bash
uv add bertopic
```

or with [pip](https://github.com/pypa/pip):

```bash
pip install bertopic
```

If you want to install BERTopic with other embedding models, you can choose one of the following:

````bash



## Usage

We start by extracting topics from the well-known 20 newsgroups dataset containing English documents:

```python
from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups

docs = fetch_20newsgroups(subset='all',  remove=('headers', 'footers', 'quotes'))['data']

topic_model = BERTopic()
topics, probs = topic_model.fit_transform(docs)
````

After generating topics and their probabilities, we can access all of the topics together with their topic representations:

```python
>>>

```
