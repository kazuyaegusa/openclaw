---
name: yihui-knitr
description: "A general-purpose tool for dynamic report generation in R"
homepage: https://github.com/yihui/knitr
metadata:
  openclaw:
    emoji: "📄"
    auto_generated: true
---

# Yihui Knitr

# knitr

## Installation

You can install the stable version on
[CRAN](https://cran.r-project.org/package=knitr):

```r
install.packages('knitr')
```

You can also install the development version (hourly build) from
<https://yihui.r-universe.dev>:

```r
options(repos = c(
  yihui = 'https://yihui.r-universe.dev',
  CRAN = 'https://cloud.r-project.org'
))

install.packages('knitr')
```

## Usage

```r
library(knitr)
?knit
knit(input)
```

If options are not explicitly specified, **knitr** will try to guess
reasonable default settings. A few manuals are available such as the [main
manual](https://yihui.org/knitr/demo/manual/), and the
[graphics
manual](https://yihui.org/knitr/demo/graphics/). For a
more organized reference, see the [knitr book](https://www.amazon.com/dp/1498716962/).
