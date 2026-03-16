---
name: google-cadvisor
description: "Analyzes resource usage and performance characteristics of running containers."
homepage: https://github.com/google/cadvisor
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["docker"]
---

# Google Cadvisor

![cAdvisor](logo.png "cAdvisor")

![test status](https://github.com/google/cadvisor/workflows/Test/badge.svg)

cAdvisor (Container Advisor) provides container users an understanding of the resource usage and performance characteristics of their running containers. It is a running daemon that collects, aggregates, processes, and exports information about running containers. Specifically, for each container it keeps resource isolation parameters, historical resource usage, histograms of complete h
