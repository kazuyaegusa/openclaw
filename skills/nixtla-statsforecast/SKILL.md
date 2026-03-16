---
name: nixtla-statsforecast
description: "Lightning ⚡️ fast forecasting with statistical and econometric models."
homepage: https://github.com/Nixtla/statsforecast
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["pip", "statsforecast"]
---

# Nixtla Statsforecast

# Nixtla

## Installation

You can install `StatsForecast` with:

```python
pip install statsforecast
```

or

```python
conda install -c conda-forge statsforecast
```

Vist our [Installation Guide](https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/installation.html) for further instructions.

## Usage

**Minimal Example**

```python
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
from statsforecast.utils import AirPassengersDF

df = AirPassengersDF
sf = StatsForecast(
    models=[AutoARIMA(season_length=12)],
    freq='ME',
)
sf.fit(df)
sf.predict(h=12, level=[95])
```

**Get Started [quick guide](https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/getting_started_short.html)**

\*\*Follow this [end-to-end walkthrough](https://nixtlaverse.nixtla.io
