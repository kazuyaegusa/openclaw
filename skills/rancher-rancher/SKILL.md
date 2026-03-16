---
name: rancher-rancher
description: "Complete container management platform"
homepage: https://github.com/rancher/rancher
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker"]
---

# Rancher Rancher

# Rancher

## Installation

See [Installing/Upgrading Rancher](https://ranchermanager.docs.rancher.com/v2.8/pages-for-subheaders/installation-and-upgrade) for all installation options.

## Usage

sudo docker run -d --restart=unless-stopped -p 80:80 -p 443:443 --privileged rancher/rancher

Open your browser to https://localhost
