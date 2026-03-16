---
name: jwilder-docker-gen
description: "Generate files from docker container meta-data"
homepage: https://github.com/nginx-proxy/docker-gen
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "git", "go"]
---

# Jwilder Docker Gen

# docker-gen

## Installation

There are three common ways to run docker-gen:

- on the host
- bundled in a container with another application
- separate standalone containers

## Usage

```
$ docker-gen
Usage: docker-gen [options] template [dest]

Generate files from docker container meta-data

Options:
  -config path
      config files with template directives.
      Config files will be merged if this option is specified multiple times. (default [])
  -container-filter key=value
      container filter for inclusion by docker-gen.
      You can pass this option multiple times to combine filters with AND.
      https://docs.docker.com/engine/reference/commandline/ps/#filter
  -

```
