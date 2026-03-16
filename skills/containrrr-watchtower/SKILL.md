---
name: containrrr-watchtower
description: "A process for automating Docker container base image updates."
homepage: https://github.com/containrrr/watchtower
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker"]
---

# Containrrr Watchtower

<div align="center">

### ⚠️ This project is no longer maintained

See https://github.com/containrrr/watchtower/discussions/2135 for details.

---

  <img src="./logo.png" width="450" />
  
  # Watchtower
  
  A process for automating Docker container base image updates.
  <br/><br/>
  
  [![Circle CI](https://circleci.com/gh/containrrr/watchtower.svg?style=shield)](https://circleci.com/gh/containrrr/watchtower)
  [![codecov](https://codecov.io/gh/containrrr/watchtower/branch/main/graph/b

## Usage

With watchtower you can update the running version of your containerized app simply by pushing a new image to the Docker Hub or your own image registry.

Watchtower will pull down your new image, gracefully shut down your existing container and restart it with the same options that were used when it was deployed initially. Run the watchtower container with the following command:

```
$ docker run --detach \
    --name watchtower \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    con

```
