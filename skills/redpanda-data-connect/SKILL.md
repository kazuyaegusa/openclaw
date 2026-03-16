---
name: redpanda-data-connect
description: "Fancy stream processing made operationally mundane"
homepage: https://github.com/redpanda-data/connect
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "git", "go", "redpanda"]
---

# Redpanda Data Connect

# Redpanda Connect

[![Build Status][actions-badge]][actions-url]

API for Apache V2 builds: [![godoc for redpanda-data/connect ASL][godoc-badge]][godoc-url-apache]

API for Enterprise builds: [![godoc for redpanda-data/connect RCL][godoc-badge]][godoc-url-enterprise]

Redpanda Connect is a high performance and resilient stream processor, able to connect various [sources][inputs] and [sinks][outputs] in a range of brokering patterns and perform [hydration, enrichments, transformat

## Installation

Install on Linux:

```shell
curl -LO https://github.com/redpanda-data/redpanda/releases/latest/download/rpk-linux-amd64.zip
unzip rpk-linux-amd64.zip -d ~/.local/bin/
```

Or use Homebrew:

```shell
brew install redpanda-data/tap/redpanda
```

Or pull the docker image:

```shell
docker pull docker.redpanda.com/redpandadata/connect
```

For more information check out the [getting started guide][getting-started].
