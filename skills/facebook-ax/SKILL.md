---
name: facebook-ax
description: "Adaptive Experimentation Platform"
homepage: https://github.com/facebook/Ax
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["ax-platform", "git", "pip"]
---

# Facebook Ax

<img width="300" src="https://ax.dev/img/ax_logo_lockup.svg" alt="Ax Logo" />

<hr/>

[![Support Ukraine](https://img.shields.io/badge/Support-Ukraine-FFD500?style=flat&labelColor=005BBB)](https://opensource.fb.com/support-ukraine)
[![Build Status](https://img.shields.io/pypi/v/ax-platform.svg)](https://pypi.org/project/ax-platform/)
[![Build Status](https://img.shields.io/pypi/pyversions/ax-platform.svg)](https://pypi.org/project/ax-platform/)
[![Build Status](https://img.shields.io/pypi/wheel/

## Installation

To run a simple optimization loop in Ax (using the
[Booth response surface](https://www.sfu.ca/~ssurjano/booth.html) as the
artificial evaluation function):

```python
>>> from ax import Client, RangeParameterConfig

>>> client = Client()
>>> client.configure_experiment(
      parameters=[
          RangeParameterConfig(
              name="x1",
              bounds=(-10.0, 10.0),
              parameter_type=ParameterType.FLOAT,
          ),
          RangeParameterConfig(
              name="x



```
