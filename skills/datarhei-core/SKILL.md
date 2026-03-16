---
name: datarhei-core
description: "datarhei Core is management for FFmpeg processes without development effort. Whether your streaming"
homepage: https://github.com/datarhei/core
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker"]
---

# Datarhei Core

# Core

## Usage

1. Run the Docker image

```sh
docker run --name core -d \
    -e CORE_API_AUTH_USERNAME=admin \
    -e CORE_API_AUTH_PASSWORD=secret \
    -p 8080:8080 \
    -v ${HOME}/core/config:/core/config \
    -v ${HOME}/core/data:/core/data \
    datarhei/core:latest
```

2. Open Swagger
   http://host-ip:8080/api/swagger/index.html

3. Log in with Swagger
   Authorize > Basic authorization > Username: admin, Password: secret
