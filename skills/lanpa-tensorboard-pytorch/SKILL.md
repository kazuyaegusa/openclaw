---
name: lanpa-tensorboard-pytorch
description: "tensorboard for pytorch (and chainer, mxnet, numpy, ...)"
homepage: https://github.com/lanpa/tensorboardX
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["crc32c", "pip", "soundfile"]
---

# Lanpa Tensorboard Pytorch

# tensorboardX

## Installation

`pip install tensorboardX`

or build from source:

`pip install 'git+https://github.com/lanpa/tensorboardX'`

You can optionally install [`crc32c`](https://github.com/ICRAR/crc32c) to speed up.

`pip install crc32c`

Starting from tensorboardX 2.1, You need to install `soundfile` for the `add_audio()` function (200x speedup).

`pip install soundfile`
