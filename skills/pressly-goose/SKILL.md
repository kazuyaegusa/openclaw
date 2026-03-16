---
name: pressly-goose
description: "A database migration tool. Supports SQL migrations and Go functions."
homepage: https://github.com/pressly/goose
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["go", "goose"]
---

# Pressly Goose

# goose

## Installation

```shell
go install github.com/pressly/goose/v3/cmd/goose@latest
```

This will install the `goose` binary to your `$GOPATH/bin` directory.

Binary too big? Build a lite version by excluding the drivers you don't need:

```shell
go build -tags='no_postgres no_mysql no_sqlite3 no_ydb' -o goose ./cmd/goose



## Usage

<details>
<summary>Click to show <code>goose help</code> output</summary>

```

Usage: goose DRIVER DBSTRING [OPTIONS] COMMAND

or

Set environment key
GOOSE_DRIVER=DRIVER
GOOSE_DBSTRING=DBSTRING
GOOSE_MIGRATION_DIR=MIGRATION_DIR

Usage: goose [OPTIONS] COMMAND

Drivers:
postgres
mysql
sqlite3
spanner
mssql
redshift
tidb
clickhouse
ydb
starrocks
turso

Examples:
goose sqlite3 ./foo.db status
goose sqlite3 ./foo.db create init sql
goose sqlit
