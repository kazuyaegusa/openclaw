---
name: nginx-proxy-nginx-proxy
description: "Automated nginx proxy for Docker containers using docker-gen"
homepage: https://github.com/nginx-proxy/nginx-proxy
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker"]
---

# Nginx Proxy Nginx Proxy

[![Test](https://github.com/nginx-proxy/nginx-proxy/actions/workflows/test.yml/badge.svg)](https://github.com/nginx-proxy/nginx-proxy/actions/workflows/test.yml)
[![GitHub release](https://img.shields.io/github/v/release/nginx-proxy/nginx-proxy)](https://github.com/nginx-proxy/nginx-proxy/releases)
[![nginx 1.29.6](https://img.shields.io/badge/nginx-1.29.6-brightgreen.svg?logo=nginx)](https://nginx.org/en/CHANGES)
[![Docker Image Size](https://img.shields.io/docker/image-size/nginxproxy/nginx-pr

## Usage

To run it:

```shell
docker run --detach \
    --name nginx-proxy \
    --publish 80:80 \
    --volume /var/run/docker.sock:/tmp/docker.sock:ro \
    nginxproxy/nginx-proxy:1.10
```

Then start any containers (here an nginx container) you want proxied with an env var `VIRTUAL_HOST=subdomain.yourdomain.com`

```shell
docker run --detach \
    --name your-proxied-app \
    --env VIRTUAL_HOST=foo.bar.com \
    nginx
```

Provided your DNS is setup to resolve `foo.bar.com` to the host running nginx-
