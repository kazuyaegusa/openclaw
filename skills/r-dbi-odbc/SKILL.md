---
name: r-dbi-odbc
description: "Connect to ODBC databases (using the DBI interface)"
homepage: https://github.com/r-dbi/odbc
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
---

# R Dbi Odbc

<!-- README.md is generated from README.Rmd. Please edit that file -->

## Installation

Install the latest release of odbc from CRAN with the following code:

```r
install.packages("odbc")
```

To get a bug fix or to use a feature from the development version, you
can install the development version of odbc from GitHub:

````r



## Usage

To use odbc, begin by creating a database connection, which might look
something like this:

``` r
library(DBI)

con <- dbConnect(
  odbc::odbc(),
  driver = "SQL Server",
  server = "my-server",
  database = "my-database",
  uid = "my-username",
  pwd = rstudioapi::askForPassword("Database password")
)
````

(See `vignette("setup")` for examples of connecting to a variety of
databases.)

`dbListTables()` is used for listing all existing tables in a database.

```r
dbListTables(con)
```

`dbRead
