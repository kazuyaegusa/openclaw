---
name: uber-kraken
description: "P2P Docker registry capable of distributing TBs of data in seconds"
homepage: https://github.com/uber/kraken
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker", "node"]
---

# Uber Kraken

<p align="center"><img src="assets/kraken-logo-color.svg" width="175" title="Kraken Logo"></p>

<p align="center">
  <a href="https://github.com/uber/kraken/releases"><img src="https://img.shields.io/github/release/uber/kraken.svg?cache-control=no-cache" /></a>
  <a href="https://godoc.org/github.com/uber/kraken"><img src="https://godoc.org/github.com/uber/kraken?status.svg&cache-control=no-cache"></a>
  <a href="https://goreportcard.com/badge/github.com/uber/kraken"><img src="https://goreportca

## Usage

All Kraken components can be deployed as Docker containers. To build the Docker images:

```
$ make images
```

For information about how to configure and use Kraken, please refer to the [documentation](docs/CONFIGURATION.md).
