---
name: bytebase-dbhub
description: "Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB,"
homepage: https://github.com/bytebase/dbhub
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["dbhub", "docker", "npx"]
---

# Bytebase Dbhub

> [!NOTE]  
> Brought to you by [Bytebase](https://www.bytebase.com/), open-source database DevSecOps platform.

<p align="center">
<a href="https://dbhub.ai/" target="_blank">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bytebase/dbhub/main/docs/images/logo/full-dark.svg" width="75%">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/bytebase/dbhub/main/docs/images/logo/full-light.svg" width="75%">
  <

## Installation

See the full [Installation Guide](https://dbhub.ai/installation) for detailed instructions.

## Usage

**Docker:**

```bash
docker run --rm --init \
   --name dbhub \
   --publish 8080:8080 \
   bytebase/dbhub \
   --transport http \
   --port 8080 \
   --dsn "postgres://user:password@localhost:5432/dbname?sslmode=disable"
```

**NPM:**

```bash
npx @bytebase/dbhub@latest --transport http --port 8080 --dsn "postgres://user:password@localhost:5432/dbname?sslmode=disable"
```

**Demo Mode:**

```bash
npx @bytebase/dbhub@latest --transport http --port 8080 --demo
```

See [Command-Line Options](http
