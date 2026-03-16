---
name: redis-redis
description: "For developers, who are building real-time data-driven applications, Redis is the preferred,"
homepage: https://github.com/redis/redis
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins:
        [
          "automake",
          "cmake",
          "coreutils",
          "curl",
          "docker",
          "git",
          "gnu-sed",
          "jq",
          "libtool",
          "llvm",
          "make",
          "openssl",
          "python3",
          "wget",
        ]
---

# Redis Redis

[![codecov](https://codecov.io/github/redis/redis/graph/badge.svg?token=6bVHb5fRuz)](https://codecov.io/github/redis/redis)

This document serves as both a quick start guide to Redis and a detailed resource for building it from source.

- New to Redis? Start with [What is Redis](#what-is-redis) and [Getting Started](#getting-started)
- Ready to build from source? Jump to [Build Redis from Source](#build-redis-from-source)
- Want to contribute? See the [Code contributions](#code-contributions) se

## Installation

If you want to get up and running with Redis quickly without needing to build from source, use one of the following methods:

- [**Redis Cloud**](https://cloud.redis.io/)
- [**Official Redis Docker images (Alpine/Debian)**](https://hub.docker.com/_/redis)
  ```sh
  docker run -d -p 6379:6379 redis:latest
  ```
- **Redis binary distributions**
  - [**Snap**](https://github.com/redis/redis-snap)
  - [**Homebrew**](https://github.com/redis/homebrew-redis)
  - [**RPM**](https://github.com/redis/redi
