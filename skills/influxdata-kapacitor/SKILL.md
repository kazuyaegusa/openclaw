---
name: influxdata-kapacitor
description: "Open source framework for processing, monitoring, and alerting on time series data"
homepage: https://github.com/influxdata/kapacitor
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["go"]
---

# Influxdata Kapacitor

# Kapacitor [![Circle CI](https://circleci.com/gh/influxdata/kapacitor/tree/master.svg?style=svg&circle-token=78c97422cf89526309e502a290c230e8a463229f)](https://circleci.com/gh/influxdata/kapacitor/tree/master) [![Docker pulls](https://img.shields.io/docker/pulls/library/kapacitor.svg)](https://hub.docker.com/_/kapacitor/)

Open source framework for processing, monitoring, and alerting on time series data

## Installation

Kapacitor has two binaries:

- kapacitor – a CLI program for calling the Kapacitor API.
- kapacitord – the Kapacitor server daemon.

You can either download the binaries directly from the [downloads](https://influxdata.com/downloads/#kapacitor) page or go get them:

```sh
go get github.com/influxdata/kapacitor/cmd/kapacitor
go get github.com/influxdata/kapacitor/cmd/kapacitord
```
