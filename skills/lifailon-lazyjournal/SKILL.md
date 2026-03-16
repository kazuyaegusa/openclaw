---
name: lifailon-lazyjournal
description: "TUI for viewing logs from journald, auditd, file system, Docker and Podman containers, Compose"
homepage: https://github.com/Lifailon/lazyjournal
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "git", "go", "lazyjournal"]
---

# Lifailon Lazyjournal

<p align="center">
    <img src="/img/logo.png">
</p>

<p align="center">
    <a href="https://github.com/Lifailon/lazyjournal/releases"><img title="GitHub Download" src="https://img.shields.io/github/downloads/lifailon/lazyjournal/total?logo=github&color=green&label=Downloads"></a>
    <a href="https://launchpad.net/~lifailon/+archive/ubuntu/lazyjournal"><img title="Ubuntu Launchpad PPA" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.launchpad.net%2F1.0%2F~lifailon%2F%2Bar

## Installation

Binaries are available for download on the GitHub [releases](https://github.com/Lifailon/lazyjournal/releases) page.

## Usage

You can start the interface from anywhere: `lazyjournal` or use `lazyjournal -h` for help on available flags.

The application is an interface for viewing logs with the ability to filter them for analysis. Therefore, to access the logs themselves, it is necessary that such programs as [docker-cli](https://github.com/docker/cli), [compose](https://github.com/docker/compose), [podman](https://github.com/containers/podman) and [kubectl](https://github.com/kubernetes/kubectl) are already installed o
