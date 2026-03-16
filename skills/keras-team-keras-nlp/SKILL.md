---
name: keras-team-keras-nlp
description: "Pretrained model hub for Keras 3."
homepage: https://github.com/keras-team/keras-hub
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["pip"]
---

# Keras Team Keras Nlp

# KerasHub: Multi-framework Pretrained Models

[![](https://github.com/keras-team/keras-hub/workflows/Tests/badge.svg?branch=master)](https://github.com/keras-team/keras-hub/actions?query=workflow%3ATests+branch%3Amaster)
![Python](https://img.shields.io/badge/python-v3.11.0+-success.svg)
[![Kaggle Models](https://img.shields.io/badge/Kaggle-Models-brightgreen?colorA=0099ff)](https://www.kaggle.com/organizations/keras/models)
[![contributions welcome](https://img.shields.io/badge/contributions-we

## Installation

To install the latest KerasHub release with Keras 3, simply run:

```
pip install --upgrade keras-hub
```

To install the latest nightly changes for both KerasHub and Keras, you can use
our nightly package.

```
pip install --upgrade keras-hub-nightly
```

Currently, installing KerasHub will always pull in TensorFlow for use of the
`tf.data` API for preprocessing. When pre-processing with `tf.data`, training
can still happen on any backend.

Visit the [core Keras getting started page](https://ke
