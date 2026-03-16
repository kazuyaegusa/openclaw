---
name: projectatomic-bubblewrap
description: "Low-level unprivileged sandboxing tool used by Flatpak and similar projects"
homepage: https://github.com/containers/bubblewrap
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["docker"]
---

# Projectatomic Bubblewrap

# Bubblewrap

Many container runtime tools like `systemd-nspawn`, `docker`,
etc. focus on providing infrastructure for system administrators and
orchestration tools (e.g. Kubernetes) to run containers.

These tools are not suitable to give to unprivileged users, because it
is trivial to turn such access into a fully privileged root shell
on the host.

## User namespaces

There is an effort in the Linux kernel called
[user namespaces](https://www.google.com/search?q=user+nam
