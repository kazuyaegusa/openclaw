---
name: rdatatable-data-table
description: "R's data.table package extends data.frame:"
homepage: https://github.com/Rdatatable/data.table
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
---

# Rdatatable Data Table

# data.table <a href="https://r-datatable.com"><img src="https://raw.githubusercontent.com/Rdatatable/data.table/master/.graphics/logo.png" align="right" height="140" /></a>

## Installation

````r
install.packages("data.table")



## Usage

Use `data.table` subset `[` operator the same way you would use `data.frame` one, but...

* no need to prefix each column with `DT$` (like `subset()` and `with()` but built-in)
* any R expression using any package is allowed in `j` argument, not just list of columns
* extra argument `by` to compute `j` expression by group

```r
library(data.table)
DT = as.data.table(iris)

````
