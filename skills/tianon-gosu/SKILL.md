---
name: tianon-gosu
description: "Simple Go-based setuid+setgid+setgroups+exec"
homepage: https://github.com/tianon/gosu
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["docker"]
---

# Tianon Gosu

# gosu

## Installation

High-level steps:

1. download `gosu-$(dpkg --print-architecture | awk -F- '{ print $NF }')` as `gosu`
2. download `gosu-$(dpkg --print-architecture | awk -F- '{ print $NF }').asc` as `gosu.asc`
3. fetch my public key (to verify your download): `gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4`
4. `gpg --batch --verify gosu.asc gosu`
5. `chmod +x gosu`

For explicit `Dockerfile` instructions, see [`INSTALL.md`](INSTALL.md).
