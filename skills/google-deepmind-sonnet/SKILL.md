---
name: google-deepmind-sonnet
description: "TensorFlow-based neural network library"
homepage: https://github.com/google-deepmind/sonnet
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["dm-sonnet", "pip", "tensorflow"]
---

# Google Deepmind Sonnet

![Sonnet](https://sonnet.dev/images/sonnet_logo.png)

## Installation

To get started install TensorFlow 2.0 and Sonnet 2:

```shell
$ pip install tensorflow tensorflow-probability
$ pip install dm-sonnet
```

You can run the following to verify things installed correctly:

```python
import tensorflow as tf
import sonnet as snt

print("TensorFlow version {}".format(tf.__version__))
print("Sonnet version {}".format(snt.__version__))
```

## Usage

The easiest way to try Sonnet is to use Google Colab which offers a free Python
notebook attached to a GPU or TPU.

- [Predicting MNIST with an MLP](https://colab.research.google.com/github/deepmind/sonnet/blob/v2/examples/mlp_on_mnist.ipynb)
- [Training a Little GAN on MNIST](https://colab.research.google.com/github/deepmind/sonnet/blob/v2/examples/little_gan_on_mnist.ipynb)
- [Distributed training with `snt.distribute`](https://colab.research.google.com/github/deepmind/sonnet/blob/v2/examples/
