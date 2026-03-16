---
name: dokku-dokku
description: "A docker-powered PaaS that helps you build and manage the lifecycle of applications"
homepage: https://github.com/dokku/dokku
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
---

# Dokku Dokku

# Dokku

## Installation

To install the latest stable release, run the following commands as a user who has access to `sudo`:

```shell
wget -NP . https://dokku.com/install/v0.37.7/bootstrap.sh
sudo DOKKU_TAG=v0.37.7 bash bootstrap.sh
```

You can then proceed to configure your server domain (via `dokku domains:set-global`) and user access (via `dokku ssh-keys:add`) to complete the installation.

If you wish for a more unattended installation method, see [these](https://dokku.com/docs/getting-started/install/debian/#una
