---
name: ropensci-targets
description: "Function-oriented Make-like declarative workflows for R"
homepage: https://github.com/ropensci/targets
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
---

# Ropensci Targets

# targets <img src='man/figures/logo.png' align="right" height="139"/>

## Installation

If you are using `targets` [with `crew` for distributed
computing](https://books.ropensci.org/targets/crew.html), it is
recommended to use `crew` version `0.4.0` or higher.

```r
install.packages("crew")
```

There are multiple ways to install the `targets` package itself, and
both the latest release and the development version are available.

| Type        | Source | Command                          |
| ----------- | ------ | -------------------------------- |
| Release     | CRAN   | `install.packages("targets")`    |
| Development | GitHub | `pak::pkg_install("ropensci/targ |

## Usage

To create a pipeline of your own:

1.  [Write R
    functions](https://books.ropensci.org/targets/functions.html) for a
    pipeline and save them to R scripts (ideally in the `"R/"` folder of
    your project).
2.  Call
    [`use_targets()`](https://docs.ropensci.org/targets/reference/use_targets.html)
    to write key files, including the vital `_targets.R` file which
    configures and defines the pipeline.
3.  Follow the comments in `_targets.R` to fill in the details of your
    specific pi
