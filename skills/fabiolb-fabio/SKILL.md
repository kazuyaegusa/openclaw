---
name: fabiolb-fabio
description: "Consul Load-Balancing made simple"
homepage: https://github.com/fabiolb/fabio
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker", "fabio", "go"]
---

# Fabiolb Fabio

<p align="center">
  <p align="center" style="width: 50%; height: 64px;">
    <img src="https://cdn.rawgit.com/fabiolb/fabio/015e999/fabio.svg" height="64"/>
  </p>
  <p align="center" style="margin-top: 16px">
    <a href="http://ebay.github.io/"><img src="https://cdn.rawgit.com/fabiolb/fabio/7a02e1f/ebay.png" height="32" style="padding-right: 4px"/></a>
    <a href="http://www.ebayclassifiedsgroup.com"><img src="https://cdn.rawgit.com/fabiolb/fabio/7a02e1f/ecg.png" height="32"/></a>
    <a hre

## Installation

1. Install from source, [binary](https://github.com/fabiolb/fabio/releases),
   [Docker](https://hub.docker.com/r/fabiolb/fabio/) or [Homebrew](http://brew.sh).

   ```shell
   # go 1.15 or higher is required
   go install github.com/fabiolb/fabio@latest          (>= go1.15)

   brew install fabio                                  (OSX/macOS stable)
   brew install --devel fabio                          (OSX/macOS devel)

   docker pull fabiolb/fabio                           (Docker)

   http
   ```
