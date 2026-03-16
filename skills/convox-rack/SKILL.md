---
name: convox-rack
description: "Private PaaS built on native AWS services for maximum privacy and minimum upkeep"
homepage: https://github.com/convox/rack
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
---

# Convox Rack

# convox/rack

## Installation

Install a Rack from [Convox Console](https://console.convox.com)

## Usage

```console
$ convox apps create myapp
Creating app myapp... OK

$ convox env set SECRET=foo -a myapp
Setting SECRET... OK, RABCDEFGH

$ convox deploy ~/src/myapp -a myapp
Building myapp... OK
Creating release RHGFEFCBA... OK
Promoting release RHGFEFCBA... OK
```
