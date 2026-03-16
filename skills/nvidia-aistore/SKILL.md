---
name: nvidia-aistore
description: "AIStore: scalable storage for AI applications"
homepage: https://github.com/NVIDIA/aistore
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["docker", "git"]
---

# Nvidia Aistore

**AIStore: High-Performance, Scalable Storage for AI Workloads**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-v4.1-green.svg)
![Go Report Card](https://goreportcard.com/badge/github.com/NVIDIA/aistore)

AIStore (AIS) is a lightweight distributed storage stack tailored for AI applications. It's an elastic cluster that can grow and shrink at runtime and can be ad-hoc deployed, with or without Kubernetes, anywhere from a single Linux

## Usage

1. Read the [Getting Started Guide](/docs/getting_started.md) for a 5-minute local install, or
2. Run a [minimal](https://github.com/NVIDIA/aistore/tree/main/deploy/prod/docker/single) AIS cluster consisting of a single gateway and a single storage node, or
3. Clone the repo and run `make kill cli aisloader deploy` followed by `ais show cluster`

---
