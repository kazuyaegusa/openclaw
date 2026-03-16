---
name: wagoodman-dive
description: "A tool for exploring each layer in a docker image"
homepage: https://github.com/wagoodman/dive
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["curl", "dive", "docker", "go"]
---

# Wagoodman Dive

# dive

[![GitHub release](https://img.shields.io/github/release/wagoodman/dive.svg)](https://github.com/wagoodman/dive/releases/latest)
[![Validations](https://github.com/wagoodman/dive/actions/workflows/validations.yaml/badge.svg)](https://github.com/wagoodman/dive/actions/workflows/validations.yaml)
[![Go Report Card](https://goreportcard.com/badge/github.com/wagoodman/dive)](https://goreportcard.com/report/github.com/wagoodman/dive)
[![License: MIT](https://img.shields.io/badge/License-MIT%20

## Installation

**Ubuntu/Debian**

Using debs:

```bash
DIVE_VERSION=$(curl -sL "https://api.github.com/repos/wagoodman/dive/releases/latest" | grep '"tag_name":' | sed -E 's/.*"v([^"]+)".*/\1/')
curl -fOL "https://github.com/wagoodman/dive/releases/download/v${DIVE_VERSION}/dive_${DIVE_VERSION}_linux_amd64.deb"
sudo apt install ./dive_${DIVE_VERSION}_linux_amd64.deb
```

Using snap:

```bash
sudo snap install docker
sudo snap install dive
sudo snap connect dive:docker-executables docker:docker-executables
sudo s



```
