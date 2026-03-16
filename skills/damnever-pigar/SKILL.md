---
name: damnever-pigar
description: ":coffee: A tool to generate requirements.txt for Python project, and more than that. (IT IS NOT A"
homepage: https://github.com/damnever/pigar
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["pigar", "pip"]
---

# Damnever Pigar

## pigar

## Installation

`pigar` can run on Python 3.7+.

To install it with `pip`, use:

```
[sudo] pip install pigar
```

To install it with `conda`, use:

```
conda install -c conda-forge pigar
```

To get the newest code from GitHub:

```
pip install git+https://github.com/damnever/pigar.git@[main or other branch] --upgrade
```

## Usage

- `pigar` can consider most kinds of complicated situations(see [FAQ](#faq)). For example, `pigar v1` has [py2_requirements.txt](https://github.com/damnever/pigar/blob/c68d372fba4a6f98228ec3cf8e273f59d68d0e3c/py2_requirements.txt) and [py3_requirements.txt](https://github.com/damnever/pigar/blob/c68d372fba4a6f98228ec3cf8e273f59d68d0e3c/py3_requirements.txt) for different Python versions.

  ```
  # Generate requirements.txt for current directory.
  $ pigar generate

  # Generating requir
  ```
