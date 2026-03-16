---
name: praqma-helmsman
description: "Helm Charts as Code"
homepage: https://github.com/mkubaczyk/helmsman
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "helmsman"]
---

# Praqma Helmsman

[![GitHub release](https://img.shields.io/github/v/release/mkubaczyk/helmsman)](https://github.com/mkubaczyk/helmsman/releases)

![helmsman-logo](docs/images/helmsman.png)

> Helmsman v4.x supports Helm 3.x and Helm 4.x. For Helm 2.x, use Helmsman v1.x

## Usage

Helmsman can be used in three different settings:

- [As a binary with a hosted cluster](https://github.com/mkubaczyk/helmsman/blob/master/docs/how_to/settings).
- [As a docker image in a CI system or local machine](https://github.com/mkubaczyk/helmsman/blob/master/docs/how_to/deployments/ci.md) Always use a tagged docker image from [GHCR](https://github.com/mkubaczyk/helmsman/pkgs/container/helmsman).
- [As a docker image inside a k8s cluster](https://github.com/mkubaczyk/helmsman/blob/master/d
