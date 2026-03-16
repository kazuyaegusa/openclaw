---
name: manujosephv-pytorch-tabular
description: "A unified framework for Deep Learning Models on tabular data"
homepage: https://github.com/pytorch-tabular/pytorch_tabular
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["extra", "git", "pip"]
---

# Manujosephv Pytorch Tabular

![PyTorch Tabular](docs/imgs/pytorch_tabular_logo.png)

_PyTorch Tabular_ provides a unified interface to deep learning architectures for tabular data. It provides a high-level API and uses [PyTorch Lightning](https://pytorch-lightning.readthedocs.io/) to scale training on GPU or CPU, with automatic logging.

| | **[Documentation](https://pytorch-tabular.readthedocs.io/en/latest/)** · \*\*[Tutorials](https://pytorch-tabular.readthedocs.io/en/latest/tutorials/01-Approaching%20Any%20Tabular%20Probl

## Installation

Although the installation includes PyTorch, the best and recommended way is to first install PyTorch from [here](https://pytorch.org/get-started/locally/), picking up the right CUDA version for your machine.

Once, you have got Pytorch installed, just use:

```bash
pip install -U “pytorch_tabular[extra]”
```

to install the complete library with extra dependencies (Weights&Biases & Plotly).

And :

```bash
pip install -U “pytorch_tabular”
```

for the bare essentials.

The sources for pytorch_ta

## Usage

```python
from pytorch_tabular import TabularModel
from pytorch_tabular.models import CategoryEmbeddingModelConfig
from pytorch_tabular.config import (
    DataConfig,
    OptimizerConfig,
    TrainerConfig,
    ExperimentConfig,
)

data_config = DataConfig(
    target=[
        "target"
    ],  # target should always be a list.
    continuous_cols=num_col_names,
    categorical_cols=cat_col_names,
)
trainer_config = TrainerConfig(
    auto_lr_find=True,  # Runs the LRFinder to automatically der

```
