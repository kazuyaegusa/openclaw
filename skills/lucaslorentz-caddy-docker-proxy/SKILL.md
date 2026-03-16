---
name: lucaslorentz-caddy-docker-proxy
description: "Caddy as a reverse proxy for Docker"
homepage: https://github.com/lucaslorentz/caddy-docker-proxy
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "go"]
---

# Lucaslorentz Caddy Docker Proxy

# Caddy-Docker-Proxy

[![Build Status](https://dev.azure.com/lucaslorentzlara/lucaslorentzlara/_apis/build/status/lucaslorentz.caddy-docker-proxy?branchName=master)](https://dev.azure.com/lucaslorentzlara/lucaslorentzlara/_build/latest?definitionId=1) [![Go Report Card](https://goreportcard.com/badge/github.com/lucaslorentz/caddy-docker-proxy)](https://goreportcard.com/report/github.com/lucaslorentz/caddy-docker-proxy)

## Usage

Proxying all requests to a domain to the container

```yml
caddy: example.com
caddy.reverse_proxy: { { upstreams } }
```

Proxying all requests to a domain to a subpath in the container

```yml
caddy: example.com
caddy.rewrite: * /target{path}
caddy.reverse_proxy: {{upstreams}}
```

Proxying requests matching a path

```yml
caddy: example.com
caddy.handle: /source/*
caddy.handle.0_reverse_proxy: { { upstreams } }
```

Proxying requests matching a path, while stripping that path prefix

```yml
caddy: example
```
