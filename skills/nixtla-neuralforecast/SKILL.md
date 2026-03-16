---
name: nixtla-neuralforecast
description: "Scalable and user friendly neural :brain: forecasting algorithms."
homepage: https://github.com/Nixtla/neuralforecast
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["neuralforecast", "pip"]
---

# Nixtla Neuralforecast

# Nixtla

## Installation

You can install `NeuralForecast` with:

```python
pip install neuralforecast
```

or

```python
conda install -c conda-forge neuralforecast
```

Vist our [Installation Guide](https://nixtlaverse.nixtla.io/neuralforecast/docs/getting-started/installation.html) for further details.

## Usage

**Minimal Example**

```python
from neuralforecast import NeuralForecast
from neuralforecast.models import NBEATS
from neuralforecast.utils import AirPassengersDF

nf = NeuralForecast(
    models = [NBEATS(input_size=24, h=12, max_steps=100)],
    freq = 'ME'
)

nf.fit(df=AirPassengersDF)
nf.predict()
```

**Get Started with this [quick guide](https://nixtlaverse.nixtla.io/neuralforecast/docs/getting-started/quickstart.html).**
