---
name: hadley-ggplot2
description: "An implementation of the Grammar of Graphics in R"
homepage: https://github.com/tidyverse/ggplot2
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
---

# Hadley Ggplot2

<!-- README.md is generated from README.Rmd. Please edit that file -->

## Installation

````r



## Usage

It’s hard to succinctly describe how ggplot2 works because it embodies a
deep philosophy of visualisation. However, in most cases you start with
`ggplot()`, supply a dataset and aesthetic mapping (with `aes()`). You
then add on layers (like `geom_point()` or `geom_histogram()`), scales
(like `scale_colour_brewer()`), faceting specifications (like
`facet_wrap()`) and coordinate systems (like `coord_flip()`).

``` r
library(ggplot2)

ggplot(mpg, aes(displ, hwy, colour = class)) +
  geom_point()
``

````
