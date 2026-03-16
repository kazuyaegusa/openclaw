---
name: containers-youki
description: "A container runtime written in Rust"
homepage: https://github.com/youki-dev/youki
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker", "git", "go"]
---

# Containers Youki

# youki: A container runtime in Rust

## Usage

Start the docker daemon.

```bash
dockerd --experimental --add-runtime="youki=$(pwd)/youki"
```

If you get an error like the below, that means your normal Docker daemon is running, and it needs to be stopped. Do that with your init system (i.e., with systemd, run `sudo systemctl stop docker`, as root if necessary).

```console
failed to start daemon: pid file found, ensure docker is not running or delete /var/run/docker.pid
```

Now repeat the command, which should start the docker daemon.

You
