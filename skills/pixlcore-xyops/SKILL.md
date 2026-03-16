---
name: pixlcore-xyops
description: "A complete workflow automation and server monitoring system."
homepage: https://github.com/pixlcore/xyops
metadata:
  openclaw:
    emoji: "⚡"
    auto_generated: true
    requires:
      bins: ["docker", "git", "go", "node", "npm"]
---

# Pixlcore Xyops

# xyOps™

## Installation

See our **[Self-Hosting Guide](https://docs.xyops.io/hosting)** for installation details.

Just want to test out xyOps locally really quick? One-liner Docker command:

```sh
docker run --detach --init --restart unless-stopped -v xy-data:/opt/xyops/data -v /var/run/docker.sock:/var/run/docker.sock -e TZ="America/Los_Angeles" -e XYOPS_xysat_local="true" -p 5522:5522 -p 5523:5523 --name "xyops01" --hostname "xyops01" ghcr.io/pixlcore/xyops:latest
```

Then open http://localhost:5522 in your browse
