---
name: moby-buildkit
description: "concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit"
homepage: https://github.com/moby/buildkit
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["buildkit", "docker", "git", "jq", "lima"]
---

# Moby Buildkit

[![asciicinema example](https://asciinema.org/a/gPEIEo1NzmDTUu2bEPsUboqmU.png)](https://asciinema.org/a/gPEIEo1NzmDTUu2bEPsUboqmU)

## Usage

:information_source: For Kubernetes deployments, see [`examples/kubernetes`](./examples/kubernetes).

BuildKit is composed of the `buildkitd` daemon and the `buildctl` client.
While the `buildctl` client is available for Linux, macOS, and Windows, the `buildkitd` daemon is only available for Linux and \*Windows currently.

The latest binaries of BuildKit are available [here](https://github.com/moby/buildkit/releases) for Linux, macOS, and Windows.
