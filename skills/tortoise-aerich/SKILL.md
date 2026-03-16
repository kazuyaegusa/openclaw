---
name: tortoise-aerich
description: "A database migrations tool for TortoiseORM, ready to production."
homepage: https://github.com/tortoise/aerich
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["pip"]
---

# Tortoise Aerich

# Aerich

## Installation

Just install from pypi:

```shell
pip install "aerich[toml]"
```

Or install the latest version directly from _github_ with the
following command:

```shell
pip install "aerich[toml] @git+https://github.com/tortoise/aerich"
```

## Usage

```shell
> aerich -h

Usage: aerich [OPTIONS] COMMAND [ARGS]...

Options:
  -V, --version      Show the version and exit.
  -c, --config TEXT  Config file.  [default: pyproject.toml]
  --app TEXT         Tortoise-ORM app name.
  -h, --help         Show this message and exit.

Commands:
  downgrade  Downgrade to specified version.
  fix-migrations   Fix migration files to include models state for aerich...
  heads      Show current available heads in migrate location.
  history    List all migrat

```
