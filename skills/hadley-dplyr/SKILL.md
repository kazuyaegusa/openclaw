---
name: hadley-dplyr
description: "dplyr: A grammar of data manipulation"
homepage: https://github.com/tidyverse/dplyr
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
---

# Hadley Dplyr

<!-- README.md is generated from README.Rmd. Please edit that file -->

## Installation

````r



## Usage

``` r
library(dplyr)

starwars |>
  filter(species == "Droid")
#> # A tibble: 6 × 14
#>   name   height  mass hair_color skin_color  eye_color birth_year sex   gender
#>   <chr>   <int> <dbl> <chr>      <chr>       <chr>          <dbl> <chr> <chr>
#> 1 C-3PO     167    75 <NA>       gold        yellow           112 none  masculi…
#> 2 R2-D2      96    32 <NA>       white, blue red               33 none  masculi…
#> 3 R5-D4      97    32 <NA>       white, red  red               NA none  masc

````
