---
name: wannesm-dtaidistance
description: "Time series distances: Dynamic Time Warping (fast DTW implementation in C)"
homepage: https://github.com/wannesm/dtaidistance
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["dtaidistance", "pip"]
---

# Wannesm Dtaidistance

[![PyPi Version](https://img.shields.io/pypi/v/dtaidistance.svg)](https://pypi.org/project/dtaidistance/)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/dtaidistance.svg)](https://anaconda.org/conda-forge/dtaidistance)
[![Documentation Status](https://readthedocs.org/projects/dtaidistance/badge/?version=latest)](https://dtaidistance.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/80764246.svg)](https://zenodo.org/badge/latestdoi/80764246)

## Installation

$ pip install dtaidistance

or

    $ conda install -c conda-forge dtaidistance

The pip installation requires Numpy as a dependency to compile Numpy-compatible
C code (using Cython). However, this dependency is optional and can be removed.

The source code is available at
[github.com/wannesm/dtaidistance](https://github.com/wannesm/dtaidistance).

If you encounter any problems during compilation (e.g. the C-based implementation or OpenMP
is not available), see the
[documentation](https://d
